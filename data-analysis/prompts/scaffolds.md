# Data Analysis Prompt Scaffolds

Use these YAML-formatted scaffolds to generate rigorous data analysis code. Each prompt is designed to reference the `standards.md` and `decisions.md` to ensure project-specific alignment.

---

## Initial Data Cleaning

```yaml
role: Data Quality Engineer
task: Load and validate a new hardware CSV dataset.
prompt: |
  Based on the data quality rules in `tools/data-analysis/standards.md`, generate a Python cell to load the CSV at [FILE_PATH]. 
  1. Attach a `source_file` column for provenance.
  2. Create masks for schema validation, duplicates, and invalid numeric values.
  3. Display a Data Quality Summary table comparing raw rows vs. cleaned rows.
```

---

## Statistical Hypothesis Testing

```yaml
role: Statistical Researcher
task: Test a hypothesis comparing two simulation groups.
prompt: |
  Compare the distributions of [GROUP_A] and [GROUP_B] for the metric [METRIC_NAME]. 
  1. Refer to `tools/data-analysis/standards.md` for non-parametric defaults.
  2. Calculate the Median and Bootstrap 95% Confidence Interval for each group.
  3. Perform a Mann-Whitney U test and print an explicit "SUPPORTED / NOT supported" verdict (alpha=0.05).
  4. Use a fixed `random_state=42` for reproducibility.
```

---

## Advanced Machine Learning Evaluation

```yaml
role: ML Engineer
task: Evaluate a model on right-skewed simulation outcomes with OOF diagnostics.
prompt: |
  Evaluate a [RandomForest/k-NN] model for predicting [TARGET] (right-skewed target).
  1. Apply a `log1p` transformation to the target before training.
  2. Implement a [StratifiedKFold/KFold] CV loop using parameters from `standards.md`.
  3. Generate an "Honest" scatter plot using `cross_val_predict` for Out-of-Fold (OOF) predictions.
  4. Back-transform the MAE via per-sample residuals in the original space.
  5. Define a `stamp` variable and version the model save using `joblib.dump(model, f'models/[NAME]_{stamp}.joblib')`.
```
