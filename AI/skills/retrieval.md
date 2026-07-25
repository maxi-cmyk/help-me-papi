# Retrieval

Patterns for retrieval strategy, recall, ranking, and source selection.

## Strategy
- **Hybrid retrieval is the current default**: combine dense (embedding/vector) search with sparse (BM25/keyword) search and merge results (e.g. reciprocal rank fusion). Pure vector search alone under-performs on exact-match queries (IDs, error codes, proper nouns).
- Use metadata filters (date range, source, permission scope) *before* the similarity search where possible  filtering post-retrieval wastes the top-k budget on results you'll discard anyway.
- Query rewriting/expansion (have the LLM reformulate a vague user query into 23 search queries) meaningfully improves recall on conversational queries.

## Ranking
- Always **re-rank** the top-k candidates from initial retrieval with a cross-encoder (e.g. Cohere Rerank, a local cross-encoder model) before passing to the LLM  bi-encoder similarity search is a recall tool, not a precision tool.
- Typical pipeline: retrieve top 2050 candidates cheaply (vector/hybrid search) -> re-rank down to top 38 -> pass to LLM context.
- Track re-ranker latency separately from retrieval latency  it's usually the more expensive step and the one worth caching/batching.

## Filters
- Scope retrieval to the requesting user/tenant's permitted documents at the query layer, not by filtering the LLM's output  never let an unauthorized chunk reach the prompt.
- Recency filters/decay: for fast-changing corpora (docs, tickets), weight recent content higher unless the query is explicitly historical.
- Log which chunks were retrieved and cited per query  this is the dataset you'll need for eval and for debugging bad answers.
