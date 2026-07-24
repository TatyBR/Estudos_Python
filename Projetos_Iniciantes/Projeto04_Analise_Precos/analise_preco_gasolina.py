# Análise variação do preço da gasolina
# Gerar uma tabela com a variação percentual ano a no do preço médio da gasolina comum no estado do Rio de Janeiro
# Dados do kaggle

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
df_precos = pd.read_csv('dataset/precos.tsv', sep='\t', parse_dates=['DATA INICIAL','DATA FINAL'], encoding='utf-8')

# %%
df_precos.head()
# %%
df_precos.info()
# %%
# Selecionando apenas algumas colunas
# loc[linhas,colunas]: [todas as linhas, da 1ª coluna até 'PREÇO MÁXIMO REVENDA']
df_precos_trat = df_precos.loc[:,: 'PREÇO MÁXIMO REVENDA'].copy()

# %%
df_precos_trat.columns = ['dt_inicial', 'dt_final', 'regiao', 'estado', 'produto',
       'nr_postos_pesquisados', 'und_medida', 'preco_medio_revenda', 'std_revenda', 'preco_min_revenda',
       'preco_max_revenda']

# %%
df_precos_trat.head()
# %%
