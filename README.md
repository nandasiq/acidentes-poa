# 🚦 Análise de Acidentes de Trânsito em Porto Alegre (2020–2024)

Este repositório contém o código, dados e configuração de ambiente para o 
Trabalho de Conclusão de Curso (MBA em Tecnologia para Negócios:
AI, Data Science e Big Data), cujo objetivo é:

- Analisar dados de acidentes de trânsito em Porto Alegre (2020–2024);
- Investigar fatores de risco (clima, horário, regiões críticas);
- Criar modelos preditivos para estimar acidentes futuros;
- Propor medidas de **moderação de tráfego** baseadas em dados.

---

## 📂 Estrutura do projeto
acidentes-poa/  
│  
├── .devcontainer/ # configuração de ambiente Codespaces  
│ └── devcontainer.json  
│
├── jupyter/ # notebooks e dados  
│ ├── dados/  
│ │ └── acidentes.csv  
│ └── projeto.ipynb  
│  
├── ambiente.txt # dependências Python  
└── README.md # este arquivo  

---

## ⚙️ Ambiente de Desenvolvimento

Este projeto foi pensado para rodar diretamente no **GitHub Codespaces**
ou em containers Docker com suporte a **devcontainers**.

### 1. Abrir no Codespaces
- Clique no botão **Code > Codespaces > Create codespace on main**.  
- O container será criado com **Python 3.12**.  
- Automaticamente, o comando abaixo será executado:

```bash
pip install -r ambiente.txt
```

### 2. Dependências principais

O arquivo ambiente.txt lista as bibliotecas necessárias:
  - pandas, numpy, pyarrow → manipulação de dados
  - matplotlib, seaborn, plotly → visualização
  - scikit-learn, statsmodels → modelagem estatística e preditiva
  - requests, openmeteo-requests, requests-cache, retry-requests → integração com API Open-Meteo
  - jupyter → execução dos notebooks

---

### 📊 Uso

1. Acesse a pasta jupyter/
2. Abra o notebook projeto.ipynb
3. Execute a primeira célula de validação do ambiente

   Ela irá confirmar se o ambiente está pronto ou sugerir a instalação de bibliotecas faltantes.

### 📌 Observações
- Os dados de acidentes são fornecidos pela EPTC/Prefeitura de Porto Alegre.
- Dados climáticos são obtidos via Open-Meteo API
- O foco é explorar correlações entre acidentes e fatores externos (horário, clima, localização)
e avaliar medidas preventivas de segurança viária.
