# 📍 Cálculo de Distância entre Locais usando a API do Google Maps

# 📌 Materiais de Apoio:
# - Documentação: https://cran.rstudio.com/web/packages/mapsapi/vignettes/intro.html
# - Uso e cobrança da API: https://developers.google.com/maps/documentation/distance-matrix/usage-and-billing

# 🚧 Restrições da API Distance Matrix:
# - Máximo de 25 origens ou 25 destinos por requisição.
# - Máximo de 100 elementos por requisição server-side.
# - Máximo de 1000 elementos por segundo (EPS).

# 📦 Instalação e carregamento das bibliotecas necessárias
if (!requireNamespace("mapsapi", quietly = TRUE)) install.packages("mapsapi")
if (!requireNamespace("remotes", quietly = TRUE)) install.packages("remotes")
if (!requireNamespace("readxl", quietly = TRUE)) install.packages("readxl")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr")
remotes::install_github("michaeldorman/mapsapi")

library(mapsapi)
library(readxl)
library(dplyr)

# 🔑 Chave da API do Google Maps (substituir pela chave real)
key <- "SUA_CHAVE_AQUI"

# 🔹 Definir origens e destinos para a matriz de cálculo
# A API irá calcular a distância entre todas as combinações de origem e destino
origens <- c("80000-090", "00000-000", "Rua Sete de Setembro, 1500 - Curitiba")
destinos <- c("01455-000", "Shopping Curitiba")

# 🔍 Gerar o XML para a consulta na API
doc <- mp_matrix(
  origins = origens,
  destinations = destinos,
  key = key,
  quiet = TRUE
)

# 📊 Realiza a consulta e formata os resultados como tabela
matriz_distancia <- mp_get_matrix(doc, value = "distance_m")
colnames(matriz_distancia) <- destinos
rownames(matriz_distancia) <- origens

# 📌 Exibir a matriz de distâncias
print(matriz_distancia)