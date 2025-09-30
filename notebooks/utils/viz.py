"""
Funções de visualização padronizadas.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def config_graf():
    """Configura estilo global dos gráficos."""
    sns.set_style("whitegrid")
    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "axes.titlesize": 14,
        "axes.labelsize": 12
    })

def graf_contagem(df, coluna, titulo, rotacao=0, top=None, ordenar="valor"):
    contagem = df[coluna].value_counts()
    if ordenar == "indice":
        contagem = contagem.sort_index()
    if top:
        contagem = contagem.head(top)
    contagem.plot(kind="bar", title=titulo)
    plt.xticks(rotation=rotacao)
    plt.show()

def graf_crosstab(df, coluna1, coluna2, titulo, empilhado=True,
                   rotacao=0, top=None, horizontal=False):
    tabela = pd.crosstab(df[coluna1], df[coluna2])
    if top:
        tabela = tabela.sort_values(by=tabela.columns.tolist(),
                                    ascending=False).head(top)
    ax = tabela.plot(kind="barh" if horizontal else "bar",
                     stacked=empilhado, figsize=(10,6))
    plt.xticks(rotation=rotacao)
    plt.title(titulo)
    plt.show()

def graf_temporal(df, coluna_data, coluna_valor, freq="M", titulo="Série temporal"):
    serie = df.set_index(coluna_data).resample(freq)[coluna_valor].count()
    serie.plot(marker="o", title=titulo)
    plt.show()

def graf_heatmap_cont(df, eixo_y, eixo_x, titulo="Mapa de Calor - Contagem",
                      largura=10, altura=6, cmap="Blues"):
    tabela = pd.crosstab(df[eixo_y], df[eixo_x])
    plt.figure(figsize=(largura, altura))
    sns.heatmap(tabela, annot=True, fmt=".0f", cmap=cmap, cbar=True)
    plt.title(titulo)
    plt.show()

def graf_heatmap_val(df, eixo_y, eixo_x, valor, aggfunc="sum",
                     titulo="Mapa de Calor - Valores", largura=10, altura=6, cmap="Reds", fmt=".0f"):
    tabela = pd.crosstab(
        index=df[eixo_y], columns=df[eixo_x],
        values=df[valor], aggfunc=aggfunc
    ).fillna(0).astype("float64")
    plt.figure(figsize=(largura, altura))
    sns.heatmap(tabela, annot=True, fmt=fmt, cmap=cmap, cbar=True)
    plt.title(titulo)
    plt.show()
