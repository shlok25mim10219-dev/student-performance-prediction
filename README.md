# Student Performance Prediction & Academic Analysis

**Integrated MTech AI Project — VIT Bhopal University**

A terminal-based AI/ML project that uses **Multiple Linear Regression** to estimate student final performance from academic indicators and combines that prediction with an academic analysis workflow.

## Project purpose

The system demonstrates a complete AI/ML workflow:

**Academic data → preprocessing → 80/20 train-test split → Multiple Linear Regression → prediction → academic calculation → eligibility/pass analysis → recommendation**

The dataset contains **240 simulated records** created for educational demonstration. It is not real student data and is not an official VIT dataset.

## Main features

- Multiple Linear Regression implemented using Python's standard library
- 80/20 training and testing split
- MAE, RMSE, R² and baseline MAE evaluation
- Student performance prediction
- Academic contribution calculation
- Attendance and pass-condition checks
- Transparent recommendations
- Input validation and error handling
- Interactive terminal mode
- Non-interactive example, metrics and validation-test modes
- No third-party Python packages required

## Requirements

- Python 3.9 or newer
- Windows, Linux or macOS
- No external Python packages are required

## Command-line execution

From the project root:

```bash
python main.py
```

### Run validation tests

```bash
python main.py --test
```

Expected result:

```text
All CLI validation tests passed.
Records: 240 | Test MAE: 1.13 | RMSE: 1.32 | R2: 0.9831
```

### Show model metrics

```bash
python main.py --metrics
```

### Run the complete example

```bash
python main.py --example
```

### Run with direct student inputs

```bash
python main.py --study 5 --attendance 86 --cam 78 --previous 72 --cat1 38 --cat2 40 --tee 72
```

### Windows shortcut

Double-click:

```text
run_cli.bat
```

## Source structure

```text
main.py
src/
├── config.py
├── data_loader.py
├── regression.py
├── academic.py
├── analysis.py
├── reporting.py
└── app.py
data/
└── vit_student_dataset.csv
```

## Model

The project uses ordinary least-squares **Multiple Linear Regression**. Input features are:

- Study hours
- Attendance
- CAM percentage
- Previous final score
- CAT-1 raw marks
- CAT-2 raw marks
- TEE raw marks

The target is `Final_Score_100`.

The reported model metrics are demonstrations on the supplied simulated dataset. Because the data is synthetic and the target is generated from related academic variables, the high R² should not be interpreted as real-world predictive accuracy.

## Academic analysis

The project includes an academic calculation layer that represents the provided course-assessment structure used for this project. It calculates CAM, attendance, CAT-1, CAT-2, internal total, TEE contribution and final score, then checks the project-defined attendance/TEE/raw-score conditions.

These calculations are a project implementation for educational demonstration and are not an official university result generator.

## Testing

The project includes built-in validation tests covering:

- Dataset size
- 80/20 split
- Regression evaluation
- Baseline comparison
- Academic calculation
- Eligibility/pass checks

See `TESTING.md` and `CLI_EXECUTION.md`.

## Limitations

- Dataset is simulated rather than real institutional data.
- Predictions are prototypes and should not be used as official academic decisions.
- No external database or university portal credentials are collected.
- Model performance on this synthetic dataset does not establish performance on real students.

## License / academic use

This repository is an academic project for educational demonstration.
