# Testing

The project was tested in Windows PowerShell using Python 3.13.

## Automated validation

Command:

```bash
python main.py --test
```

Expected:

```text
All CLI validation tests passed.
Records: 240 | Test MAE: 1.13 | RMSE: 1.32 | R2: 0.9831
```

The test validates dataset size, 80/20 split, regression metrics, baseline comparison, academic calculation and pass conditions.

## Model evaluation

Command:

```bash
python main.py --metrics
```

Expected evaluation:

- Dataset records: 240
- Training records: 192
- Test records: 48
- MAE: approximately 1.13
- RMSE: approximately 1.32
- R²: approximately 0.9831
- Baseline MAE: approximately 8.86

## Example workflow

Command:

```bash
python main.py --example
```

This executes prediction, academic calculation, eligibility analysis, recommendations and model evaluation without interactive prompts.

## Interactive workflow

Command:

```bash
python main.py
```

The application validates each numeric input, loads the dataset, trains the regression model and produces a complete analysis.

## Direct argument workflow

The application also supports direct command-line inputs:

```bash
python main.py --study 5 --attendance 86 --cam 78 --previous 72 --cat1 38 --cat2 40 --tee 72
```

## Limitations of testing

Testing was performed on the supplied simulated dataset and local Python runtime. No claim is made that the model is suitable for real institutional prediction.
