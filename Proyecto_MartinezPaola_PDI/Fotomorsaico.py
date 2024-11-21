import pathlib
import json
import os
import math
import random

import numpy as np
import cv2

# Funcion para calcular el color promedio de una imagen 
def get_average_color(img):
    average_color = np.average(np.average(img, axis=0), axis=0)
    average_color = np.around(average_color, decimals=1)
    average_color = tuple(int(i) for i in average_color)
    return average_color

# Funcion para encontrar el color mas cercano en caso de que no este el color buscado
# color = es el color que estamos buscando
# colors = son los colores que tenemos en el archivo json
def get_closest_color(color, colors):
    cr, cg, cb = color

    min_difference = float("inf")
    closest_color = None
    for c in colors:
        r, g, b = eval(c)
        difference = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b -cb) ** 2)
        if difference < min_difference:
            min_difference = difference
            closest_color = eval(c)

    return closest_color

# En caso de ya tener el archivo json ya no lo volvera a hacer
if "cache.json" not in os.listdir():
    pass

# Creamos una ruta para la carpeta de imagenes 
imgs_dir = pathlib.Path("Imagenes")
# Creamos una ruta por si las imagenes se encuentran dentro de carpetas 
images = list(imgs_dir.glob("**/*.jpg"))

# Para obtener la ruta de las imagenes 
data = {}
for img_path in images:
    img = cv2.imread(str(img_path))
    average_color = get_average_color(img)

# Funcion para obtener las imagenes que cumplen con un color promedio establecido
    if str(tuple(average_color)) in data:
        data[str(tuple(average_color))].append(str(img_path))
    else:
        data[str(tuple(average_color))] = [str(img_path)]
# Capturamos toda la información anterior en un json
with open("cache.json", "w") as file:
    json.dump(data, file, indent=2, sort_keys=True)
print("Caching done")

with open("cache.json", "r") as file:
    data = json.load(file)

# Tomamos nuestra imagen principal y obtenenmos propiedades (altura, ancho)
img = cv2.imread("image.jpg")
img_height, img_width, _ = img.shape
tile_height, tile_width = 20, 20 # Definimos el tamaño de cada pixel

# Hacemos lo siguiente para dividir la imagen principal
num_tiles_h, num_tiles_w = img_height // tile_height, img_width // tile_width
img = img[:tile_height * num_tiles_h, :tile_width * num_tiles_w]

tiles = []
for y in range(0, img_height, tile_height):
    for x in range(0, img_width, tile_width):
        tiles.append((y, y + tile_height, x, x + tile_width))

for tile in tiles:
    y0, y1, x0, x1 = tile
    try:
        average_color = get_average_color(img[y0:y1, x0:x1])
    except Exception:
        continue
    closest_color = get_closest_color(average_color, data.keys())

    # Redimensionamos las medidas de las imagenenes que se colocaran 
    i_path = random.choice(data[str(closest_color)])
    i = cv2.imread(i_path)
    i = cv2.resize(i, (tile_width, tile_height))
    img[y0:y1, x0:x1] = i

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cv2.imwrite("NuevaImagen.jpg", img)
