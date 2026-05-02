/**
 * add_vec_index.mjs — build the sqlite-vec HNSW index for resume.db
 *
 * Run after build_rag.py (which writes plain chunks + meta tables):
 *   pnpm rag:index          # or: node services/rag/add_vec_index.mjs
 *   pnpm rag:index data/custom.db   # optional path override
 *
 * Why Node instead of Python: Python's sqlite3 module is compiled without
 * extension-loading support on many macOS distributions, preventing sqlite-vec
 * from being loaded.  Node + better-sqlite3 have no such restriction.
 */

import { createRequire } from 'module';
import { fileURLToPath }  from 'url';
import path               from 'path';
import fs                 from 'fs';

const __dirname  = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT  = path.resolve(__dirname, '../..');
const FN_MODULES = path.join(REPO_ROOT, 'packages', 'functions', 'node_modules');

// Load sqlite-vec and better-sqlite3 from the functions package node_modules
const _require  = createRequire(FN_MODULES + path.sep);
const Database  = _require('better-sqlite3');
const sqliteVec = _require('sqlite-vec');

const DB_PATH = process.argv[2] ?? path.join(REPO_ROOT, 'data', 'resume.db');

if (!fs.existsSync(DB_PATH)) {
  console.error(`Error: database not found at ${DB_PATH}`);
  console.error('Run `pnpm rag:embed` first to generate the embeddings.');
  process.exit(1);
}

const db = new Database(DB_PATH);
sqliteVec.load(db);

// Read the embedding dimension from the meta table written by build_rag.py
const dimsRow = db.prepare("SELECT value FROM meta WHERE key = 'embed_dims'").get();
if (!dimsRow) {
  console.error('Error: meta table is missing embed_dims — run `pnpm rag:embed` first.');
  process.exit(1);
}
const DIMS = parseInt(dimsRow.value, 10);

// Drop any existing HNSW index (safe to rerun)
db.exec('DROP TABLE IF EXISTS vec_chunks');

// vec0 virtual table — sqlite-vec builds an HNSW graph at insert time.
// Uses L2 distance by default; for unit-normalized vectors (Qwen3 output)
// L2 ranking is equivalent to cosine similarity: ||a−b||² = 2 − 2·cos(θ).
db.exec(`
  CREATE VIRTUAL TABLE vec_chunks USING vec0(
    embedding FLOAT[${DIMS}]
  )
`);

const rows   = db.prepare('SELECT id, embedding FROM chunks').all();
const insert = db.prepare('INSERT INTO vec_chunks(rowid, embedding) VALUES (?, ?)');

// BigInt is required for the rowid binding — vec0 rejects JS Number type
db.transaction(() => {
  for (const row of rows) {
    const floats = new Float32Array(
      row.embedding.buffer,
      row.embedding.byteOffset,
      row.embedding.byteLength / 4,
    );
    insert.run(BigInt(row.id), JSON.stringify(Array.from(floats)));
  }
})();

const { n } = db.prepare('SELECT COUNT(*) as n FROM vec_chunks').get();
console.log(`Built HNSW index: ${n} vectors (FLOAT[${DIMS}]) → ${DB_PATH}`);

// Quick sanity: self-similarity of chunk 1 should be distance ≈ 0
const firstChunk = db.prepare('SELECT id, embedding FROM chunks LIMIT 1').get();
const queryFloats = new Float32Array(
  firstChunk.embedding.buffer,
  firstChunk.embedding.byteOffset,
  firstChunk.embedding.byteLength / 4,
);
const result = db.prepare(`
  SELECT v.rowid, v.distance, c.category
  FROM   vec_chunks v
  JOIN   chunks c ON c.id = v.rowid
  WHERE  v.embedding MATCH ? AND k = ?
  ORDER BY v.distance
`).all(JSON.stringify(Array.from(queryFloats)), BigInt(1));

const selfDist = result[0]?.distance ?? '?';
console.log(`Sanity check — chunk ${firstChunk.id} self-distance: ${Number(selfDist).toFixed(6)} (expect ≈ 0)`);

db.close();
