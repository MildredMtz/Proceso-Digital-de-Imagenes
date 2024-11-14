from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import cv2
import imutils
import numpy as np

# Configurar la ventana principal
root = Tk()
root.title("Proyecto Final FotoMorsaicos")

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


# Botón para cargar la imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Iniciar el bucle principal de la GUI
root.mainloop()