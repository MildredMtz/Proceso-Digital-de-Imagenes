"""
Aplicacion de filtros a imagen en formato jpg
Filtros:
gray scale
gray luminace 
mica effect

@author Paola Mildred Martinez Hidalgo 
@version 1.0
"""

from PIL import Image

# Gray scale (escala de grises)
# Codigo para aplicar filtro que pasa una imagen a escalas de grises 
# Gray = (R*1 + G*1 + B*1) / 3 (división entera)

def gray_scale(img):
    width, height = img.size 
    gray_img = img.copy()
    for x in range(width): # definimos el ancho con x 
        for y in range(height): # definimos la altura con y 
            r, g, b = gray_img.getpixel((x, y)) #nos aseguramos que este en RGB
            gray = (r + g + b) // 3 #como se multiplica por 1 no es necesario ponerlo
            gray_img.putpixel((x, y), (gray, gray, gray))
    return gray_img


# Gray luminance (grises con luminancia)
# Codigo para aplicar filtro que calcula la escala de grises basada en la luminancia 
# Gray = (Red * 0.299 + Green * 0.587 + Blue * 0.114)

def gray_luminance(img):
    width, height = img.size
    gray_img = img.copy()
    for x in range(width): # definimos el ancho con x
        for y in range(height): # definimos la altura con y
            r, g, b = gray_img.getpixel((x, y)) # nos aseguramos que este en RGB
            gray = int(r * 0.299 + g * 0.587 + b * 0.114 ) # definimos los valores de RGB
            gray_img.putpixel((x, y), (gray, gray, gray))
    return gray_img

# Mica effect (Efecto mica)
# Codigo para aplicar filtro efecto Mica 
# Efecto mica. Cualquier RGB sobre una imagen

def mica_effect(img, color):
    img = img.convert('RGBA') # Convertimos a RGBA para manejar la transparencia
    overlay = Image.new('RGBA', img.size, color) # Creamos una imagen del color deseado
    combined = Image.blend(img, overlay, alpha=0.5)  # Combina ambas imágenes (mica y foto original)
    return combined

def apply_filters(image_path):
    img = Image.open(image_path).convert('RGB')
    
    # Aplicar cada filtro
    gray_sca = gray_scale(img)
    gray_lum = gray_luminance(img)
    mica_img = mica_effect(img, (0, 0, 250, 128))  # Seleccionar el efecto mica que queremos
    
    # Mostrar las imágenes resultantes
    gray_sca.show(title="Escala de grises")
    gray_lum.show(title="Grises con luminancia")
    mica_img.show(title="Efecto mica")

    # Guardar las imágenes automáticamente
    gray_sca.save('Escala_grises.jpg')
    gray_lum.save('Grises_luminancia.jpg')
    mica_img.save('Efecto_mica.png')  # Guardar como PNG para conservar la transparencia

apply_filters('imagen.jpg')
