from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import cv2
import imutils
import numpy as np
import random

# Configurar la ventana principal
root = Tk()
root.title("Aplicación de Filtros de Imagen")

# Variables globales
image = None
image_pillow = None
semitonos = []  # Lista para almacenar las imágenes de semitono

# Función para cargar las imágenes de semitonos
def cargar_semitonos():
    global semitonos
    for i in range(10):
        semitono = Image.open(f"semitono_{i}.png").convert("L")  
        semitonos.append(semitono)

# Función para elegir una imagen
def elegir_imagen():
    # Especificar los tipos de archivos, para elegir solo imágenes
    path_image = filedialog.askopenfilename(filetypes=[("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")])

    if len(path_image) > 0:
        global image, image_pillow

        # Leer la imagen de entrada y redimensionarla
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)
        
        # Convertir la imagen de OpenCV a Pillow para mostrar
        imageToShow = imutils.resize(image, width=380)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        image_pillow = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=image_pillow)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

# Función para cuadricular la imagen y aplicar semitonos
def cuadricular():
    if image_pillow is not None:
        bloques = 65  # Número de bloques en cada dimensión (horizontal y vertical)
        width, height = image_pillow.size
        bloque_ancho = width // bloques
        bloque_alto = height // bloques
        
        nueva_imagen = Image.new("L", (width, height))  # Nueva imagen en blanco (escala de grises)
        
        for y in range(0, height, bloque_alto):
            for x in range(0, width, bloque_ancho):
                # Definir el área del bloque
                caja = (x, y, x + bloque_ancho, y + bloque_alto)
                region = image_pillow.crop(caja)
                
                # Calcular el promedio de gris en la región
                gris_promedio = promedio_gris(region)
                
                # Asignar un semitono según el valor de gris promedio
                semitono = asignar_semitono(gris_promedio)
                
                # Redimensionar el semitono para que encaje en el bloque
                semitono_resized = semitono.resize((bloque_ancho, bloque_alto))
                
                # Pegar el semitono en la nueva imagen
                nueva_imagen.paste(semitono_resized, caja)
        
        # Mostrar la imagen procesada en la interfaz
        img = ImageTk.PhotoImage(image=nueva_imagen)
        lblInputImage.configure(image=img)
        lblInputImage.image = img  

# Función para calcular el promedio de gris de una región
def promedio_gris(region):
    # Convierte la región en escala de grises
    gris_region = region.convert("L")
    # Obtiene el valor promedio de gris de todos los píxeles en la región
    promedio = sum(gris_region.getdata()) // len(gris_region.getdata())
    return promedio

# Función para asignar un semitono basado en el valor de gris
def asignar_semitono(gris_promedio):
    # Mapea el valor de gris (0-255) a uno de los 10 semitonos
    indice_semitono = gris_promedio // 25  # Cada semitono cubre un rango de 25 unidades
    indice_semitono = min(indice_semitono, len(semitonos) - 1)  # Evitar índice fuera de rango
    return semitonos[indice_semitono]

# Función para aplicar dithering al azar
def dithering_azar():
   global image_pillow
   if image_pillow is not None:

    # Convertir a tonos grises la imagen 
    image = image_pillow.convert('L')

    # Obtener las dimensiones de la imagen 
    width, height = image.size 

    # Definir si lleva un punto blanco o negro
    nueva_imagen = Image.new('1', (width, height))

    # Recorrer los pixeles de la imagen 
    for y in range(height):
        for x in range(width):
            valor_gris = image.getpixel((x, y)) # Obtener valor de gris de 0 a 255
            valor_azar = random.randint(0,255) # Generar un valor aleatorio
            # Se comparan los valores dados si el valor generado es mayor que el valor de cada pizel, 
            # se pone un punto blanco, sino se pone uno negro.
            if valor_azar > valor_gris:
                nueva_imagen.putpixel((x,y), 255) # punto blanco
            else:
                nueva_imagen.putpixel((x,y), 0) # punto negro

# Mostrar la imagen procesada en la interfaz
   img = ImageTk.PhotoImage(image=nueva_imagen)
   lblInputImage.configure(image=img)
   lblInputImage.image = img 


# Funcion para aplicar filtro floyd-steinberg
def floyd_steinberg():
    global image_pillow
    if image_pillow is not None:
        # Convertir a escala de grises
        image = image_pillow.convert('L')
        image_np = np.array(image, dtype=float)  # Convertir la imagen a un arreglo numpy de punto flotante

        # Obtener dimensiones de la imagen
        width, height = image.size

        for y in range(height):
            for x in range(width):
                old_pixel = image_np[y, x]
                new_pixel = 255 if old_pixel > 127 else 0  # color más cercano (blanco o negro)
                image_np[y, x] = new_pixel
                quant_error = old_pixel - new_pixel

                # Distribuir el error de cuantización a los vecinos
                if x + 1 < width:
                    image_np[y, x + 1] += quant_error * 7 / 16
                if x - 1 >= 0 and y + 1 < height:
                    image_np[y + 1, x - 1] += quant_error * 3 / 16
                if y + 1 < height:
                    image_np[y + 1, x] += quant_error * 5 / 16
                if x + 1 < width and y + 1 < height:
                    image_np[y + 1, x + 1] += quant_error * 1 / 16

    # Convertir el array de nuevo a imagen PIL
    nueva_imagen = Image.fromarray(np.uint8(image_np))

    # Mostrar la imagen procesada en la interfaz
    img = ImageTk.PhotoImage(image=nueva_imagen)
    lblInputImage.configure(image=img)
    lblInputImage.image = img  # Actualizar la imagen en la etiqueta


# Función para aplicar dithering ordenado
def dithering_ordenado():
    global image_pillow
    if image_pillow is not None:
        # Convertir la imagen a escala de grises
        image = image_pillow.convert('L')
        image_np = np.array(image, dtype=float)

        # Matriz Bayer 8x8 
        matriz_bayer = np.array([[0, 48, 12, 60, 3, 51, 15, 63],
                                 [32, 16, 44, 28, 35, 19, 47, 31],
                                 [8, 56, 4, 52, 11, 59, 7, 55],
                                 [40, 24, 36, 20, 43, 27, 39, 23],
                                 [2, 50, 14, 62, 1, 49, 13, 61],
                                 [34, 18, 46, 30, 33, 17, 45, 29],
                                 [10, 58, 6, 54, 9, 57, 5, 53],
                                 [42, 26, 38, 22, 41, 25, 37, 21]], dtype=float)
        matriz_bayer = matriz_bayer / 64.0 * 255.0  # Normalizar la matriz Bayer a escala 0-255

        # Aplicar el patrón de la matriz Bayer
        width, height = image.size
        for y in range(height):
            for x in range(width):
                threshold = matriz_bayer[y % 8, x % 8]
                if image_np[y, x] > threshold:
                    image_np[y, x] = 255
                else:
                    image_np[y, x] = 0

    # Convertir el array de nuevo a imagen PIL
    nueva_imagen = Image.fromarray(np.uint8(image_np))

    # Mostrar la imagen procesada en la interfaz
    img = ImageTk.PhotoImage(image=nueva_imagen)
    lblInputImage.configure(image=img)
    lblInputImage.image = img  

# Función para aplicar dithering disperso 
def dithering_disperso():
    global image_pillow
    if image_pillow is not None:
        # Convertir la imagen a escala de grises
        image = image_pillow.convert('L')
        image_np = np.array(image, dtype=float)

        # Matriz de error de dispersión Stucki (similar a Floyd-Steinberg pero más disperso)
        coeficientes = np.array([[0, 0, 0, 8, 4],
                                 [2, 4, 8, 4, 2],
                                 [1, 2, 4, 2, 1]]) / 42.0

        # Aplicar el algoritmo de dithering disperso
        width, height = image.size
        for y in range(height):
            for x in range(width):
                old_pixel = image_np[y, x]
                new_pixel = 255 if old_pixel > 127 else 0  # Blanco o negro
                image_np[y, x] = new_pixel
                quant_error = old_pixel - new_pixel

                # Distribuir el error de cuantización con la matriz de dispersión
                for dy in range(3):
                    for dx in range(5):
                        if (x + dx - 2) < width and (y + dy) < height:
                            image_np[y + dy, x + dx - 2] += quant_error * coeficientes[dy, dx]

    # Convertir el array de nuevo a imagen PIL
    nueva_imagen = Image.fromarray(np.uint8(image_np))

    # Mostrar la imagen procesada en la interfaz
    img = ImageTk.PhotoImage(image=nueva_imagen)
    lblInputImage.configure(image=img)
    lblInputImage.image = img  # Actualizar la imagen en la etiqueta

# Botón para cargar la imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5)

# Botón para cuadricular y aplicar semitonos
btnCuadricular = Button(root, text="Aplicar Semitonos", command=cuadricular)
btnCuadricular.grid(column=1, row=1, padx=5, pady=5)

# Botón para aplicar dithering
btnDithering = Button(root, text="Aplicar Dithering", command=dithering_azar)
btnDithering.grid(column=2, row=1, padx=5, pady=5)

# Botón para aplicar floyd-steinberg
btnfloyd_steinberg = Button(root, text="Aplicar Floyd-Steinberg", command=floyd_steinberg)
btnfloyd_steinberg.grid(column=3, row=1, padx=5, pady=5)

# Botón para aplicar dithering ordenado
btnDitOrdenado = Button(root, text="Aplicar Dithering Ordenado", command=dithering_ordenado)
btnDitOrdenado.grid(column=4, row=1, padx=5, pady=5)

# Botón para aplicar dithering disperso
btnDitDisperso = Button(root, text="Aplicar Dithering Disperso", command=dithering_disperso)
btnDitDisperso.grid(column=5, row=1, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2, columnspan=2)

# Cargar los semitonos al iniciar la aplicación
cargar_semitonos()

# Iniciar el bucle principal de la GUI
root.mainloop()
