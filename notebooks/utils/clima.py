"""
Funções para tratamento de dados meteorológicos (Open-Meteo).
"""

import pandas as pd
from pathlib import Path
from .paths import PATH_CHUVA
from .const import ANOS, COORD

def carregar_parquets_chuva(path: str = PATH_CHUVA) -> pd.DataFrame:
    """
    Carrega e concatena todos os arquivos parquet de chuva, ajustando a coluna 'regiao'.

    Args:
        path (str): Caminho da pasta com arquivos parquet.

    Returns:
        pd.DataFrame: Dados meteorológicos concatenados.
    """
    pasta = Path(path)
    dfs = []
    for f in pasta.iterdir():
        if f.suffix == ".parquet":
            nome = f.stem
            regiao, _ = nome.split("_")
            df_tmp = pd.read_parquet(f)
            df_tmp["regiao"] = regiao.upper()
            dfs.append(df_tmp)

    df_meteo = pd.concat(dfs, ignore_index=True)
    df_meteo["regiao"] = df_meteo["regiao"].astype("category")
    return df_meteo
