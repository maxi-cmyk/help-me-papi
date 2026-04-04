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
