# RAG Builder

This folder contains the one-time build step that turns curated resume content into `data/resume.db` for the portfolio chat Lambda.

## Prerequisites

- Python 3.11+
- An OpenRouter API key with embedding access

## Files

- `build_rag.py`: Reads `docs/resume_curated.md` plus the curated Q&A bank at `docs/resume_qa.md`. Falls back to PDFs in `docs/` when `SOURCE_MODE=pdf` (Q&A boost is skipped in PDF mode).
- `docs/resume_qa.md`: Question-shaped retrieval boost. Each `### entry` carries a `Question:` line of paraphrases (embedded for retrieval) and an answer body (returned to the LLM). Optional `Weight: N` duplicates the chunk N times so high-priority Q&A pulls more strongly in topK.
- `pyproject.toml` / `requirements.txt`: Minimal dependency declarations for the builder
- `../../data/resume.db`: Generated SQLite output consumed by the Lambda

## Rebuild The Database

Create or activate a virtual environment in this folder, install dependencies, then run the builder:

```bash
cd services/rag
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENROUTER_API_KEY=your_key_here
python build_rag.py
```

To force legacy PDF parsing instead of the curated markdown source:

```bash
SOURCE_MODE=pdf python build_rag.py
```

## Output Contract

The generated SQLite database stores:

- `chunks(category, content, embedding)` for retrieval
- `meta(embed_model, embed_dims)` so the Lambda can validate model compatibility at startup

After regenerating `data/resume.db`, redeploy the SST function so the Lambda bundle picks up the new file.