Proceso digital de imágenes.

Tarea 3.

Nombre: Martínez Hidalgo Paola Mildred 319300217

Nuevos filtros: Imágenes recursivas en tonos grises e imágenes recursivas en 
color real.

¿Cómo correr el programa?

Lenguaje de programación utilizado: Python 

Dentro del ZIP tendremos los siguientes archivos:
- Recursividad.py
- README.txt
- Imagen.jpg

Nos ubicamos en el archivo "Recursividad.py" y corremos el programa. Si lo 
corremos mediante Visual Studio Code simplemente le damos en "run", si lo corremos 
mediante la terminal hacemos lo siguiente:

- Navegamos al directorio donde se encuentra nuestro archivo.
- Una vez que nos encontremos en el direcctorio correcto ejecutamos el archivo con el 
siguiete comando:
      pyhon nombreDelPrograma.py
      python Recursividad.py

Despues de hcaer esto nos abrirá la interfaz de usuario donde tendremos tres botones
- Cargar Imagen
- Filtro Recursivo Color
- Filtro Recursivo Gris 

Primero seleccionaremos la imagen, dentro del zip hay una imagen llamada "Imagen.jpg"
la seleccionamos y después aplicamos uno de los dos filtros, esperamos unos momentos 
y aparecerá la imagen com el filtro aplicado. 


¿Qué hace nuestra práctica?
El propósito de este programa es poder aplicar el efecto recursivo en tonos grises y el 
efecto recursivo en tonos de color real a una imágen. 
Para ambos filtros el código es muy similar, al igual que creamos una interfaz para que 
el programa sea más amigable con el usuario.
El programa se encarga de que sólo se ingresen formatos de imágenes como png, jpeg y jpg.
Todo el programa se encuentra documentado en caso de que se quiera hacer un cambio o 
revisar algo en específico. 
Para el caso del efecto recursivo en tonos de grises ya no se usó el código del programa
anterior, sino que se usó la librería pillow y sólo se uso "L", mientras que para el 
filtro de color real se usó "RGB". 

