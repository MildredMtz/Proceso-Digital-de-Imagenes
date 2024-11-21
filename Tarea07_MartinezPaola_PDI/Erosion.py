from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np

# Configurar la ventana principal
root = Tk()
root.title("Aplicación de Filtros de Erosión")

# Variables globales
image = None
filtered_image = None
image_pillow = None

# Función para elegir una imagen
def elegir_imagen():
    global image, image_pillow, filtered_image

    # Especificar los tipos de archivos, para elegir solo imágenes
    path_image = filedialog.askopenfilename(filetypes=[("Imagen", "*.jpeg;*.png;*.jpg")])

    if len(path_image) > 0:
        # Leer la imagen de entrada y redimensionarla
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)
        filtered_image = image.copy()  # Crear una copia para procesar filtros

        # Convertir la imagen de OpenCV a Pillow para mostrar
        mostrar_imagen(image)

# Función para mostrar imágenes en el label
def mostrar_imagen(img):
    global image_pillow

    imageToShow = imutils.resize(img, width=380)
    imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
    image_pillow = Image.fromarray(imageToShow)
    img_tk = ImageTk.PhotoImage(image=image_pillow)

    lblInputImage.configure(image=img_tk)
    lblInputImage.image = img_tk

# Función para aplicar dilatación
def aplicar_dilatacion():
    global filtered_image

    if image is None:
        return

    kernel = np.ones((3, 3), np.uint8)  # Definir kernel
    filtered_image = cv2.dilate(filtered_image, kernel, iterations=1)
    mostrar_imagen(filtered_image)

# Función para aplicar erosión
def aplicar_erosion():
    global filtered_image

    if image is None:
        return

    kernel = np.ones((3, 3), np.uint8)  # Definir kernel
    filtered_image = cv2.erode(filtered_image, kernel, iterations=1)
    mostrar_imagen(filtered_image)

# Botón para cargar la imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=0, padx=5, pady=5)

# Botón para aplicar dilatación
btnDilate = Button(root, text="Aplicar Erosión Mínima", command=aplicar_dilatacion)
btnDilate.grid(column=1, row=0, padx=5, pady=5)

# Botón para aplicar erosión
btnErode = Button(root, text="Aplicar Erosión Máxima", command=aplicar_erosion)
btnErode.grid(column=2, row=0, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=1, columnspan=3)

# Iniciar el bucle principal de la GUI
root.mainloop()
