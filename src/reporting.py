"""Terminal presentation helpers."""
from .academic import academic_analysis
from .analysis import clamp, recommendations

def print_model_metrics(rows, beta):
    split = int(len(rows) * 0.8)
    test_rows = rows[split:]
    from .regression import evaluate
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
    for item in recommendations(a):
        print("- " + item)
