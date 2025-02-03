/**
 * Função para enviar e-mails com anexo PDF gerado no Google Drive.
 */
function enviar_email() {
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var dataBase = planilha.getSheetByName('Base_Dados');
  
  var valoresColunaC = dataBase.getRange("C:C").getValues();
  var linhaAtual = 3;

  while (valoresColunaC[linhaAtual-1][0] !== "") {
    var employeeName = dataBase.getRange("D"+linhaAtual).getValue();
    var emailFuncionario = dataBase.getRange("AR"+linhaAtual).getValue();
    var remetente = dataBase.getRange("AS"+linhaAtual).getValue();
    
    var id = dataBase.getRange("AU"+linhaAtual).getValue();
    var anexo = DriveApp.getFileById(id);
    var assunto = 'Extrato P4P 2023 | ' + employeeName;
    var destinatario = emailFuncionario;

    enviarEmail(anexo, destinatario, assunto, remetente);
    dataBase.getRange("AV" + linhaAtual).setValue("Enviado");
    linhaAtual++;
  }
}

/**
 * Função auxiliar para envio de e-mail via Gmail.
 */
function enviarEmail(anexo, destinatario, assunto, remetente) {
  var blob = anexo.getBlob();
  
  GmailApp.sendEmail(destinatario, assunto, 'Segue anexo.', {
    attachments: [blob],
    from: remetente
  });
}
