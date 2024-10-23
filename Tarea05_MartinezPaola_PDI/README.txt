Proceso digital de imágenes.

Tarea 5.

Nombre: Martínez Hidalgo Paola Mildred 319300217

Nuevos filtros: Semitonos, Dithering, Floyd-Steinberg, Dithering Ordenado y 
Dithering Disperso.

¿Cómo correr el programa?

Lenguaje de programación utilizado: Python 

Dentro del ZIP tendremos los siguientes archivos:
- Tarea05.py
- Imagen.jpg
- Imagenes para los semitonos 0-9
- README.txt

Nos ubicamos en el archivo "Tarea05.py" y corremos el programa. Si lo 
corremos mediante Visual Studio Code simplemente le damos en "run", si lo corremos 
mediante la terminal hacemos lo siguiente:

- Navegamos al directorio donde se encuentra nuestro archivo.
- Una vez que nos encontremos en el direcctorio correcto ejecutamos el archivo con el 
siguiete comando:
      pyhon nombreDelPrograma.py
      python Tarea05.py

Despues de hacer esto nos abrirá la interfaz de usuario donde tendremos los siguiente 
botones:
- Cargar Imagen
- Aplicar Semitonos
- Aplicar Dithering
- Aplicar Floyd-Steinberg
- Aplicar Dithering Ordenado
- Aplicar Dithering Disperso

Primero seleccionaremos la imagen, dentro del zip hay una imagen llamada "Imagen.jpg"
la seleccionamos y después aplicamos uno de los filtros con los botones que se 
encunetran en la interfaz, esperamos unos momentos y aparecerá la imagen com el filtro aplicado. 

¿Qué hace nuestra práctica?
El propósito de esta práctica es poder aplicar diferentes filtros a una imágen, el programa
cuenta con una interfaz para que sea más amigable con el usuario.
El programa se encarga de que sólo se ingresen formatos de imágenes como png, jpeg y jpg.
Todo el código se encuentra documentado en caso de que se quiera hacer un cambio o 
revisar algo en específico.
En el caso del filtro de semitonos se usan imágenes auxiliares las cuales van desde las más
obscuras (semitono_0) a las más claras (semitono_9). En caso de que se quiera colocar otra 
imágen para aplicarle el filtro esta debe de ser llamada "Imagen".

