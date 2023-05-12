import math
import base64
from PIL import Image
from io import BytesIO


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


def get_by_pk(model, pk):
    object = model.objects.get(pk=pk)
    return object


def decodify_image(base64_string):
    # Decodifica el string en base64 a bytes
    imagen_bytes = base64.b64decode(base64_string)

    # Crea un objeto BytesIO para leer los bytes
    imagen_io = BytesIO(imagen_bytes)

    # Abre la imagen utilizando PIL (Python Imaging Library)
    imagen = Image.open(imagen_io)

    return imagen


def codify_image_base64(imagen):
    # Crea un objeto BytesIO para guardar la imagen
    buffer = BytesIO()

    # Guarda la imagen en el objeto buffer en el formato deseado (por ejemplo, PNG)
    imagen.save(buffer, format='PNG')

    # Obtén los bytes de la imagen desde el buffer
    imagen_bytes = buffer.getvalue()

    # Codifica los bytes en base64
    base64_string = base64.b64encode(imagen_bytes).decode('utf-8')

    return base64_string
