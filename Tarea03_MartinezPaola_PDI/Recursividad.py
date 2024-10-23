"""
Programa para aplicar un filtro recursivo en tonos grises y tonos en color real
@author Paola Mildred Martinez HIdalgo
@version 1.0
"""

from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk, ImageOps, ImageFilter
import cv2
import imutils
import numpy as np

# Configurar la ventana principal
root = Tk()
root.title("Aplicación de Filtros de Imagen")

# Variables globales
image = None
image_pillow = None

def elegir_imagen():
    # Especificar los tipos de archivos, para elegir solo imágenes
    path_image = filedialog.askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])

    if len(path_image) > 0:
        global image, image_pillow

        # Leer la imagen de entrada y redimensionarla
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=480)
        
        # Convertir la imagen de OpenCV a Pillow para mostrar
        imageToShow = imutils.resize(image, width=480)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        image_pillow = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=image_pillow)

        lblInputImage.configure(image=img)
        lblInputImage.image = img 

     
# Filtro para imagenes recursivas en tonos de grises 
def recursive_gray_scale():
    if image_pillow is not None:
        bloques = 65  # Define el número de bloques en los que se dividirá la imagen
        width, height = image_pillow.size
        bloque_ancho = width // bloques
        bloque_alto = height // bloques

# Crear una nueva imagen en blanco del mismo tamaño que la original
        nueva_imagen = Image.new("RGB", (width, height))

        for y in range(0, height, bloque_alto):
            for x in range(0, width, bloque_ancho):
                # Definir el área del bloque
                caja = (x, y, x + bloque_ancho, y + bloque_alto)

                # Extraer la región de la imagen original
                region = image_pillow.crop(caja)

                # Calcular el valor promedio de gris en esta región
                gris_promedio = promedio_gris(region)

                # Redimensionar la imagen original para que quepa en este bloque
                imagen_reducida = image_pillow.resize((bloque_ancho, bloque_alto))

                # Convertir la imagen reducida a escala de grises
                imagen_reducida_gris = imagen_reducida.convert("L")

                # Aplicar el tono de gris promedio a la imagen reducida
                imagen_final = Image.new("L", imagen_reducida_gris.size, gris_promedio)
                imagen_reducida_coloreada = Image.composite(imagen_reducida_gris, imagen_final, imagen_reducida_gris)

                # Pegar la imagen reducida coloreada en la nueva imagen
                nueva_imagen.paste(imagen_reducida_coloreada.convert("RGB"), caja)

        # Convertir la imagen resultante para mostrar en Tkinter
        img_recursiva = ImageTk.PhotoImage(nueva_imagen.resize((580, 480)))
        lblInputImage.configure(image=img_recursiva)
        lblInputImage.image = img_recursiva

# Cálculo del promedio de gris para una región
def promedio_gris(region):
    # Convierte la región en escala de grises
    gris_region = region.convert("L")
    # Obtiene el valor promedio de gris de todos los píxeles en la región
    promedio = sum(gris_region.getdata()) // len(gris_region.getdata())
    return promedio

# Filtro de imágenes recursivas con colores reales
def recursive_color_scale():
    if image_pillow is not None:
        bloques = 65  # Define el número de bloques en los que se dividirá la imagen
        width, height = image_pillow.size
        bloque_ancho = width // bloques
        bloque_alto = height // bloques

        # Crear una nueva imagen en blanco del mismo tamaño que la original
        nueva_imagen = Image.new("RGB", (width, height))

        for y in range(0, height, bloque_alto):
            for x in range(0, width, bloque_ancho):
                # Definir el área del bloque
                caja = (x, y, x + bloque_ancho, y + bloque_alto)

                # Extraer la región de la imagen original
                region = image_pillow.crop(caja)

                # Calcular el valor promedio de color (RGB) en esta región
                color_promedio = promedio_color(region)

                # Crear una imagen del color promedio para este bloque
                imagen_promedio = Image.new("RGB", (bloque_ancho, bloque_alto), color_promedio)

                # Pegar la imagen del color promedio en el bloque de la nueva imagen
                nueva_imagen.paste(imagen_promedio, caja)

        # Convertir la imagen resultante para mostrar en Tkinter
        img_recursiva = ImageTk.PhotoImage(nueva_imagen.resize((580, 480)))
        lblInputImage.configure(image=img_recursiva)
        lblInputImage.image = img_recursiva

# Cálculo del promedio de color (RGB) para una región
def promedio_color(region):
    # Convierte la región a modo RGB
    rgb_region = region.convert("RGB")
    # Obtiene los valores promedio de cada canal de color
    promedio_r = sum([pixel[0] for pixel in rgb_region.getdata()]) // len(rgb_region.getdata())
    promedio_g = sum([pixel[1] for pixel in rgb_region.getdata()]) // len(rgb_region.getdata())
    promedio_b = sum([pixel[2] for pixel in rgb_region.getdata()]) // len(rgb_region.getdata())
    return promedio_r, promedio_g, promedio_b

# Botón para cargar imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5) # Coordenadas del boton 

# Botón para aplicar filtro de imágenes recursivas en tonos de grises
btnRecursiveGrayScale = Button(root, text="Filtro Recursivo Gris", command=recursive_gray_scale)
btnRecursiveGrayScale.grid(column=2, row=1, padx=5, pady=5)

# Botón para aplicar filtro de mosaico de colores reales
btnColorMosaic = Button(root, text="Filtro Recursivo Color", command=recursive_color_scale)
btnColorMosaic.grid(column=3, row=1, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Iniciar el bucle principal de la GUI
root.mainloop()

