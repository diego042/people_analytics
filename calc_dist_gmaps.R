# CALCULAR DISTANCIA ENTRE LOCAIS USANDO A API DO GOOGLE MAPS

# Materiais de apoio
#https://cran.rstudio.com/web/packages/mapsapi/vignettes/intro.html
#https://developers.google.com/maps/documentation/distance-matrix/usage-and-billing

# Restrições
#Maximum of 25 origins or 25 destinations per request.
#Maximum 100 elements per server-side request.
#Maximum 100 elements per client-side request.
#1000 elements per second (EPS)

# Instala e carrega as bibliotecas
#install.packages("mapsapi")
#install.packages("remotes")
#remotes::install_github("michaeldorman/mapsapi")
library(mapsapi)
library(readxl)
library(dplyr)

# Chave da API do distance matrix
key <- "AIz....."

# Define origens e destinos na matriz
# Vai cruzar todas as origens contra todos os destinos
origem = c("80000-090", "00000-000", "Rua Sete de Setembro, 1500 - curitiba")
destino = c("01455-000", "Shopping curitiba")

# Gera o XML para a consulta
doc = mp_matrix(
  origins = origem,
  destinations = destino,
  key = key,
  quiet = TRUE
)

# Realiza a consulta e formata como tabela
m = mp_get_matrix(doc, value = "distance_m")
colnames(m) = destino
rownames(m) = origem
m
