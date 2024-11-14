Proceso digital de imágenes.

Tarea 6.

Nombre: Martínez Hidalgo Paola Mildred 319300217

Nuevos filtros: Filtro oleo digital en imágenes de color y blanco y negro.

¿Cómo correr el programa?

Lenguaje de programación utilizado: Python 

Dentro del ZIP tendremos los siguientes archivos:
- Oleo.py
- README.txt
- Imagen1.jpg
- Imagen2.jpg

Nos ubicamos en el archivo "Oleo.py" y corremos el programa. Si lo 
corremos mediante Visual Studio Code simplemente le damos en "run", si lo corremos 
mediante la terminal hacemos lo siguiente:

- Navegamos al directorio donde se encuentra nuestro archivo.
- Una vez que nos encontremos en el direcctorio correcto ejecutamos el archivo con el 
siguiete comando:
      pyhon nombreDelPrograma.py
      python Oleo.py

Despues de hacer esto nos abrirá la interfaz de usuario donde tendremos tres botones
- Cargar Imagen
- Oleo Blanco y Negro
- Oleo Color 

Primero seleccionaremos la imagen, dentro del zip hay dos imágenes llamadas "Imagen1.jpg"
y "Imagen2.jpg", para aplicar el filtro oleo blanco y negro podemos seleccionar 
cualquiera de las dos imágenes. Para aplicar el filtro oleo a color seleccionamos la 
"Imagen1" que está a color. 
Después de seleccionar la imágen aplicamos cualqueira de los dos filtros precionando
el botón, esperamos unos momentos y aparecerá la imagen com el filtro aplicado. 


¿Qué hace nuestra práctica?
El propósito de este programa es poder aplicar el filtro oleo digital a imágenes
a color y en blanco y negro. 
Para ambos filtros el código es muy similar, al igual que creamos una interfaz para que 
el programa sea más amigable con el usuario.
El programa se encarga de que sólo se ingresen formatos de imágenes como png, jpeg y jpg.
Todo el programa se encuentra documentado en caso de que se quiera hacer un cambio o 
revisar algo en específico. 
Para el caso del oleo en tonos de grises se usó la librería pillow,, mientras que para 
las imágenes a color se usó "RGB". 

