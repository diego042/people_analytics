##########################################################
# DOWNLOAD DOS DADOS DE USO DA BIBLIOTECA DO CONHECIMENTO
##########################################################

# Documentacao basica do facebook
# https://developers.facebook.com/docs/workplace/reference/graph-api/category#examples

# Bibliotecas necessarias
import urllib3
import urllib.request
import facebook
import requests
import csv
import time

# Definir funcoes para coleta de dados da biblioteca do conhecimento
    
# Funcao para obter numero de comentarios
def num_comentarios(grupo):
    site = 'https://graph.facebook.com/'
    pagina = str(grupo)
    token= <"TOKEN PARA ACESSO À API">
    request = requests.get(site+pagina+'/'+'comments?summary=true&access_token='+token)
    comentarios = (request.json())['summary']['total_count']
    #df = pd.DataFrame(data={'grupo': [grupo], 'comentarios': [comentarios]})
    #return(df)
    return(comentarios)

# Funcao para obter numero de reacoes
#aceita <since={unix_timestamp}&until={unix_timestamp}>
def num_reacoes(grupo):
    site = 'https://graph.facebook.com/'
    pagina = str(grupo)
    token= <"TOKEN PARA ACESSO À API">
    request = requests.get(site+pagina+'/reactions?summary=true&access_token='+token)
    reacoes = (request.json())['summary']['total_count']
    return(reacoes)

# Funcao para obter numero de visualizacoes unicas
#aceita <since={unix_timestamp}&until={unix_timestamp}>
def num_visualizacoes(grupo):
    site = 'https://graph.facebook.com/'
    pagina = str(grupo)
    token= <"TOKEN PARA ACESSO À API">
    request = requests.get(site+pagina+'/seen?summary=true&access_token='+token)
    visualizacoes = (request.json())['summary']['total_count']
    return(visualizacoes)

# Funcao para obter o tamanho da audiencia (desenhada, mas nao palicada no case)
def num_audiencia(grupo):
    site = 'https://graph.facebook.com/'
    pagina = str(grupo)
    token= <"TOKEN PARA ACESSO À API">
    request = requests.get(site+pagina+'?fields=read_audience{static_users}'+'&access_token='+token)
    audiencia = (request.json())['read_audience']['static_users']['data']
    return(len(audiencia))

# Lista de grupos a serem analisados
grupos = pd.DataFrame([[<'nome do grupo 1'>, <'id do grupo 1'>],
                       [<'nome do grupo 2'>, <'id do grupo 2'>],
                       [<'nome do grupo 3'>, <'id do grupo 3'>]],
                      columns=['nome','id'])

# Tabela com dados
grupos['comentarios'] = grupos.apply (lambda row: num_comentarios(row.id), axis=1)
grupos['reacoes'] = grupos.apply (lambda row: num_reacoes(row.id), axis=1)
grupos['visualizacoes'] = grupos.apply (lambda row: num_visualizacoes(row.id), axis=1)

grupos
