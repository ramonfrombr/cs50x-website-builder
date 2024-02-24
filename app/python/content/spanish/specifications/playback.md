

# Velocidad de reproducción

Algunas personas tienen el hábito de hablar rápidamente durante sus conferencias, y sería bueno poder ralentizarlos, como la velocidad de reproducción de 0.75 en YouTube, o incluso haciendo que hagan pausas entre palabras.

En un archivo llamado `playback.py`, implementa un programa en Python que solicite al usuario una entrada y luego muestre esa misma entrada, reemplazando cada espacio con `...` (es decir, tres puntos).

Sugerencias

- Recuerda que `input` devuelve una `str`, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que una `str` cuenta con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí mismo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego, ejecuta

    mkdir playback

para crear una carpeta llamada `playback` en tu espacio de codificación.

Después ejecuta

    cd playback

para cambiar al directorio de esa carpeta. Ahora deberías ver que tu indicador de terminal muestra `playback/ $`. Ahora puedes ejecutar

    code playback.py

para crear un archivo llamado `playback.py` donde escribirás tu programa.

## Cómo probar

Aquí te mostramos cómo probar tu código manualmente:

- Ejecuta tu programa con `python playback.py`. Escribe `This is CS50` y presiona Enter. Tu programa debería mostrar:

      This...is...CS50

- Ejecuta tu programa con `python playback.py`. Escribe `This is our week on functions` y presiona Enter. Tu programa debería mostrar:

      This...is...our...week...on...functions

- Ejecuta tu programa con `python playback.py`. Escribe `Let's implement a function called hello` y presiona Enter. Tu programa debería mostrar:

      Let's...implement...a...function...called...hello

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo por ti mismo también!

    check50 cs50/problems/2022/python/playback

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, la salida que se esperaba y la salida real que dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/playback