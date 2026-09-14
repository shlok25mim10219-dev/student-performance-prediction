"""Application orchestration for the terminal edition."""
from .data_loader import read_dataset
from .regression import fit, predict
from .academic import academic_analysis
from .analysis import validate
from .reporting import print_analysis, print_model_metrics

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
    validate(v)
    print_analysis(v, predict(beta, v))
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
