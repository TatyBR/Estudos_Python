# %%
import pandas as pd

# %%

df = pd.read_excel('dataset/vendas_geral.xlsx')
df.head(8)

# %%
# Verificando os tipos de cada coluna
#(Obs.: Não há dados faltantes)
df.info()
print("Dimensão do DataFrame:", df.shape)

# %%
# Verificando as colunas
df.columns

# %%
for coluna in df.columns:
    print(coluna)

# %%
# Acessando apenas uma coluna:
#(Pode ser usado df.Segmento = desde que não há acentos/ espaços no nome da coluna)
df['Segmento']

# %%
# Alterando o nome das colunas:
# Desta maneira ter que ter todas as colunas certinho
colunas = ['segmento', 'pais', 'produto', 'unidades_vendidas',
       'preço_unitario', 'valor_total', 'desconto', 'valor_total_desconto',
       'custo_total', 'lucro', 'data', 'mes', 'ano']

df.columns = colunas

#%%
# OUTRA FORMA DE ALTERAR O NOME DAS COLUNAS:
# df.columns = df.columns.str.lower().str.replace(" ", "_")

# %%
# OUTRA FORMA DE ALTERAR O NOME DAS COLUNAS:
# df = df.rename(columns={
    # "qtde_de_unidades_vendidas": "unidades_vendidas",
    # "valor_total_c/_desconto": "valor_total_desconto"
# })
# print(df.columns)