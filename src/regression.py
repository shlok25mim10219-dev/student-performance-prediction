"""Multiple Linear Regression implemented with the Python standard library."""
import math
from .config import FEATURES

def vector(row):
    return [1.0] + [row[k] for k in FEATURES]

def solve_linear(A, b):
    """Gauss-Jordan elimination with partial pivoting."""
    n = len(b)
    a = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            raise ValueError("Singular matrix while fitting regression model.")
        a[col], a[pivot] = a[pivot], a[col]
        p = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= p
        for r in range(n):
            if r == col:
                continue
            factor = a[r][col]
            if factor:
                for j in range(col, n + 1):
                    a[r][j] -= factor * a[col][j]
    return [a[i][n] for i in range(n)]

def fit(rows):
    """Fit ordinary least-squares multiple linear regression."""
    n = len(FEATURES) + 1
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    for row in rows:
        x = vector(row)
        for i in range(n):
            for j in range(n):
                A[i][j] += x[i] * x[j]
            b[i] += x[i] * row["final"]
    return solve_linear(A, b)

def predict(beta, row):
    return sum(a * b for a, b in zip(vector(row), beta))

def evaluate(rows, beta):
    errors = [r["final"] - predict(beta, r) for r in rows]
    mae = sum(abs(e) for e in errors) / len(errors)
    rmse = math.sqrt(sum(e * e for e in errors) / len(errors))
    mean = sum(r["final"] for r in rows) / len(rows)
    denom = sum((r["final"] - mean) ** 2 for r in rows)
    r2 = 1 - sum(e * e for e in errors) / denom if denom else 0
    baseline_mae = sum(abs(r["final"] - mean) for r in rows) / len(rows)
    return mae, rmse, r2, baseline_mae
