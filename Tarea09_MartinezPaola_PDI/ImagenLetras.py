from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import cv2
import imutils
import numpy as np

# Configurar la ventana principal
root = Tk()
root.title("Aplicación de Filtros de Mosaico de Letras")

# Variables globales
image = None
processed_image = None
image_pillow = None

# Ajuste del color promedio para mejorar la percepción
def get_average_color(region):
    average_color = cv2.mean(region)
    return tuple(map(int, average_color[:3]))  # Ignora el canal alfa si existe



# Función para aplicar el filtro de mosaico de letras
def aplicar_filtro_mosaico():
    global image, processed_image, image_pillow

    if image is None:
        lblStatus.config(text="Por favor, carga una imagen primero.")
        return

    letra = letra_var.get() or "M"  # Letra predeterminada: 'A'
    region_size = int(region_size_var.get() or 5)  # Tamaño predeterminado: 10
    font_path = "arial.ttf"  # Cambiar si no tienes Arial instalada

    img_height, img_width, _ = image.shape

    # Crear una imagen PIL para dibujar
    pil_img = Image.new("RGB", (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(pil_img)

    try:
        font = ImageFont.truetype(font_path, region_size)
    except IOError:
        lblStatus.config(text="No se encontró la fuente Arial. Instala o ajusta el font_path.")
        return

    for y in range(0, img_height, region_size):
        for x in range(0, img_width, region_size):
            # Extraer la región de interés (ROI)
            region = image[y:y + region_size, x:x + region_size]
            if region.size == 0:
                continue

            # Calcular el color promedio de la región
            average_color = get_average_color(region)

            # Posición centrada de la letra
            text_x = x + region_size // 2
            text_y = y + region_size // 2

            # Dibujar la letra con el color promedio
            draw.text((text_x, text_y), letra, fill=average_color, font=font, anchor="mm")

    # Convertir la imagen procesada de vuelta a formato OpenCV
    processed_image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # Mostrar la imagen procesada en la interfaz
    imageToShow = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    imageToShow = imutils.resize(imageToShow, width=380)
    image_pillow = Image.fromarray(imageToShow)
    img = ImageTk.PhotoImage(image=image_pillow)

    lblOutputImage.configure(image=img)
    lblOutputImage.image = img
    lblStatus.config(text="Mosaico de letras aplicado con éxito.")

# Función para elegir una imagen
def elegir_imagen():
    path_image = filedialog.askopenfilename(filetypes=[("Imagen", ".jpeg .png .jpg")])
    if len(path_image) > 0:
        global image, image_pillow

        # Leer la imagen y redimensionarla
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)

        # Convertir la imagen a formato Pillow para mostrarla
        imageToShow = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imageToShow = imutils.resize(imageToShow, width=380)
        image_pillow = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=image_pillow)

        lblInputImage.configure(image=img)
        lblInputImage.image = img
        lblStatus.config(text="Imagen cargada correctamente.")

# Botón para cargar la imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5)

# Entradas para parámetros del filtro
letra_var = StringVar(value="M")
region_size_var = StringVar(value="5")

lblLetra = Label(root, text="Letra:")
lblLetra.grid(column=1, row=1)
entryLetra = Entry(root, textvariable=letra_var, width=5)
entryLetra.grid(column=2, row=1)

lblRegionSize = Label(root, text="Tamaño región:")
lblRegionSize.grid(column=1, row=2)
entryRegionSize = Entry(root, textvariable=region_size_var, width=5)
entryRegionSize.grid(column=2, row=2)

# Botón para aplicar el filtro
btnApplyFilter = Button(root, text="Aplicar Mosaico de Letras", command=aplicar_filtro_mosaico)
btnApplyFilter.grid(column=0, row=3, padx=5, pady=5)

# Etiquetas para mostrar imágenes
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=4)

lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=4)

# Etiqueta de estado
lblStatus = Label(root, text="", fg="green")
lblStatus.grid(column=0, row=5, columnspan=3)

# Iniciar el bucle principal de la GUI
root.mainloop()
