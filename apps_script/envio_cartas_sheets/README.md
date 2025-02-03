# Envio de Cartas via Google Sheets

Este projeto contém **scripts do Google Apps Script** para **gerar PDFs automaticamente a partir de uma planilha** e **enviar e-mails** com os documentos anexados.

## Funcionalidades

**Gerar PDFs** automaticamente no Google Drive a partir de um modelo no Google Sheets  
**Salvar os IDs dos arquivos** na planilha para referência  
**Enviar e-mails pelo Gmail** com os PDFs anexados  
**Ler arquivos no Google Drive e extração de texto de PDFs**  
**Criar um menu personalizado no Google Sheets** para facilitar a execução  

---

## Estrutura dos Arquivos

envio_cartas_sheets/ 
├── envio_cartas_sheets.gs # Função principal para gerar PDFs e enviar emails 
├── gerar_pdf.gs # Geração de PDFs a partir do Google Sheets 
├── enviar_email_gmail.gs # Envio de e-mails via Gmail 
├── ler_arquivos_drive.gs # Listagem de arquivos no Google Drive 
├── ler_conteudo_pdf.gs # Extração de texto de PDFs no Drive 
├── gerar_menu.gs # Criação de menu personalizado no Google Sheets 
├── criptografar_pdf.py # Script Python para criptografar PDFs
└── README.md # Este documento


---

## Como Usar

### 🔹 **Passo 1: Adicionar os scripts ao Google Apps Script**
1. No Google Sheets, vá em **Extensões > Apps Script**.
2. Copie e cole os arquivos `.gs` para dentro do editor.
3. Salve e autorize as permissões.

### 🔹 **Passo 2: Configurar o Google Sheets**
1. Certifique-se de que sua planilha tem as abas:
   - `Base_Dados` → Contém as informações dos funcionários e os e-mails.
   - `AUX` → Contém a aba modelo e os IDs das pastas do Google Drive.

2. Configure as seguintes colunas na aba `Base_Dados`:
   - **D** → Nome do funcionário
   - **AT** → Nome do arquivo PDF
   - **AU** → ID do PDF gerado
   - **AR** → E-mail do funcionário
   - **AS** → Remetente do e-mail
   - **AV** → Status do envio (`"Enviado"` será salvo aqui)

### 🔹 **Passo 3: Executar os scripts**
- Para gerar PDFs:  
  ```javascript
  gerarPDFp4p();
  ```

- Para enviar e-mails:
  ```javascript
  enviar_email();
  ```

- Para listar arquivos no Drive:
  ```javascript
  listarArquivosNaPlanilha();
  ```

- Para extrair texto de PDFs:
  ```javascript
  lerArquivosPDF();
  ```

- Requisitos e Dependências
- Google Sheets (para armazenar os dados)
- Google Drive (para armazenar os PDFs gerados)
- Gmail (para envio dos e-mails)
- Google Apps Script (para execução dos códigos)

Se necessário, ative as permissões no Google Apps Script ao executar os scripts pela primeira vez.

- Contato
Caso tenha dúvidas ou sugestões, entre em contato via GitHub Issues.
