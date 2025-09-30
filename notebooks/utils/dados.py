"""
Funções utilitárias para manipulação de DataFrames.
"""

import pandas as pd
import warnings
from .const import COLS_CAT, COLS_INT, COLS_STR

# Configurações globais do pandas
warnings.filterwarnings("ignore", category=FutureWarning)
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:,.2f}".format)

def resumo_df(df, linhas=5):
    """Mostra resumo rápido de dimensões, tipos, nulos e primeiras linhas."""
    print("Dimensões:", df.shape)
    print("\nTipos de dados:")
    print(df.dtypes)
    print("\nNulos por coluna:")
    print(df.isnull().sum())
    display(df.head(linhas))

def salvar_parquet(df, caminho):
    """Salva DataFrame em formato parquet sem index."""
    df.to_parquet(caminho, index=False)
    print(f"Salvo: {caminho}")

def checar_nulos(df):
    """Retorna percentual de valores nulos por coluna."""
    return (df.isnull().mean() * 100).round(2).sort_values(ascending=False)

def ajustar_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza tipos de colunas (categoria, inteiro, string)."""
    for c in COLS_CAT:
        if c in df.columns:
            df[c] = df[c].astype("category")
    for c in COLS_INT:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int32")
    for c in COLS_STR:
        if c in df.columns:
            df[c] = df[c].astype("string")
    return df
