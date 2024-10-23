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
        image = imutils.resize(image, height=380)
        
        # Convertir la imagen de OpenCV a Pillow para mostrar
        imageToShow = imutils.resize(image, width=380)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        image_pillow = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=image_pillow)

        lblInputImage.configure(image=img)
        lblInputImage.image = img 

    # Escala de grises 

def gray_scale():
    if image_pillow is not None:
        # Aplicar el filtro de escala de grises usando la función proporcionada
        gray_image = gray_scale_pillow(image_pillow)
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_gray = ImageTk.PhotoImage(gray_image.resize((480, 380)))
        lblInputImage.configure(image=img_gray)
        lblInputImage.image = img_gray

def gray_scale_pillow(img):
    width, height = img.size 
    gray_img = img.copy()
    for x in range(width): # definimos el ancho con x 
        for y in range(height): # definimos la altura con y 
            r, g, b = gray_img.getpixel((x, y)) # nos aseguramos que esté en RGB
            gray = (r + g + b) // 3 # calcular el valor de gris
            gray_img.putpixel((x, y), (gray, gray, gray))
    return gray_img

# Grises con luminancia

def gray_luminance_image():
    if image_pillow is not None:
        # Aplicar el filtro de escala de grises usando la función proporcionada
        gray_lum = gray_luminance(image_pillow)
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_graylum = ImageTk.PhotoImage(gray_lum.resize((480, 380)))
        lblInputImage.configure(image=img_graylum)
        lblInputImage.image = img_graylum

def gray_luminance(img):
    width, height = img.size
    gray_img = img.copy()
    for x in range(width): # definimos el ancho con x
        for y in range(height): # definimos la altura con y
            r, g, b = gray_img.getpixel((x, y)) # nos aseguramos que este en RGB
            gray = int(r * 0.299 + g * 0.587 + b * 0.114 ) # definimos los valores de RGB
            gray_img.putpixel((x, y), (gray, gray, gray))
    return gray_img

# Efecto mica

def mica_effect_image():
    if image_pillow is not None:
        # Permitir que el usuario seleccione un color para el efecto mica
        color = askcolor()[1]  # Esto abre un selector de color y obtiene el color elegido
        if color is None:
            return  # Si el usuario cancela el selector de color, no se aplica el efecto

        # Aplicar el efecto mica usando la función proporcionada
        mica = mica_effect(image_pillow, color)
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        imgME = ImageTk.PhotoImage(mica.resize((480, 380)))
        lblInputImage.configure(image=imgME)
        lblInputImage.image = imgME

def mica_effect(img, color):
    img = img.convert('RGBA')  # Convertimos a RGBA para manejar la transparencia
    overlay = Image.new('RGBA', img.size, color)  # Creamos una imagen del color deseado
    combined = Image.blend(img, overlay, alpha=0.5)  # Combina ambas imágenes (mica y foto original)
    return combined

# Filtro BLUR (borroso)

def blur_image():
    if image_pillow is not None:
        # Aplicar el filtro BLUR usando la función proporcionada
        blur_image = blur(image_pillow)
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_blur = ImageTk.PhotoImage(blur_image.resize((480, 380)))
        lblInputImage.configure(image=img_blur)
        lblInputImage.image = img_blur

# Filtro BLUR (borroso)
def blur(img):
    return img.filter(ImageFilter.BLUR)

# Filtro Motion Blur (movimiento)

def motion_blur_image():
    if image_pillow is not None:
        # Convertir la imagen PIL a un array de NumPy (en RGB)
        img_array = np.array(image_pillow)
        
        # Convertir de RGB a BGR
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Aplicar el filtro Motion Blur usando la función proporcionada
        mblur_image_array = motion_blur(img_array)
        
        # Convertir la imagen resultante de nuevo a RGB para formato PIL
        mblur_image_pillow = Image.fromarray(cv2.cvtColor(mblur_image_array, cv2.COLOR_BGR2RGB))
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_mblur = ImageTk.PhotoImage(mblur_image_pillow.resize((480, 380)))
        lblInputImage.configure(image=img_mblur)
        lblInputImage.image = img_mblur
        

def motion_blur(img):
    size = 30  # Cantidad de desenfoque

    # Crear un kernel de movimiento horizontal
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size - 1)/2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size
    
    # Aplicar el filtro a la imagen usando el kernel
    motion_blurred = cv2.filter2D(img, -1, kernel_motion_blur)
    return motion_blurred


    # Encontrar bordes 

def bordes_image():
    if image_pillow is not None:
        # Convertir la imagen PIL a un array de NumPy
        img_array = np.array(image_pillow)
        
        # Aplicar el filtro de bordes 
        bordes_image_array = detect_bordes(img_array)
        
        # Convertir la imagen resultante de nuevo a formato PIL
        bordes_image_pillow = Image.fromarray(bordes_image_array)
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_bordes = ImageTk.PhotoImage(bordes_image_pillow.resize((480, 380)))
        lblInputImage.configure(image=img_bordes)
        lblInputImage.image = img_bordes

def detect_bordes(img):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Kernel para detectar bordes a 45 grados
    kernel_45 = np.array([
        [-1, -1,  0],
        [-1,  0,  1],
        [ 0,  1,  1]
    ], dtype=np.float32)
    
    # Aplicar el filtro a la imagen usando el kernel
    diagonal_bordes = cv2.filter2D(gray, -1, kernel_45)
    
    return diagonal_bordes

#Filtro Sharped (Enfocar)

def sharpen_image():
    if image_pillow is not None:
        # Convertir la imagen PIL a un array de NumPy (en RGB)
        img_array = np.array(image_pillow)
        
        # Convertir de RGB a BGR
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Aplicar el filtro sharpen usando la función proporcionada
        sharpen_image_array = sharpen(img_array)
        
        # Convertir la imagen resultante de nuevo a RGB para formato PIL
        sharpen_image_pillow = Image.fromarray(cv2.cvtColor(sharpen_image_array, cv2.COLOR_BGR2RGB))
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_sharpen = ImageTk.PhotoImage(sharpen_image_pillow.resize((480, 380)))
        lblInputImage.configure(image=img_sharpen)
        lblInputImage.image = img_sharpen


def sharpen(img):
    # Kernel para el filtro sharpen
    kernel_sharpen = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ], dtype=np.float32)
    
    # Aplicar el filtro a la imagen usando el kernel
    sharpened = cv2.filter2D(img, -1, kernel_sharpen)
    
    return sharpened

# Filtro Promedio

def average_blur_image():
    if image_pillow is not None:
        # Convertir la imagen PIL a un array de NumPy (en RGB)
        img_array = np.array(image_pillow)
        
        # Convertir de RGB a BGR
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Aplicar el filtro Average Blur usando la función proporcionada
        avg_blur_image_array = average_blur(img_array)
        
        # Convertir la imagen resultante de nuevo a RGB para formato PIL
        avg_blur_image_pillow = Image.fromarray(cv2.cvtColor(avg_blur_image_array, cv2.COLOR_BGR2RGB))
        
        # Convertir la imagen a PhotoImage para mostrar en Tkinter
        img_avg_blur = ImageTk.PhotoImage(avg_blur_image_pillow.resize((480, 380)))
        lblInputImage.configure(image=img_avg_blur)
        lblInputImage.image = img_avg_blur

def average_blur(img):
    # Kernel para el filtro promedio
    kernel_average = np.ones((3, 3), dtype=np.float32) / 9.0
    
    # Aplicar el filtro a la imagen usando el kernel
    avg_blurred = cv2.filter2D(img, -1, kernel_average)
    
    return avg_blurred

# Botón para cargar imagen
btnChooseImage = Button(root, text="Cargar Imagen", command=elegir_imagen)
btnChooseImage.grid(column=0, row=1, padx=5, pady=5) # Coordenadas del boton 

# Botón para aplicar filtro de escala de grises
btnGrayScale = Button(root, text="Escala de Grises", command=gray_scale)
btnGrayScale.grid(column=1, row=1, padx=5, pady=5) # Coordenadas del boton 

# Botón para aplicar filtro BLUR
blurFilter = Button(root, text="BLUR", command=blur_image)
blurFilter.grid(column=2, row=1, padx=5, pady=5) # Coordenadas del boton 

# Botón para aplicar filtro Motion BLUR
motionBlurFilter = Button(root, text="Motion BLUR", command=motion_blur_image)
motionBlurFilter.grid(column=3, row=1, padx=5, pady=5) # Coordenadas del boton

# Botón para aplicar filtro de bordes
encontrarBordes = Button(root, text="Encontrar bordes", command=bordes_image)
encontrarBordes.grid(column=4, row=1, padx=5, pady=5)

# Botón para aplicar filtro Sharpen
sharpenFilter = Button(root, text="Sharpen", command=sharpen_image)
sharpenFilter.grid(column=1, row=2, padx=5, pady=5)

# Botón para aplicar filtro Promedio
averageBlurFilter = Button(root, text="Filtro Promedio", command=average_blur_image)
averageBlurFilter.grid(column=2, row=2, padx=5, pady=5)

# Botón para aplicar filtro grises con luminancia
grayLum = Button(root, text="Grises con luminancia", command=gray_luminance_image)
grayLum.grid(column=3, row=2, padx=5, pady=5)

# Botón para aplicar filtro efecto mica
micaEffect = Button(root, text="Efecto Mica", command=mica_effect_image)
micaEffect.grid(column=4, row=2, padx=5, pady=5)

# Etiqueta para mostrar la imagen de entrada
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Iniciar el bucle principal de la GUI
root.mainloop()
