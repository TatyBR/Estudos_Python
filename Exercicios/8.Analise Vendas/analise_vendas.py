# %%
import pandas as pd
import numpy as np
import os

# %%
caminho = os.path.join('datasets', 'bd_vendas.csv')

# parse: já defini quais colunas serão do tipo data e index_col: defini a coluna 'dt_venda' como índice do DataFrame
df = pd.read_csv(caminho, sep=",", parse_dates=['dt_entrega','dt_venda'], index_col='dt_venda', dayfirst=True)
df_novo = df.copy()
df_novo.head()

# %%
df_novo.info()

# %%
# Padronizando os nomes das colunas
df_novo.columns
# df_novo.columns = df_novo.columns.str.strip().str.lower().str.replace(' ', '_')

# %%

novas_colunas = ['matricula_funcionario', 'nome_funcionario', 'cargo', 'codigo_loja',
       'nome_loja', 'codigo_produto', 'descricao_produto', 'categoria',
       'preco_custo', 'valor_unitario', 'quantidade', 'comissao', 
       'dt_entrega']

df_novo.columns = novas_colunas
df_novo = df_novo[['dt_entrega','matricula_funcionario', 'nome_funcionario', 'cargo', 'codigo_loja',
       'nome_loja', 'codigo_produto', 'descricao_produto', 'categoria',
       'preco_custo', 'valor_unitario', 'quantidade', 'comissao', 
       ]]
df_novo.head()

# %%
df_novo.info()

# %%
# Alterando os tipos de dados
df_novo['matricula_funcionario'] = df_novo['matricula_funcionario'].astype(str)
df_novo['codigo_produto'] = df_novo['codigo_produto'].astype(str)
df_novo['preco_custo'] = df_novo['preco_custo'].str.replace(',', '.').astype(float)
df_novo['valor_unitario'] = df_novo['valor_unitario'].str.replace(',', '.').astype(float)
df_novo['comissao'] = df_novo['comissao'].str.replace(',', '.').astype(float)

# tipo data já alterado na leitura do arquivo com parse_dates
# df_novo['dt_venda'] = pd.to_datetime(df_novo['dt_venda'], format='%d/%m/%Y %H:%M')
# df_novo['dt_entrega'] = pd.to_datetime(df_novo['dt_entrega'], format='%d/%m/%Y %H:%M')  


# %%
df_novo.head()

# %%
df_novo.info()

# %%
# Tratando valores nulos da coluna 'comissao'
df_novo['comissao'] = df_novo['comissao'].fillna(0)

# %%
df_novo.info()

# %%
df_novo.head()

# %%
# Criando novas colunas
df_novo['total_venda'] = df_novo['valor_unitario'] * df_novo['quantidade']
df_novo.head()


# %%
# Verificando dados estatísticos
df_novo.describe().round(2)

# %%

# Definindo quais colunas quero analisar
df_novo.describe()[['preco_custo', 'valor_unitario', 'comissao', 'total_venda']].round(2)

# %%
# count: conta a quantidade de valores não nulos em cada coluna
# Em todo DataFrame
print('Contagem de valores não nulos por colunas:')
df_novo.count()

# %%
# Em uma única coluna/ ou em um subconjunto de colunas
print(df_novo['total_venda'].count())
print(df_novo[['total_venda','codigo_produto']].count())

# %%
# sum/mean: apenas em uma coluna ou de um subconjunto de colunas
# Soma em sentido de toda coluna (vertical)
colunas = ['preco_custo', 'valor_unitario', 'comissao', 'total_venda']

print('Soma total por colunas:')
print(df_novo[colunas].sum())

print('\nSoma total da coluna "total_venda": R$', df_novo['total_venda'].sum().round(2))

# %%
# axis=0 (axis='rows'): soma os valores de cada coluna (vertical) (eixo=linhas)
# axis=1 (axis='columns'): soma os valores de cada linha (horizontal) (eixo=colunas)

print(f'Soma total das colunas: {colunas} por linhas (data de venda):')
df_novo[colunas].sum(axis=1)  

# %%
print(f'Soma total das colunas: {colunas} por linhas (data de venda):')
np.sum(df_novo[colunas], axis=1)  # Soma horizontal (linhas)

# %%
print('Cálculo da Média por colunas:')
df_novo[colunas].mean().round(2)  # Média vertical (colunas)

# %%

print(f'Cálculo da Média das colunas: {colunas} por linhas (data de venda):')
df_novo[colunas].mean(axis=1).round(2)  # Média horizontal (linhas)

# %%
print(f'Cálculo da Média das colunas: {colunas} por linhas (data de venda):')
np.mean(df_novo[colunas], axis=1).round(2)  # Média horizontal (linhas)

# %%
# median: mediana, não é afetada por outliers
# tb aplicada apenas em uma coluna ou em um subconjunto de colunas]
# não é usada aplicada no DataFrame todo
print('Cálculo da Mediana por colunas:')
df_novo[colunas].median().round(2)  

# %%
# moda: valor mais frequente em uma coluna
# mais usada em dados qualitativos/categóricos, mas pode ser aplicada em dados quantitativos

print('Cálculo da Moda:')
df_novo[['categoria','nome_funcionario']].mode()  # Moda da coluna 'categoria' 

# %%
print('Cálculo da Moda:')
df_novo[['preco_custo','descricao_produto']].mode()

# %%
print('Cálculo da Moda:')
df_novo['codigo_loja'].mode()

# %%
print('Cálculo do Desvio Padrão por colunas:')
df_novo[colunas].std().round(2)  # Desvio padrão vertical (colunas)

# %%

print(f'Cálculo do Desvio Padrão das colunas: {colunas} por linhas (data de venda):')
df_novo[colunas].std(axis=1).round(2)

# %%
# quantis: valores que dividem os dados em partes iguais
# 25% dos dados estão abaixo do primeiro quartil (Q1)
# 50% dos dados estão abaixo do segundo quartil (Q2) ou mediana
# 75% dos dados estão abaixo do terceiro quartil (Q3)
print('Valores dos Quartis (Q1, Q2, Q3):')
df_novo[colunas].quantile([0.25, 0.5, 0.75]).round(2)

# %%
print('Valores do Primeiro quartil (Q1):')
df_novo[colunas].quantile(0.25).round(2)  # Primeiro quartil (Q1)

# %%
print('Contagem dos valores da coluna "descrição_produto":')
df_novo['descricao_produto'].value_counts()

# %%
# é usado o sort_index() pois a coluna descrição se torna o índice da serie resultante do value_counts()
print('Contagem dos valores da coluna "descrição_produto":')
print('(Por ordem alfabética)')
df_novo['descricao_produto'].value_counts().sort_index()

# %%
# Filtrando dados com loc (rótulo/ label)
df_novo.loc['2020-09-28']

# Filtrando dados com iloc (pela posição)
df_novo.iloc[200]  # Primeira linha do DataFrame

# %%

# UTILIZANDO FILTROS PARA ANALISAR DADOS
print('Total de vendas menor que R$ 100,00:')
df_novo[df_novo['total_venda'] < 100].head()

# %%
# Usando desta forma, o resultado é uma série booleana, onde cada linha é avaliada como True ou False
df_novo['total_venda'] < 100

# %%
print('Total de vendas menor que R$ 100,00:')
filtro_total_venda = df_novo['total_venda'] < 100
df_novo[filtro_total_venda].head()

# %%
filtro_total_venda = df_novo['total_venda'] < 100
filtro_loja = df_novo['nome_loja'] == 'Filial SP'

print('Total de vendas menor que R$ 100,00 e loja "Filial SP":')
df_novo[filtro_total_venda & filtro_loja].head()

# %%
# Relembrando o loc
# d.loc[linha, coluna]
df_novo.loc['2020-04-05 09:55:00', ['total_venda']]

# %% 

print('Todas as lojas CL004 com todas as colunas:')
df_novo.loc[df_novo['codigo_loja'] == 'CL004', : ]

# %%

print('Todas os produtos 10017 com as colunas preco_custo para frente:')
df_novo.loc[df_novo['codigo_produto'] == '10017', 'preco_custo': ]

# %%
# FILTRANDO POR QUERYS
# Usar " " para a query

print('Todas as vendas da categoria "Cozinha":')
df_novo.query("categoria == 'Cozinha'")


# %%


# usando query com AND ou OR
print('Todas as vendas da categoria "Cozinha" e loja "Filial SP":')
df_novo.query("nome_loja == 'Filial SP' and descricao_produto == 'Fritadeira elétrica'")

# %%
df_novo.iloc[0:5, 0:5]  # Primeiras 5 linhas e primeiras 5 colunas

# %%
df_novo.groupby('nome_loja')['total_venda'].sum().round(2)

# %%
df_novo.groupby('nome_loja')['total_venda'].sum().round(2).to_frame()

# %%
df_novo.groupby('nome_funcionario')['total_venda'].sum().round(2).to_frame()

# %%
df_fatura_funcionario = df_novo.groupby('nome_funcionario')['total_venda'].sum().round(2).to_frame()
df_fatura_funcionario.loc['Marta Cury']

# %%

# AGREGAÇÕES
df_novo.groupby('descricao_produto')['total_venda'].agg(['sum', 'mean', 'std', 'count']).round(2)

# %%
df_novo.groupby('descricao_produto').agg(
                                   {'total_venda': ['sum', 'mean', 'std', 'count'], 
                                    'quantidade': ['sum', 'mean']}).round(2)

# %%

# Agrupando pelo índice
df_novo.groupby(df.index).agg({'total_venda': 'sum'})

# %% 
df_novo.groupby(df.index.year).agg({'total_venda': 'sum'})

# %%

# Agrupando por mais de uma coluna
# As colunas se tornam o índice
# a primeira coluna do groupby é a mais externa, ou seja, a mais geral, e a última coluna é a mais interna, ou seja, a mais específica
df_novo.groupby(['nome_loja', 'nome_funcionario', 'descricao_produto']).agg({'total_venda': 'sum'}).round(2)

# %%
# exportar o resultado para o excel
# deve-se instalar a biblioteca openpyxl 
df_novo.groupby(['nome_loja', 'nome_funcionario', 'descricao_produto']).agg({'total_venda': 'sum'}).round(2).to_excel('total_venda_funcionario.xlsx')

# %%
# AGRUPANDO DADOS POR PIVOT_TABLE()
# index: coluna que se torna o índice do DataFrame
# values: coluna que se torna os valores do DataFrame
# columns: linhas que se tornam as colunas do DataFrame 
df_novo.pivot_table(index='descricao_produto',
                    values='total_venda',
                    aggfunc='sum').round(2)

# %%
df_novo.pivot_table(index='descricao_produto',
                    values=('preco_custo','total_venda'),
                    aggfunc='sum').round(2)

# %%
df_novo.pivot_table(index='descricao_produto',
                    values=('total_venda'),
                    columns='nome_loja',
                    margins=True,  # Adiciona uma coluna e uma linha final de totais
                    aggfunc='sum').round(2)

# %%
df_novo.head(4)

# %%
df_novo.pivot_table(index='nome_funcionario',
                    values=('total_venda'),
                    columns='descricao_produto',
                    margins=True,  # Adiciona uma coluna e uma linha final de totais
                    aggfunc='sum').round(2)

# %%
df_novo.pivot_table(index='descricao_produto',
                    values=('total_venda'),
                    columns=('nome_loja','nome_funcionario'),
                    margins=True,  # Adiciona uma coluna e uma linha final de totais
                    aggfunc='sum').round(2)

# %%

# iterando sobre as linhas do DataFrame
for label, row in df_novo.iterrows():
    print(f'Índice: {label}')
    print(f'Linha: {row}')
    print('---')
    # break  # Para o loop após a primeira iteração para evitar imprimir todas as linhas

# %%

# se usar for _, row....o índice é descartado, apenas a linha
for label, row in df_novo.iterrows():
    print(f'Índice: {label}')
    print(f'Linha: {row.total_venda}')
    print('---')

# %%
# itertuples: itera sobre as linhas do DataFrame, mas retorna uma tupla com o índice e a linha como um Series
for row in df_novo.itertuples():
    print(f'Índice: {row.Index}')
    print(f'Linha: {row}')
    print('---')

# %%   
for row in df_novo.itertuples():
    print(f'Categoria do produto: {row.categoria}')
    print(f'Descrição do produto: {row.descricao_produto}')
    print(f'Total de vendas: {row.total_venda}')
    print('---')