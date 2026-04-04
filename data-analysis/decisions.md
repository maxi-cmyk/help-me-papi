# Data Analysis Decisions

This document records the philosophical and technical architectural choices for data analysis in this project.

## Statistical Philosophy

### Non-Parametric by Default
**Decision**: Use non-parametric methods (Bootstrap CI, Spearman , Mann-Whitney U) as the default analytical path.
**Rationale**: Hardware-generated data (e.g., ESP32 simulation exports) is frequently skewed and small-sample-driven. Relying on Pearson or t-tests without explicit normality confirmation can lead to misleading conclusions.

### Alpha Level Consistency
**Decision**: Standardize on `alpha=0.05` for all hypothesis tests.
**Rationale**: Adhering to the project's standard ensures comparability across experiments and over time.

---

## Technical Stack

### Python Scientific Stack
**Decision**: Standardize on the following libraries:
- **`pandas`**: Data manipulation and cleaning.
- **`numpy`**: Numerical and array operations.
- **`scipy.stats`**: Statistical testing engine.
- **`scikit-learn`**: Machine learning and cross-validation.
- **`matplotlib` / `seaborn`**: Visualization standards.
- **`joblib`**: Model persistence and versioning.

### Notebook Structure
**Decision**: Follow a strict cell-based notebook pattern.
**Rationale**: Self-contained notebooks improve readability for both humans and AI models. This structure ensures that every analysis session starts from a validated data state.

---

## Modeling and Evaluation

### Log Transformation Pattern
**Decision**: Use `log1p` when the target (e.g., generation counts, session lifespans) has a heavy right tail.
**Rationale**: Equal gaps in log space correspond to equal *ratios* in original space rather than equal differences. A log-space error of 0.04 represents a ~4% proportional error, ensuring consistent evaluation across all session lifespans.

### Back-Transforming MAE
**Decision**: Always compute residuals in the original space first before deriving the mean.
**Rationale**: Due to Jensen's inequality, an `expm1` of the mean log error does not equal the mean real error. Back-transforming per sample is mandatory for defensible metric reporting.

### Out-of-Fold (OOF) Evaluation
**Decision**: Use `cross_val_predict` for all diagnostic scatter plots and residual analysis.
**Rationale**: Never plot predictions on training data. OOF predictions ensure that each data point is predicted by a model that never encountered it during training, preventing circular reasoning and training leakage.

### Model Persistence
**Decision**: Pre-define a `stamp` (e.g., `datetime.now().strftime('%Y%m%d')`) before all modeling blocks and use it for `joblib` save paths.
**Rationale**: Silent overwriting destroys baseline comparisons. Versioning models with timestamps allows for honest tracking of historical performance improvements.

---

## Model Selection Guide

| Model | Choose When | Key Constraint | Rationale |
|---|---|---|---|
| **k-NN** | Small, clean datasets with clear distance metrics. | **Scaling Mandatory** | Highly sensitive to feature magnitude; distance-based. |
| **Random Forest** | Noisy hardware datasets; non-linear relationships. | **None** | Robust to outliers via bootstrap/subsampling. |
| **Decision Tree** | Simple, interpretable rules; rapid prototyping. | **Depth Guards** | Prone to overfitting on small data without constraints. |
| **Linear/Logistic** | Baseline linear relationships; fast convergence. | **Scaling Rec.** | Efficient for large-scale data; gradient-basis. |

---

## Hyperparameter Search
**Decision**: Use Nested Cross-Validation for hyperparameter selection.
**Rationale**: Standard CV scores obtained during hyperparameter search are optimistically biased. Nested CV ensures an honest estimate of model performance by isolating the search process within an inner loop.
