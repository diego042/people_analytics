/**
 * Função para gerar um PDF e armazená-lo na pasta especificada do Google Drive.
 */
function gerarPDF(intervalo, aba, pasta, nomeArquivo) {
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var abaPlanilha = planilha.getSheetByName(aba);
  var abaId = abaPlanilha.getSheetId();
  
  var url = `https://docs.google.com/spreadsheets/d/${planilha.getId()}/export?exportFormat=pdf&gid=${abaId}&range=${intervalo}&portrait=true&fitw=true&gridlines=false`;
  var token = ScriptApp.getOAuthToken();
  
  var response = UrlFetchApp.fetch(url, { headers: { 'Authorization': 'Bearer ' + token } });
  var blob = response.getBlob().setName(nomeArquivo);
  
  var pastaDestino = DriveApp.getFolderById(pasta);
  var arquivo = pastaDestino.createFile(blob);
  
  return arquivo;
}


function gerarPDFp4p() {
  var dataAux = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("AUX");
  const abaModelo = dataAux.getRange("D6").getValue();
  const pastaDestino = dataAux.getRange("D3").getValue();

  var dataBase = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Base_Dados");
  var detalhado = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(abaModelo);

  var valoresColunaD = dataBase.getRange("D:D").getValues();
  var linhaAtual = 3;

  while (valoresColunaD[linhaAtual - 1][0] !== "") {
    var nomeFuncionario = dataBase.getRange("D" + linhaAtual).getValue();
    detalhado.getRange("C3").setValue(nomeFuncionario);

    var nomeArquivo = dataBase.getRange("AT" + linhaAtual).getValue();
    var intervalo = 'B2:O71';
    var pdf = gerarPDF(intervalo, abaModelo, pastaDestino, nomeArquivo);

    var id_pdf = pdf.getId();
    dataBase.getRange("AU" + linhaAtual).setValue(id_pdf);

    Utilities.sleep(3500);
    linhaAtual++;
  }

  Logger.log('Processo finalizado.');
  SpreadsheetApp.getUi().alert('Arquivos gerados com sucesso.', SpreadsheetApp.getUi().ButtonSet.OK);
}
