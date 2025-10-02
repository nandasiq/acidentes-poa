# Análise e Modelagem de Acidentes de Trânsito em Porto Alegre (2020–2025)

Este projeto é parte do Trabalho de Conclusão de Curso (TCC) do MBA em **Tecnologia para Negócios: IA, Data Science e Big Data**.  
O objetivo é aplicar técnicas de **Ciência de Dados e Aprendizado de Máquina** para analisar os acidentes de trânsito em Porto Alegre, correlacionando com fatores climáticos (chuva) e propondo modelos preditivos para apoiar políticas públicas como o **PNATRANS** (Plano Nacional de Redução de Mortes e Lesões no Trânsito).  

---

## Objetivo

1. **Limpeza e integração dos dados de acidentes (2020–2024)**, fornecidos pela EPTC/POA.  
2. **Enriquecimento dos dados** com variáveis externas, como chuva, obtidas via API **Open-Meteo**.  
3. **Análise Exploratória (EDA)** para identificar padrões temporais, geográficos e sazonais nos acidentes.  
4. **Modelagem Preditiva** utilizando técnicas de **Machine Learning** e **Séries Temporais**, com validação nos dados de **2025**.  
5. **Agente Inteligente** para correlacionar pontos críticos e sugerir ações alinhadas ao PNATRANS.  

---

## Estrutura do Projeto

- `notebooks/`  
  - `01_limpeza.ipynb` → Preparação inicial da base: padronização, tratamento de tipos e limpeza conforme dicionário de variáveis.    
  - `02_chuva.ipynb` → Integração dos dados meteorológicos via **API Open-Meteo**, enriquecendo a base com indicadores climáticos.
  - `03_eda.ipynb` → **Análise Exploratória de Dados (EDA)** para identificar padrões temporais, regionais e contextuais.   
  - `04_modelagem.ipynb` → Construção e comparação de modelos preditivos (**estatísticos e de ML**).  
  - `05_agente.ipynb` → Protótipo de **Agente Inteligente** que correlaciona pontos críticos e propõe soluções alinhadas ao PNATRANS.  
  - `utils/` → Funções utilitárias (constantes, caminhos, integração de dados), promovendo **reuso de código e boas práticas**.  

- `dados/`  
  - `primarios/` → Dados originais (acidentes e clima).  
  - `intermediarios/` → Dados tratados e integrados.  

- `apendices/`
   - `graficos/` → Gráficos gerados nos notebooks.  
   - `modelo/` → Armazena melhor modelo.  

---

## Metodologia

A metodologia segue as boas práticas de **Ciência de Dados**:

1. **Coleta e Limpeza de Dados**  
   - Compreensão e resumo dos dados.  
   - Padronização de colunas e tipagem (int, category, datetime).   

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

## Tecnologias Utilizadas

- **Linguagem:** Python (pandas, seaborn, matplotlib, scikit-learn, statsmodels)  
- **Infraestrutura:** GitHub Codespaces / Jupyter Notebooks  
- **APIs e Dados Externos:** Open-Meteo API  
- **Metodologias de Ciência de Dados:** CRISP-DM, TDSP  

---

## Como Executar

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

* Breiman, L. Statistical Modeling: The Two Cultures. (2001).
* Bishop, C. Pattern Recognition and Machine Learning. Springer. (2006).
* Géron, A. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow. O’Reilly. (2022).
* Han, J. et al. *Data Mining: Concepts and Techniques* (2011).
* Hastie, T.; Tibshirani, R.; Friedman, J. The Elements of Statistical Learning. Springer. (2009).
* Hyndman, R.J.; Athanasopoulos, G. *Forecasting: Principles and Practice* (2021).
* Murphy, K. P. Machine Learning: A Probabilistic Perspective. MIT Press. (2012).
* Provost, F.; Fawcett, T. *Data Science para Negócios* (2016).
* Scopel, R.; Rodrigues, R. D. *DS e AI para Eficiência nas Finanças* (2023).
* Shearer, C. *The CRISP-DM Model* (2000); Wirth, R.; Hipp, J. (2000).    
* Ward, M.; Keim, D.; Grinstein, G. *Interactive Data Visualization* (2015).  
* Ware, C. *Information Visualization: Perception for Design* (2013).  
* Zabala, F. J. Modelagem Preditiva. PUCRS (2019).