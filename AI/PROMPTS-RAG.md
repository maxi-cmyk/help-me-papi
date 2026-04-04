# RAG Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Context First**: Always provide `skills/SKILLS.md` and your data schema (sample JSON/CSV) as context before running these macros.
> 2. **Pipeline Chaining**: Use `DESIGN_RAG_PIPELINE` to set the architecture, then `IMPLEMENT_RETRIEVAL_LOGIC`.
> 3. **Statistical Integrity**: Use the `data-analysis-mastery.md` skill for all evaluation logic.

---

### **Stage 1: Pipeline Design**

#### **Macro: DESIGN_RAG_PIPELINE**
```markdown
[ROLE] You are a RAG Architect.
[CONTEXT] Analyze the `docs/PRD.md` and the sample dataset provided.
[TASK] Design an end-to-end RAG pipeline tailored for this use case.

[PILLAR CHECKLIST]
1. CHUNKING Strategy: Sentence-based, fixed-size with overlap, or semantic?
2. EMBEDDING Model: Selection based on latency vs accuracy (e.g. text-embedding-3-small).
3. VECTOR DB: Selection (Supabase pgvector, Pinecone, or Local).
4. RETRIEVAL: Top-k, MMR, or Hybrid search.

[OUTPUT]
1. ARCHITECTURE DIAGRAM: Mermaid.js flow of the ingestion and query pipes.
2. CHUNKING LOGIC: Python/JS snippet for optimal data splitting.
3. RETRIEVAL STRATEGY: Rationale for the chosen search parameters.
```

---

### **Stage 2: Implementation**

#### **Macro: IMPLEMENT_RETRIEVAL_LOGIC**
```markdown
[ROLE] You are an AI Engineer.
[CONTEXT] Paste the Vector DB schema and the Chunking Logic.
[TASK] Implement the retrieval function with re-ranking logic.

[REQUIREMENTS]
- Use Hybrid Search (Semantic + Keyword) if possible.
- Implement a Re-ranker (e.g. Cohere or simple Cross-Encoder).
- Add metadata filtering support (e.g. filter by user_id or category).

[OUTPUT]
Return the complete retrieval function code and a validation script to test "retrieval recall."
```

---

### **Stage 3: Evaluation & Optimization**

#### **Macro: EVALUATE_RAG_QUALITY**
```markdown
[ROLE] You are an AI Quality Auditor (LLM-as-a-Judge).
[CONTEXT] Paste the Query, Retrived Chunks, and Generated Answer.
[TASK] Score the response based on RAGAS metrics.

[METRICS]
1. FAITHFULNESS: Is the answer derived strictly from the chunks?
2. RELEVANCE: Does the answer address the query directly?
3. RETRIEVAL PRECISION: Are the retrieved chunks actually useful?

[OUTPUT] Scores (1-10) for each metric and a "Root Cause" analysis for low scores.
```
