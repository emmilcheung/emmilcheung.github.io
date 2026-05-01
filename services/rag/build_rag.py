"""
RAG build script: Resume → clean → section-aware chunk → embed → SQLite

Input modes (in priority order):
  1. Curated markdown  data/resume_curated.md  (preferred — manually refined)
  2. PDF fallback      docs/*.pdf              (legacy)

Set env var SOURCE_MODE=pdf to force PDF mode.

Output: ../../data/resume.db
    Table: chunks(id, category, content, embedding BLOB)
    Table: meta(key, value)

Improvements over v1:
  - Section-aware chunking: each resume section / sub-entry becomes its own
    chunk rather than splitting blindly by token count.
  - Metadata: every chunk is tagged with its category (experience, skills, …).
  - Data cleaning: strips PDF artefacts, normalises whitespace, removes noise.
  - Embedding enrichment: category label is prepended to the text sent to the
    embedding API so the vector captures semantic context, not just surface text.
  - The category is stored separately in the DB and surfaced in the RAG prompt
    so the LLM knows which section each excerpt came from.
"""

import os
import re
import sqlite3
import struct
import sys
from dataclasses import dataclass
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT      = Path(__file__).resolve().parents[2]
PDF_DIR        = REPO_ROOT / "docs"
CURATED_TEXT   = REPO_ROOT / "docs" / "resume_curated.md"
DB_OUTPUT      = REPO_ROOT / "data" / "resume.db"

# ── Config ────────────────────────────────────────────────────────────────────
API_BASE      = "https://openrouter.ai/api/v1"
EMBED_MODEL   = "qwen/qwen3-embedding-4b"
EMBED_DIMS    = 2560

# Fallback PDF chunking (only used when SOURCE_MODE=pdf)
CHUNK_SIZE    = 300
CHUNK_OVERLAP = 30


@dataclass
class Chunk:
    category: str   # e.g. "experience", "skills", "projects"
    content: str    # cleaned prose sent to the LLM as context
    embed_text: str # content prefixed with category — sent to the embedding API


# ── Env check ─────────────────────────────────────────────────────────────────
def check_env() -> None:
    if not os.environ.get("OPENROUTER_API_KEY"):
        sys.exit("Error: OPENROUTER_API_KEY environment variable is not set.")


# ── Data cleaning ─────────────────────────────────────────────────────────────
# Known bullet characters that appear in PDF text extraction
_BULLET_RE  = re.compile(r"^[\u25cf\u2022\u2023\u25e6\u2043\-\*]\s*", re.MULTILINE)
# Collapse 3+ consecutive blank lines → 2
_BLANK_RE   = re.compile(r"\n{3,}")
# Remove soft hyphens and zero-width spaces
_NOISE_RE   = re.compile(r"[\xad\u200b\u200c\u200d\ufeff]")
# Collapse mid-word line breaks introduced by narrow PDF columns
_MIDWORD_RE = re.compile(r"([a-zA-Z,])\n([a-zA-Z])")


def clean_text(raw: str) -> str:
    """Remove PDF extraction artefacts and normalise whitespace."""
    text = _NOISE_RE.sub("", raw)
    # Rejoin words broken across lines (PDF column wrap artefact)
    text = _MIDWORD_RE.sub(r"\1 \2", text)
    # Normalise bullet characters to hyphens for uniform parsing
    text = _BULLET_RE.sub("- ", text)
    # Collapse excessive blank lines
    text = _BLANK_RE.sub("\n\n", text)
    # Strip trailing whitespace per line
    lines = [ln.rstrip() for ln in text.splitlines()]
    return "\n".join(lines).strip()


# ── Section-aware chunking from curated markdown ──────────────────────────────
# Maps markdown section headings (## HEADING) to canonical category names
_SECTION_MAP = {
    "CONTACT":         "contact",
    "EXPERIENCE":      "experience",
    "PROJECTS":        "projects",
    "EDUCATION":       "education",
    "CERTIFICATIONS":  "certifications",
    "CERTIFICATE":     "certifications",
    "SKILLS":          "skills",
    "SUMMARY":         "summary",
}

_H2_RE = re.compile(r"^##\s+(.+)$")   # top-level section  ## EXPERIENCE
_H3_RE = re.compile(r"^###\s+(.+)$")  # sub-entry          ### Job Title, Company


def chunk_markdown(path: Path) -> list[Chunk]:
    """
    Parse resume_curated.md into structured Chunk objects.

    Strategy:
      - ## SECTION  → sets current category
      - ### Sub-item → each sub-item (job, project, degree) becomes its own chunk
      - Content without sub-items (CONTACT, SKILLS, CERTIFICATIONS) → single chunk
        per section, or one chunk per ### group within that section.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    chunks: list[Chunk] = []
    current_category = "general"
    current_heading  = ""
    buffer: list[str] = []

    def flush(category: str, heading: str, body_lines: list[str]) -> None:
        body = clean_text("\n".join(body_lines))
        if not body:
            return
        content = f"{heading}\n\n{body}".strip() if heading else body
        embed_text = f"Category: {category}\n\n{content}"
        chunks.append(Chunk(category=category, content=content, embed_text=embed_text))

    for line in lines:
        h2 = _H2_RE.match(line)
        h3 = _H3_RE.match(line)

        if h2:
            # Flush whatever was accumulating under the previous section/sub-item
            flush(current_category, current_heading, buffer)
            buffer = []
            heading_text = h2.group(1).strip().upper()
            current_category = _SECTION_MAP.get(heading_text, heading_text.lower())
            current_heading  = ""

        elif h3:
            # Flush the previous sub-entry
            flush(current_category, current_heading, buffer)
            buffer = []
            current_heading = h3.group(1).strip()

        else:
            buffer.append(line)

    # Flush final accumulated buffer
    flush(current_category, current_heading, buffer)

    print(f"  Parsed {len(chunks)} section-aware chunks from {path.name}")
    return chunks


# ── PDF fallback chunking (legacy) ────────────────────────────────────────────
def chunk_pdf() -> list[Chunk]:
    """Fall back to SentenceSplitter when no curated text is available."""
    from llama_index.core import SimpleDirectoryReader
    from llama_index.core.node_parser import SentenceSplitter

    print(f"Loading PDFs from {PDF_DIR} …")
    docs = SimpleDirectoryReader(
        input_dir=str(PDF_DIR),
        required_exts=[".pdf"],
    ).load_data()
    print(f"  Loaded {len(docs)} document(s)")

    parser = SentenceSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        paragraph_separator="\n\n",
    )
    nodes = parser.get_nodes_from_documents(docs)

    chunks = []
    for node in nodes:
        content = clean_text(node.get_content())
        if content:
            chunks.append(Chunk(
                category="resume",
                content=content,
                embed_text=f"Category: resume\n\n{content}",
            ))

    print(f"  Created {len(chunks)} chunks (size≤{CHUNK_SIZE} tokens, overlap={CHUNK_OVERLAP})")
    return chunks


# ── Embedding ─────────────────────────────────────────────────────────────────
def embed_chunks(chunks: list[Chunk]) -> list[tuple[Chunk, list[float]]]:
    """Return [(chunk, embedding_floats)] for every chunk."""
    import requests

    headers = {
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
    }

    print(f"Embedding {len(chunks)} chunks with {EMBED_MODEL} …")
    results = []
    for i, chunk in enumerate(chunks, 1):
        if not chunk.embed_text.strip():
            continue
        resp = requests.post(
            f"{API_BASE}/embeddings",
            headers=headers,
            json={"model": EMBED_MODEL, "input": chunk.embed_text},
            timeout=30,
        )
        if not resp.ok:
            raise RuntimeError(f"OpenRouter {resp.status_code}: {resp.text}")
        embedding = resp.json()["data"][0]["embedding"]
        results.append((chunk, embedding))
        if i % 10 == 0 or i == len(chunks):
            print(f"  {i}/{len(chunks)} done")

    return results


# ── SQLite writer ─────────────────────────────────────────────────────────────
def write_sqlite(pairs: list[tuple[Chunk, list[float]]]) -> None:
    """Persist chunks + float32 embeddings to SQLite."""
    DB_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_OUTPUT)
    conn.execute("DROP TABLE IF EXISTS chunks")
    conn.execute("DROP TABLE IF EXISTS meta")

    conn.execute(
        """
        CREATE TABLE chunks (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            category  TEXT    NOT NULL DEFAULT 'general',
            content   TEXT    NOT NULL,
            embedding BLOB    NOT NULL   -- packed float32 little-endian
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE meta (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    conn.execute("INSERT INTO meta VALUES ('embed_model', ?)", (EMBED_MODEL,))
    conn.execute("INSERT INTO meta VALUES ('embed_dims',  ?)", (str(EMBED_DIMS),))

    for chunk, emb in pairs:
        blob = struct.pack(f"<{len(emb)}f", *emb)
        conn.execute(
            "INSERT INTO chunks (category, content, embedding) VALUES (?, ?, ?)",
            (chunk.category, chunk.content, blob),
        )

    conn.commit()
    conn.close()

    # Print a summary per category
    conn2 = sqlite3.connect(DB_OUTPUT)
    rows = conn2.execute(
        "SELECT category, COUNT(*) FROM chunks GROUP BY category ORDER BY category"
    ).fetchall()
    conn2.close()
    print("\nChunks per category:")
    for cat, cnt in rows:
        print(f"  {cat:<20} {cnt}")

    size_kb = DB_OUTPUT.stat().st_size // 1024
    print(f"\nWrote {len(pairs)} chunks → {DB_OUTPUT}  ({size_kb} KB)")


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    check_env()

    force_pdf = os.environ.get("SOURCE_MODE", "").lower() == "pdf"

    if not force_pdf and CURATED_TEXT.exists():
        print(f"Using curated markdown source: {CURATED_TEXT}")
        chunks = chunk_markdown(CURATED_TEXT)
    else:
        print("Falling back to PDF source (set SOURCE_MODE=pdf to silence this)")
        chunks = chunk_pdf()

    pairs = embed_chunks(chunks)
    write_sqlite(pairs)
    print("\nDone. Deploy the Lambda to pick up the new resume.db.")


if __name__ == "__main__":
    main()
