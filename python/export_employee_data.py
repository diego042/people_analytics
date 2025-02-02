#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para exportar dados de funcionários (Employee Data) do Workplace (Facebook).

Descrição:
  1. Faz uma solicitação à API do Workplace para gerar um relatório de dados de funcionários.
  2. Aguarda um tempo (5 minutos) até que o relatório esteja pronto.
  3. Faz o download do arquivo Excel e salva em um diretório especificado.

Dependências:
  - requests (para requisições HTTP)
  - time (biblioteca padrão do Python)
  - urllib (para download do arquivo via URL)

Como usar:
  1. Instale as dependências, se necessário:
     pip install requests
  2. Defina o token de acesso (FB_TOKEN). Recomendado usar variável de ambiente ou arquivo de config.
  3. Execute:
     python export_employee_data.py
  4. O script vai esperar ~5 minutos até que o link esteja pronto e, então, fará o download.

Atenção:
  - Verifique se você possui as permissões corretas no Workplace para exportar esses dados.
  - O script faz uso de `time.sleep()`. Caso a API demore mais que 5 minutos, será preciso ajustar.
  - Para ambientes mais complexos, considere criar um loop de verificação em vez de esperar fixo.
"""

import os
import time
import requests
import urllib.request

# =========================================================
# Configurações
# =========================================================

# Token de acesso. Ideal obter via variável de ambiente, por exemplo:
# FB_TOKEN = os.getenv("FB_TOKEN")
FB_TOKEN = "<SEU_TOKEN_AQUI>"  # substitua ou use os.getenv("FB_TOKEN")

# Endpoint para gerar export de dados de funcionários
EXPORT_URL = "https://graph.facebook.com/community/export_employee_data"

# Caminho de saída do arquivo Excel
# Ajuste conforme sua necessidade (pode ser local, rede, etc.)
OUTPUT_PATH = r"C:\Users\MeuUsuario\Documentos\workplace.xlsx"

# Tempo de espera (segundos) para compilação do arquivo
TOTAL_WAIT_TIME = 5 * 60  # 5 minutos (300 segundos)

# =========================================================
# Função Principal
# =========================================================

def main():
    """
    Fluxo principal:
      1. Solicita à API do Workplace a geração do relatório.
      2. Aguarda o link de download ficar pronto (tempo fixo).
      3. Faz o download do arquivo Excel para o caminho desejado.
    """
    if not FB_TOKEN or FB_TOKEN.startswith("<"):
        print("[AVISO] Defina corretamente o FB_TOKEN no código ou por variável de ambiente.")
        return

    print("[1/4] Solicitando export de dados de funcionários ao Workplace...")
    post_data = {"access_token": FB_TOKEN}
    response_post = requests.post(EXPORT_URL, data=post_data)

    if response_post.status_code != 200:
        print(f"[ERRO] Falha na solicitação de export. Status code: {response_post.status_code}")
        print(response_post.text)
        return

    result_json = response_post.json()
    export_id = result_json.get("id")
    if not export_id:
        print("[ERRO] Não foi possível obter o ID de exportação.")
        print(response_post.text)
        return

    print(f"[OK] ID de solicitação de export: {export_id}")

    # Solicita status
    print("[2/4] Verificando link de download inicial (pode não estar pronto)...")
    status_url = f"https://graph.facebook.com/{export_id}?access_token={FB_TOKEN}"
    response_status = requests.get(status_url)

    print(f"[STATUS INICIAL] {response_status.text}")

    # Espera 5 minutos para que o Workplace compile o arquivo
    print("[3/4] Aguardando ~5 minutos para compilação do relatório...")
    time.sleep(TOTAL_WAIT_TIME)

    # Solicita novamente o link de download
    print("[4/4] Verificando link de download final...")
    response_status = requests.get(status_url)
    if response_status.status_code != 200:
        print(f"[ERRO] Falha ao obter o link de download. Status code: {response_status.status_code}")
        print(response_status.text)
        return

    status_json = response_status.json()
    download_url = status_json.get("result")
    if not download_url:
        print("[ERRO] Link de download não encontrado no JSON retornado.")
        print(response_status.text)
        return

    # Faz o download do arquivo .xlsx
    print(f"[DOWNLOAD] Baixando arquivo para: {OUTPUT_PATH}")
    urllib.request.urlretrieve(download_url, OUTPUT_PATH)
    print("[OK] Trabalho finalizado com sucesso!")


if __name__ == "__main__":
    main()
