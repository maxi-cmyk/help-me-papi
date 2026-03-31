---
name: data-analysis
description: >
  Trigger this skill for any data analysis task — statistical testing, cross-validation,
  model evaluation, data cleaning, exploratory analysis, or notebook structure.
  Covers the full pipeline from raw CSV to defensible conclusions.
  Context: this user collects data from hardware experiments (ESP32 → CSV),
  analyses it in Jupyter notebooks, and tests hypotheses about physical/simulation systems.
  When triggered: (1) flag applicable checklist items for the current task,
  (2) prefer distribution-free methods unless normality is confirmed,
  (3) always surface data quality issues before analysis,
  (4) self-document all CV parameters in printed output.
---

# Data Analysis Skill

---

## 🔧 Self-Improvement Instructions

- **New method used** → add to the appropriate reference table with advantages, drawbacks, and when-to-use.
- **New pattern confirmed working** → add to the Analysis Checklist.
- **New library used** → add to Libraries table.
- **New project analysed** → add to Completed Analyses table.
- **Always scan the Analysis Checklist** at the start of every analysis response and flag applicable items.

---

## ✅ Analysis Checklist
> Scan at the start of every analysis response. Flag every applicable item.

| # | Rule | When It Applies |
|---|---|---|
| 1 | **Run data quality cell first** — file count, rows loaded vs cleaned, duplicate count, missing count, density/coverage gaps | Every notebook, before any plot or stat |
| 2 | **Validate source provenance** — `source_file`, `expected_id` vs actual `id`, check for filename/content mismatches | Any multi-file CSV load |
| 3 | **Drop duplicate keys before analysis** — `duplicated(subset=[id, session], keep='first')` | Any dataset with session/run structure |
| 4 | **Never suppress warnings globally** — `warnings.simplefilter('default')`, not `'ignore'` | Every notebook |
| 5 | **Choose non-parametric by default** — only use parametric (t-test, Pearson) if normality is confirmed | Small samples, skewed data, hardware experiments |
| 6 | **Print fold-size + derived params before CV** — n_splits, test fold size, train size, k for k-NN | Every cross-validation block |
| 7 | **Check for negative R² folds** — flag if any fold has R² < 0 (model worse than mean baseline) | Any regression CV |
| 8 | **Per-model try/except in CV loop** — one model failing shouldn't crash the whole cell | Multi-model CV |
| 9 | **State hypothesis verdict explicitly** — "SUPPORTED / NOT supported (alpha=0.05)" after the test | Any hypothesis test |
| 10 | **Add per-group error breakdown** — MAE/RMSE per density band, not just global | Regression on grouped data |
| 11 | **Comment bin boundary rationale** — explain offset bins (e.g. 14.5, 29.5) and hypothesis zone | Any `pd.cut` / binning |
| 12 | **Guard all stats with minimum sample sizes** — bootstrap ≥5, Spearman ≥8, Mann-Whitney ≥5 per group | All statistical tests |

---

## 📊 Statistical Methods Reference

### Non-Parametric Methods (prefer these by default)

| Method | Use When | Advantage | Drawback |
|---|---|---|---|
| **Bootstrap CI** | Estimating uncertainty on any statistic (median, mean, custom) | No distribution assumption; works on any sample size ≥5; estimates the actual sampling distribution from data | Computationally heavier; results vary slightly with seed (fix seed for reproducibility) |
| **Spearman ρ** | Correlation between two variables on skewed/ordinal data | Rank-based — outliers can't inflate it; no linearity assumption | Less powerful than Pearson when data actually is normal and linear |
| **Mann-Whitney U** | Comparing two independent groups (e.g. edge band vs outer bands) | No normality required; works on ordinal or continuous skewed data | Only tells you if distributions differ, not *how* — use with median/CI for effect size |
| **Kruskal-Wallis** | Comparing 3+ groups (extension of Mann-Whitney) | Non-parametric ANOVA equivalent | Post-hoc pairwise tests needed to identify which groups differ |

### Parametric Methods (use only when justified)

| Method | Use When | Advantage | Drawback |
|---|---|---|---|
| **Pearson r / t-test** | Data confirmed normal, n large enough for CLT | More statistical power when assumptions hold | Misleading on skewed small samples — right-skewed data (like generation counts) needs 100+ samples before CLT smooths it |
| **R² (coefficient of determination)** | Regression model evaluation | Intuitive — fraction of variance explained | Undefined on single-row test folds; negative when model is worse than mean baseline; not comparable across datasets with different variance |

### Key Relationships to Remember

- **R² = r² in simple linear regression** — R² is literally Pearson's r squared. In polynomial/multiple regression this relationship breaks (R² still valid, but no single r backs it out).
- **R² < 0** means SS_res > SS_tot — the model's predictions are further from truth than just predicting the mean. Formula: `R² = 1 − SS_res / SS_tot`.
- **Bootstrap and Mann-Whitney share a philosophy** — both avoid assuming a distribution shape. Use them together on the same dataset for consistent reasoning.
- **CLT convergence is slower for skewed data** — right-skewed distributions (hardware session lifespans, generation counts) need ~100+ samples before sample means look normal. Don't rely on CLT with small n.

---

## 🤖 Machine Learning / CV Reference

### Cross-Validation Guards

```python
# Classification — stratified k-fold
min_class_count = int(class_counts.min())
n_splits = min(5, min_class_count)          # never more folds than smallest class
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

max_test_size  = int(np.ceil(len(df) / n_splits))
min_train_size = len(df) - max_test_size
knn_k = min(5, max(1, min_train_size))      # k never exceeds training fold size

# Always print this before results (Checklist #6)
print(f'{n_splits}-fold CV (~{min_test_fold}–{max_test_size} test rows/fold, '
      f'{min_train_size} min train rows, k-NN k={knn_k})')
```

```python
# Regression — fold-aware split count
reg_splits = min(5, len(df) // 4)           # ensures multi-row test folds
```

### Why Scaling Matters for k-NN but Not Decision Trees

| Model | Scaling needed? | Reason |
|---|---|---|
| k-NN | **Yes** — always use `StandardScaler` | Distance-based: a feature with range 0–40 dominates one with range 0–1 by ~1600× in squared Euclidean distance |
| Decision Tree | **No** | Threshold-based splits — only ordering matters, not magnitude |
| Logistic Regression | **Yes** — gradient descent converges faster | Large feature scales cause slow/unstable convergence |
| Linear Regression | Technically no, but good practice | Coefficients become hard to interpret without it |

### Negative R² — What It Means

A negative R² on a fold means the quadratic fit is *actively worse* than just predicting `mean(y_train)` for every point. Common causes:
- Fold contains outliers the model was never trained on
- Dataset too small — a few anomalous test rows spike SS_res
- Model genuinely doesn't explain the target variable

Always flag: `neg_r2_folds = (reg_scores['test_r2'] < 0).sum()`

---

## 🗂️ Notebook Structure Pattern

The structure that works well for hardware experiment analysis:

```
Cell 0:  Markdown — title, pipeline overview, hypothesis statement
Cell 1:  Imports (warnings.simplefilter('default'), NOT 'ignore')
Cell 2:  Markdown — load section description
Cell 3:  Load & validate code (schema check, provenance, clean, bin)
Cell 4:  Markdown — quality section description
Cell 5:  Data quality summary (always first, before any plot)
Cell 6:  Markdown — EDA section
Cell 7:  Exploratory plots (scatter grid + boxplot by band)
Cell 8:  Markdown — stats section + method rationale
Cell 9:  Statistics code (bootstrap CI, Spearman, Mann-Whitney + verdict)
Cell 10: Markdown — ML section + guard thresholds
Cell 11: ML code (classification CV + regression CV)
Cell 12: Markdown — next steps
```

Key principles:
- **Markdown explains *why*, code shows *how*** — don't put rationale in comments alone
- **Each section is self-contained** — a reader can run cells top-to-bottom and understand every decision
- **Guards before models** — every model block has a minimum-sample guard that prints a clear message instead of crashing

---

## 🧹 Data Quality Pattern

Standard checks for hardware CSV pipelines:

```python
# Per-file: schema + provenance
frame['source_file']    = path.name
frame['expected_run_id'] = path.stem
# → later: filename_mismatch_mask = raw_df['run_id'] != raw_df['expected_run_id']

# After concat: clean masks
invalid_reason_mask  = ~raw_df['endReason'].isin(valid_reasons)
invalid_numeric_mask = raw_df[numeric_cols].isna().any(axis=1)
duplicate_mask       = raw_df.duplicated(subset=['run_id', 'session'], keep='first')

# Quality summary table — always display before any analysis
pd.DataFrame({
    'metric': ['files_loaded', 'rows_loaded', 'rows_after_cleaning',
               'bad_rows_removed', 'duplicates_removed', 'filename_mismatches'],
    'value':  [len(files), raw_row_count, len(df),
               bad_row_count, duplicate_count, filename_mismatch_count]
})
```

---

## 📚 Libraries (confirmed used)

| Library | Purpose | Key Functions |
|---|---|---|
| `pandas` | Data loading, cleaning, groupby summaries | `read_csv`, `pd.cut`, `groupby().agg()`, `duplicated`, `pd.to_numeric` |
| `numpy` | Numerical operations, array math | `np.percentile`, `np.median`, `np.ceil`, `np.arange` |
| `scipy.stats` | Non-parametric tests | `spearmanr`, `mannwhitneyu`, `shapiro`, `ks_2samp` |
| `scikit-learn` | ML models, CV, pipelines | `StratifiedKFold`, `KFold`, `cross_validate`, `Pipeline`, `StandardScaler` |
| `matplotlib` / `seaborn` | Plots | `scatterplot`, `boxplot`, `sns.set_theme` |

---

## 📁 Completed Analyses

| Project | Dataset | Key Findings | Methods Used |
|---|---|---|---|
| Conway's Game of Life (Phase 6) | ESP32 dashboard CSV exports — density vs simulation outcome | Hypothesis: 30–40% density maximises session lifespan. Tested with Mann-Whitney + bootstrap CI. Quadratic regression + per-band MAE to assess model fit in hypothesis zone. | Bootstrap CI, Spearman ρ, Mann-Whitney U, stratified k-fold, quadratic regression CV |

---

## ⚠️ Common Mistakes & Fixes

| Mistake | Why It's Bad | Fix |
|---|---|---|
| `warnings.filterwarnings('ignore')` | Hides undefined R², convergence failures, small-sample warnings — bad runs look valid | `warnings.simplefilter('default')` |
| k-NN k chosen from total dataset size | On small datasets a fold can have fewer training rows than k → invalid scores | `knn_k = min(5, max(1, min_train_size))` |
| R² with 1-row test folds | R² undefined on single sample | `reg_splits = min(5, len(df) // 4)` ensures multi-row folds |
| Pearson/t-test on skewed small samples | Normality not satisfied → p-values misleading | Use Spearman + Mann-Whitney + bootstrap CI |
| Reporting only global MAE | Hides whether model fails specifically in the hypothesis zone | Add per-band `groupby` MAE breakdown |
| Hypothesis test with no verdict | Reader must interpret p-value themselves | Print "SUPPORTED / NOT supported (alpha=0.05)" explicitly |
