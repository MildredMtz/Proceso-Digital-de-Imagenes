Proceso digital de imágenes.

Tarea 4.

Nombre: Martínez Hidalgo Paola Mildred 319300217

Programa para agregar mara de agua a una imágen

¿Cómo correr el programa?

Lenguaje de programación utilizado: Python 

Dentro del ZIP tendremos las siguientes carpetas :
- Imagenes_concurso
- Programa

*NOTA: Antes de correr este programa nos tenemos que asegurar de tener los siguientes 
archivos en la misma carpeta "Programa".
- Imagen.jpeg: Esta imagen será a la cual se le apliacará la marca de agua, igual
podemos tener una imágen en formato png, pero sería necesario modificar la línea 10
del código. 
- marca_de_agua.png: Esta imágen contendrá la marca de agua, podemos poner cualquier 
otra, en este caso ya tenemos una por defecto, en caso de cambiarla nos tenemos que 
asegurar de que la imágen se encuentre en formato png y con fondo transparente. 


Una vez hecho lo anterior nos ubicamos dentro de la carpeta "Programa" y en él 
encontraremos un archivo con el nombre "MarcaDeAgua.py", tendremos que correr este 
programa. Si lo corremos mediante Visual Studio Code simplemente le damos en "run", 
si lo corremos mediante la terminal hacemos lo siguiente:

- Navegamos al directorio donde se encuentra nuestro archivo.
- Una vez que nos encontremos en el direcctorio correcto ejecutamos el archivo con el 
siguiete comando:
      pyhon nombreDelPrograma.py
      python MarcaDeAgua.py

Despues de correr el programa se creará un archivo nuevo llamado 
"imagen_con_marca_agua.jepg", este archivo contendrá la imágen nueva con su respectiva
marca de agua.  


¿Qué hace nuestro programa?
El objetivo de este programa es poder poner una marca de agua a una imágen mediante
la ejecución de un programa en python . Dentro del código se puede cambiar la posición 
de la marca de agua y su tamaño, igual se pueden poner otras imágenes, sólo respetando 
el nombre y formato. 