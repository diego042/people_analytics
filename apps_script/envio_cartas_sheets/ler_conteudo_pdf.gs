/**
 * Função para ler o conteúdo de arquivos PDF armazenados em uma pasta do Google Drive
 * e salvar as informações extraídas em uma planilha do Google Sheets.
 */
function lerArquivosPDF() {
  var pastaId = 'ID_Pasta'; // Substitua pelo ID real da pasta do Google Drive
  var pasta = DriveApp.getFolderById(pastaId);
  var arquivos = pasta.getFilesByType(MimeType.PDF);

  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var aba = planilha.getSheetByName('LerPDFs');
  
  if (!aba) {
    aba = planilha.insertSheet('LerPDFs');
  }
  
  // Verifica se a aba já tem dados e determina o ponto de inserção
  var ultimaLinha = aba.getLastRow();
  var ultimoArquivoProcessado = ultimaLinha > 1 ? aba.getRange(ultimaLinha, 1).getValue() : '';
  var continuar = ultimoArquivoProcessado === '';
  
  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var nome = arquivo.getName();
    if (nome === ultimoArquivoProcessado) {
      continuar = true;
    }
    if (continuar) {
      var blob = arquivo.getBlob();
      var texto = '';
      try {
        texto = extractTextFromPDF(blob).substring(23, 60); // Ajuste o range conforme necessário
      } catch(e) {
        texto = 'Erro ao extrair texto: ' + e.message;
      }
      aba.appendRow([nome, texto]);
    }
  }
}
