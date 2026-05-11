# %%

# Encontrar correlações entre duas variáveis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

# %%

plt.scatter(x=df['petal_length'], y=df['petal_width'])
plt.show()  

# %%
df.loc[:,['petal_length', 'petal_width']]

# %%
plt.figure(figsize=(6, 6))
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.title('Tamanho/ comprimento das Pétalas')
plt.show()


# %%
sns.pairplot(data=df);

# %%

sns.pairplot(data=df, hue='species');

