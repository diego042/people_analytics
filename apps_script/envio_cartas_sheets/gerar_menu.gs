/**
 * Função para criar um menu personalizado no Google Sheets.
 */
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();
  const menu = ui.createMenu("Gerenciamento de Arquivos e E-mails")
    .addItem('Gerar PDF - P4P', 'gerarPDFp4p')
    .addSeparator()
    .addItem('Enviar E-mail - P4P', 'enviar_email')
    .addSeparator()
    .addItem('Listar Arquivos no Drive', 'listarArquivosNaPlanilha')
    .addSeparator()
    .addItem('Ler Conteúdo de PDFs', 'lerArquivosPDF')
    .addToUi();
}
