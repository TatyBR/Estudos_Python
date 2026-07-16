# %%
import pandas as pd

# %%

df_vendas = pd.read_excel('dataset/vendas_geral.xlsx')
df_vendas.head(8)

# %%
# Verificando os tipos de cada coluna
#(Obs.: Não há dados faltantes)
df_vendas.info()
print("Dimensão do DataFrame:", df.shape)

# %%
# Verificando as colunas
df_vendas.columns

# %%
for coluna in df_vendas.columns:
    print(coluna)

# %%
# Acessando apenas uma coluna:
#(Pode ser usado df.Segmento = desde que não há acentos/ espaços no nome da coluna)
df_vendas['Segmento']

# %%
# Alterando o nome das colunas:
# Desta maneira ter que ter todas as colunas certinho
colunas = ['segmento', 'pais', 'produto', 'unidades_vendidas',
       'preço_unitario', 'valor_total', 'desconto', 'valor_total_desconto',
       'custo_total', 'lucro', 'data', 'mes', 'ano']

# para verificar se em colunas colocamos a quantidade correta de nomes
# print(len(colunas))
# compara com o número de colunas em df_vendas.shape

df_vendas.columns = colunas

#%%
# OUTRA FORMA DE ALTERAR O NOME DAS COLUNAS:
# df_vendas.columns = df_vendas.columns.str.lower().str.replace(" ", "_")


# %%
# OUTRA FORMA DE ALTERAR O NOME DAS COLUNAS:
# df_vendas = df_vendas.rename(columns={
    # "qtde_de_unidades_vendidas": "unidades_vendidas",
    # "valor_total_c/_desconto": "valor_total_desconto"
# })
# print(df_vendas.columns)

#%%
df_vendas.head()

# %%

# Contagem de registros 
print(df_vendas.segmento.value_counts())
print('\n')
print(df_vendas.pais.value_counts())

# %%
# # Analisando as COLUNAS QUANTITATIVAS com DESCRIBE()
df_vendas.describe().round(2).T

# %%
# Análise de margem de lucro

# Utilizando agrupamento

colunas = ['valor_total_desconto','custo_total', 'lucro']
print("Valor total por segmento:")
print(df_vendas.groupby('segmento')['valor_total'].sum().round(2))
print('\n')
print(df_vendas.groupby('segmento')[colunas].sum().round(2))
# %%
df_segmento = df_vendas.groupby('segmento')[colunas].sum().round(2)
df_segmento['margem_lucro'] = round((df_segmento['lucro']/df_segmento['valor_total_desconto']) * 100,2)

# %%
df_segmento

# %%
colunas = ['valor_total_desconto','custo_total', 'lucro']
df_produto = df_vendas.groupby('produto')[colunas].sum().round(2)
df_produto['margem_lucro'] = round((df_produto['lucro']/df_produto['valor_total_desconto']) * 100,2)
df_produto

# %%

colunas = ['valor_total_desconto','custo_total', 'lucro']
df_pais = df_vendas.groupby('pais')[colunas].sum().round(2)
df_pais['margem_lucro'] = round((df_pais['lucro']/df_pais['valor_total_desconto']) * 100,2)
df_pais
# %%
