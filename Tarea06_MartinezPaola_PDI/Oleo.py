from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import cv2
import imutils
import numpy as np

# Configurar la ventana principal
root = Tk()
root.title("Aplicación de Filtros de Imagen")

# Variables globales
image = None
image_pillow = None

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

# Función para aplicar la convolución de 7x7 a cada bloque
def convolucion_oleo(imagen):
    imagen_array = np.array(imagen)

# Suavizar los tonos de gris 
    imagen_convolucionada = cv2.medianBlur(imagen_array, 7)
    return Image.fromarray(imagen_convolucionada)

# Funcion para agregar textura a una imagen en tonos grises
def agregar_textura(imagen):
    width, height = imagen.size
    imagen_array = np.array(imagen)

    noise = np.random.normal(0, 20, (height, width)).astype(np.int16) 
    imagen_con_textura = np.clip(imagen_array + noise, 0, 255).astype(np.uint8)  # Los valores deben de estar en el rango [0, 255]
    
    return Image.fromarray(imagen_con_textura)

# Funcion para agregar textura a una imagen a color con RGB 
def agregar_textura_color(imagen):
    width, height = imagen.size
    imagen_array = np.array(imagen)

    noise = np.random.normal(0, 20, (height, width, 3)).astype(np.int16) 
    imagen_con_textura_color = np.clip(imagen_array + noise, 0, 255).astype(np.uint8) # Los valores deben de estar en el rango [0, 255]

    return Image.fromarray(imagen_con_textura_color)


# Funcion para aplicar filtro oleo a una imagen en blanco y negro 
def oleo_bn():
    global image_pillow
    if image_pillow is not None:

    # Convertir imagen a tonos grises 
       image_gray = image_pillow.convert("L")

    # Aplicar la convolución de 7x7 para suavizar
       image_convolucionada = convolucion_oleo(image_gray)

    # Reducir niveles de color (posterización) para acentuar efecto de óleo
       image_posterizada = ImageOps.posterize(image_convolucionada, 3)

    # Agregar textura de pinceladas
       image_texturizada = agregar_textura(image_posterizada)

    # Mostrar la imagen final en la interfaz 
    img_result = ImageTk.PhotoImage(image_texturizada)
    lblInputImage.configure(image=img_result)
    lblInputImage.image = img_result

# Funcion para aplicar filtro oleo a una imagen a color 
def oleo_color():
    global image_pillow
    if image_pillow is not None:

    # Aplicar la convolución de 7x7 para suavizar
       image_convolucionada = convolucion_oleo(image_pillow)

    # Reducir niveles de color (posterización) para acentuar efecto de óleo
       image_posterizada = ImageOps.posterize(image_convolucionada, 3)

    # Agregar textura de pinceladas
       image_texturizada = agregar_textura_color(image_posterizada)

    # Mostrar la imagen final en la interfaz 
    img_result = ImageTk.PhotoImage(image_texturizada)
    lblInputImage.configure(image=img_result)
    lblInputImage.image = img_result


# Botón para cargar la imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5)

# Botón para aplicar filteo oleo balnco y negro 
btnOleo_bn = Button(root, text="Oleo Branco y Negro", command=oleo_bn)
btnOleo_bn.grid(column=1, row=1, padx=5, pady=5)

# Botón para aplicar filteo oleo a color
btnOleo_color = Button(root, text="Oleo Color", command=oleo_color)
btnOleo_color.grid(column=2, row=1, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Iniciar el bucle principal de la GUI
root.mainloop()