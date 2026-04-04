# Data Analysis Standards

This document establishes the mandatory rules and checklists for all data analysis tasks. Following these standards ensures that project conclusions are statistically defensible and data-driven.

## Analysis Checklist

| # | Rule | Application |
|---|---|---|
| 1 | **Data Quality First**  Run a data quality cell covering file count, rows loaded vs. cleaned, duplicate count, and missing values. | Every notebook, before any analysis. |
| 2 | **Validate Source**  Check for filename/content mismatches and ensure `source_file` provenance match. | Any multi-file CSV load. |
| 3 | **Drop Duplicates**  Always drop duplicate session/run keys before performing statistical tests. | Any dataset with a session/run structure. |
| 4 | **No Warning Suppression**  Never suppress warnings globally. Use `warnings.simplefilter('default')`. | Every notebook. |
| 5 | **Non-Parametric by Default**  Use distribution-free methods (Bootstrap, Spearman, Mann-Whitney) unless normality is explicitly confirmed. | Small samples, skewed datasets. |
| 6 | **Document CV Parameters**  Print `n_splits`, test fold size, train size, and model-specific parameters (e.g., k for k-NN). | Every cross-validation block. |
| 7 | **Guard Against Inf/Nan**  Check for negative R folds and Infinite/NaN values in derived features. | Any regression analysis. |
| 8 | **Explicit Hypothesis Verdict**  State verdicts clearly as "SUPPORTED / NOT supported (alpha=0.05)" after every test. | Any hypothesis test. |
| 9 | **Group-Specific MAE**  Always provide per-group error breakdown (e.g., MAE per density band). | Grouped regression analysis. |
| 10 | **Statistical Guards**  Ensure minimum sample sizes (Bootstrap 5, Spearman 8, Mann-Whitney 5 per group). | All statistical tests. |
| 11 | **OOF Predictions Only**  Never plot `model.predict(X_train)`. Always use `cross_val_predict` for out-of-fold scatter plots. | Any regression/classification plot. |
| 12 | **MAE in Original Units**  Back-transform MAE via per-sample residuals for log-transformed targets, not `expm1(mean_log_error)`. | Any log-transformed regression target. |
| 13 | **Versioned Model Saves**  Always date-stamp `joblib` filenames to preserve baselines for comparison. | Any `joblib.dump` call. |
| 14 | **Pre-Defined Stamp**  Define the `stamp` variable (today's date) before any model block to prevent save crashes. | Notebooks with both classifier and regressor. |

## Data Quality Pattern

Standard checks for hardware-export CSV pipelines include the following masks:

- **Schema Check**: Confirm all expected columns are present.
- **Provenance Check**: Confirm `raw_df['run_id'] == raw_df['expected_run_id']`.
- **Cleaning Masks**: Identify rows removed due to invalid numeric data, invalid reasons, or duplication.

## Statistical Confidence

- **Alpha Level**: Use `alpha=0.05` as the standard threshold for significance.
- **Effect Size**: Always report effect sizes (e.g., Median + Bootstrap CI) alongside p-values.
- **Reproducibility**: Fix random seeds (e.g., `random_state=42`) for all bootstrap and machine learning operations.
