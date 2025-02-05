"""
📍 Cálculo de Distância Haversine

Este script calcula a distância geodésica entre dois pontos na superfície da Terra, 
com base em suas coordenadas de latitude e longitude. 
O método utiliza a **fórmula de Haversine**, sendo útil para cálculos 
de proximidade entre cidades, análise de entregas e deslocamentos.

🔹 **Funcionalidades:**
- Calcula a distância entre dois pares de coordenadas (latitude, longitude)
- Ideal para ser atrelado a bases de CEPs e coordenadas geográficas
- Implementação compatível com **Apache Spark** usando `pyspark.sql.functions`

🔹 **Bibliotecas Utilizadas:**
- `math` → Para cálculos trigonométricos
- `pyspark.sql.functions` → Aplicação da função em DataFrames do Spark

🔹 **Fórmula de Haversine:**
\[ d = 2 * R * asin( sqrt( sin^2(Δφ/2) + cos(φ1) * cos(φ2) * sin^2(Δλ/2) ) ) \]
Onde:
- \( R \) = Raio da Terra (aproximadamente 6371 km)
- \( Δφ \) e \( Δλ \) são diferenças de latitude e longitude em radianos
- \( φ1 \) e \( φ2 \) são as latitudes convertidas para radianos
"""

import math
from pyspark.sql.types import FloatType
import pyspark.sql.functions as f

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula a distância entre dois pontos geográficos usando a fórmula de Haversine.
    
    Parâmetros:
    - lat1, lon1: Latitude e longitude do primeiro ponto (graus decimais)
    - lat2, lon2: Latitude e longitude do segundo ponto (graus decimais)
    
    Retorno:
    - Distância em quilômetros entre os pontos
    """
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(a))

# 🔹 Exemplo de uso: Distância entre Curitiba e São Paulo
curitiba_to_sao_paulo = haversine_distance(-25.450108, -49.28545, -23.55031, -46.6342)
print(f"Distância Curitiba → São Paulo: {curitiba_to_sao_paulo:.2f} km")

# 🔹 Aplicação em DataFrames do Spark
# Exemplo de utilização em uma base de dados com coordenadas
# de_para_sem_base_frete = de_para_sem_base_frete.withColumn(
#     'distancia', haversine_distance(
#         f.col('latitude'), f.col('longitude'), f.col('latitude_sfs'), f.col('longitude_sfs')
#     )
# )
