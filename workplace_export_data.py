import urllib3
import urllib.request
import facebook
import requests
import csv
import time

# Gera id para solicitar export dos dados
site = 'https://graph.facebook.com/community/export_employee_data'
token= {'access_token':<"TOKEN PARA ACESSO À API">}
post = requests.post(site, data = token)
y = post.json()
id = y['id']
print("id da para solicitacao: "+id)

# Solicita a criacao da tabela
request = requests.get('https://graph.facebook.com/'+id+'?access_token='+token['access_token'])
print("Link para download do arquivo: "+request.text)

# Aguarda 5 min até o Facebook gerar o link para download
print("Aguarde 5 minutos enquanto o Facebook compila os dados...")
time.sleep(240)
print("Mais um minuto...")
time.sleep(60)
request = requests.get('https://graph.facebook.com/'+id+'?access_token='+token['access_token'])

# Baixa excel na pasta 'documentos'
link_arquivo = request.json()
url = link_arquivo['result']
urllib.request.urlretrieve(url, <"<Local na rede>/Documentos/workplace.xlsx")
print("Trabalho finalizado!")
