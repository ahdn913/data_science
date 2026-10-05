# Customer Churn Prediction with Python and Scikit-learn

An end-to-end binary classification project using the Telco Customer Churn dataset, covering EDA, feature engineering, model comparison, hyperparameter tuning, and evaluation with F1 and AUC.

## Overview

This project predicts customer churn in a telecommunications company using machine learning. It demonstrates a complete binary classification pipeline: data cleaning, exploratory data analysis, feature engineering, baseline definition, comparison of two models (Logistic Regression and Random Forest), hyperparameter tuning with GridSearchCV, and evaluation with F1, AUC, precision, recall, and confusion matrix.

The project answers a practical question: can we identify customers at risk of churn early enough to act and reduce revenue loss?

## Data Source

- Telco Customer Churn (Kaggle): https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- File: WA_Fn-UseC_-Telco-Customer-Churn.csv
- Rows: 7,043
- Target: Churn (Yes/No), roughly 26.5% positive class

## Requirements

- Python 3.10+
- PostgreSQL 14+ (optional, for SQL exploration)
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## How to Run

1. Download the CSV from Kaggle and place it in `data/raw/`

2. Install dependencies:

    pip install pandas numpy matplotlib seaborn scikit-learn

3. (Optional) Load data into PostgreSQL:

    python scripts/load_data.py

4. Open the notebooks and run them in order:

    jupyter notebook notebooks/01_eda.ipynb
    jupyter notebook notebooks/02_modeling.ipynb

## Feature Engineering

- `avg_monthly_spend`: TotalCharges divided by tenure
- `is_new_customer`: flag for customers with less than 12 months
- `is_monthly_contract`: flag for month-to-month contracts
- One-hot encoding for categorical variables (drop first)

## Modeling Approach

- Baseline: predict majority class (no churn)
- Models: Logistic Regression (with StandardScaler) and Random Forest
- Validation: StratifiedKFold with 5 folds
- Tuning: GridSearchCV on Random Forest
- Metrics: F1, AUC, precision, recall, confusion matrix

## Results

| Model | F1 (churn) | AUC |
|---|---|---|
| Baseline (majority class) | 0.00 | 0.50 |
| Logistic Regression | 0.62 | 0.84 |
| Random Forest (default) | 0.55 | 0.82 |
| Random Forest (tuned) | 0.61 | 0.85 |

Most important features: `tenure`, `TotalCharges`, `MonthlyCharges`, `avg_monthly_spend`, `is_monthly_contract`.

## Business Interpretation

- Customers on month-to-month contracts have much higher churn.
- New customers (tenure < 12 months) are the highest-risk group.
- The model can support retention campaigns: focus on high-probability customers with month-to-month contracts and short tenure.

## Technologies

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- SQL (PostgreSQL, optional)
- Jupyter Notebook
- Git

## Author

Adriano Neves
GitHub: https://github.com/ahdn913
LinkedIn: https://www.linkedin.com/in/adriano-henrique-neves/

## License

This project is licensed under the MIT License.