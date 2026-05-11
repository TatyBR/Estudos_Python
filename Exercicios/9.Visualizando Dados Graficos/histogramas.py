# %%

# Histogramas: visualiza a distribuição de frequências de uma coluna 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

# %%
df.hist(figsize=(10, 8));

# %%
df['sepal_length'].hist()

# %%
# bins: número de barras do histograma
df['sepal_length'].hist(bins=10)

# %%
plt.hist(df['petal_length'], bins=10)
plt.show()

# %%
sns.histplot(df['petal_length'], bins=10, color='blue')
plt.title('Histograma do comprimento da pétala')
plt.xlabel('Comprimento da pétala')
plt.ylabel('Frequência')
plt.show()

# %%
sns.histplot(df)    # não é uma boa prática!!!
plt.show()