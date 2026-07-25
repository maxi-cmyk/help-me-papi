# Chunking

Notes on splitting strategy, metadata, and context assembly.

## Chunk Size
- Default to **semantic chunking** (split on headings/paragraphs, then cap size) over naive fixed-size splitting  it keeps related ideas together and improves retrieval precision.
- Fixed-size fallback: 400800 tokens per chunk with 1015% overlap. Overlap prevents context from being severed mid-idea at chunk boundaries.
- For code: chunk by function/class boundary (AST-aware splitting), never by raw line count  a chunk that cuts a function in half is useless to the retriever.
- For tables/structured data: keep the header row attached to every chunk derived from that table.

## Metadata
- Attach source (file/URL), section heading, and position (chunk N of M) to every chunk  this is what makes citations and re-ranking possible.
- Store a `parent_id` linking a chunk back to its full document for "expand context" retrieval (fetch the chunk, then pull the surrounding chunks if the LLM needs more).
- Timestamp/version metadata matters for any corpus that changes over time  stale chunks should be filterable or re-embedded on a schedule.

## Tradeoffs
- Smaller chunks -> higher retrieval precision, but risk losing surrounding context the LLM needs to answer well.
- Larger chunks -> more context per hit, but dilutes the embedding (a chunk about 3 different topics embeds poorly for any single one).
- When in doubt, chunk smaller and rely on **context expansion** (grab neighboring chunks after retrieval) rather than chunking large and hoping the embedding stays precise.
