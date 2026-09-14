#!/usr/bin/env python3
"""Entry point for the VIT Student Performance Prediction terminal application."""
from __future__ import annotations
import argparse
import sys
from src.data_loader import read_dataset
from src.regression import fit, predict, evaluate
from src.academic import academic_analysis
from src.analysis import validate
from src.app import interactive, run_example
from src.reporting import print_model_metrics, print_analysis
from src.config import FEATURES

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
    expected_internal = 78/100*35 + 5 + 38/50*15 + 40/50*15
    assert abs(a["internal"] - expected_internal) < 1e-9
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
