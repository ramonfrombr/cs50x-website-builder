

# Extensiones de archivo

Aunque a veces Windows y macOS las ocultan, la mayoría de los archivos tienen [extensiones de archivo](https://es.wikipedia.org/wiki/Extensi%C3%B3n_de_archivo), un sufijo que comienza con un punto (`.`) al final de su nombre. Por ejemplo, los nombres de archivo para [GIFs](https://es.wikipedia.org/wiki/GIF) terminan con `.gif`, y los nombres de archivo para [JPEGs](https://es.wikipedia.org/wiki/JPEG) terminan con `.jpg` o `.jpeg`. Cuando haces doble clic en un archivo para abrirlo, tu computadora utiliza su extensión de archivo para determinar qué programa se debe abrir.

En cambio, los navegadores web se basan en [tipos de medios](https://es.wikipedia.org/wiki/Tipo_de_medio), anteriormente conocidos como tipos MIME, para determinar cómo mostrar archivos que se encuentran en la web. Cuando descargas un archivo de un servidor web, ese servidor envía una [cabecera HTTP](https://es.wikipedia.org/wiki/Lista_de_campos_de_cabecera_HTTP), junto con el archivo en sí, indicando el tipo de medio del archivo. Por ejemplo, el tipo de medio para un GIF es `image/gif`, y el tipo de medio para un JPEG es `image/jpeg`. Para determinar el tipo de medio de un archivo, un servidor web generalmente examina la extensión del archivo, asignando uno al otro.

Consulta [developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types](https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) para conocer los tipos comunes.

En un archivo llamado `extensions.py`, implementa un programa que solicite al usuario el nombre de un archivo y luego muestre el tipo de medio de ese archivo si el nombre del archivo termina, sin distinguir mayúsculas de minúsculas, con alguno de estos sufijos:

- `.gif`
- `.jpg`
- `.jpeg`
- `.png`
- `.pdf`
- `.txt`
- `.zip`

Si el nombre del archivo termina con otro sufijo o no tiene sufijo, muestra `application/octet-stream` en su lugar, que es una opción predeterminada común.

Indicaciones:

- Recuerda que una `str` incluye varios métodos, consulta [docs.python.org/es/3/library/stdtypes.html#string-methods](https://docs.python.org/es/3/library/stdtypes.html#string-methods) para más información.

## Demostración

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta el comando `cd` sin nada más. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego, ejecuta

    mkdir extensions

para crear una carpeta llamada `extensions` en tu espacio de trabajo.

Después, ejecuta

    cd extensions

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de tu terminal como `extensions/ $`. Ahora puedes ejecutar

    code extensions.py

para crear un archivo llamado `extensions.py` donde escribirás tu programa.

## Cómo hacer las pruebas

Así es como puedes probar tu código de forma manual:

- Ejecuta tu programa con `python extensions.py`. Escribe `happy.jpg` y presiona Enter. Tu programa debería mostrar:

      image/jpeg

- Ejecuta tu programa con `python extensions.py`. Escribe `document.pdf` y presiona Enter. Tu programa debería mostrar:

      application/pdf

Asegúrate de probar cada uno de los otros formatos de archivo, varía las mayúsculas y minúsculas de tu entrada y agrega "accidentalmente" espacios antes y después de tu entrada antes de presionar Enter. Tu programa debería comportarse como se espera, sin importar las mayúsculas y minúsculas y sin tener en cuenta los espacios.

Puedes ejecutar el siguiente comando para revisar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de también probarlo por tu cuenta!

    check50 cs50/problems/2022/python/extensions

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa produce algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le ofreció a tu programa, qué salida esperaba y qué salida tu programa realmente dio.

## Cómo enviar tu trabajo

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/extensions