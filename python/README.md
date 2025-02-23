# Scripts em Python

Esta pasta contém scripts Python voltados para People Analytics, incluindo automações de coleta, exportação e análise de dados.

## Pré-requisitos

- **Python 3.x** instalado
- (Opcional) Uso de virtualenv/venv para isolar dependências

## Dependências Comuns

- `requests` (requisições HTTP)
- `pandas` (manipulação de dados)
- `openpyxl` (para escrever/ler arquivos .xlsx, se necessário)
- Possíveis outras, conforme descrito em cada script

Instale-as, se necessário:
```bash
pip install requests pandas openpyxl
```

## Scripts Disponíveis
### 1. coleta_biblioteca_conhecimento.py
Descrição: Coleta dados de uso da “Biblioteca do Conhecimento” (Workplace/Facebook), explora categorias e subcategorias, obtém métricas de engajamento e salva em Excel.
Execução:
```bash
python coleta_biblioteca_conhecimento.py
```
Observações: Ajuste o token de acesso ao Workplace no código ou via variável de ambiente.

### 2. export_employee_data.py
Descrição: Exporta dados de funcionários do Workplace (Employee Data), aguarda a geração do relatório e baixa em formato Excel.
Execução:
```bash
python export_employee_data.py
```
Observações: Requer permissões adequadas no Workplace, ajusta tempo de espera e caminho de salvamento conforme necessário.

### 3 `haversine_distance.py` (📍 Cálculo de Distância Haversine)
Descrição: Calcula a distância geodésica entre dois pontos a partir de suas coordenadas geográficas.
Bibliotecas: `math`, `pyspark.sql.functions`
Execução:
  ```python
  from haversine_distance import haversine_distance
  distancia = haversine_distance(-25.450108, -49.28545, -23.55031, -46.6342)
  print(f"Distância: {distancia:.2f} km")
  ```

### 4️ `gerar_base_rh_ficticia.py` (📊 Geração de Base Fictícia de RH)
Descrição: Gera uma base fictícia de funcionários para análise de People Analytics e recrutamento.
Bibliotecas: `pandas`, `faker`, `random`, `datetime`
Saída:
  - Cria um **CSV** com informações simuladas de funcionários, incluindo **nome, CPF, cargo, salário, data de admissão e diversidade**.
  - Pode ser utilizado para simulações de **folha de pagamento, análise de diversidade e estudos estatísticos**.
Execução:
  ```bash
  python gerar_base_rh_ficticia.py
  ```