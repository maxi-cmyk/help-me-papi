---
name: ai-mastery
description: Mastery skill for AI-related research, machine learning workflows, and RAG implementation.
---

# AI and Machine Learning Mastery

This mastery skill governs the architecture and implementation of AI-driven systems, ranging from pure machine learning pipelines to retrieval-augmented generation (RAG) setups.

## Core Principles

1. **Context Isolation**: Strictly define the boundaries of the AI's knowledge to prevent hallucinations and context leakage.
2. **Evaluation First**: Never deploy an AI feature without a clear evaluation framework (e.g., RAGAS for RAG or standard ML metrics for modeling).
3. **Prompt Scaffolding**: Use token-efficient templates that delegate domain knowledge to external context files.

---

## Navigating the AI Domains

For specialized AI tasks, manually attach the following context files to your prompt to ensure the highest standard of generation:

### 1. [RAG Implementation and Retrieval](../RAG/guidelines.md)
**When to attach**: When building or refining retrieval-augmented generation systems. Includes standards for chunking strategies, vector database configurations, and retrieval optimization.

### 2. [Machine Learning and Modeling](../ML/guidelines.md)
**When to attach**: For tasks involving model training, data preprocessing, feature engineering, and evaluation of traditional ML or deep learning models.

---

## Execution Workflow

1. Define the specific AI task (RAG improvement, model training, etc.).
2. Attach the relevant domain `guidelines.md` or `skills/` from the navigation above.
3. Use the localized `PROMPTS.md` in each domain for specific task execution.
