# Arquivo de configuração global

# Imports principais
import os
import warnings

# Manipulação de dados
import pandas as pd
import numpy as np

# Visualização
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

###########################
# Configurações globais
###########################

# Suprimir warnings desnecessários
warnings.filterwarnings("ignore", category=FutureWarning)

# Pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:,.2f}".format)

# Estilo de gráficos
plt.style.use("seaborn-v0_8")
sns.set_theme(palette="deep", style="whitegrid")

###########################
# Funções utilitárias
##########################

# Mostra um resumo rápido de um DataFrame:
# dimensões, tipos, nulos e primeiras linhas.
def resumo_df(df, linhas=5):
    
    print("Dimensões:", df.shape)
    print("\nTipos de dados:")
    print(df.dtypes)
    print("\nNulos por coluna:")
    print(df.isnull().sum())
    display(df.head(linhas))

# Salva DataFrame em formato Parquet sem index.
def salvar_parquet(df, caminho):
    df.to_parquet(caminho, index=False)
    print(f"✅ DataFrame salvo em {caminho}")

# Retorna percentual de valores nulos por coluna.
def checar_nulos(df):
    return (df.isnull().mean() * 100).round(2).sort_values(ascending=False)


# Cria um gráfico de barras para uma coluna categórica ou histograma se numérica.
def grafico_simples(df, coluna, titulo="Distribuição"):
    plt.figure(figsize=(8,5))
    if pd.api.types.is_numeric_dtype(df[coluna]):
        sns.histplot(df[coluna], kde=False, bins=20)
    else:
        sns.countplot(x=df[coluna], order=df[coluna].value_counts().index)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.show()


def evolucao_varios(df, cols_veic):
    """
    Plota a evolução anual de acidentes para uma lista de veículos.
    
    Parâmetros:
    df : DataFrame com a coluna 'data' em datetime
    cols_veic : list de str, colunas de veículos
    """
    df_group = df.groupby(df["data"].dt.year)[cols_veic].sum()
    df_group.plot(kind="line", marker="o", figsize=(10,6))
    plt.title("Evolução de acidentes por tipo de veículo (2020–2024)")
    plt.xlabel("Ano")
    plt.ylabel("Nº de acidentes")
    plt.legend(title="Veículo")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()