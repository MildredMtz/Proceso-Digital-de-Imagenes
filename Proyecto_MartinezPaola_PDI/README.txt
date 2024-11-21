PROCESO DIGITAL DE IMÁGENES

PROYECTO FINAL

NOMBRE: Martínez Hidalgo Paola Mildred 
NÚM. CUENTA: 319300217

ENLACES PARA DESCARGAR CARPETAS DE IMÁGENES:
- https://www.mediafire.com/file/9g3nznnn91y3hh6/10000_images.rar/file
- https://www.mediafire.com/file/g8z12ixbqi7e0m9/63000fotos.rar/file
- https://www.mediafire.com/file/8jlbjfegcosh7i6/art_explosion.rar/file
- https://www.mediafire.com/file/r3i4v5l91e3rolx/bboa.rar/file

** IMPORTANTE ** Debido a que las carpetas de imágenes están muy pesadas NO se van a 
incluir en el ZIP, sólo le incluirá la carpeta donde se deben de almacenar. Favor de 
extraer las imágenes de los enlaces y almacenarlas en la carpeta indicada ("Imagenes").


PRERREQUISITOS:
- Antes de correr el programa se deben de tener las imágenes descomprimidas y dentro de 
una carpeta llamada "Imagenes". Las imágenes se pueden encontrar en subcarpetas.
- La imagen principal o a la que se le quiere aplicar el filtro debe de ser llamada 
"image.jpg".
- Para correr el programa utilizaremos las siguientes paqueterías de pyhon: opencv y numpy
Para instalarlas puedes usar el siguiente comando
   C:\> pip install opencv-python
Con este comando se deben de instalar los dos correctamente.


¿CÓMO CORRER EL PROGRAMA?

**IMPORTANTE** Toma en cuenta que el programa puede tardar, así que ten paciencia 
para obtener la imagen final c:

Lenguaje de programación utilizado: Python 

Dentro del ZIP tendremos los siguientes archivos:
- Fotomorsaico.py
- README.txt
- image.jpg
- NuevaImagen2.jpg Evidencia de una imagen ya procesada
- NuevaImagen3.jpg Evidencia de una imagen ya procesada 

** NOTA ** Las imágenes ya procesadas se hicieron con las imágenes obtenidas de TODOS 
los enlaces.

Nos ubicamos en el archivo "Fotomorsaico.py" y corremos el programa. Si lo 
corremos mediante Visual Studio Code simplemente le damos en "run", si lo corremos 
mediante la terminal hacemos lo siguiente:

- Abrimos una terminal y navegamos al directorio donde se encuentra nuestro archivo.
- Una vez que nos encontremos en el directorio correcto ejecutamos el archivo con el 
siguiete comando:
      pyhon nombreDelPrograma.py
      python Fotomorsaico.py

Una vez que se corrio el programa nos creará un archivo json llamado "cache.json".
Este archivo contendrá la información de cada imagen de la carpeta "Imagenes", así como
su ruta, nombre y lo más importante su RGB, esto permitirá al programa obtener la imagen 
que mejor se adapte al pixel que va a sutituir.

Después python abrirá una pequeña ventana donde se mostrará el proceso de como se va 
cambiando cada pixel por una imágen de la galería de imágenes que tenemos (esto puede 
ser tardado, así que ve por un café). Una vez terminado se guardará en nuestra carpeta 
principal una imagen llamada "NuevaImagen.jpg", esta será la imagen obtenida. 


¿QUÉ HACE NUESTRO PROYECTO?
El propósito de este proyecto es poder hacer un foto mosaico a partir de una imagen fuente,
para la elección de imágenes se cuenta con una carpeta con más de 5,000 imágenes extraídas 
de internet.
Este programa cuenta con la posibilidad de incluir tus propias imagenes y no de internet,
sólo se debe de tomar en cuenta que a mayor número de imágenes será mejor el resultado, 
esto debido a que habrá una mayor posibilidad de encontrar la imagen más parecida al 
bloque que se va a sustituir. 
Igual en caso de que se quiera que los pixeles de cada imagen sean de mayor o menor 
tamaño se puede modidficar directamente en el código, sólo toma en cuenta que si el 
bloque es de un tamaño muy grande la resolución de la imágen se irá perdiendo.

