# Project Report Content

## 1. Introduction & Executive Summary
Academic performance prediction enables educational stakeholders and students to identify academic risk early, set realistic milestone targets, and optimize time management. This project delivers a production-grade, browser-based analytics system tailored to the VIT Bhopal University assessment structure, applying Multiple Linear Regression (OLS) alongside automated regulatory rule evaluation.

## 2. Methodology & Model Architecture
The system employs Multiple Linear Regression:

$$\hat{y} = \beta_0 + \sum_{i=1}^{p} \beta_i x_i$$

### Predictor Variables ($x_i$):
1. **Study Hours ($x_1$)**: Daily self-study hours.
2. **Attendance Percentage ($x_2$)**: Overall course attendance.
3. **CAM Percentage ($x_3$)**: Continuous assessment score percentage.
4. **Previous Final Score ($x_4$)**: Prior academic achievement.
5. **CAT-1 Raw Mark ($x_5$)**: Continuous assessment test 1 score (/50).
6. **CAT-2 Raw Mark ($x_6$)**: Continuous assessment test 2 score (/50).
7. **TEE Raw Mark ($x_7$)**: Term-end examination score (/100).

### Mathematical Optimization:
Coefficients $\boldsymbol{\beta}$ are determined analytically using the Ordinary Least Squares (OLS) normal equations:

$$\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

Solved numerically via Gaussian elimination with partial pivoting in native JavaScript.

## 3. VIT Bhopal Academic Assessment Framework
Conforming to the revised regulations dated 10 July 2026:

$$\text{Internal Marks (70)} = \text{CAM (35)} + \text{Att (5)} + \left(\frac{\text{CAT1}}{50} \times 15\right) + \left(\frac{\text{CAT2}}{50} \times 15\right)$$

$$\text{TEE Contribution (30)} = \frac{\text{TEE}}{100} \times 30$$

$$\text{Final Score (100)} = \text{Internal (70)} + \text{TEE (30)}$$

### Mandatory Pass Constraints:
1. **Attendance Threshold**: $\text{Attendance} \ge 75\%$.
2. **TEE Minimum Floor**: $\text{TEE} \ge 40 / 100$.
3. **Aggregate Raw Threshold**: $\text{CAT1} + \text{CAT2} + \text{TEE} \ge 80 / 200$.

## 4. Exam Target & Study Planning Heuristic
- Minimum CAT-2 required for pass given CAT-1 and target TEE:
  $$\text{Min CAT-2} = \max(0, 80 - \text{CAT1} - \text{TEE}_{\text{target}})$$
  Feasible if $\text{Min CAT-2} \le 50$.
- Minimum TEE required for pass given CAT-1 and CAT-2:
  $$\text{Min TEE} = \max(40, 80 - \text{CAT1} - \text{CAT2})$$
  Feasible if $\text{Min TEE} \le 100$.
- Daily study hour allocation:
  $$H_{\text{rec}} = \text{clamp}\left(2.0 + 2.5 \times (\Delta_{\text{CAT2}} + \Delta_{\text{TEE}}) + 3.0 \times \Delta_{\text{desired}},\; 2.0,\; 8.0\right)$$

## 5. Experimental Results & Model Evaluation
The dataset consists of 240 simulated records partitioned into 192 training records (80%) and 48 testing records (20% holdout).

| Metric | Linear Regression | Naive Mean Baseline | Improvement |
|---|---|---|---|
| **Mean Absolute Error (MAE)** | **1.13 marks** | 8.86 marks | **87.2% reduction** |
| **Root Mean Squared Error (RMSE)** | **1.32 marks** | 10.15 marks | **87.0% reduction** |
| **Coefficient of Determination ($R^2$)** | **0.983** | 0.000 | **High explained variance** |

## 6. Implementation Integrity
- Implemented as a self-contained Python terminal application in `main.py`.
- Uses only Python standard-library modules; no external packages, npm packages, server processes, or database are required.
- Designed for reproducible command-line execution on a Python 3.9+ environment.
