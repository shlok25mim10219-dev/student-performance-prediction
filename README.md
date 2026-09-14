# Student Performance Prediction & Academic Analysis
**Integrated MTech AI Project • VIT Bhopal University**

An intelligent, lightweight, terminal-based academic assistant that turns raw assessment marks into predictive performance insights, risk analysis, exam target thresholds, and practical study plans.

---

## How to Run

### Requirements
- Python 3.9 or newer
- Windows PowerShell, Command Prompt, or another terminal
- No third-party Python packages are required

### Run the application
From the repository root:

```bash
python main.py
```

The program loads the supplied 240-record simulated dataset, trains Multiple Linear Regression using an 80/20 split, accepts student academic inputs, predicts the final score, calculates the academic assessment breakdown, checks eligibility/pass conditions, and prints recommendations.

### Run validation tests
```bash
python main.py --test
```

### Run model evaluation
```bash
python main.py --metrics
```

### Run a complete example
```bash
python main.py --example
```

### Run with command-line inputs
```bash
python main.py --study 5 --attendance 86 --cam 78 --previous 72 --cat1 38 --cat2 40 --tee 72
```

### Windows shortcut
Double-click `run_cli.bat` to start the interactive terminal application.

## Core Features

1. **Student Academic Inputs**
   - Direct raw-mark inputs (no manual percentage calculations needed):
     - CAM Raw Mark (/35)
     - CAT-1 Raw Mark (/50)
     - CAT-2 Raw Mark (/50, optional if pending)
     - TEE Raw Mark (/100, optional if pending)
     - Attendance % (0–100%)
     - Study Hours per Day (0–24)
     - Previous Final Score (/100)
   - Real-time mark status strip showing calculated percentages and pending exam badges.

2. **Integrated MTech Course Selector**
   - Searchable, keyboard-accessible combobox containing all 98 courses from the Integrated MTech AI curriculum.
   - Search by course code (e.g. `CSA2001`), course name (e.g. `Fundamentals in AI and ML`), or partial text (e.g. `Data Structures`).
   - Supports keyboard navigation (`ArrowUp`, `ArrowDown`, `Enter`, `Escape`), mouse clicks, and custom subject names.

3. **Multiple Linear Regression (ML) Engine**
   - Ordinary Least Squares (OLS) model trained on an 80/20 train/test split of 240 simulated student records.
   - Achieves test MAE of 1.13, RMSE of 1.32, and R² of 0.983.
   - Evaluated against a naive mean baseline (MAE: 8.86), showing an 87% error reduction.
   - Multi-stage model adaptation: accurately predicts projected performance even when CAT-2 or TEE is pending.

4. **VIT Bhopal Academic Regulation Alignment (10 July 2026)**
   - Internal Assessment (70 marks): CAM (35) + Attendance (5 marks if ≥ 75%, 0 if < 75%) + CAT-1 (15 weightage) + CAT-2 (15 weightage).
   - TEE Scaled Contribution: 30 marks (`TEE / 100 × 30`).
   - Final Result: 70 Internal + 30 TEE = 100.
   - Mandatory Passing Rules:
     - Attendance ≥ 75% for eligibility.
     - Raw TEE score ≥ 40/100.
     - Aggregate raw score (CAT-1 + CAT-2 + TEE) ≥ 80/200.

5. **Exam Target & Study Planner**
   - Collapsible planner supporting two distinct operational modes:
     - **Mode A (CAT-2 Not Held Yet)**: Treats CAT-2 as a future target (not 0); calculates minimum CAT-2 to pass, minimum TEE to pass, safe targets, and daily study hours. Detects impossible targets (e.g. required CAT-2 > 50).
     - **Mode B (CAT-2 Already Completed)**: Uses actual CAT-2 marks to determine exact TEE needed for a pass or a desired final score.
   - Practical study-time heuristic with focused daily hours and timeline breakdown.

6. **Semester Subject Tracker & LocalStorage**
   - Save and monitor multiple courses across the semester.
   - Saves automatically in browser `localStorage` (`vitSemesterSubjects`).
   - Actionable table with `[Load]` and `[Delete]` buttons.
   - CSV Import & Template Download (`vit_student_marks_template.csv`).

7. **Academic Command Center**
   - Automated priority ranking across saved subjects based on risk, low scores, and attendance.
   - Dynamic **"What Should I Do Next?"** contextual recommendations.
   - Automated study plan distributing daily hours across subjects.

8. **What-If Scenario Analysis**
   - Adjust study hours, attendance, CAT-2, and TEE to observe immediate impact on predicted and calculated scores.

9. **Performance Visualization & Factor Analysis**
   - Lightweight HTML5 Canvas scatter plot showing the simulated dataset, regression curve, and student prediction marker.
   - Relative factor contribution progress bars with causal disclaimer.

10. **Printable Academic Report**
    - Clean, professional summary report with one-click print/save dialog (`window.print()`).

11. **VTOP Portal Shortcut**
    - Direct secure link to VIT Bhopal VTOP portal (`https://vtop.vitbhopal.ac.in/vtop/login`).
    - Never requests or stores student login credentials.


## Command-Line Execution (Required Evaluation Path)

The project is a standalone terminal application in `main.py`. It uses only Python's standard library; no pip packages, npm, server, database, or GUI setup is required.

### Requirements
- Python 3.9 or newer
- A terminal / Command Prompt / PowerShell

### Run interactively

From the repository root:

```bash
python main.py
```

The program loads the supplied 240-record simulated dataset, trains Multiple Linear Regression with an 80/20 split, accepts student academic inputs, predicts the final score, calculates the academic assessment breakdown, checks eligibility/pass conditions, and prints recommendations.

### Run the example without prompts

```bash
python main.py --example
```

### Run model evaluation

```bash
python main.py --metrics
```

### Run validation tests

```bash
python main.py --test
```

### Run with command-line arguments

```bash
python main.py --study 5 --attendance 86 --cam 78 --previous 72 --cat1 38 --cat2 40 --tee 72
```

### Windows shortcut

Double-clicking `run_cli.bat` starts the interactive terminal application, but the recommended evaluator command is `python main.py`.

