import pandas as pd
import numpy as np


caminho_dados = 'dados/acidentes.csv'
separador_original = ';'
codificacao = 'utf-8'

caminho_dados_virgula = 'dados/acidentes-virgula.csv'
separador_virgula = ','

try:
    df = pd.read_csv(caminho_dados, sep=separador_original, encoding=codificacao)

    print("CSV original lido com sucesso! Primeiras 5 linhas:")
    print(df.head())
    print("\nInformações do DataFrame original:")
    df.info()

    df.to_csv(caminho_dados_virgula, sep=separador_virgula, encoding=codificacao, index=False)

    print(f"\nArquivo ajustado salvo como '{caminho_dados_virgula}' com separador '{separador_virgula}'.")


except FileNotFoundError:
    print(f"Erro: Arquivo '{caminho_dados}' não encontrado. Verifique o caminho.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")