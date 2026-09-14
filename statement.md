# Project Statement

## Title
Student Performance Prediction and Academic Analysis Using Multiple Linear Regression

## Problem Statement
University students face diverse multi-component assessment structures comprising continuous internal evaluations (quizzes, assignments, laboratory work), mid-term examinations, attendance criteria, and comprehensive final examinations. Without integrated analytical tools, students struggle to:
1. Accurately monitor their cumulative internal marks against university weightages;
2. Understand examination eligibility requirements before critical cutoffs;
3. Predict final course performance using historical study habits and current academic performance;
4. Formulate actionable target scores for pending examinations to satisfy minimum passing thresholds;
5. Efficiently distribute limited self-study hours across multiple enrolled courses.

## Objectives
1. Implement a client-side Multiple Linear Regression model to predict continuous final academic performance from multiple academic indicators.
2. Formulate and automate the exact assessment calculation structure defined in the VIT Bhopal University Revised Academic Regulations (10 July 2026).
3. Validate and enforce critical institutional eligibility and pass criteria:
   - 75% attendance requirement for examination clearance;
   - 40/100 raw score floor on Term End Examinations (TEE);
   - 80/200 combined aggregate raw score across CAT-1, CAT-2, and TEE.
4. Design a dynamic Exam Target and Study Planner supporting both pre-CAT-2 and post-CAT-2 scenarios.
5. Provide a multi-subject semester dashboard with automated priority ranking, scenario analysis (What-If), and personalized study hour recommendations.
6. Ensure zero operational overhead: the entire system operates purely in client-side HTML5, CSS3, and vanilla JavaScript without servers or dependencies.

## Academic Regulation Foundation
The application strictly models the official **VIT Bhopal University Revised Academic Regulations** dated 10 July 2026:
- **CAT-1**: 50 raw marks, closed book (Modules 1 & 2) → 15 internal weightage marks.
- **CAT-2**: 50 raw marks, open book (Modules 3 & 4) → 15 internal weightage marks.
- **CAM**: Continuous Assessment Marks → 35 internal marks.
- **Attendance**: 5 internal marks (granted if attendance ≥ 75%, 0 marks if < 75%).
- **TEE**: 100 raw marks → 30 scaled marks.
- **Final Result**: 70 Internal + 30 TEE = 100 Final Score.
- **Passing Rules**: Attendance ≥ 75% AND TEE ≥ 40/100 AND (CAT-1 + CAT-2 + TEE) ≥ 80/200.
