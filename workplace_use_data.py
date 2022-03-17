##########################################################
# DOWNLOAD DOS DADOS DE USO DA BIBLIOTECA DO CONHECIMENTO
##########################################################

# Documentacao basica do facebook
# https://developers.facebook.com/docs/workplace/reference/graph-api/category#examples
# https://developers.facebook.com/docs/graph-api/results

# Descrição
#  O Workplace registra as informações página a página, então não adianta pegar só
# os números das paginas principais (Categorias). É necessário mapear nivel a nível.
#  O script a seguir é um passo a passo recursivo que pega todas as páginas de um nível e
# vai para a camada abaixo gerando um mapa hierarquico.
#  Após mapear os 5 níveis de categorias e subcategorias, usa-se o id de cada página
# para coletar comentários, reações e visualizações.


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
site = 'https://graph.facebook.com/'
site_bc = 'https://graph.facebook.com/community/knowledge_library_categories'
token= 'token' # aqui adicionar o token com as devidas permissões de acesso


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


# Funcao para chamar API Categorias
# Só publicadas pra não arriscar quebrar paginação)
# paginador = (request.json())['paging']['cursors']['after']
def req_cat():
    request = requests.get(site_bc+'?access_token='+token+'&fields=title,id,status')
    cat = (pd.DataFrame((request.json())['data']))
    return(cat)
    
# Funcao para chamar API Subcategorias
def req_subcat(df):
    dfs = pd.DataFrame()
    for i in (df['id']):
        request = requests.get(site+i+'/subcategories?access_token='+token+'&fields=title,id,status')
        dfs0 = pd.DataFrame((request.json())['data'])
        dfs0['pai'] = i #list((df[df.id == i]['title']))[0]
        dfs = dfs.append(dfs0, ignore_index=True)
    return(dfs)

# Coleta Categorias
categorias = req_cat()
categorias['Nivel'] = 0
categorias['Categoria'] = categorias['title']
categorias['Subcategoria1'] = ''
categorias['Subcategoria2'] = ''
categorias['Subcategoria3'] = ''
categorias['Subcategoria4'] = ''

# Coleta subcategorias
sub1 = req_subcat(categorias)
sub1['Nivel'] = 1
antecessor = categorias[['id', 'Categoria']]
antecessor.rename(columns={"id": "pai"}, inplace=True)
sub1 = pd.merge(sub1, antecessor, how='left')
sub1['Subcategoria1'] = sub1['title']
sub1['Subcategoria2'] = ''
sub1['Subcategoria3'] = ''
sub1['Subcategoria4'] = ''

sub2 = req_subcat(sub1)
sub2['Nivel'] = 2
antecessor = sub1[['id', 'Categoria', 'Subcategoria1']]
antecessor.rename(columns={"id": "pai"}, inplace=True)
sub2 = pd.merge(sub2, antecessor, how='left')
sub2['Subcategoria2'] = sub2['title']
sub2['Subcategoria3'] = ''
sub2['Subcategoria4'] = ''

sub3 = req_subcat(sub2)
sub3['Nivel'] = 3
antecessor = sub2[['id', 'Categoria', 'Subcategoria1',
                   'Subcategoria2']]
antecessor.rename(columns={"id": "pai"}, inplace=True)
sub3 = pd.merge(sub3, antecessor, how='left')
sub3['Subcategoria3'] = sub3['title']
sub3['Subcategoria4'] = ''

sub4 = req_subcat(sub3)
sub4['Nivel'] = 4
antecessor = sub3[['id', 'Categoria', 'Subcategoria1',
                   'Subcategoria2', 'Subcategoria3']]
antecessor.rename(columns={"id": "pai"}, inplace=True)
sub4 = pd.merge(sub4, antecessor, how='left')
sub4['Subcategoria4'] = sub4['title']


grupos = categorias.append(sub1, ignore_index=True)
grupos = grupos.append(sub2, ignore_index=True)
grupos = grupos.append(sub3, ignore_index=True)
grupos = grupos.append(sub4, ignore_index=True)
grupos = grupos[grupos.status == 'PUBLISHED'] #Mantem apenas as com status "publicado"
grupos = grupos.sort_values('Subcategoria4')
grupos = grupos.sort_values('Subcategoria3')
grupos = grupos.sort_values('Subcategoria2')
grupos = grupos.sort_values('Subcategoria1')
grupos = grupos.sort_values('Categoria')
grupos = grupos.sort_values('Nivel')

	
# Tabela com dados
grupos['comentarios'] = grupos.apply (lambda row: num_comentarios(row.id), axis=1)
grupos['reacoes'] = grupos.apply (lambda row: num_reacoes(row.id), axis=1)
grupos['visualizacoes'] = grupos.apply (lambda row: num_visualizacoes(row.id), axis=1)

grupos.drop('id', axis='columns', inplace=True)
grupos.drop('status', axis='columns', inplace=True)
  
grupos
	
# salvar excel
grupos.to_excel('biblioteca_conhecimento.xlsx')
