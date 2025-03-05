"""
📊 Dashboard Interativo de RH

Este script cria um **dashboard interativo** para visualização de dados de funcionários de uma empresa.

🔹 **Funcionalidades:**
- **Geração de dados fictícios** para análise de RH.
- **Filtro de departamentos** para visualizar métricas específicas.
- **Gráficos interativos**:
  - 📊 **Funcionários por Departamento** (gráfico de barras).
  - 🍕 **Distribuição de Desempenho** (gráfico de pizza).
- **Tabela interativa** com detalhes dos funcionários.

🔹 **Bibliotecas Utilizadas:**
- `dash`, `dash_table` → Construção do dashboard.
- `plotly.express` → Visualizações interativas.
- `pandas`, `numpy` → Manipulação e geração de dados fictícios.
- `jupyter_dash` → Execução do Dash dentro do Jupyter Notebook.

"""

import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from jupyter_dash import JupyterDash

# 🔹 Geração de dados fictícios de RH
np.random.seed(42)
num_employees = 200
departments = ['Vendas', 'Engenharia', 'RH', 'Financeiro', 'Marketing']
employee_ids = range(1, num_employees + 1)
names = [f'Funcionário {i}' for i in employee_ids]
department = np.random.choice(departments, size=num_employees)
salary = np.random.randint(3000, 15000, size=num_employees)
performance = np.random.choice(['Ruim', 'Regular', 'Bom', 'Excelente'], 
                               size=num_employees, 
                               p=[0.1, 0.4, 0.3, 0.2])

# 🔹 Gerando datas de admissão aleatórias entre 2018 e 2023
start_date = pd.to_datetime("2018-01-01")
end_date = pd.to_datetime("2023-12-31")
join_date = pd.to_datetime(
    np.random.randint(start_date.value // 10**9, end_date.value // 10**9, num_employees),
    unit='s'
)

# 🔹 Criando DataFrame
df = pd.DataFrame({
    'ID Funcionário': list(employee_ids),
    'Nome': names,
    'Departamento': department,
    'Salário': salary,
    'Desempenho': performance,
    'Data de Admissão': join_date
})

# 🔹 Inicializando o aplicativo Dash
app = JupyterDash(__name__)

# 🔹 Layout do Dashboard
app.layout = html.Div([
    html.H1("Dashboard de RH"),
    
    # 🔹 Filtro de Departamento
    html.Div([
        html.Label("Filtrar por Departamento:"),
        dcc.Dropdown(
            id='filtro-departamento',
            options=[{'label': 'Todos', 'value': 'Todos'}] +
                    [{'label': dept, 'value': dept} for dept in departments],
            value='Todos',
            clearable=False
        )
    ], style={'width': '300px', 'margin-bottom': '20px'}),
    
    # 🔹 Gráficos
    html.Div([
        dcc.Graph(id='grafico-departamento'),
        dcc.Graph(id='grafico-desempenho')
    ], style={'display': 'flex', 'justify-content': 'space-around'}),
    
    # 🔹 Tabela de Dados
    html.H2("Tabela de Funcionários"),
    dash_table.DataTable(
        id='tabela-dados',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'}
    )
])

# 🔹 Callback para atualizar gráficos e tabela com base no filtro
@app.callback(
    Output('grafico-departamento', 'figure'),
    Output('grafico-desempenho', 'figure'),
    Output('tabela-dados', 'data'),
    Input('filtro-departamento', 'value')
)
def atualizar_dashboard(dept_value):
    if dept_value == 'Todos':
        df_filtrado = df.copy()
    else:
        df_filtrado = df[df['Departamento'] == dept_value]
    
    # 📊 Gráfico de Funcionários por Departamento
    dept_count = df_filtrado['Departamento'].value_counts().reset_index()
    dept_count.columns = ['Departamento', 'Contagem']
    fig_dept = px.bar(dept_count, x='Departamento', y='Contagem',
                      title="Funcionários por Departamento")
    
    # 🍕 Gráfico de Distribuição de Desempenho
    perf_count = df_filtrado['Desempenho'].value_counts().reset_index()
    perf_count.columns = ['Desempenho', 'Contagem']
    fig_perf = px.pie(perf_count, values='Contagem', names='Desempenho',
                      title="Distribuição de Desempenho")
    
    # Atualizando a tabela
    table_data = df_filtrado.to_dict('records')
    
    return fig_dept, fig_perf, table_data

# 🔹 Executando o Dashboard no Jupyter Notebook
app.run_server(mode='inline')
