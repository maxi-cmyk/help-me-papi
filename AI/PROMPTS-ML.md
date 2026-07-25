# ML Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Context First**: Always provide `skills/data-analysis-mastery.md` and your dataset metadata before running these macros.
> 2. **Notebook Standards**: All Python output must follow the "Statistical Integrity" guidelines (reproducible seeds, explicit hypothesis testing).
> 3. **Validation**: Every training macro requires a "Degradation Check" to ensure the model doesn't overfit.

---

### **Stage 1: Exploration & Preprocessing**

#### **Macro: EDA_AND_PREPROCESSING**
```markdown
[ROLE] You are a Data Scientist focusing on Exploratory Data Analysis.
[CONTEXT] Analyze the dataset description/head and the `docs/PRD.md`.
[TASK] Perform a rigorous EDA and prepare the preprocessing pipeline.

[CHECKLIST]
1. MISSING DATA: Strategy for imputation vs removal.
2. FEATURE ENGINEERING: Suggest 3-5 derived features based on domain logic.
3. DISTRIBUTIONS: Visualize skewness and suggest transformations (e.g. Log, Box-Cox).
4. CORRELATIONS: Multi-collinearity check.

[OUTPUT]
1. CLEANING SCRIPT: Python code for the preprocessing pipeline.
2. INSIGHTS REPORT: Bulleted list of data anomalies or opportunities.
3. VISUALIZATION CODE: Matplotlib/Seaborn snippets for key distributions.
```

---

### **Stage 2: Model Training**

#### **Macro: SCAFFOLD_TRAINING_LOOP**
```markdown
[ROLE] You are a Machine Learning Engineer.
[CONTEXT] Paste the Preprocessing Pipeline and the Target Objective.
[TASK] Scaffold a production-ready training loop.

[REQUIREMENTS]
- Use `scikit-learn`, `PyTorch`, or `XGBoost` as specified in `techStack.md`.
- Implement K-Fold Cross Validation.
- Include Experiment Tracking (e.g. MLflow or simple JSON logging).
- Automated Early Stopping based on validation loss.

[OUTPUT]
The complete training script including hyperparameter configuration and evaluation hooks.
```

---

### **Stage 3: Evaluation & Error Analysis**

#### **Macro: ANALYZE_MODEL_FAILURE**
```markdown
[ROLE] You are a Model Auditor.
[CONTEXT] Paste the Confusion Matrix, Loss Curves, and Misclassified Samples.
[TASK] Perform a deep-dive error analysis.

[DIAGNOSTIC STEPS]
1. BIAS CHECK: Is the model failing on specific feature slices?
2. OVERFITTING: Compare Training vs Validation curves for "The Gap."
3. RESIDUAL ANALYSIS: For regression, check if residuals are i.i.d.

[OUTPUT]
A prioritized list of "Next Experiments" (e.g. data augmentation, regularization increase, or feature pruning).
```

#### **Macro: SELECT_MODEL_FOR_TASK**
```markdown
[ROLE] You are an ML/AI Platform Engineer making a build-vs-buy, model-selection call.
[CONTEXT] Describe the task, expected call volume, latency budget, and quality bar.
[TASK] Recommend a model (or routing/cascade strategy) with an explicit cost/latency/quality tradeoff analysis.

[DECISION FRAMEWORK]
1. QUALITY FLOOR: What accuracy/faithfulness score is the minimum acceptable (tie to `AI/skills/evaluation.md` metrics)?
2. LATENCY BUDGET: Real-time (<300ms), interactive (<2s), or async/batch?
3. VOLUME & COST: Requests/day and $/1k-tokens tradeoff  does a routing/cascade (cheap model first, escalate on low confidence) beat a single frontier model?
4. BENCHMARK: Test top 23 candidate models against the golden eval set, not general leaderboards  task-specific performance is what matters.

[OUTPUT] A recommendation table (model, est. cost/1k requests, p95 latency, eval score) and the final pick with rationale.
```
