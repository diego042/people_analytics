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