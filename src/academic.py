"""Academic score calculation and eligibility checks."""

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
