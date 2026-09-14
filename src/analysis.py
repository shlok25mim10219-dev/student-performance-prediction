"""Validation and recommendation logic."""
import math
from .config import LIMITS

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def validate(v):
    for k, (lo, hi) in LIMITS.items():
        if not math.isfinite(v[k]) or not (lo <= v[k] <= hi):
            raise ValueError(f"{k} must be between {lo} and {hi}.")

def recommendations(academic):
    gaps = []
    if not academic["attendance_ok"]:
        gaps.append("attendance must reach at least 75%")
    if not academic["tee_ok"]:
        gaps.append("TEE score must reach at least 40/100")
    if not academic["raw_pass"]:
        gaps.append(
            f"raw CAT1 + CAT2 + TEE total needs "
            f"{max(0, 80-academic['raw_total']):.1f} more marks"
        )
    if not gaps:
        gaps.append("Maintain the current level and use timed revision/practice.")
    gaps.append("Use the ML prediction as a prototype estimate, not an official university result.")
    return gaps
