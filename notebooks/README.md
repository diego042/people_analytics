# Notebooks

Esta pasta contém **notebooks Jupyter** para análises, demonstrações e visualizações relacionadas a People Analytics.

## Como usar

1. Certifique-se de ter o **Jupyter** instalado (ou use o JupyterLab/VSCode).
2. Abra o notebook desejado (`.ipynb`) no seu ambiente Jupyter.
3. Siga as instruções dentro das células para instalar dependências e executar as análises.

## Lista de Notebooks

### 1. `venn_diagrams_diversity.ipynb`
- **Descrição**: Gera diagramas de Venn para analisar recortes de diversidade (raça, gênero, PCD, LGBTQIA+) por especialidade.
- **Dependências**: `pandas`, `matplotlib`, `venn`
- **Execução**:
  - Abra `venn_diagrams_diversity.ipynb` no Jupyter.
  - Execute as células em ordem.
  - Ajuste os dados e rótulos conforme necessário.

### 2. `eda_examples.ipynb` (Exploratory Data Analysis - EDA)
- **Descrição**: Template completo para **Análise Exploratória de Dados (EDA)** utilizando bibliotecas avançadas como `pandas_profiling`, `dtale` e `sweetviz`.
- **Funcionalidades**:
  - Geração automática de relatórios detalhados sobre os dados
  - Visualizações interativas para análise rápida
  - Suporte para comparação entre conjuntos de dados
- **Execução**:
  - Instale as dependências com:
    ```bash
    pip install pandas numpy dtale sweetviz pandas-profiling
    ```
  - Abra o Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
  - Execute o notebook `eda_examples.ipynb` e substitua o dataset pelos seus próprios dados.

📌 **Dica:** Esse template pode ser reutilizado para qualquer dataset, bastando modificar o caminho do arquivo de entrada.
