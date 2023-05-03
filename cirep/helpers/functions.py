import math


# Funcion para obtener en metros la distancia entre 2 puntos especificados por coordenadas
def calculate_distance_between_coordinates(lat1, lon1, lat2, lon2):
    # Convertir las coordenadas de grados a radianes
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Radio de la tierra en metros
    radio_tierra = 6371000

    # Diferencias de latitud y longitud
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    # Aplicar la fórmula de Haversine
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia_km = radio_tierra * c

    # Convertir la distancia a metros
    distancia_m = distancia_km * 1000
    print('Distancia en km entre [{0}, {1}] y [{2}, {3}] = {4}'.format(lat1, lon1, lat2, lon2, distancia_km))
    print('Distancia en m entre [{0}, {1}] y [{2}, {3}] = {4}'.format(lat1, lon1, lat2, lon2, distancia_m))
    return distancia_m
