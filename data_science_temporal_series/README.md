# Influenza Forecast in Paraná with Python and Scikit-learn

An end-to-end time series forecasting project using public health data from OpenDataSUS, covering exploratory data analysis, feature engineering, baseline definition, model training, temporal cross-validation, hyperparameter tuning, and evaluation with RMSE and MAPE.

## Overview

This project analyzes and forecasts weekly influenza cases in the state of Paraná, Brazil, using publicly available data from OpenDataSUS (SRAG 2024). It demonstrates a complete machine learning pipeline for time series: EDA, feature engineering with lags and rolling averages, baseline definition, Random Forest training with TimeSeriesSplit, hyperparameter tuning with GridSearchCV, and final evaluation.

## Data Source

- OpenDataSUS SRAG dataset: https://dadosabertos.saude.gov.br/dataset/srag-2019-a-2026
- Filtered for Paraná state (`SG_UF_NOT == 'PR'`) and influenza cases (`CLASSI_FIN == 1`)
- Aggregated weekly
- Period: 2024-01 to 2025-01
- Total weeks: 57
- Total cases: 2,747

## Requirements

- Python 3.10+
- Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## How to Run

1. Download the SRAG CSV from OpenDataSUS and place it in `data/raw/`

2. Install Python dependencies:

    pip install pandas numpy matplotlib seaborn scikit-learn jupyter

3. Aggregate the data weekly:

    python scripts/load_data.py

4. Open the notebooks and run them in order:

    jupyter notebook notebooks/01_eda.ipynb
    jupyter notebook notebooks/02_modeling.ipynb

## Feature Engineering

- Lags: lag_1, lag_2, lag_4, lag_8
- Rolling averages: ma_4, ma_8
- Calendar features: month, week of year

## Modeling Approach

- Baseline: last observed value
- Model: Random Forest Regressor
- Validation: TimeSeriesSplit with 3 folds
- Tuning: GridSearchCV with TimeSeriesSplit
- Metrics: RMSE and MAPE

## Results

| Model | RMSE | MAPE |
|---|---|---|
| Baseline (last value) | 30.01 | 650.07% |
| Random Forest (default) | 23.67 | 149.80% |
| Random Forest (tuned) | 23.24 | 436.49% |

The tuned Random Forest reduced RMSE by approximately 23% compared to the baseline.

## Limitations

- MAPE is not a reliable metric for this series because case counts drop to near zero in the summer months, which makes the percentage error explode. RMSE is the primary metric used here.
- The model shows an upward bias during the decline phase (November-December). It captures the autumn/winter peak but reacts slowly to the seasonal decline.
- Only one year of data was used. Time series models typically benefit from multiple seasonal cycles (3+ years) to learn annual patterns more reliably.

## Future Work

- Include multiple years of SRAG data to give the model more seasonal cycles.
- Compare against time-series-specific models such as SARIMA, Prophet, or LSTM.
- Add exogenous features such as vaccination coverage and temperature.

## Technologies

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Jupyter Notebook
- Git

## Lessons Learned

- Temporal cross-validation is essential for time series, since random splits leak future information.
- A simple baseline is often strong and should always be compared against.
- Feature engineering with lags and rolling averages is more impactful than model complexity.
- RMSE and MAPE tell different stories; MAPE breaks down when values approach zero.

## Author

Adriano Neves
GitHub: https://github.com/ahdn913
LinkedIn: https://www.linkedin.com/in/adriano-henrique-neves/

## License

This project is licensed under the MIT License.