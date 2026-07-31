#%%
import pandas as pd
import plotly.express as px
import openpyxl
import nbformat

#%%
df_vendas = pd.read_excel('dados/vendas.xlsx')

#%%
df_vendas.head()

# %%
df_vendas.shape

# %%
print(df_vendas.dtypes)
print("\n")
print(df_vendas.info())

# %%
df_vendas.describe()

# %%
df_vendas['loja'].value_counts().to_frame()

# %%
df_vendas['tamanho'].value_counts().to_frame(name='total_pedidos')

# %%
df_vendas['forma_pagamento'].value_counts().to_frame(name='total_pgs')

# %%
df_vendas.groupby('loja')['preco'].sum().to_frame(name='soma_total')

# %%

# preço médio por loja
df_vendas.groupby('loja')['preco'].mean().to_frame(name='preço_medio')
# %%

# ticket médio por loja: valor médio por pedido/venda completa
# valor igual o anterior pois cada linha representa 1 pedido
valor_por_pedido = df_vendas.groupby(['loja', 'id_pedido'])['preco'].sum()
ticket_medio = valor_por_pedido.groupby('loja').mean()
ticket_medio.to_frame(name='ticket_medio')

# %%
df_vendas.groupby(['estado','loja'])['preco'].sum().to_frame(name='total_preco')

# %%
df_vendas.groupby(['estado','loja','forma_pagamento'])['preco'].sum().to_frame(name='total_preco')

# %%
df_vendas.groupby(['loja','tamanho','forma_pagamento'])['preco'].sum().to_frame(name='total_preco')

# %%

px.histogram(df_vendas, x='loja', y='preco', text_auto=True, color ='forma_pagamento',title="Pedidos por Loja", labels={'preco': 'Total Preços',
        'loja': 'Loja', 'forma_pagamento': 'Forma de Pagamento'})

# gerou o gráfico mas deu erro: ValueError: Mime type rendering requires nbformat>=4.2.0 but it is not installed
# corrigir: pip install nbformat
# devido a visualização pelo #%%

# %%

# corrigindo a legenda do eixo y
fig = px.histogram(
    df_vendas,
    x='loja',
    y='preco',
    text_auto=True,
    color='forma_pagamento',
    title="Pedidos por Loja",
    labels={'preco': 'Total Preços',
            'loja': 'Loja',
            'forma_pagamento': 'Forma de Pagamento'}
)

fig.update_layout(yaxis_title="Total Preços")
fig.show()

# %%

graf_vendas_estados = px.histogram(
    df_vendas,
    x='estado',
    y='preco',
    text_auto=True,
    color='forma_pagamento',
    title="Pedidos por Loja",
    labels={'preco': 'Total Preços',
            'estado': 'Estados',
            'forma_pagamento': 'Forma de Pagamento'})

graf_vendas_estados.update_layout(yaxis_title="Total Preços")
graf_vendas_estados.show()

# %%

graf_vendas_estados.write_html("Grafico_vendas_estado.html")
# %%

# Automatizando a criação de vários graficos
colunas = ['loja','cidade','estado','regiao','tamanho','local_consumo']

for col in colunas:
    graficos = px.histogram(
    df_vendas,
    x=col,
    y='preco',
    text_auto=True,
    color='forma_pagamento',
    title="Pedidos por Loja",
    labels={'preco': 'Total Preços',
            f'{col}': col.title().replace('_',' '),
            'forma_pagamento': 'Forma de Pagamento'})

    graficos.update_layout(yaxis_title="Total Preços")
    graficos.write_html(f"Faturamento_por_{col}.html")
    graficos.show()

#%%
df_vendas.head()

# %%
df_vendas['ano_mes'] = df_vendas['data'].dt.strftime('%Y-%m')

#%%
df_vendas.head()

#%%
# Criando Gráfico Dinâmico

df_loja_mes = df_vendas.groupby(['loja','ano_mes']).preco.sum().to_frame(name='Total_Preço')
df_loja_mes.reset_index(inplace=True)
# cumsum(): soma acumulada
df_loja_mes['acumulado'] = df_loja_mes.groupby('loja')['Total_Preço'].cumsum()

graf_dinamico_loja_mes = px.histogram(
    df_loja_mes,
    x='acumulado',
    y='loja',
    text_auto=True,
    color='loja',
    title="Pedidos por Loja",
    range_x=[0,123000],
    animation_frame='ano_mes',
    labels={'loja': ' ',
            'acumulado': 'Total Preços Acumulado',
            'ano_mes': 'Evolução Ano/ Mês '})

graf_dinamico_loja_mes.update_layout(yaxis_title=" ")
graf_dinamico_loja_mes.update_layout(xaxis_title="Total Preços Acumulado")
graf_dinamico_loja_mes.write_html("grafico_dinamico_loja_mes.html")
graf_vendas_estados.show()

# %%
