# Data Science Projects

Portfolio of end-to-end data science projects covering time series forecasting and binary classification. Each project demonstrates a complete pipeline: data cleaning, exploratory analysis, feature engineering, model training, evaluation, and interpretation.

## Projects

### 1. [Temporal Series: Influenza Forecast](./data_science_temporal_series/)

Weekly influenza case forecasting in the state of Paraná, Brazil, using public data from OpenDataSUS.

- **Task:** time series regression (forecast)
- **Model:** Random Forest with TimeSeriesSplit and GridSearchCV
- **Metrics:** RMSE (MAPE not used due to near-zero values in the summer)
- **Result:** ~23% RMSE reduction vs. baseline (23.24 vs. 30.01)
- **Stack:** Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter

### 2. [Classification: Customer Churn Prediction](./data_science_classification/)

Predicting churn probability in a telecom company using the Telco Customer Churn dataset.

- **Task:** binary classification
- **Models:** Logistic Regression and Random Forest, compared
- **Metrics:** F1, AUC, precision, recall, confusion matrix
- **Result:** Random Forest tuned with AUC ~0.85, F1 (churn class) ~0.61
- **Stack:** Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter, PostgreSQL (optional)

## Common Tools

Across both projects:

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Jupyter Notebook for analysis and modeling
- Git for version control
- PostgreSQL for optional SQL exploration

## Skills Demonstrated

- Exploratory data analysis (EDA)
- Feature engineering (lags, rolling averages, derived flags, one-hot encoding)
- Temporal cross-validation (TimeSeriesSplit)
- Stratified cross-validation for imbalanced classes
- Hyperparameter tuning with GridSearchCV
- Model evaluation with task-appropriate metrics
- Interpretation and communication of results

## Author

Adriano Neves
GitHub: https://github.com/ahdn913
LinkedIn: https://www.linkedin.com/in/adriano-henrique-neves/