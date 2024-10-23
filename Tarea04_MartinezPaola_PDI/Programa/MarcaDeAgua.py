"""
Programa para poner marca de agua a un archivo o imagen
@author Paola Mildred Martínez Hidalgo
@version 1.0

"""
from PIL import Image

# Cargar la imagen principal y la marca de agua
imagen = Image.open('Imagen.jpeg')
marca = Image.open('marca_de_agua.png')

# Redimensionar la marca de agua si es necesario
marca = marca.resize((300, 300))  # Ajustar el tamaño de la marca de agua

# Obtener el tamaño de la imagen principal
width, height = imagen.size

# Definir la posición de la marca de agua 
# En este caso se encuentra en la parte inferior derecha 
posicion = (width - marca.width - 10, height - marca.height - 10)  

# Pegar la marca de agua en la imagen principal
imagen.paste(marca, posicion, marca) 

# Guardar la imagen con la marca de agua 
imagen.save('imagen_con_marca_agua.jpeg')

# Mostrar la imagen final 
imagen.show()
