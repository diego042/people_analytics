#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para download dos dados de uso da Biblioteca do Conhecimento (Workplace Facebook).

Descrição:
  O Workplace registra as informações página a página, então não basta pegar só
  os números das páginas principais (Categorias). É necessário mapear nível a nível.
  O script abaixo é um passo a passo recursivo que pega todas as páginas de um nível e
  desce para a camada abaixo gerando um mapa hierárquico.
  Depois de mapear 5 níveis de categorias e subcategorias, usa-se o id de cada página
  para coletar comentários, reações e visualizações.

Dependências:
  - Python 3.x
  - requests
  - pandas
  - openpyxl (para salvar em Excel)

Como usar:
  1. Instale as dependências: 
     pip install requests pandas openpyxl
  2. Defina seu token do Workplace no código ou usando variável de ambiente.
  3. Execute:
     python coleta_biblioteca_conhecimento.py

Atenção:
  - Caso haja muitas categorias/subcategorias, verifique a necessidade de paginar 
    os resultados (não implementado neste script).
  - É recomendável não “hard-code” o token, e sim usar uma variável de ambiente
    ou um arquivo de configuração separado.
"""

import os
import requests
import pandas as pd

pd.options.mode.chained_assignment = None  # Desabilita warning de chained_assignment

# Endpoints base
SITE = "https://graph.facebook.com/"
SITE_BC = "https://graph.facebook.com/community/knowledge_library_categories"

# Token de acesso (idealmente, use uma variável de ambiente ou arquivo de config)
# Exemplo: FB_TOKEN = os.getenv("FB_TOKEN")
FB_TOKEN = "SEU_TOKEN_AQUI"


def num_comentarios(page_id: str) -> int:
    """
    Retorna o número total de comentários de uma determinada página (page_id).
    :param page_id: ID da página (categoria ou subcategoria).
    :return: Número de comentários (int).
    """
    url = f"{SITE}{page_id}/comments"
    params = {
        "summary": "true",
        "access_token": FB_TOKEN
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERRO] Falha ao obter comentários de {page_id}: {response.text}")
        return 0
    
    data = response.json()
    return data.get("summary", {}).get("total_count", 0)


def num_reacoes(page_id: str) -> int:
    """
    Retorna o número total de reações de uma determinada página (page_id).
    :param page_id: ID da página (categoria ou subcategoria).
    :return: Número de reações (int).
    """
    url = f"{SITE}{page_id}/reactions"
    params = {
        "summary": "true",
        "access_token": FB_TOKEN
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERRO] Falha ao obter reações de {page_id}: {response.text}")
        return 0

    data = response.json()
    return data.get("summary", {}).get("total_count", 0)


def num_visualizacoes(page_id: str) -> int:
    """
    Retorna o número total de visualizações únicas de uma determinada página (page_id).
    :param page_id: ID da página (categoria ou subcategoria).
    :return: Número de visualizações únicas (int).
    """
    url = f"{SITE}{page_id}/seen"
    params = {
        "summary": "true",
        "access_token": FB_TOKEN
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERRO] Falha ao obter visualizações de {page_id}: {response.text}")
        return 0

    data = response.json()
    return data.get("summary", {}).get("total_count", 0)


def num_audiencia(page_id: str) -> int:
    """
    Retorna o tamanho da audiência (lista de usuários) que tem acesso à página.
    :param page_id: ID da página (categoria ou subcategoria).
    :return: Número de usuários (int).
    """
    url = f"{SITE}{page_id}"
    params = {
        "fields": "read_audience{static_users}",
        "access_token": FB_TOKEN
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERRO] Falha ao obter audiência de {page_id}: {response.text}")
        return 0

    data = response.json()
    try:
        audience_data = data["read_audience"]["static_users"]["data"]
        return len(audience_data)
    except KeyError:
        return 0


def req_cat() -> pd.DataFrame:
    """
    Retorna as categorias principais da Biblioteca do Conhecimento.
    :return: DataFrame com colunas [title, id, status].
    """
    params = {
        "access_token": FB_TOKEN,
        "fields": "title,id,status"
    }
    response = requests.get(SITE_BC, params=params)
    if response.status_code != 200:
        print(f"[ERRO] Falha ao obter categorias: {response.text}")
        return pd.DataFrame()
    
    data = response.json().get("data", [])
    return pd.DataFrame(data)


def req_subcat(df: pd.DataFrame) -> pd.DataFrame:
    """
    Para cada ID presente no DataFrame recebido, obtém as subcategorias correspondentes.
    :param df: DataFrame com pelo menos a coluna "id".
    :return: DataFrame com as subcategorias de todos os IDs processados.
    """
    all_subcats = pd.DataFrame()
    for page_id in df["id"]:
        url = f"{SITE}{page_id}/subcategories"
        params = {
            "access_token": FB_TOKEN,
            "fields": "title,id,status"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"[ERRO] Falha ao obter subcategorias de {page_id}: {response.text}")
            continue

        data = response.json().get("data", [])
        df_temp = pd.DataFrame(data)
        df_temp["pai"] = page_id
        all_subcats = pd.concat([all_subcats, df_temp], ignore_index=True)

        # Opcional: inserir um delay para evitar muitas requisições em sequência
        # time.sleep(0.2)

    return all_subcats


def main():
    """
    Função principal do script:
      1. Coleta categorias do nível 0.
      2. Coleta recursivamente até nível 4 de subcategorias.
      3. Faz merges para manter a hierarquia completa.
      4. Coleta métricas (comentários, reações, visualizações).
      5. Salva o resultado em Excel.
    """

    # Coleta Categorias (nível 0)
    categorias = req_cat()
    categorias["Nivel"] = 0
    categorias["Categoria"] = categorias["title"]
    categorias["Subcategoria1"] = ""
    categorias["Subcategoria2"] = ""
    categorias["Subcategoria3"] = ""
    categorias["Subcategoria4"] = ""

    # Subcategorias nível 1
    sub1 = req_subcat(categorias)
    sub1["Nivel"] = 1
    antecessor = categorias[["id", "Categoria"]].rename(columns={"id": "pai"})
    sub1 = pd.merge(sub1, antecessor, how="left", on="pai")
    sub1["Subcategoria1"] = sub1["title"]
    sub1["Subcategoria2"] = ""
    sub1["Subcategoria3"] = ""
    sub1["Subcategoria4"] = ""

    # Subcategorias nível 2
    sub2 = req_subcat(sub1)
    sub2["Nivel"] = 2
    antecessor = sub1[["id", "Categoria", "Subcategoria1"]].rename(columns={"id": "pai"})
    sub2 = pd.merge(sub2, antecessor, how="left", on="pai")
    sub2["Subcategoria2"] = sub2["title"]
    sub2["Subcategoria3"] = ""
    sub2["Subcategoria4"] = ""

    # Subcategorias nível 3
    sub3 = req_subcat(sub2)
    sub3["Nivel"] = 3
    antecessor = sub2[["id", "Categoria", "Subcategoria1", "Subcategoria2"]].rename(columns={"id": "pai"})
    sub3 = pd.merge(sub3, antecessor, how="left", on="pai")
    sub3["Subcategoria3"] = sub3["title"]
    sub3["Subcategoria4"] = ""

    # Subcategorias nível 4
    sub4 = req_subcat(sub3)
    sub4["Nivel"] = 4
    antecessor = sub3[["id", "Categoria", "Subcategoria1", "Subcategoria2", "Subcategoria3"]].rename(columns={"id": "pai"})
    sub4 = pd.merge(sub4, antecessor, how="left", on="pai")
    sub4["Subcategoria4"] = sub4["title"]

    # Junta tudo em um único DataFrame
    grupos = pd.concat([categorias, sub1, sub2, sub3, sub4], ignore_index=True)

    # Mantém apenas os itens com status "PUBLISHED"
    grupos = grupos[grupos["status"] == "PUBLISHED"].copy()

    # Ordenação final por nível e categorias
    grupos.sort_values(
        by=["Nivel", "Categoria", "Subcategoria1", "Subcategoria2", "Subcategoria3", "Subcategoria4"],
        inplace=True
    )

    print("Coletando métricas (comentários, reações, visualizações)...")
    grupos["comentarios"] = grupos["id"].apply(num_comentarios)
    grupos["reacoes"] = grupos["id"].apply(num_reacoes)
    grupos["visualizacoes"] = grupos["id"].apply(num_visualizacoes)

    # Se quiser também coletar audiência (pode ser lento/restrito):
    # grupos["audiencia"] = grupos["id"].apply(num_audiencia)

    # Remove colunas não utilizadas no resultado final
    grupos.drop(columns=["id", "status"], inplace=True)

    # Salva em Excel
    output_file = "biblioteca_conhecimento.xlsx"
    grupos.to_excel(output_file, index=False)
    print(f"Arquivo Excel gerado: {output_file}")


if __name__ == "__main__":
    main()
