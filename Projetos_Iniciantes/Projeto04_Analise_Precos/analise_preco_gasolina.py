# Análise variação do preço da gasolina
# Gerar uma tabela com a variação percentual ano a no do preço médio da gasolina comum no estado do Rio de Janeiro
# Dados do kaggle

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

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
# Verficando a quantidade de estados
len(df_precos_trat['estado'].unique())

# %%
# Verficando os produtos existentes
df_precos_trat['produto'].unique()

# %%
substituir = {'OLEO DIESEL':'ÓLEO DIESEL',
              'OLEO DIESEL S10':'ÓLEO DIESEL S10'}

df_precos_trat['produto'] = df_precos_trat['produto'].replace(substituir)
# %%
# Verificando o min() e o max() nas colunas de data conseguimos ver se temos anos incompletos
# Analisamos se deixamos ou excluímos os anos incompletos
print(df_precos_trat['dt_final'].min())
print(df_precos_trat['dt_final'].max())

#%%
df_precos_trat.shape
# %%
# Selecionando o estado e o produto necessário
df_precos_RJ = df_precos_trat.query("estado == 'RIO DE JANEIRO' and produto == 'GASOLINA COMUM'").copy()

# %%
df_precos_RJ.head()

# %%
# modificando o índice do dataframe RJ
df_precos_RJ.set_index('dt_final', inplace=True)

# %%
df_precos_RJ.head()

# %%
# Trás todos os registro do ano de 2010
df_precos_RJ.loc['2010']

#%%
# Verificando os anos e meses do Dataset
datas = []
# percorre todas as datas e retira o ano e o mês delas
for i in df_precos_RJ.index:
    datas.append((i.year, i.month))
datas

# %%
# para que "datas" tenha apenas valores únicos, transformar em conjunto:
# Aqui conseguimos visualizar que os anos 2004 e 2021 estão incompletos
set(datas)

# %%
# Selecionando apenas os anos completos:
df_precos_RJ = df_precos_RJ.loc['2005':'2020'].copy()
# %%
df_precos_RJ.shape

# %%
# ESTATÍSTICAS BÁSICAS
plt.figure(figsize = (15,5))
df_precos_RJ['preco_medio_revenda'].hist()
plt.show()
plt.savefig('histograma_preco_medio_revenda.png')
# %%
# Verificando a existência de outliers através do boxplot
plt.figure(figsize = (15,5))
sns.set_style('darkgrid')
sns.boxplot(data=df_precos_RJ, x='preco_medio_revenda')
plt.show()
plt.savefig('boxplot_preco_medio_revenda.png')

# %%
df_precos_RJ['preco_medio_revenda'].describe()
# %%
# Gerando a tabela de variação percentual
# last(): Trás a última informação de cada ano
df_precos_RJ.groupby(df_precos_RJ.index.year).last()
# %%
df_final_RJ = df_precos_RJ.groupby(df_precos_RJ.index.year).agg({
    'preco_medio_revenda':np.mean})

# %%
df_final_RJ.head()

# %%
df_final_RJ['valor_ano_anterior'] = df_final_RJ.shift(1)
# %%
df_final_RJ.head()
# %%
# "Exluindo" o ano de 2005 que ficou sem valor em "valor_ano-anterior"
df_final_RJ = df_final_RJ.loc['2006':]
# %%
df_final_RJ['variacao_perc'] = round(((df_final_RJ['preco_medio_revenda'] / df_final_RJ['valor_ano_anterior']) - 1) *100,2)

# %%
df_final_RJ.head()
# %%
df_final_RJ.to_excel('variacao_gasolina_RJ.xlsx')
# %%
