# %%
from extraindo_vendas import carregar_vendas
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

df_original = carregar_vendas()
df_original.head()