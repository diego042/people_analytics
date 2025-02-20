# 📊 Scripts em R

Esta pasta contém **scripts em R** voltados para análise de dados, automação de processos e integração com APIs externas.

## 📂 Scripts Disponíveis

### 1️⃣ `calcular_distancia_google_maps.R`
- **Descrição**: Calcula distâncias entre locais usando a API Distance Matrix do Google Maps.
- **Bibliotecas**: `mapsapi`, `readxl`, `dplyr`
- **Uso**:
  - Substitua `SUA_CHAVE_AQUI` por uma chave válida da API do Google.
  - Defina os endereços de origem e destino.
  - Execute o script para gerar a matriz de distâncias entre os locais.
- **Limitações**:
  - A API tem restrições de 25 origens e 25 destinos por requisição.

## 📌 Como usar
1. **Instalar dependências** (se necessário):
   ```r
   install.packages(c("mapsapi", "readxl", "dplyr", "remotes"))
   remotes::install_github("michaeldorman/mapsapi")
   ```
2. **Executar um script**:
   ```r
   source("calcular_distancia_google_maps.R")
   ```

📌 **Dica:** Para usar scripts específicos, consulte a documentação de cada um nos comentários dentro do código.