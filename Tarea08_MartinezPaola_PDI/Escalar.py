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
img_original = None

# Función para elegir una imagen
def elegir_imagen():
    # Especificar los tipos de archivos, para elegir solo imágenes
    path_image = filedialog.askopenfilename(filetypes=[("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")])

    if len(path_image) > 0:
        global image, image_pillow, img_original

        # Leer la imagen de entrada
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)
        img_original = image.copy()  # Guardar una copia de la imagen original
        
        # Convertir la imagen de OpenCV a Pillow para mostrar
        imageToShow = imutils.resize(image, width=380)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        image_pillow = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=image_pillow)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

# Función para aplicar el escalado
def aplicar_escalado():
    if img_original is not None:
        # Crear una ventana para obtener el factor de escala del usuario.
        ventana_escalado = Toplevel(root)
        ventana_escalado.title("Escalar Imagen")
        ventana_escalado.geometry("300x100")
        #ventana_escalado.configure(bg='#2E2E2E')

        Label(ventana_escalado, text="Factor de Escalado (ej. 0.5 o 2.0):")
        escala_entry = Entry(ventana_escalado, width=10)
        escala_entry.pack()

        def confirmar_escalado():
            try:
                factor = float(escala_entry.get())
                if factor <= 0:
                    raise ValueError("El factor debe ser mayor que 0.")

                # Escalar la imagen usando interpolación bilineal.
                global image, image_pillow
                img_original_np = np.array(img_original)
                nueva_altura = int(img_original_np.shape[0] * factor)
                nueva_anchura = int(img_original_np.shape[1] * factor)

                # Crear la imagen escalada.
                img_procesada_np = np.zeros((nueva_altura, nueva_anchura, img_original_np.shape[2]), dtype=np.uint8)
                for i in range(nueva_altura):
                    for j in range(nueva_anchura):
                        # Calcular las coordenadas originales.
                        src_y = i / factor
                        src_x = j / factor

                        # Encontrar los píxeles más cercanos.
                        y0, x0 = int(src_y), int(src_x)
                        y1, x1 = min(y0 + 1, img_original_np.shape[0] - 1), min(x0 + 1, img_original_np.shape[1] - 1)

                        # Calcular pesos para la interpolación bilineal.
                        wy = src_y - y0
                        wx = src_x - x0

                        # Interpolar los valores.
                        pixel = (
                            (1 - wy) * (1 - wx) * img_original_np[y0, x0]
                            + (1 - wy) * wx * img_original_np[y0, x1]
                            + wy * (1 - wx) * img_original_np[y1, x0]
                            + wy * wx * img_original_np[y1, x1]
                        )
                        img_procesada_np[i, j] = pixel

                # Convertir de nuevo a formato PIL y mostrar.
                img_procesada_rgb = cv2.cvtColor(img_procesada_np, cv2.COLOR_BGR2RGB)
                img_procesada = Image.fromarray(img_procesada_rgb)
                image_pillow = img_procesada
                img = ImageTk.PhotoImage(image=image_pillow)
                lblInputImage.configure(image=img)
                lblInputImage.image = img
                ventana_escalado.destroy()


            except ValueError:
                print("Por favor, ingrese un valor válido.")
        
        # Botón de confirmar el escalado
        btnConfirmarEscalado = Button(ventana_escalado, text="Aplicar Filtro (0.1 - 2.0)", command=confirmar_escalado)
        btnConfirmarEscalado.pack(pady=5)

# Botones para cargar la imagen y aplicar filtros
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5)

btnEscalar = Button(root, text="Medida Escalar", command=aplicar_escalado)
btnEscalar.grid(column=0, row=2, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=3, columnspan=3)

# Iniciar el bucle principal de la GUI
root.mainloop()
