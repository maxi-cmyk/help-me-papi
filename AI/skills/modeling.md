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
