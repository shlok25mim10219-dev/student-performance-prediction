"""Project configuration and feature definitions."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "vit_student_dataset.csv"
FEATURES = ["study", "attendance", "cam", "previous", "cat1", "cat2", "tee"]

LIMITS = {
    "study": (0, 12),
    "attendance": (0, 100),
    "cam": (0, 100),
    "previous": (0, 100),
    "cat1": (0, 50),
    "cat2": (0, 50),
    "tee": (0, 100),
}
