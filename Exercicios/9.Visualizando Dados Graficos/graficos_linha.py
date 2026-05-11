# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# lista os datasets disponíveis no seaborn
# precisa de conexão com a internet
sns.get_dataset_names()

# %%
# carrega o dataset 'iris' do seaborn   
df = sns.load_dataset('iris')
df.head()

# %%
df.info()

# %%
df['species'].value_counts()

# %%

# GRÁFICO DE LINHA
df['sepal_length'].plot()

# %%

# figsize: largura x altura (tamanho do gráfico)
# linewidth: espessura da linha
# color: cor da linha
# marker: marcador/"bolinha" para cada ponto (opcional)
df['sepal_length'].plot(figsize=(15, 5),
                        linewidth=4,
                        color='red',
                        title='Tamanho da Sépala',
                        xlabel='Índice',
                        ylabel='Tamanho (cm)',
                        marker='o',
                        linestyle='-.',
                        legend=True)

# %%
# Gráfico com matplotlib
# Aqui consigo definir meu eixo X e Y
# Para que não apareça uma linha de informação junto com o gráfio: colocar , no fim do plt.plot() ou usar plt.show()
plt.figure(figsize=(15, 5))
plt.plot(df.index, df['sepal_length'])
plt.plot(df.index, df['sepal_width'], color='green', linewidth=2, linestyle='--')    
plt.title('Tamanho da Sépala')
plt.xlabel('Índice')        
plt.ylabel('Tamanho (cm)')
plt.legend(['Altura da Sépala', 'Largura da Sépala'])
plt.show()

# %%
df.head(5)

# %%
# visualizando vários gráficos juntos
plt.figure(figsize=(15, 5))

# plt.subplot(linha, qtde_colunas, posição do gráfico)
plt.subplot(1, 3, 1)  # (n_linhas, n_colunas, posição)
plt.plot(df.index, df['sepal_length'], color='red')
plt.title('Altura da Sépala')
plt.ylabel('Tamanho (cm)')  

plt.subplot(1, 3, 2)  # (n_linhas, n_colunas, posição)
plt.plot(df.index, df['sepal_width'], color='green', linewidth=2, linestyle='--')
plt.title('Largura da Sépala')
plt.ylabel('Tamanho (cm)')  

plt.subplot(1, 3, 3)  # (n_linhas, n_colunas, posição)
plt.plot(df.index, df['petal_length'], color='blue')
plt.title('Altura da Pétala')
plt.ylabel('Tamanho (cm)')  

plt.show()

# %%
# GRÁFICO DE LILNHA COM SEABORN
sns.set_style('darkgrid')  # estilo do gráfico
plt.figure(figsize=(15, 5))
sns.lineplot(data=df, x=df.index, y='sepal_length', color='red', hue='species')
plt.title('Tamanho da Sépala')
plt.xlabel('Índice')
plt.ylabel('Tamanho (cm)')
plt.legend(title='Espécies', loc='upper left')
plt.show()


