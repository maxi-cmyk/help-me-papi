## Why Scaling Matters for k-NN but Not Decision Trees

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