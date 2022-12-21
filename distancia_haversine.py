##############################################################################
### DISTÂNCIA HAVERSINE
##############################################################################

# Script para calcular a distância entre dois pares de coordenadas (lat, long)
# Idealmente deve ser atrelada a uma base de CEPs e coordenadas

#@udf(returnType=FloatType())
from pyspark.sql.types import FloatType
import pyspark.sql.functions as f
import math

def haversine_distance (lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map (math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(a))
  
# Aplicação da função  
#haversine_distance(latl, lon1, lat2, lon2)

# Exemplo Curitiba -> São Paulo
haversine_distance(-25.450108,-49.28545,-23.55031,-46.6342)

# Exemplo de tabela
#cep,"latitude","longitude","cidade","uf"
#1001000,-23.55031,-46.6342,São Paulo,SP
#80230090,-25.45225,-49.266033,Curitiba,PR

#de_para_sem_base_frete = de_para_sem_base_frete.withColumn('distancia', haversine_distance(f.col('latitude'),
#                                                                                           f.col('longitude'),
#                                                                                           f.col('latitude_sfs'),
#                                                                                           f.col('longitude_sfs')
#                                                                                          ))
