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
    print("\nInfo: ")
    df.info()
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

# Adicionar/Substituir em: notebooks/utils/manipula_dados.py

def ajustar_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unifica a conversão de tipos de dados, preparando o DataFrame para EDA e Modelagem.
    - Converte colunas numéricas para float64 para lidar com nulos (compatível com ML).
    - Converte colunas de texto para 'string' ou 'category' para otimização.
    """
    # Converte colunas que devem ser inteiras para float, para suportar nulos (np.nan)
    for c in COLS_INT:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').astype('float64')
    # Converte colunas que devem ser strings
    for c in COLS_STR:
        if c in df.columns:
            df[c] = df[c].astype("string").str.strip()
    # Converte colunas categóricas explícitas e qualquer 'object' restante
    cols_to_category = COLS_CAT + df.select_dtypes(include=["object"]).columns.tolist()
    for c in set(cols_to_category): # 'set' para evitar processamento duplicado
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip().astype("category")
    return df

def criar_feat_temp(df, coluna_data='data_hora'):
    """Cria features temporais (ano, mês, dia, hora) a partir de uma coluna de data."""
    df["ano"] = df[coluna_data].dt.year
    df["mes"] = df[coluna_data].dt.month
    df["dia"] = df[coluna_data].dt.day
    df["hora_int"] = df[coluna_data].dt.hour
    return df
