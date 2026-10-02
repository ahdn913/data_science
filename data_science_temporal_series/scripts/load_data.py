import pandas as pd

# 1. Carregar apenas as colunas necessarias
usecols = ['DT_NOTIFIC', 'SG_UF_NOT', 'CLASSI_FIN']
df = pd.read_csv(
    'data/raw/srag_2024.csv',
    sep=';',
    encoding='utf-8',
    usecols=usecols,
    low_memory=False
)

# 2. Filtrar Parana
df = df[df['SG_UF_NOT'] == 'PR'].copy()

# 3. Filtrar influenza (codigo 1 no dicionario do SRAG)
df = df[df['CLASSI_FIN'] == 1].copy()

# 4. Converter data (formato ISO)
df['DT_NOTIFIC'] = pd.to_datetime(df['DT_NOTIFIC'], errors='coerce')
df = df.dropna(subset=['DT_NOTIFIC'])

# 5. Agregar por semana
df['semana'] = df['DT_NOTIFIC'].dt.to_period('W').dt.start_time

weekly = df.groupby('semana').size().reset_index(name='casos')
weekly = weekly.sort_values('semana').reset_index(drop=True)

# 6. Salvar
weekly.to_csv('data/raw/influenza_parana_semanal.csv', index=False)
print(f'Total de semanas: {len(weekly)}')
print(f'Total de casos: {weekly["casos"].sum()}')