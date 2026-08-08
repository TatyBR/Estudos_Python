#%%
import pandas as pd
import numpy as np

#%%
# excel = openpyxl 
df_xsales = pd.read_excel("dados/BaseDados.xlsx")

# %%
df_xsales.head()

#%%
df_xsales.tail()
# %%

df_xsales.info()
# %%

print(f"O DataFrame possui {df_xsales.shape[0]} linhas e {df_xsales.shape[1]} colunas.")

# %%

df_xsales[['Valor Total', 'Desconto', 'Valor Total c/ Desconto','Custo Total']].describe().round(2)

# %%,
# Alterando o nome das colunas:
colunas_novas = {
    'Tipos de Clientes': 'tipo_clientes',
    'País': 'pais',
    'Produto': 'produto',
    'Valor Total': 'valor_total',
    'Desconto': 'desconto',
    'Valor Total c/ Desconto': 'desconto_total',
    'Custo Total':'custo_total',
    'Data':'data'
}
df_xsales.rename(columns=colunas_novas, inplace=True)

#%%
df_xsales.head()

# %%

# A empresa gerou Lucro ou Prejuízo no período?
# - Qual período? Como não especificou: todo período.
# - Base: set/2018 até dez/2019, 2018 incompleto!!!
# - Calcular o lucro: Valor com desconto - Custo total
# - Verificar se é $ ou R$, antes de especificar.

df_xsales['lucro'] = df_xsales['desconto_total'] - df_xsales['custo_total']

# %%
df_xsales.head()

# %%

# Há valores de lucro negativo (Prejuízo)?
df_xsales[df_xsales['lucro']<0]

# %%

resultado_periodo = df_xsales['lucro'].sum()
# :, representa a separação do milhar
print(f"O resultado do período foi de $ {resultado_periodo.round(2):,}")

# %%

# as colunas agrupadas viram índice, no caso, a coluna data virou um índice
df_xsales_agrup_data = df_xsales.groupby('data').agg({
        'desconto_total': np.sum
})

# %%

# Resetando o índice (coluna data)
df_xsales_agrup_data.reset_index(inplace=True)

# %%

df_xsales_agrup_data.head()

# %%
df_xsales_agrup_data.columns
# %%

# Qual o faturamento Médio Mensal desta Empresa?

media_periodo = df_xsales_agrup_data['desconto_total'].mean()
print(f"O resultado do período foi de $ {media_periodo.round(2):,}")

# %%
