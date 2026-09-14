# System Architecture

```text
User / CLI
   |
   v
main.py
   |
   +--> app.py ----------------------+
   |                                  |
   +--> data_loader.py --> CSV        |
   |                                  v
   +--> regression.py ----------> Prediction
   |                                  |
   +--> academic.py ------------> Academic Analysis
   |                                  |
   +--> analysis.py ------------> Validation / Recommendations
   |                                  |
   +--> reporting.py -----------> Terminal Output
   |
   +--> config.py -------------> Paths / Features / Limits
```

The design separates data access, machine learning, academic calculations, validation, presentation and application orchestration.
