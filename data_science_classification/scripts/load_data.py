import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:3141@localhost:5432/churn')

df = pd.read_csv('data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.columns = [c.lower().replace(' ', '_') for c in df.columns]

df.to_sql('raw_churn', engine, if_exists='replace', index=False)
print(f'Loaded {len(df)} lines.')