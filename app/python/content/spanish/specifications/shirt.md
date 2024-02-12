

# CS50 P-Shirt

![Camiseta CS50](took.png)

Después de terminar el propio curso CS50, tradicionalmente los estudiantes en el campus de Harvard reciben su propia camiseta [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt). No es necesario comprar una en línea, ¿pero te gustaría probarte una virtualmente?

En un archivo llamado `shirt.py`, implementa un programa que espere exactamente dos argumentos de línea de comandos:

- en `sys.argv[1]`, el nombre (o la ruta) de un archivo JPEG o PNG para leer (es decir, abrir) como entrada
- en `sys.argv[2]`, el nombre (o la ruta) de un archivo JPEG o PNG para escribir (es decir, guardar) como salida

El programa debe luego superponer [shirt.png](shirt.png) (que tiene un fondo transparente) sobre la entrada después de redimensionar y recortar la entrada para que tenga el mismo tamaño, guardando el resultado como salida.

Abre la entrada con `Image.open`, según [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), redimensiona y recorta la entrada con `ImageOps.fit`, según [pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit), utilizando los valores predeterminados para `method`, `bleed` y `centering`, superpone la camiseta con `Image.paste`, según [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste), y guarda el resultado con `Image.save`, según [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

El programa deberá salir mediante `sys.exit` en los siguientes casos:

- si el usuario no especifica exactamente dos argumentos de línea de comandos,
- si los nombres de entrada y salida no terminan en `.jpg`, `.jpeg` o `.png`, sin distinguir entre mayúsculas y minúsculas,
- si el nombre de la entrada no tiene la misma extensión que el nombre de la salida, o
- si la entrada especificada no existe.

Supón que la entrada será una foto de alguien posando de la manera correcta, como [estas demostraciones](#demos), de modo que, cuando se redimensionen y recorten, la camiseta parezca ajustarse perfectamente.

Si quieres ejecutar tu programa en una foto tuya, primero arrastra la foto a la exploradora de archivos de VS Code, en la misma carpeta que `shirt.py`. No es necesario enviar ninguna foto con tu código. Pero, si quieres, tienes la opción (pero no la obligación) de compartir una foto tuya usando tu camiseta virtual en cualquiera de [las comunidades de CS50](https://cs50.harvard.edu/python/communities)!

Pistas

- Ten en cuenta que se puede determinar la extensión de un archivo con `os.path.splitext`, según [docs.python.org/3/library/os.path.html#os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext).
- Ten en cuenta que `open` puede generar un `FileNotFoundError`, según [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Ten en cuenta que el paquete `Pillow` viene con bastantes clases y métodos, según [pypi.org/project/Pillow](https://pypi.org/project/Pillow/). Podrías encontrar útiles su [manual](https://pillow.readthedocs.io/en/stable/handbook/) y su [referencia](https://pillow.readthedocs.io/en/stable/reference/). Puedes instalar el paquete con:

      pip install Pillow

  Puedes abrir una imagen (por ejemplo, `shirt.png`) con código como este:

      shirt = Image.open("shirt.png")

  Puedes obtener el ancho y el alto, respectivamente, de esa imagen como una tupla con código como este:

      size = shirt.size

  Y puedes superponer esa imagen sobre otra (por ejemplo, `photo`) con código como este:

      photo.paste(shirt, shirt)

  donde el primer `shirt` representa la imagen para superponer y el segundo `shirt` representa una "máscara" que indica qué píxeles en `photo` actualizar.

- Ten en cuenta que puedes abrir una imagen (por ejemplo, `shirt.png`) en VS Code ejecutando

      code shirt.png

  o haciendo doble clic en su icono en la exploradora de archivos de VS Code.

## Demostración

### Antes

[![antes](before1.jpg)](before1.jpg) [![antes](before2.jpg)](before2.jpg) [![antes](before3.jpg)](before3.jpg)

### Después

![después](after1.jpg) ![después](after2.jpg) ![después](after3.jpg)

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta el comando `cd` por sí mismo. Deberías ver que el indicador de tu terminal se parece a esto:

    $

A continuación, ejecuta

    mkdir shirt

para crear una carpeta llamada `shirt` en tu espacio de código.

Luego ejecuta

    cd shirt

para cambiar a ese directorio. Ahora deberías ver el indicador de tu terminal como `shirt/ $`. Ahora puedes ejecutar

    code shirt.py

para crear un archivo llamado `shirt.py` donde escribirás tu programa. Asegúrate de ejecutar

    wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png

para descargar [shirt.png](shirt.png). También asegúrate de ejecutar

    wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip

para descargar [muppets.zip](muppets.zip) en tu carpeta. Puedes ejecutar

    unzip muppets.zip

para extraer una colección de fotos de los Muppets.

## Cómo Probar

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `python shirt.py`. Tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Too few command-line arguments

- Asegúrate de descargar [muppets.zip](muppets.zip) y extraer una colección de fotos de los Muppets usando `unzip muppets.zip`. Ejecuta tu programa con `python shirt.py before1.jpg before2.jpg before3.jpg`. Tu programa debería mostrar:

      Too many command-line arguments

- Ejecuta tu programa con `python shirt.py before1.jpg invalid_format.bmp`. Tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Invalid output

- Ejecuta tu programa con `python shirt.py before1.jpg after1.png`. Tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Input and output have different extensions

- Ejecuta tu programa con `python shirt.py non_existent_image.jpg after1.jpg`. Tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Input does not exist

- Ejecuta tu programa con `python shirt.py before1.jpg after1.jpg`. Suponiendo que hayas descargado y descomprimido [muppets.zip](muppets.zip), tu programa debería crear una imagen como esta:
  ![después](after1.jpg)

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/shirt

¡Las caritas sonrientes verdes significan que tu programa ha pasado una prueba! Las muecas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/shirt