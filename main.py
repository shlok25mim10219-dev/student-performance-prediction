#!/usr/bin/env python3
"""
Terminal interface for the VIT Student Performance Prediction and Academic Analysis project.

No third-party Python packages are required. The terminal application:
- loads the supplied simulated dataset,
- trains Multiple Linear Regression using an 80/20 split,
- reports MAE/RMSE/R2,
- predicts a student's final score,
- calculates the supplied VIT academic structure,
- checks attendance and pass conditions,
- gives a transparent study recommendation.

This terminal application is the primary executable interface for the submission.
"""

from __future__ import annotations
import argparse
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "vit_student_dataset.csv"

FEATURES = ["study", "attendance", "cam", "previous", "cat1", "cat2", "tee"]


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def read_dataset():
    rows = []
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "study": float(r["Study_Hours"]),
                "attendance": float(r["Attendance"]),
                "cam": float(r["CAM_Percent"]),
                "previous": float(r["Previous_Marks"]),
                "cat1": float(r["CAT1_Raw"]),
                "cat2": float(r["CAT2_Raw"]),
                "tee": float(r["TEE_Raw"]),
                "final": float(r["Final_Score_100"]),
            })
    return rows


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


def vector(row):
    return [1.0] + [row[k] for k in FEATURES]


def fit(rows):
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


def academic_analysis(v):
    cam_weight = v["cam"] / 100 * 35
    attendance_weight = 5 if v["attendance"] >= 75 else 0
    cat1_weight = v["cat1"] / 50 * 15
    cat2_weight = v["cat2"] / 50 * 15
    tee_weight = v["tee"] / 100 * 30
    internal = cam_weight + attendance_weight + cat1_weight + cat2_weight
    final = internal + tee_weight
    raw_total = v["cat1"] + v["cat2"] + v["tee"]
    attendance_ok = v["attendance"] >= 75
    tee_ok = v["tee"] >= 40
    raw_pass = raw_total >= 80
    passed = attendance_ok and tee_ok and raw_pass
    if final >= 85:
        level = "Excellent"
    elif final >= 70:
        level = "Good"
    elif final >= 55:
        level = "Satisfactory"
    elif final >= 40:
        level = "Needs Improvement"
    else:
        level = "At Risk"
    return {
        "cam_weight": cam_weight,
        "attendance_weight": attendance_weight,
        "cat1_weight": cat1_weight,
        "cat2_weight": cat2_weight,
        "tee_weight": tee_weight,
        "internal": internal,
        "final": final,
        "raw_total": raw_total,
        "attendance_ok": attendance_ok,
        "tee_ok": tee_ok,
        "raw_pass": raw_pass,
        "passed": passed,
        "level": level,
    }


def validate(v):
    limits = {
        "study": (0, 12),
        "attendance": (0, 100),
        "cam": (0, 100),
        "previous": (0, 100),
        "cat1": (0, 50),
        "cat2": (0, 50),
        "tee": (0, 100),
    }
    for k, (lo, hi) in limits.items():
        if not math.isfinite(v[k]) or not (lo <= v[k] <= hi):
            raise ValueError(f"{k} must be between {lo} and {hi}.")


def get_float(prompt, lo, hi, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt} ({lo}-{hi}){suffix}: ").strip()
        if not raw and default is not None:
            return float(default)
        try:
            value = float(raw)
            if lo <= value <= hi:
                return value
        except ValueError:
            pass
        print("Please enter a valid number in the allowed range.")


def make_student_from_args(args):
    return {
        "study": args.study,
        "attendance": args.attendance,
        "cam": args.cam,
        "previous": args.previous,
        "cat1": args.cat1,
        "cat2": args.cat2,
        "tee": args.tee,
    }


def print_model_metrics(rows, beta):
    split = int(len(rows) * 0.8)
    test_rows = rows[split:]
    mae, rmse, r2, baseline = evaluate(test_rows, beta)
    print("\nMODEL EVALUATION")
    print("----------------")
    print(f"Dataset records : {len(rows)}")
    print(f"Train records   : {split}")
    print(f"Test records    : {len(test_rows)}")
    print(f"MAE             : {mae:.2f}")
    print(f"RMSE            : {rmse:.2f}")
    print(f"R2              : {r2:.4f}")
    print(f"Baseline MAE    : {baseline:.2f}")
    print("\nNote: the supplied dataset is simulated for educational demonstration.")


def print_analysis(v, pred):
    a = academic_analysis(v)
    print("\nSTUDENT PERFORMANCE ANALYSIS")
    print("-----------------------------")
    print(f"ML predicted final score : {clamp(pred, 0, 100):.2f}/100")
    print(f"Performance level        : {a['level']}")
    print(f"CAM contribution         : {a['cam_weight']:.2f}/35")
    print(f"Attendance contribution  : {a['attendance_weight']:.2f}/5")
    print(f"CAT-1 contribution       : {a['cat1_weight']:.2f}/15")
    print(f"CAT-2 contribution       : {a['cat2_weight']:.2f}/15")
    print(f"Internal total           : {a['internal']:.2f}/70")
    print(f"TEE contribution         : {a['tee_weight']:.2f}/30")
    print(f"Calculated final score   : {a['final']:.2f}/100")
    print("\nELIGIBILITY / PASS CHECK")
    print("------------------------")
    print(f"Attendance >= 75%       : {'Eligible' if a['attendance_ok'] else 'Not eligible'}")
    print(f"TEE >= 40/100            : {'Satisfied' if a['tee_ok'] else 'Not satisfied'}")
    print(f"CAT1+CAT2+TEE >= 80/200 : {'Satisfied' if a['raw_pass'] else 'Not satisfied'}")
    print(f"Overall pass condition   : {'PASS' if a['passed'] else 'NOT YET PASSED'}")

    print("\nRECOMMENDATION")
    print("--------------")
    gaps = []
    if not a["attendance_ok"]:
        gaps.append("attendance must reach at least 75%")
    if not a["tee_ok"]:
        gaps.append("TEE score must reach at least 40/100")
    if not a["raw_pass"]:
        gaps.append(f"raw CAT1 + CAT2 + TEE total needs {max(0, 80-a['raw_total']):.1f} more marks")
    if gaps:
        for g in gaps:
            print("- " + g)
    else:
        print("- Maintain the current level and use timed revision/practice.")
    print("- Use the ML prediction as a prototype estimate, not an official university result.")


def interactive():
    print("=" * 62)
    print("VIT STUDENT PERFORMANCE PREDICTION & ACADEMIC ANALYSIS")
    print("Terminal Edition")
    print("=" * 62)
    rows = read_dataset()
    split = int(len(rows) * 0.8)
    beta = fit(rows[:split])
    print(f"\nLoaded {len(rows)} simulated records.")
    print("Multiple Linear Regression trained using an 80/20 split.")

    print("\nEnter student data.")
    v = {
        "study": get_float("Study hours per day", 0, 12),
        "attendance": get_float("Attendance %", 0, 100),
        "cam": get_float("CAM %", 0, 100),
        "previous": get_float("Previous final score", 0, 100),
        "cat1": get_float("CAT-1 raw marks", 0, 50),
        "cat2": get_float("CAT-2 raw marks", 0, 50),
        "tee": get_float("TEE raw marks", 0, 100),
    }
    pred = predict(beta, v)
    print_analysis(v, pred)
    print_model_metrics(rows, beta)


def run_example():
    rows = read_dataset()
    split = int(len(rows) * 0.8)
    beta = fit(rows[:split])
    v = {"study": 5, "attendance": 86, "cam": 78, "previous": 72, "cat1": 38, "cat2": 40, "tee": 72}
    print("EXAMPLE RUN")
    print("-----------")
    print_analysis(v, predict(beta, v))
    print_model_metrics(rows, beta)


def run_tests():
    rows = read_dataset()
    assert len(rows) == 240, f"Expected 240 rows, found {len(rows)}"
    split = int(len(rows) * 0.8)
    beta = fit(rows[:split])
    mae, rmse, r2, baseline = evaluate(rows[split:], beta)
    assert 0 < mae < 3
    assert 0 < rmse < 3
    assert 0.9 < r2 <= 1.0
    assert baseline > mae
    v = {"study": 5, "attendance": 86, "cam": 78, "previous": 72, "cat1": 38, "cat2": 40, "tee": 72}
    a = academic_analysis(v)
    assert abs(a["internal"] - (78/100*35 + 5 + 38/50*15 + 40/50*15)) < 1e-9
    assert a["tee_ok"] is True
    assert a["raw_pass"] is True
    print("All CLI validation tests passed.")
    print(f"Records: {len(rows)} | Test MAE: {mae:.2f} | RMSE: {rmse:.2f} | R2: {r2:.4f}")


def main():
    p = argparse.ArgumentParser(description="VIT Student Performance Prediction and Academic Analysis")
    p.add_argument("--example", action="store_true", help="run a complete example without prompts")
    p.add_argument("--test", action="store_true", help="run built-in validation tests")
    p.add_argument("--metrics", action="store_true", help="show model evaluation metrics")
    for name, lo, hi in [
        ("study", 0, 12), ("attendance", 0, 100), ("cam", 0, 100),
        ("previous", 0, 100), ("cat1", 0, 50), ("cat2", 0, 50), ("tee", 0, 100)
    ]:
        p.add_argument("--" + name, type=float, default=None)
    args = p.parse_args()

    if args.test:
        run_tests()
        return

    if args.example:
        run_example()
        return

    rows = read_dataset()
    split = int(len(rows) * 0.8)
    beta = fit(rows[:split])

    if args.metrics:
        print_model_metrics(rows, beta)
        return

    values = [getattr(args, k) for k in FEATURES]
    if all(v is not None for v in values):
        v = make_student_from_args(args)
        validate(v)
        print_analysis(v, predict(beta, v))
    elif any(v is not None for v in values):
        p.error("Provide all seven student inputs together, or provide none for interactive mode.")
    else:
        interactive()


if __name__ == "__main__":
    main()
