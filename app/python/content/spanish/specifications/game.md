

# Juego de Adivinanzas

Estoy pensando en un número entre 1 y 100...

¿Cuál es?

¡Es 50! ¿Pero qué pasaría si fuera más aleatorio?

En un archivo llamado `game.py`, implemente un programa que:

- Solicite al usuario un nivel, \\(n\\). Si el usuario no ingresa un entero positivo, el programa debe solicitar nuevamente.
- Genere aleatoriamente un número entero entre 1 y \\(n\\), inclusive, utilizando el módulo `random`.
- Solicite al usuario adivinar ese número. Si la suposición no es un entero positivo, el programa debe solicitar al usuario nuevamente.
  - Si la suposición es menor que ese número, el programa debe mostrar `¡Demasiado pequeño!` y solicitar al usuario nuevamente.
  - Si la suposición es mayor que ese número, el programa debe mostrar `¡Demasiado grande!` y solicitar al usuario nuevamente.
  - Si la suposición es igual a ese número, el programa debe mostrar `¡Correcto!` y salir.

Consejos

- Tenga en cuenta que el módulo `random` viene con varias funciones, según [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demostración

## Antes de comenzar

Inicie sesión en [cs50.dev](https://cs50.dev/), haga clic en la ventana de la terminal y ejecute `cd` por sí solo. Verá que el indicador de la ventana de la terminal se parece al siguiente:

    $

A continuación, ejecute

    mkdir game

para crear una carpeta llamada `game` en su espacio de códigos.

Luego ejecute

    cd game

para cambiar de directorio a esa carpeta. Ahora debería ver su indicador de terminal como `game/ $`. Ahora puede ejecutar

    code game.py

para crear un archivo llamado `game.py` donde escribirá su programa.

## Cómo probar

Aquí está cómo probar su código manualmente:

- Ejecute su programa con `python game.py`. Escriba `cat` en un mensaje que diga `Nivel:` y presione Enter. Su programa debería solicitarle nuevamente:

      Nivel:

- Ejecute su programa con `python game.py`. Escriba `-1` en un mensaje que diga `Nivel:` y presione Enter. Su programa debería solicitarle nuevamente:

      Nivel:

- Ejecute su programa con `python game.py`. Escriba `10` en un mensaje que diga `Nivel:` y presione Enter. Su programa ahora debería estar listo para aceptar suposiciones:

      Suposición:

- Ejecute su programa con `python game.py`. Escriba `10` en un mensaje que diga `Nivel:` y presione Enter. Luego escriba `cat`. Su programa debería solicitarle nuevamente:

      Suposición:

- Ejecute su programa con `python game.py`. Escriba `10` en un mensaje que diga `Nivel:` y presione Enter. Luego escriba `-1`. Su programa debería solicitarle nuevamente:

      Suposición:

- Ejecute su programa con `python game.py`. Escriba `1` en un mensaje que diga `Nivel:` y presione Enter. Luego escriba `1`. Su programa debería mostrar:

      ¡Correcto!

  ¡Solo hay un número posible que podría ser la respuesta!

- Ejecute su programa con `python game.py`. Escriba `10` en un mensaje que diga `Nivel:` y presione Enter. Luego escriba `100`. Su programa debería mostrar:

      ¡Demasiado grande!

  Parece que estás adivinando fuera del rango que especificaste.

- Ejecute su programa con `python game.py`. Escriba `10000` en un mensaje que diga `Nivel:` y presione Enter. Luego escriba `1`. Su programa debería mostrar:

      ¡Demasiado pequeño!

  Lo más probable es que así sea: podrías tener suerte y ver `¡Correcto!`. Pero sería extraño ver `¡Correcto!` cada vez. Y definitivamente no deberías ver `¡Demasiado grande!`.

Puede ejecutar el siguiente comando para verificar su código utilizando `check50`, un programa que CS50 utilizará para probar su código cuando lo envíe. ¡Pero asegúrese de probarlo usted mismo también!

    check50 cs50/problems/2022/python/game

¡Las caritas verdes significan que su programa ha superado una prueba! Las caritas rojas indicarán que su programa produjo algo inesperado. Visite la URL que `check50` muestra para ver la entrada que `check50` proporcionó a su programa, la salida que esperaba y la salida que su programa realmente dio.

## Cómo enviar

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2022/python/game