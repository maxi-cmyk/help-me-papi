# RAG Evaluation

Ways to measure retrieval quality, answer grounding, and failure modes. Eval-driven development means these checks exist *before* you ship a prompt/pipeline change, not after users complain.

## Metrics
- **Retrieval**: recall@k (did the right chunk make it into top-k?), precision@k, MRR (mean reciprocal rank of the first relevant hit).
- **Generation / grounding** (RAGAS-style):
  - **Faithfulness**: is every claim in the answer supported by the retrieved chunks? (catches hallucination)
  - **Answer relevance**: does the answer actually address the question asked?
  - **Context precision/recall**: were the retrieved chunks the right ones, and were all necessary chunks retrieved?
- Track cost and latency (p50/p95) alongside quality metrics  a 2% quality gain that doubles latency or cost is not automatically a win.

## Test Sets
- Build a golden eval set of realistic (query, expected_chunks, expected_answer) triples early  even 3050 hand-labeled examples catch most regressions.
- Include adversarial/edge cases: queries with no good answer in the corpus (the system should say "I don't know," not hallucinate), ambiguous queries, and queries that need multi-chunk synthesis.
- Re-run the eval set on every prompt, chunking, or retrieval-parameter change. Treat it like a test suite, not a one-off audit  wire it into CI if the pipeline is a real product surface.
- Use an LLM-as-judge for scoring at scale, but spot-check its scores against human judgment periodically  judge models drift and have their own biases.

## Failure Review
- When an answer is wrong, classify the failure before fixing it: **retrieval miss** (right chunk never surfaced), **ranking miss** (right chunk surfaced but buried below top-k), or **generation miss** (right chunks present, LLM still got it wrong/hallucinated).
- Different failure classes need different fixes  more chunking granularity or hybrid search for retrieval misses, a better re-ranker for ranking misses, tighter grounding prompts or guardrails for generation misses. Don't reach for a bigger model as the default fix for every failure class.
- Keep a running log of real failure cases from production; feed the worst ones back into the golden eval set so they can't silently regress again.
