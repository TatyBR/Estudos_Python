# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

# Em graf. barras geralmente o eixo X são variáveis categóricas e o eixo Y são variáveis numéricas.

# %%
# Gráfico sem sentido:
df['sepal_length'].plot(kind='bar')
plt.show()

# %%
df['sepal_length'].head().plot(kind='bar')
plt.show()

# %%
# Gráfico mais interessante/correto:
# Contando valores e plotando um gráfico de barras:
df['species'].value_counts().plot(kind='bar',
                                  title='Contagem de espécies',
                                  color='orange')
plt.show()

# %%
# UTILIZANDO O MATPLOTLIB:
plt.figure(figsize=(15, 5))
plt.bar(x=df['species'], height=df['species'].count(), color='orange')
plt.title('Contagem de espécies')
plt.xlabel('Espécies')  
plt.ylabel('Total')
plt.show()

# %%
# barras horizontais:
plt.figure(figsize=(15, 5))
plt.barh(y=df['species'], width=df['species'].count(), color='magenta')
plt.title('Contagem de espécies')
plt.xlabel('Total')
plt.ylabel('Espécies')  
plt.show()

# %%
contagem = df['species'].value_counts()

plt.barh(y=contagem.index, width=contagem.values, color='magenta')
plt.xlabel("Quantidade")
plt.ylabel("Espécies")
plt.title("Distribuição das espécies")
plt.show()

# %%
# UTILIZANDO O SEABORN:
df_grupo = df.groupby('species').agg({'sepal_length': np.median})
df_grupo.head()

# %%
sns.barplot(data=df_grupo, x=df_grupo.index, y='sepal_length', palette='pastel')
plt.title('Mediana do comprimento da sépala por espécie')

# %%

sns.barplot(data=df_grupo, y=df_grupo.index, x='sepal_length', palette='Set2')
plt.title('Mediana do comprimento da sépala por espécie')
plt.show()