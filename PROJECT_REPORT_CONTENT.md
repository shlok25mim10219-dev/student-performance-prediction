# Project Report Content

## Title
Student Performance Prediction and Academic Analysis using Multiple Linear Regression

## 1. Introduction
This project presents a lightweight terminal-based AI/ML application for student academic analysis. The system combines academic indicators and a Multiple Linear Regression model to estimate a final performance score. It also calculates an academic score using the assessment structure implemented for this project and checks defined eligibility/pass conditions.

## 2. Problem Statement
Academic information can be distributed across study habits, attendance, continuous assessment, internal tests and final examination performance. Students can benefit from a single workflow that converts these inputs into a performance estimate and an interpretable academic analysis.

## 3. Objectives
- Build an executable AI/ML project using Multiple Linear Regression.
- Process a structured academic dataset.
- Train and test the model using an 80/20 split.
- Evaluate the model with MAE, RMSE and R².
- Accept individual student inputs and generate a prediction.
- Calculate academic contributions and defined pass checks.
- Produce understandable recommendations.
- Provide command-line execution without third-party packages.

## 4. Functional Requirements
- Load the supplied CSV dataset.
- Validate numerical inputs and ranges.
- Train Multiple Linear Regression.
- Predict a final score.
- Calculate CAM, attendance, CAT-1, CAT-2 and TEE contributions.
- Check attendance, TEE and raw-score conditions.
- Generate recommendations.
- Provide interactive and non-interactive CLI execution.
- Report model evaluation metrics.

## 5. Non-Functional Requirements
- Usability: simple terminal prompts and clear output.
- Reliability: built-in validation and tests.
- Maintainability: separated source modules.
- Resource efficiency: standard-library implementation without external ML packages.
- Portability: works with Python 3.9+ on common desktop operating systems.
- Error handling: invalid numeric values are rejected with a clear message.

## 6. System Architecture
The architecture is organized into configuration, data loading, model, academic analysis, validation/recommendation, reporting and application orchestration modules.

## 7. Workflow
Academic inputs are validated, the simulated dataset is loaded, the model is trained on 80% of the records, the student's predicted score is generated, the academic calculation is performed, eligibility/pass conditions are checked, and recommendations are printed.

## 8. Dataset
The repository contains 240 simulated records. Features include study hours, attendance, CAM percentage, previous marks, CAT-1, CAT-2 and TEE marks. The target is final score out of 100.

## 9. Machine Learning Method
The model is ordinary least-squares Multiple Linear Regression. The implementation solves the normal-equation system using Gauss-Jordan elimination with partial pivoting, avoiding external ML libraries.

## 10. Evaluation
The 240 records are split into 192 training records and 48 test records. The measured results are:
- MAE ≈ 1.13
- RMSE ≈ 1.32
- R² ≈ 0.9831
- Baseline MAE ≈ 8.86

Because the dataset is simulated and the target is strongly related to the predictor variables, these metrics demonstrate implementation and evaluation rather than real-world model validity.

## 11. Academic Analysis
The application converts raw assessment values into weighted contributions, produces an internal total and TEE contribution, calculates a final score and checks the project-defined attendance, TEE and raw-score conditions.

## 12. Implementation
The code is divided into small Python modules. `main.py` handles command-line options. `data_loader.py` reads the CSV. `regression.py` implements the ML model. `academic.py` performs academic calculations. `analysis.py` validates inputs and creates recommendations. `reporting.py` formats results. `app.py` coordinates interactive and example workflows.

## 13. Testing
Automated tests verify the 240-row dataset, 80/20 split, regression metrics, baseline comparison and academic calculation. The interactive, metrics and example modes were manually executed in Windows PowerShell.

## 14. Limitations
The dataset is synthetic. The model is not trained on real VIT student records. Academic rules represented in the prototype should not be interpreted as an official university result engine. No student credentials are collected.

## 15. Future Enhancements
Possible extensions include a larger validated dataset, cross-validation, additional regression models, explainability, persistent student profiles and a database layer, subject-wise analytics and integration with authorized institutional APIs if available.

## 16. Conclusion
The project demonstrates an end-to-end introductory AI/ML workflow in a command-line executable form. It combines data processing, regression, evaluation, prediction and interpretable academic analysis in a modular implementation.
