# Audit Report

## Scope
- Reviewed `services/rag/build_rag.py`
- Reviewed `packages/functions/src/chat.ts`
- Reviewed `services/rag/requirements.txt`

## Findings

### 1. `services/rag/build_rag.py`

Strengths:
- Clear data pipeline: curated markdown → chunking → embedding → SQLite.
- Good separation of concerns: cleaning, section-aware chunking, embedding, and storage.
- Uses environment variable `OPENROUTER_API_KEY` instead of in-repo secret.

Issues / recommendations:
- Error handling in `embed_chunks()` is minimal.
  - Add retries / backoff for transient HTTP failures and 429/5xx responses.
  - Validate API response shape before indexing into `resp.json()["data"][0]`.
- `requests.post()` is called once per chunk.
  - Consider batching the embedding requests if the API supports it to reduce latency and cost.
- `clean_text()` has a strong PDF extraction focus, but the code should still guard against empty or malformed input.
- Dependency pins in `requirements.txt` are broad (`>=`).
  - For public repos, prefer tighter version constraints or a lock file to improve reproducibility.
- `sqlite_vec.load(conn)` loads a SQLite extension at runtime.
  - This is acceptable when controlled, but document the dependency clearly and ensure the extension is available in deployment environments.

### 2. `packages/functions/src/chat.ts`

Strengths:
- Reuses `OpenRouter` and caches the SQLite connection across warm invocations.
- Includes origin validation and CORS header handling.
- Validates JSON request body and caps question length.
- Builds a constrained assistant prompt with explicit scope and formatting rules.

Issues / recommendations:
- `ALLOWED_ORIGIN` is optional and defaults to `*`.
  - For production, set `ALLOWED_ORIGIN` explicitly to the portfolio domain to reduce exposure.
- The handler does not explicitly handle a missing or empty `context` from the vector search.
  - Add a fallback response if no relevant chunks are found to avoid hallucinations.
- Response handling from `openRouter.chat.send()` assumes a valid choice structure.
  - Add a fallback or validation for unexpected message payloads.
- The `catch` branch inspects `e.status` but does not verify the exception type.
  - Improve error classification to avoid masking unrelated failures.

### 3. `services/rag/requirements.txt`

Observations:
- Includes necessary packages for the current pipeline.
- `llama-index-core` and `llama-index-readers-file` may change upstream.
- `sqlite-vec>=0.1.0` may introduce compatibility differences if upstream releases break APIs.

Recommendations:
- Pin dependency versions more narrowly to reduce installation drift.
- Document any platform-specific build requirements for `pymupdf` and `sqlite-vec`.
- Consider adding a `requirements.lock` or Docker-based reproducible environment if the project is intended for public use.

## Summary

The reviewed code is architecturally reasonable and avoids obvious hardcoded secrets. The main improvements are around hardening API error handling, making deployment-configurable security tighter, and locking dependency versions for reproducibility.
