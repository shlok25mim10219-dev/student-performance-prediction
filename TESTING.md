# Verification & Testing Guide

This document outlines the test cases and functional verification procedures for the **Student Performance Prediction & Academic Analysis** website.

## Automated & Functional Verification Matrix

| Test ID | Module / Feature | Input / Action | Expected Result | Status |
|---|---|---|---|---|
| **TC-01** | Exact Course Search | Type `CSA2001` | Dropdown resolves to `CSA2001 — Fundamentals in AI and ML` | Passed |
| **TC-02** | Title Course Search | Type `Data Structures and Algorithms` | Dropdown resolves to `CSE2002 — Data Structures and Algorithms` | Passed |
| **TC-03** | Partial Course Search | Type `Data Structures` | Shows matching courses (`CSE2002`, etc.) | Passed |
| **TC-04** | Keyboard Navigation | `ArrowDown`, `ArrowUp`, `Enter`, `Escape` | Highlights options and selects upon Enter; closes on Escape | Passed |
| **TC-05** | Typing Stability | Type characters continuously | Input value is not overwritten while typing | Passed |
| **TC-06** | Custom Subject Name | Type `Advanced Robotics` | Preserves custom subject without forced replacement | Passed |
| **TC-07** | Attendance Risk (<75%) | Attendance = `74%` | Shows `HIGH RISK` warning: Ineligible for CATs/TEE; grants 0 attendance marks | Passed |
| **TC-08** | Attendance Pass (≥75%) | Attendance = `75%` | Shows eligibility satisfied; grants 5 attendance marks | Passed |
| **TC-09** | TEE Minimum (<40) | TEE = `39/100` | Fails pass criteria: TEE is below the mandatory 40/100 floor | Passed |
| **TC-10** | TEE Minimum (≥40) | TEE = `40/100` | Satisfies TEE floor requirement | Passed |
| **TC-11** | Raw Total (<80) | CAT-1=25, CAT-2=14, TEE=40 (Total: 79) | Fails pass criteria: Aggregate raw total is below 80/200 | Passed |
| **TC-12** | Raw Total (≥80) | CAT-1=25, CAT-2=15, TEE=40 (Total: 80) | Satisfies 80/200 aggregate raw requirement | Passed |
| **TC-13** | Pending CAT-2 & TEE | Leave CAT-2 and TEE blank | Status strip shows `Pending`; does not treat pending marks as 0 | Passed |
| **TC-14** | Planner Mode A | CAT-1=30, Target TEE=40 | Calculates Minimum CAT-2 = `10.0 / 50` | Passed |
| **TC-15** | Planner Mode B | CAT-1=30, CAT-2=10 | Calculates Minimum TEE = `40.0 / 100` | Passed |
| **TC-16** | Planner TEE Floor | CAT-1=30, CAT-2=20 | Calculates Minimum TEE = `40.0 / 100` (floor applies even though 80-30-20=30) | Passed |
| **TC-17** | Infeasible Target | CAT-1=10, Target TEE=15 | Alerts that required CAT-2 (>50) is not feasible alone | Passed |
| **TC-18** | Full ML Prediction | Valid full inputs | Outputs continuous prediction (e.g. `71.9 / 100`) | Passed |
| **TC-19** | Projected Prediction | CAT-2 and TEE blank | Outputs valid projected score based on CAM, CAT-1, Attendance, Study | Passed |
| **TC-20** | Model Metrics | 80/20 holdout test set | Regression MAE = `1.13`, RMSE = `1.32`, R² = `0.983` | Passed |
| **TC-21** | Baseline Comparison | Test set mean comparison | Shows regression MAE (1.13) substantially beats baseline MAE (8.86) | Passed |
| **TC-22** | What-If Analysis | Adjust study hours, CAT-2, etc. | Displays scenario score and clear delta (`+X.X marks`) | Passed |
| **TC-23** | LocalStorage Save | Click `[Save Subject]` | Saves subject to `localStorage["vitSemesterSubjects"]` | Passed |
| **TC-24** | Subject Update | Edit and save same course | Updates existing record in place without duplicate | Passed |
| **TC-25** | Subject Load | Click `[Load]` on saved subject | Populates input form and triggers immediate recalculation | Passed |
| **TC-26** | Subject Delete | Click `[Delete]` on saved subject | Removes record from localStorage and refreshes dashboard | Passed |
| **TC-27** | Priority Ranking | Add high-risk & low-risk subjects | Automatically ranks subjects by urgency in Command Center | Passed |
| **TC-28** | Dynamic Advice | Change active subject status | Dynamically steers student based on attendance or score gaps | Passed |
| **TC-29** | CSV Import | Upload CSV with standard columns | Parses and imports multiple courses into semester tracker | Passed |
| **TC-30** | CSV Template | Click `[CSV Template]` | Generates downloadable CSV template file | Passed |
| **TC-31** | Dataset Modal | Click `[View Dataset Details]` | Opens modal detailing 240 records, 8 features, 80/20 split | Passed |

---

## Terminal Test Commands

Run these from the repository root:

```bash
python main.py --test
python main.py --metrics
python main.py --example
```

Expected validation output includes `All CLI validation tests passed.` and model evaluation over 240 records with 192 training records and 48 test records.
