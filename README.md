# People Analytics

Repositório com scripts, notebooks e recursos diversos para análise de dados relacionados a pessoas (People Analytics).  
Aqui você encontra soluções em Python, R, Shell, PowerShell e notebooks interativos, organizados por pastas.

## Estrutura

people_analytics/
├── python/
│   ├── README.md
│   ├── coleta_biblioteca_conhecimento.py
│   └── export_employee_data.py
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
│   ├── README.md
│   └── ...
├── shell/
│   ├── README.md
│   └── ...
├── powershell/
│   ├── README.md
│   └── ...
└── README.md


- **python/**: scripts em Python para diversas tarefas (coleta de dados, exportações, análises).
- **notebooks/**: notebooks Jupyter para visualizações, análises interativas ou POCs.
- **r/**: scripts em R para estatísticas, relatórios, etc.
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
