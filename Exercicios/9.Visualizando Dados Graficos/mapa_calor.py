# %%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = sns.load_dataset('iris')
df.head()

# %%

# CALCULANDO O COEFICIENTE DE CORRELAÇÃO (de -1 até 1)
# em aula: df.corr() (não funciona mais)
# correlação positiva: nº positivos, + perto de 1 + forte
# correlação negativa: nº negativos e + perto de -1 + forte (perto de 0: fraco)

cols_quantitativas = ['sepal_length','sepal_width',
                      'petal_length', 'petal_width']

df_corr = df[cols_quantitativas].corr().round(2)

# Ex.: petal_width e petal_length: corr. positiva + forte
# (qdo 1 cresce o outro tb cresce (gráfico))

# %%
sns.heatmap(data=df_corr)
plt.show()

