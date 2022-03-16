##########################################################
# DOWNLOAD DOS DADOS DE USO DA BIBLIOTECA DO CONHECIMENTO
##########################################################

# Documentacao basica do facebook
# https://developers.facebook.com/docs/workplace/reference/graph-api/category#examples
##https://developers.facebook.com/docs/graph-api/results

# Bibliotecas
import urllib3
import urllib.request
import facebook
import requests
import csv
import time
import pandas as pd
pd.options.mode.chained_assignment = None  # desliga o warning nas funções lambda

# Variáveis
site_bc = 'https://graph.facebook.com/community/knowledge_library_categories'
token= 'token'
site = 'https://graph.facebook.com/'

# Definir funcoes para coleta de dados da biblioteca do conhecimento
    
# Funcao para obter numero de comentarios
def num_comentarios(grupo):
    pagina = str(grupo)
    request = requests.get(site+pagina+'/'+'comments?summary=true&access_token='+token)
    comentarios = (request.json())['summary']['total_count']
    return(comentarios)

# Funcao para obter numero de reacoes
#aceita <since={unix_timestamp}&until={unix_timestamp}>
def num_reacoes(grupo):
    pagina = str(grupo)
    request = requests.get(site+pagina+'/reactions?summary=true&access_token='+token)
    reacoes = (request.json())['summary']['total_count']
    return(reacoes)

# Funcao para obter numero de visualizacoes unicas
#aceita <since={unix_timestamp}&until={unix_timestamp}>
def num_visualizacoes(grupo):
    pagina = str(grupo)
    request = requests.get(site+pagina+'/seen?summary=true&access_token='+token)
    visualizacoes = (request.json())['summary']['total_count']
    return(visualizacoes)

# Funcao para obter o tamanho da audiencia
def num_audiencia(grupo):
    pagina = str(grupo)
    request = requests.get(site+pagina+'?fields=read_audience{static_users}'+'&access_token='+token)
    audiencia = (request.json())['read_audience']['static_users']['data']
    return(len(audiencia))


# Categorias
request = requests.get(site_bc+'?access_token='+token+'&fields=title,id,status')
#paginador = (request.json())['paging']['cursors']['after']
lista = (request.json())['data']
df = pd.DataFrame(lista)
df['Categoria'] = df['title']

# Subcategorias
dfs = pd.DataFrame()
for i in (df['id']):
    request = requests.get(site+i+'/subcategories?access_token='+token+'&fields=title,id,status')
    lista = (request.json())['data']
    dfs0 = pd.DataFrame(lista)
    dfs0['Categoria'] = list((df[df.id == i]['title']))[0]
    dfs = dfs.append(dfs0, ignore_index=True)
df = df.append(dfs, ignore_index=True)
df = df.sort_values('Categoria')
grupos = df[df.status == 'PUBLISHED'] #Mantem apenas as com status "publicado"

# Tabela com dados
grupos['comentarios'] = grupos.apply (lambda row: num_comentarios(row.id), axis=1)
grupos['reacoes'] = grupos.apply (lambda row: num_reacoes(row.id), axis=1)
grupos['visualizacoes'] = grupos.apply (lambda row: num_visualizacoes(row.id), axis=1)

grupos.drop('id', axis='columns', inplace=True)
grupos.drop('status', axis='columns', inplace=True)
  
# salvar excel
grupos.to_excel('biblioteca_conhecimento.xlsx')

grupos