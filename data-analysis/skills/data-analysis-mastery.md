---
name: data-analysis-mastery
description: Mastery skill for performing rigorous data analysis on hardware experiment results and simulation datasets.
---

# Data Analysis Mastery

This mastery skill encapsulates the framework for high-level data analysis, focusing on statistical integrity, machine learning best practices, and reproducible notebook structures.

## Core Principles

1. **Statistical Integrity over Speed**: Prioritize defensible conclusions and clear hypothesis verdicts over rapid modeling.
2. **Contextual Awareness**: All analysis must account for the specific constraints of hardware-generated data (e.g., ESP32 simulation lifespans).
3. **Reproducibility**: Use fixed seeds and clearly documented parameters for all statistical and machine learning operations.

---

## Navigating the Analysis Domains

For specialized data tasks, manually attach the following context files to your prompt to ensure a high standard of generation:

### 1. [Analysis Standards](../standards.md)
**When to attach**: For any task involving data loading, cleaning, or statistical testing. Includes mandatory checklists for data quality and hypothesis verdicts.

### 2. [Analytical Decisions](../decisions.md)
**When to attach**: When making architectural choices about modeling, cross-validation strategies, or justifying the use of specific scientific libraries.

### 3. [Analysis Scaffolds](../prompts/scaffolds.md)
**When to attach**: When generating code for initial cleaning, statistical comparison, or machine learning evaluation loops.

---

## Technical Reference

### Statistical Methods
- **Non-Parametric**: Bootstrap CI, Spearman , Mann-Whitney U, Kruskal-Wallis.
- **Parametric**: Pearson r, t-test, R (use only when normality is confirmed).

### Machine Learning Patterns
- **Log-Transformation**: Use `log1p(y)` and `expm1(y_pred)` for right-skewed simulation targets (e.g., generation counts).
- **Evaluation**: Never plot predictions on training data; use `cross_val_predict` for out-of-fold (OOF) residuals.
- **Persistence**: Date-stamp all `joblib` saves using a pre-defined `stamp` variable to preserve baselines.
- **Hyperparameters**: Bias towards Random Forest for noisy data; use Nested CV for honest performance estimates.

---

## Completed Analyses

| Project | Dataset | Key Findings | Methods Used |
|---|---|---|---|
| Conway's Game of Life (Phase 6) | ESP32 dashboard CSV exports  density vs outcome | Hypothesis: 3040% density maximizes lifespan. Phase transitions confirmed at 42%, 53%, and 54% (sharp stability drops). | Bootstrap CI, Spearman , Mann-Whitney U, RF classifier/regressor, OOF scatter plots. |

---

## Notebook Structure Pattern

Refer to this structure before generating any analysis notebook:

1. **Cell 0**: Markdown Title, Pipeline, and Hypothesis.
2. **Cell 1**: Standard Imports (`warnings.simplefilter('default')`).
3. **Cell 2**: Load & Validate (schema + provenance).
4. **Cell 3**: Data Quality Summary (always before analysis).
5. **Cell 4**: Exploratory Data Analysis (EDA) and visualizations.
6. **Cell 5**: Statistical Testing (method rationale + verdict).
7. **Cell 6**: Machine Learning modeling and OOF evaluation.
8. **Cell 7**: Next Steps and Conclusions.
