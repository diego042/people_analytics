/**
 * Função para listar arquivos de uma pasta específica do Google Drive e salvar na aba do Google Sheets.
 */
function listarArquivosNaPlanilha() {
  var pastaId = 'ID_Pasta'; // Substitua pelo ID da pasta do Google Drive
  var pasta = DriveApp.getFolderById(pastaId);
  var arquivos = pasta.getFiles();
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Aba_SalvarNomesArquivos');
  
  if (!sheet) {
    sheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet('Aba_SalvarNomesArquivos');
  }
  
  // Limpa a aba antes de adicionar novos dados
  sheet.clear();
  
  // Adiciona cabeçalhos na planilha
  sheet.appendRow(['ID do Arquivo', 'Nome do Arquivo', 'Tipo']);
  
  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var id = arquivo.getId();
    var nome = arquivo.getName();
    var tipo = arquivo.getMimeType();
    sheet.appendRow([id, nome, tipo]);
  }
}
