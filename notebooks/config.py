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

# Caminhos
PATH_RAW = "../dados/primarios/"
PATH_CLEAN = "../dados/intermediarios/"
PATH_CHUVA = "../dados/intermediarios/clima/"
PATH_GRAFICOS = "../apendices/graficos/"

########################
# Configurações globais
########################

# Suprimir warnings desnecessários
warnings.filterwarnings("ignore", category=FutureWarning)

# Pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:,.2f}".format)

# Estilo de gráficos
plt.style.use("seaborn-v0_8")
sns.set_theme(palette="deep", style="whitegrid")

def config_graf():
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12


######################
# Funções utilitárias
######################

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
    print(f"Salvo: {caminho}")

# Retorna percentual de valores nulos por coluna.
def checar_nulos(df):
    print("Percentual de valores nulos por coluna (%):")
    return (df.isnull().mean() * 100).round(2).sort_values(ascending=False)


################################
# Funções Visualização de dados
################################

# Cria gráfico distribuição de valores de uma coluna
def graf_contagem(df, coluna, titulo, rotacao=0, top=None):
    ax = df[coluna].value_counts().sort_index().head(top).plot(kind="bar")
    ax.set_title(titulo)
    plt.xticks(rotation=rotacao)
    plt.show()

# Cria gráfico crosstab entre duas colunas
def graf_crosstab(df, coluna1, coluna2, titulo, empilhado=True, rotacao=0):
    pd.crosstab(df[coluna1], df[coluna2]).plot(kind="bar", stacked=empilhado)
    plt.title(titulo)
    plt.xticks(rotation=rotacao)
    plt.show()

# Cria gráfico série temporal agregada por período (M = mensal, Y = anual)
def graf_temporal(df, coluna_data, coluna_valor, freq="M", titulo="Série temporal"):
    serie = df.set_index(coluna_data).resample(freq)[coluna_valor].count()
    serie.plot(marker="o")
    plt.title(titulo)
    plt.show()

# Calcula e plota proporção de vítimas em relação ao total de acidentes por veículo.
def proporcao_por_veiculo(df, cols_veic, alvo, titulo="Proporção de vítimas por veículo"):
    proporcoes = {}
    for veic in cols_veic:
        total = df[veic].sum()
        vitimas = df.loc[df[veic] > 0, alvo].sum()
        proporcoes[veic] = vitimas / total if total > 0 else 0
    
    pd.Series(proporcoes).sort_values(ascending=False).plot(kind="bar", figsize=(10,5))
    plt.title(titulo)
    plt.ylabel("Proporção")
    plt.xlabel("Veículo")
    plt.xticks(rotation=45)
    plt.show()

# Cria gráfico de evolução anual para lista de veículos.
def evolucao_veiculos(df, cols_veic, titulo="Evolução de acidentes por veículo"):
    df_group = df.groupby(df["data"].dt.year)[cols_veic].sum()
    df_group.plot(kind="line", marker="o", figsize=(10,6))
    plt.title(titulo)
    plt.xlabel("Ano")
    plt.ylabel("Nº de acidentes")
    plt.legend(title="Veículo")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

# Ordena dias da semana
def ordenar_dias_semana(df, coluna):
    dias_ordem = ["Segunda", "Terça", "Quarta",
                  "Quinta", "Sexta", "Sábado", "Domingo"]
    df[coluna] = pd.Categorical(df[coluna], categories=dias_ordem, ordered=True)
    return df

# Cria mapa de calor relacionando duas variáveis com base em uma variável alvo.
"""
    - eixo_y: variável no eixo Y
    - eixo_x: variável no eixo X
    - alvo: coluna binária (ex: ACIMA_MEDIA_FREQUENCIA)
    - foco: valor de interesse (ex: 1 para 'acima da média')
"""
def graf_heatmap(df, eixo_y, eixo_x, alvo, foco=1, largura=8, altura=6, titulo="Mapa de Calor"):
    mapa = pd.crosstab(index=df[eixo_y], columns=df[eixo_x], values=(df[alvo] == foco), aggfunc="sum").fillna(0)
    plt.figure(figsize=(largura, altura))
    sns.heatmap(mapa, annot=True, fmt=".0f", cmap="Blues", cbar=True)
    plt.title(titulo)
    plt.ylabel(eixo_y)
    plt.xlabel(eixo_x)
    plt.show()


#################################################
# Funções enriquecimento com dados metereológicos
#################################################

# URL base da API Open-Meteo (dados históricos de precipitação)
URL = "https://archive-api.open-meteo.com/v1/archive"

# Coordenadas fixas
COORD = {
    "NORTE":  (-29.987, -51.165),
    "LESTE":  (-30.040, -51.160),
    "CENTRO": (-30.027, -51.220),
    "SUL":    (-30.120, -51.230)
}

# Lista de anos estudados
ANOS = [2020, 2021, 2022, 2023, 2024]

