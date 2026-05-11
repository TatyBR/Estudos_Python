# %%

# Somente no matplotlib!
# Usado com poucos variáveis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

# %%
df_contagem_especies = df['species'].value_counts()
df_contagem_especies

# %%
df_contagem_especies.plot(kind='pie',
                          figsize=(10, 10),
                          explode=[0.1, 0.2, 0.3])   # explode: destaca as fatias do gráfico)
plt.title('Contagem das espécies de íris')
plt.show()

# %%
df_contagem_especies.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das espécies de íris')
plt.ylabel('')    

# %%
plt.figure(figsize=(6, 6))
plt.pie(df_contagem_especies, 
        colors=['red', 'green', 'blue'], 
        labels=df_contagem_especies.values,
        explode=[0.0, 0.0, 0.1])
plt.title('Contagem das espécies de íris')
plt.legend(df_contagem_especies.index)
plt.show()