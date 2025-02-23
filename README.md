# People Analytics

Repositório com scripts, notebooks e recursos diversos para análise de dados relacionados a pessoas (People Analytics).  
Aqui você encontra soluções em Python, R, Shell, PowerShell e notebooks interativos, organizados por pastas.

## Estrutura

people_analytics/
├── python/
│   ├── coleta_biblioteca_conhecimento.py
│   ├── export_employee_data.py
│   ├── gerar_base_rh_ficticia.py
│   ├── haversine_distance.py
│   └── README.md

├── notebooks/
│   ├── README.md
│   ├── eda_examples.ipynb
│   └── venn_diagrams_diversity.ipynb
├── apps_script/
│   ├── README.md
│   ├── envio_cartas_sheets/   # Pasta específica para este projeto
│   │   ├── README.md
│   │   ├── envio_cartas_sheets.gs
│   │   ├── gerar_pdf.gs
│   │   ├── enviar_email_gmail.gs
│   │   ├── ler_arquivos_drive.gs
│   │   ├── ler_conteudo_pdf.gs
│   │   ├── gerar_menu.gs
│   │   ├── criptografar_pdf.py
├── r/
│   ├── calcular_distancia_google_maps.R
│   └── README.md
├── shell/
│   ├── README.md
│   └── ...
├── powershell/
│   ├── README.md
│   └── ...
└── README.md


- **python/**: scripts em Python para diversas tarefas (coleta de dados, exportações, análises).
  - 📍 **Cálculo de Distância Haversine** (`haversine_distance.py`) → Mede a distância entre coordenadas geográficas usando a fórmula de Haversine.
  - 📊 **Geração de Base Fictícia de RH** → Simula uma base de funcionários com cargos, salários e diversidade (`gerar_base_rh_ficticia.py`).


- **notebooks/**: notebooks Jupyter para visualizações, análises interativas ou POCs.
- **r/**: scripts em R para análises estatísticas, relatórios, geográficas, etc.
  - 📍 **Cálculo de Distância via Google Maps API** → Mede a distância entre localidades usando a API Distance Matrix.

- **shell/**: automações em Shell (bash/zsh).
- **powershell/**: automações para ambiente Windows.
- **apps_script/**: Projetos de automação no Google Apps Script.
  - 📁 **[`envio_cartas_sheets/`](apps_script/envio_cartas_sheets/)**: Gerar PDFs no Google Drive e enviá-los via Gmail automaticamente.


## Como usar

1. Faça um clone do repositório:  
   ```bash
   git clone https://github.com/diego042/people_analytics.git

2. Entre na pasta que contém o tipo de script desejado (ex.: cd people_analytics/python).

3. Leia o README.md daquela pasta para instruções específicas (dependências, como executar etc.).

## Contribuindo
Faça um fork do projeto.
Crie uma branch para suas alterações.
Abra um pull request descrevendo o que foi feito.

## Licença
Este repositório está sob licença MIT.
