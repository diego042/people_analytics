/**
 * Gerar PDFs a partir do Google Sheets e armazená-los no Google Drive.
 * Enviar e-mails com os PDFs anexados.
 * 
 * Requisitos:
 * - Planilha com abas "Base_Dados" e "AUX".
 * - Coluna "D" da aba Base_Dados deve conter o nome do funcionário.
 * - O nome da aba modelo está na célula D6 da aba AUX.
 * - O ID da pasta destino dos PDFs está na célula D3 da aba AUX.
 * - Endereço de e-mail na coluna AR da Base_Dados.
 * - O ID do arquivo PDF é salvo na coluna AU.
 * - O status "Enviado" é salvo na coluna AV.
 */

/**
 * Função principal para gerar PDFs e armazená-los no Google Drive.
 */
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
