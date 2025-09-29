# Análise e Modelagem de Acidentes de Trânsito em Porto Alegre (2020–2025)

Este projeto é parte do Trabalho de Conclusão de Curso (TCC) do MBA em **Tecnologia para Negócios: IA, Data Science e Big Data**.  
O objetivo é aplicar técnicas de **Ciência de Dados e Aprendizado de Máquina** para analisar os acidentes de trânsito em Porto Alegre, correlacionando com fatores climáticos (chuva) e propondo modelos preditivos para apoiar políticas públicas como o **PNATRANS** (Plano Nacional de Redução de Mortes e Lesões no Trânsito).

---

## 🎯 Objetivo

1. **Limpeza e integração dos dados de acidentes (2020–2024)**, fornecidos pela EPTC/POA.  
2. **Enriquecimento dos dados** com variáveis externas, como chuva, obtidas via API **Open-Meteo**.  
3. **Análise Exploratória (EDA)** para identificar padrões temporais, geográficos e sazonais nos acidentes.  
4. **Modelagem Preditiva** utilizando técnicas de **Machine Learning** e **Séries Temporais**, com validação nos dados de **2025**.  
5. **Agente Inteligente** (caderno 05) para correlacionar pontos críticos e sugerir ações alinhadas ao PNATRANS.  

---

## 🗂️ Estrutura do Projeto

- `notebooks/`  
  - `01_limpeza.ipynb` → Pré-processamento e padronização dos dados de acidentes.  
  - `02_chuva.ipynb` → Coleta e integração de dados climáticos (chuva).  
  - `03_eda.ipynb` → Análises descritivas e exploratórias.  
  - `04_modelagem.ipynb` → Modelos de aprendizado de máquina e séries temporais.  
  - `05_agente.ipynb` (em desenvolvimento) → Prototipagem de agente inteligente com recomendações para o PNATRANS.  
  - `config.py` → Funções utilitárias compartilhadas (gráficos, limpeza, integração de dados).  

- `dados/`  
  - `brutos/` → Dados originais (acidentes e clima).  
  - `intermediarios/` → Dados tratados e integrados.  
  - `processados/` → Resultados finais prontos para análise/modelagem.  

- `figures/` → Gráficos gerados nos notebooks.  
- `reports/` → Relatórios parciais e apêndices.  

---

## 📊 Metodologia

A metodologia segue as boas práticas de **Ciência de Dados**:

1. **Coleta e Limpeza de Dados**  
   - Padronização de colunas e tipagem (int, category, datetime).  
   - Criação de variáveis derivadas (UPS – Unidade Padrão de Severidade).  

2. **Integração de Dados Externos**  
   - API Open-Meteo para chuva acumulada por região de Porto Alegre.  
   - Unificação em séries temporais compatíveis com os dados de acidentes.  

3. **Análise Exploratória (EDA)**  
   - Estatísticas descritivas.  
   - Visualizações por região, logradouro, horário e severidade.  
   - Correlação entre clima e aumento de acidentes.  

4. **Modelagem Preditiva**  
   - Modelos de classificação (scikit-learn).  
   - Séries temporais (SARIMAX, LSTM).  
   - Avaliação em treino, validação e teste (70/15/15).  
   - Validação final com dados de 2025.  

5. **Agente Inteligente (PNATRANS)**  
   - Identificação de pontos críticos.  
   - Sugestão de ações alinhadas às metas de redução de mortes até 2028.  

---

## ⚙️ Como Executar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/nandasiq/acidentes-poa.git
   cd acidentes-poa
2. Clone este repositório:  
   ```bash
  python3 -m venv .venv
  source .venv/bin/activate   # Linux/Mac
  .venv\Scripts\activate      # Windows
  pip install -r ambiente.txt
3. Execute os Notebooks 01-05  

-----------------------
## Principais Referências:

* Breiman, L. (2001). Statistical Modeling: The Two Cultures.
* Bishop, C. (2006). Pattern Recognition and Machine Learning. Springer.
* Hastie, T.; Tibshirani, R.; Friedman, J. (2009). The Elements of Statistical Learning. Springer.
* Murphy, K. P. (2012). Machine Learning: A Probabilistic Perspective. MIT Press.
* Géron, A. (2022). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow. O’Reilly.
* Zabala, F. J. (2019). Modelagem Preditiva. PUCRS
