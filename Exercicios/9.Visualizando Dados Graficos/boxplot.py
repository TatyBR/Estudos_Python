# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.head()

# %%
df['sepal_length'].plot(kind='box',
                        title='Comprimento da sépala',
                        color='purple',
                        figsize=(10, 10))
plt.show()

# %%
plt.figure(figsize=(10, 10))    
plt.boxplot(df['sepal_length'])
plt.title('Comprimento da sépala')
plt.ylabel('Comprimento')  
plt.show()

# %%
plt.figure(figsize=(8, 8))
sns.boxplot(data=df, x='sepal_length', y='species', palette='Set2')
plt.title('Comprimento da sépala por espécie') 
plt.xlabel('Comprimento da sépala')
plt.ylabel('Espécies')
plt.show()