"""CSV loading and dataset preparation."""
import csv
from .config import DATA_FILE

def read_dataset():
    """Load the supplied simulated academic dataset."""
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
