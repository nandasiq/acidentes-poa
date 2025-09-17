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
    print(f"✅ DataFrame salvo em {caminho}")

# Retorna percentual de valores nulos por coluna.
def checar_nulos(df):
    return (df.isnull().mean() * 100).round(2).sort_values(ascending=False)


################################
# Funções Visualização de dados
################################

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

# Cria gráfico de barras para colunas categóricas.
def grafico_categorico(df, coluna, titulo="Distribuição de Categorias"):
    plt.figure(figsize=(8,5))
    sns.countplot(x=df[coluna], order=df[coluna].value_counts().index)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.show()

# Cria histograma para colunas numéricas.
def grafico_numerico(df, coluna, titulo="Distribuição Numérica", bins=20):
    plt.figure(figsize=(8,5))
    sns.histplot(df[coluna], bins=bins, kde=False)
    plt.title(titulo)
    plt.show()

# Cria gráfico da evolução anual para lista de veículos.
def evolucao_veiculos(df, cols_veic, titulo="Evolução de acidentes por veículo"):
    df_group = df.groupby(df["data"].dt.year)[cols_veic].sum()
    df_group.plot(kind="line", marker="o", figsize=(10,6))
    plt.title(titulo)
    plt.xlabel("Ano")
    plt.ylabel("Nº de acidentes")
    plt.legend(title="Veículo")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

# Cria gráfico da proporção de vítimas/feridos/fatais em relação ao número de acidentes por veículo.
def proporcao_veiculos(df, col_veic, col_alvo, titulo="Proporção por veículo"):
    proporcao = (df.groupby(col_veic)[col_alvo].sum() / df.groupby(col_veic)[col_alvo].count()).sort_values(ascending=False)
    proporcao.plot(kind="bar", figsize=(10,5))
    plt.title(titulo)
    plt.ylabel("Proporção")
    plt.xlabel("Veículo")
    plt.xticks(rotation=45)
    plt.show()

# Cria mapa de calor relacionando duas variáveis com base em uma variável alvo.
"""
    - eixo_y: variável no eixo Y
    - eixo_x: variável no eixo X
    - alvo: coluna binária (ex: ACIMA_MEDIA_FREQUENCIA)
    - foco: valor de interesse (ex: 1 para 'acima da média')
"""
def plota_heatmap(df, eixo_y, eixo_x, alvo, foco=1, largura=8, altura=6, titulo="Mapa de Calor"):
    mapa = pd.crosstab(index=df[eixo_y], columns=df[eixo_x], values=(df[alvo] == foco), aggfunc="sum").fillna(0)
    plt.figure(figsize=(largura, altura))
    sns.heatmap(mapa, annot=True, fmt=".0f", cmap="Blues", cbar=True)
    plt.title(titulo)
    plt.ylabel(eixo_y)
    plt.xlabel(eixo_x)
    plt.show()

# Salva o gráfico atual em PNG na pasta indicada.
def salvar_grafico(nome, pasta="graficos"):
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f"{nome}.png")
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    print(f"📊 Gráfico salvo em {caminho}")


