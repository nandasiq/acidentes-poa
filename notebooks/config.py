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
ANOS = [2020, 2021, 2022, 2023, 2024, 2025]

################################
# Funções Visualização de dados
################################

# Configura estilo global dos gráficos
def config_graf():
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12

# Cria gráfico distribuição de valores de uma coluna
def graf_contagem(df, coluna, titulo, rotacao=0, top=None, ordenar="valor"):
    contagem = df[coluna].value_counts()
    if ordenar == "indice":
        contagem = contagem.sort_index()
    if top:
        contagem = contagem.head(top)
    ax = contagem.plot(kind="bar")
    ax.set_title(titulo)
    plt.xticks(rotation=rotacao)
    plt.show()

# Cria gráfico crosstab entre duas colunas
def graf_crosstab(df, coluna1, coluna2, titulo, empilhado=True,
                   rotacao=0, top=None, horizontal=False):
    """
    Plota crosstab entre duas colunas.
    - empilhado: True para gráfico de barras empilhadas
    - rotacao: ângulo dos rótulos no eixo X
    - top: limitar aos N primeiros valores de coluna1
    - horizontal: True para gráfico de barras horizontais
    """
    tabela = pd.crosstab(df[coluna1], df[coluna2])
    if top:
        tabela = tabela.sort_values(by=tabela.columns.tolist(),
                                     ascending=False).head(top)
    if horizontal:
        tabela.plot(kind="barh", stacked=empilhado, figsize=(10,6))
    else:
        tabela.plot(kind="bar", stacked=empilhado, figsize=(12,6))
        plt.xticks(rotation=rotacao)
    plt.title(titulo)
    plt.show()

# Cria gráfico série temporal agregada por período (M = mensal, Y = anual)
def graf_temporal(df, coluna_data, coluna_valor, freq="M", titulo="Série temporal"):
    serie = df.set_index(coluna_data).resample(freq)[coluna_valor].count()
    serie.plot(marker="o")
    plt.title(titulo)
    plt.show()

# Calcula e plota proporção de vítimas em relação ao total de acidentes por veículo.
def proporcao_por_veiculo(df, cols_veic, alvo, 
                          titulo="Proporção de vítimas por veículo"):
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

# Cria mapa de calor de contagem
def graf_heatmap_cont(df, eixo_y, eixo_x, titulo="Mapa de Calor - Contagem",
                          largura=10, altura=6, cmap="Blues"):
    tabela = pd.crosstab(df[eixo_y], df[eixo_x])
    plt.figure(figsize=(largura, altura))
    sns.heatmap(tabela, annot=True, fmt=".0f", cmap=cmap, cbar=True)
    plt.title(titulo)
    plt.ylabel(eixo_y)
    plt.xlabel(eixo_x)
    plt.show()

# Heatmap de Valores (média/soma de severidade, etc.)
def graf_heatmap_val(df, eixo_y, eixo_x, valor, aggfunc="sum",
                         titulo="Mapa de Calor - Valores", largura=10, altura=6, cmap="Reds", fmt=".0f"):
    """
    Cria mapa de calor usando uma variável numérica agregada (ex.: soma ou média).
    - valor: coluna numérica
    - aggfunc: "sum", "mean", etc.
    """
    tabela = pd.crosstab(
        index=df[eixo_y],
        columns=df[eixo_x],
        values=df[valor],
        aggfunc=aggfunc
    ).fillna(0)

    # garante que todos os valores da matriz sejam float64
    tabela = tabela.astype("float64")

    plt.figure(figsize=(largura, altura))
    sns.heatmap(tabela, annot=True, fmt=fmt, cmap=cmap, cbar=True)
    plt.title(titulo)
    plt.ylabel(eixo_y)
    plt.xlabel(eixo_x)
    plt.show()

############
# Modelagem
############

# Bibliotecas

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from statsmodels.tsa.statespace.sarimax import SARIMAX
from  xgboost import XGBClassifier

# Funções

def balancear(X, y):
    sm = SMOTE(random_state=42)
    return sm.fit_resample(X, y)

def split_train_test(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

def avaliar_modelo(modelo, X_test, y_test):
    """Imprime métricas de avaliação e retorna o relatório"""
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred))
    return confusion_matrix(y_test, y_pred)

def plotar_matriz_confusao(cm, labels):
    """Exibe matriz de confusão formatada"""
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.ylabel("Real")
    plt.xlabel("Previsto")
    plt.show()

############
# Constantes
############

COLS_VEICULOS = [
    "auto",
    "taxi",
    "lotacao",
    "onibus_urb",
    "onibus_met",
    "onibus_int",
    "caminhao",
    "moto",
    "carroca",
    "bicicleta",
    "outro",
    "patinete"
]
