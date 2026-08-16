# Modeling

Notes on problem framing, objective selection, and model choice  covers both traditional ML models and LLM/API model selection.

## Objectives
- Pick the metric the business actually cares about before picking the algorithm (e.g. recall matters more than precision for fraud detection; the reverse for spam filtering). Optimizing the wrong metric is the single most common modeling mistake.
- For LLM-backed features, define the objective as an evaluable outcome (task success rate, faithfulness score, latency budget)  see `AI/skills/evaluation.md` for how to measure it.

## Baselines
- Always start with the simplest baseline that could plausibly work (logistic regression, a rules-based heuristic, or a single well-crafted prompt to a frontier model) before reaching for something heavier. It sets the bar every subsequent iteration has to beat.
- For LLM tasks: baseline with the strongest available model and a minimal prompt first. This tells you whether the task is even model-solvable before you invest in fine-tuning, RAG, or a smaller/cheaper model.

## Model Selection (cost / latency / quality tradeoffs)
Model choice for an LLM-backed feature is a three-way tradeoff, not a single "best model" decision:
- **Quality-critical, latency-tolerant** (complex reasoning, one-shot document analysis, code generation): use the frontier model for the task; the cost is usually justified by correctness.
- **Latency-critical, high-volume** (autocomplete, real-time chat turns, classification/routing): use a small/fast model, or a distilled/fine-tuned model for the narrow task  frontier-model latency will visibly hurt UX at these call volumes.
- **Cost-sensitive, high-volume**: batch requests where possible, cache aggressively (exact-match and semantic caching), and route simple queries to a cheap model while escalating only the hard cases to a stronger one (model routing / cascade).
- Re-evaluate model choice regularly  the cost/latency/quality frontier shifts every few months as new models ship; a routing decision made 6 months ago is worth re-benchmarking.
- Always benchmark candidate models against the golden eval set (see `evaluation.md`), not vibes  a "smarter-sounding" model isn't necessarily better on your specific task.

---

## Multi-Modal Analysis Pipeline 

When the product analyzes real-world media (video, audio, documents) and turns signals into actionable feedback:

### Pipeline Architecture
The analysis is too heavy for a request/response cycle. Use a queue + worker:
```
Upload → FastAPI → Redis queue → Celery/BullMQ worker → FFmpeg + MediaPipe + Librosa + OpenAI → Supabase → signed URLs → frontend
```

### Deterministic Pre-Checks First
Before invoking any LLM, run **cheap deterministic checks** that catch bad input immediately:
- Video: framing, lighting, face visibility, audio level, clipping, silence, duration.
- Document: file type, size, OCR confidence.
- Audio: sample rate, channel count, SNR.

If pre-checks fail, reject early with a clear message. Don't spend tokens analyzing unusable input.

### Grounded LLM Outputs
The LLM should narrate **facts that already exist in the analysis**, not invent assessments:
- Pass structured metrics (pacing WPM, pitch variation Hz, filler count, eye-contact %) as the prompt context.
- Instruct the model: "Base coaching only on these metrics. Do not invent claims about the speaker's personality, emotion, or medical state."
- Add a deterministic coaching fallback: if the LLM fails/times out, produce coaching from rule-based templates keyed on the metrics.

### Pinned Models + Eval Sets
- Pin the exact model version (`gpt-4o-2024-08-06`, not `gpt-4o`). Models change behavior silently; pinning makes regression detection possible.
- Build a golden eval set of (video, expected_metrics, expected_coaching_highlights) triples. Re-run after every prompt/model change.
- Separate the **scoring** (deterministic, testable) from the **coaching narration** (LLM-generated, evaluator-judged). Score correctness is a unit test; coaching quality is an eval.

### Worker Hygiene
- Heavy ML pipelines (MediaPipe, Librosa, FFmpeg) leak memory across jobs. **Restart the worker after each full analysis** to release memory. Queue durability (Redis) ensures no job is lost.
- Temporary local artifacts (extracted audio, landmark files) should expire (e.g., 24h TTL). Final reports persist in Supabase.
- Process one analysis at a time per worker. Concurrency fights over GPU/memory and degrades accuracy.

### Classification Caution
- Results describe **observable rehearsal signals**. Explicitly disclaim: not medical, psychological, personality, anxiety, or employment assessments. This isn't a legal nicety — it keeps the product honest about what it can and cannot say.
