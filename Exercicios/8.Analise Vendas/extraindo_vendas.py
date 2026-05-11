# %%
import pandas as pd
import numpy as np
import os

def carregar_vendas() -> pd.DataFrame:
    caminho_csv = os.path.join('datasets', 'bd_vendas.csv')
    df = pd.read_csv(caminho_csv, sep=",", parse_dates=['dt_entrega','dt_venda'], index_col='dt_venda', dayfirst=True)
    df_original = df.copy()
    return df_original