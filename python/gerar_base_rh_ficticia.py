"""
📊 Geração de Base Fictícia de RH

Este script gera uma **base de dados fictícia** de funcionários para simular cenários 
relacionados a People Analytics, recrutamento, diversidade e folha de pagamento.

🔹 **Características:**
- Geração de nomes fictícios baseados em personagens de séries e filmes.
- Simulação de diversidade (gênero, raça, idade, tipo de contrato, etc.).
- Criação de CPFs únicos usando a biblioteca `Faker`.
- Definição de cargos e departamentos aleatórios.
- Simulação de datas de nascimento e admissão para análise de senioridade.
- Geração de uma base estruturada e exportação para CSV.

🔹 **Bibliotecas Utilizadas:**
- `pandas` → Manipulação e estruturação dos dados.
- `random` → Sorteio aleatório de valores.
- `faker` → Geração de CPFs, endereços e dados fictícios.
- `datetime.date` → Cálculo de idades e datas de admissão.

"""

import pandas as pd
import random
from faker import Faker
from datetime import date

# Configuração do Faker
fake = Faker('pt_BR')

# Listas fictícias baseadas em personagens de séries e filmes
nomes_base = [
    "Michael", "Jim", "Pam", "Dwight", "Angela", "Rachel", "Ross", "Monica", "Chandler", "Joey",
    "Phoebe", "Luke", "Leia", "Obi-Wan", "Han", "Yoda", "James", "Spock", "Jean-Luc", "Data",
    "Worf", "Uhura", "McCoy"
]
sobrenomes_base = [
    "Scott", "Halpert", "Beesly", "Schrute", "Martin", "Green", "Geller", "Bing", "Tribbiani", "Buffay",
    "Skywalker", "Vader", "Organa", "Kenobi", "Solo", "Kirk", "Picard", "Riker", "Crusher", "Sulu",
    "Chekov", "T'Pol", "Archer"
]

# Listas de atributos diversos
sexos = ["Masculino", "Feminino", "Não-binário"]
identidade_genero = ["Cisgênero", "Transgênero", "Não-binário", "Prefere não dizer"]
racas = ["Branca", "Preta", "Parda", "Amarela", "Indígena", "Prefere não dizer"]
cargos = [
    "Analista Júnior", "Analista Pleno", "Analista Sênior", "Gerente", "Diretor",
    "Coordenador", "Assistente", "Estagiário", "Trainee"
]
niveis = ["Júnior", "Pleno", "Sênior", "Liderança", "Executivo"]
departamentos = ["TI", "Financeiro", "Recursos Humanos", "Marketing", "Vendas", "Jurídico", "Operações"]
tipo_contrato = ["CLT", "PJ", "Estágio", "Temporário", "Autônomo"]

# Gerar listas de nomes únicos
nomes_unicos = list(set(f"{random.choice(nomes_base)} {random.choice(sobrenomes_base)}" for _ in range(500)))

# Garantindo CPFs únicos
cpfs_gerados = set()

def gerar_cpf_unico():
    """Gera CPFs únicos para evitar duplicações na base."""
    while True:
        cpf = fake.cpf()
        if cpf not in cpfs_gerados:
            cpfs_gerados.add(cpf)
            return cpf

# Gerando os dados fictícios
dados = []
for i, nome in enumerate(nomes_unicos, start=1):
    cpf = gerar_cpf_unico()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
    data_admissao = fake.date_between(start_date="-10y", end_date="today")
    idade = date.today().year - data_nascimento.year
    sexo = random.choice(sexos)
    identidade = random.choice(identidade_genero)
    raca = random.choice(racas)
    cargo = random.choice(cargos)
    nivel = random.choice(niveis)
    departamento = random.choice(departamentos)
    salario = round(random.uniform(3000, 30000), 2)
    tipo_contrato_escolhido = random.choice(tipo_contrato)
    email = fake.email()
    telefone = fake.phone_number()
    endereco = fake.address()
    cidade = fake.city()
    estado = fake.state_abbr()
    
    dados.append([
        i, nome, cpf, data_nascimento, idade, data_admissao, sexo, identidade, raca,
        cargo, nivel, departamento, salario, tipo_contrato_escolhido, email, telefone, endereco, cidade, estado
    ])

# Criando o DataFrame
colunas = [
    "ID_FUNCIONARIO", "NOME", "CPF", "DATA_NASCIMENTO", "IDADE", "DATA_ADMISSAO", "SEXO", "IDENTIDADE_GENERO", "RACA",
    "CARGO", "NIVEL", "DEPARTAMENTO", "SALARIO", "TIPO_CONTRATO", "EMAIL", "TELEFONE", "ENDERECO", "CIDADE", "ESTADO"
]

df_rh = pd.DataFrame(dados, columns=colunas)

# Exibindo as primeiras linhas
print(df_rh.head())

# Salvando em CSV
#df_rh.to_csv("base_rh_ficticia.csv", index=False)
