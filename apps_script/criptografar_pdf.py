from PyPDF4 import PdfFileWriter, PdfFileReader 
import os

"""
REQUISITOS:
- Python 3.x instalado
- Biblioteca PyPDF4 instalada (caso não esteja, instale com: pip install PyPDF4)
- Criar duas pastas no mesmo diretório do script:
  1. "pdfs" → Onde estarão os arquivos a serem criptografados
  2. "saida" → Onde serão armazenados os arquivos criptografados

FUNCIONAMENTO:
- O script busca arquivos PDF na pasta "pdfs".
- Gera uma cópia protegida por senha na pasta "saida".
- A senha é gerada automaticamente com os primeiros 5 caracteres do nome do arquivo.
"""

# Diretório onde estão os arquivos PDF a serem criptografados
input_folder = "pdfs"
output_folder = "saida"

# Criar pasta de saída, se não existir
os.makedirs(output_folder, exist_ok=True)

def criptografar_pdf(arquivo, senha, output_folder):
    """
    Criptografa um arquivo PDF usando a senha especificada e salva na pasta de saída.
    
    Parâmetros:
        arquivo (str): Nome do arquivo PDF a ser criptografado.
        senha (str): Senha para proteger o PDF.
        output_folder (str): Pasta onde o arquivo criptografado será salvo.
    """
    try:
        input_path = os.path.join(input_folder, arquivo)
        output_path = os.path.join(output_folder, arquivo)
        
        # Criar um objeto PdfFileWriter para escrever o novo arquivo
        out = PdfFileWriter()
        file = PdfFileReader(input_path)
        
        # Adicionar todas as páginas do arquivo original
        for idx in range(file.numPages):
            out.addPage(file.getPage(idx))
        
        # Definir senha para o arquivo
        out.encrypt(senha)
        
        # Escrever o arquivo criptografado na pasta de saída
        with open(output_path, "wb") as f:
            out.write(f)
        
        print(f"Arquivo {arquivo} criptografado e salvo em {output_path}")
    except Exception as e:
        print(f"Erro ao criptografar {arquivo}: {str(e)}")

# Listar todos os arquivos PDF no diretório de entrada
todos_arquivos = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

# Aplicar criptografia em cada arquivo encontrado
for arquivo in todos_arquivos:
    senha = arquivo[:5]  # Utiliza os primeiros 5 caracteres do nome do arquivo como senha
    criptografar_pdf(arquivo, senha, output_folder)
