"""
Funções de visualização padronizadas.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def config_graf():
    """Configura estilo global para gráficos."""
    sns.set(
        style="whitegrid",
        rc={"figure.figsize": (12, 6), "axes.titlesize": 14, "axes.labelsize": 12}
    )


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
                                    ascending=True).head(top)
    ax = tabela.plot(kind="barh" if horizontal else "bar",
                     stacked=empilhado, figsize=(10,6))
    plt.xticks(rotation=rotacao)
    plt.title(titulo)
    plt.show()

def graf_temporal(df, coluna_data, coluna_valor, freq="M", titulo="Série temporal"):
    serie = df.set_index(coluna_data).resample(freq)[coluna_valor].count()
    serie.plot(marker="o", title=titulo)
    plt.show()

def graf_top_variaveis(df, cols, titulo="Ranking de variáveis", n=None):
    """Plota ranking das variáveis pelo total (soma)."""
    config_graf()
    df[cols].sum().nlargest(n).plot(kind="bar")
    plt.title(titulo)
    plt.ylabel("Total")
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
    # Exclui registros de 2025
    df_filtrado = df[df["data"].dt.year < 2025]

    # Agrupa por ano e soma as colunas de veículos
    df_group = df_filtrado.groupby(df_filtrado["data"].dt.year)[cols_veic].sum()

    # Plota
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