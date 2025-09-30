# Pacote `utils/` – Projeto Acidentes POA

Este pacote contém funções e constantes utilizadas em todo o projeto, 
organizadas de forma modular para facilitar a **reutilização**, **manutenção** 
e **reprodutibilidade** dos experimentos.

A estrutura segue boas práticas de ciência de dados e modularização de código 
([Grus, 2016]; [Han, 2011]; [Microsoft, 2023]).

---

## Estrutura

utils/  
├── init.py          # Agregador dos módulos  
├── paths.py         # Caminhos de dados e outputs  
├── constants.py     # Constantes de colunas, coordenadas, anos  
├── data_utils.py    # Funções utilitárias de DataFrames  
├── viz_utils.py     # Funções de visualização padronizadas  
├── model_utils.py   # Funções auxiliares de modelagem  
└── clima_utils.py   # Funções para dados meteorológicos (Open-Meteo)  
