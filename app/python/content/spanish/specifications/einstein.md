

# Einstein

Incluso si no has estudiado física (recientemente o nunca), es posible que hayas escuchado que \\(E = mc^2\\), donde \\(E\\) representa energía (medida en Joules), \\(m\\) representa masa (medida en kilogramos) y \\(c\\) representa la velocidad de la luz (medida aproximadamente como 300000000 metros por segundo), según [Albert Einstein](https://es.wikipedia.org/wiki/Albert_Einstein) y otros. Básicamente, la fórmula significa que la masa y la energía son equivalentes.

En un archivo llamado `einstein.py`, implementa un programa en Python que solicite al usuario la masa como un número entero (en kilogramos) y luego muestre el número equivalente de Joules como un número entero. Supongamos que el usuario ingresará un número entero.

Sugerencias:

- Recuerda que `input` devuelve una cadena (`str`), según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que `int` puede convertir una cadena (`str`) en un entero (`int`), según [docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int).
- Recuerda que Python viene con varias funciones integradas, según [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir einstein

para crear una carpeta llamada `einstein` en tu espacio de trabajo.

Luego ejecuta

    cd einstein

para cambiar de directorio a esa carpeta. Ahora deberías ver el indicador de tu terminal como `einstein/ $`. Ahora puedes ejecutar

    code einstein.py

para crear un archivo llamado `einstein.py` donde escribirás tu programa.

## Cómo Probar

Así es como puedes probar tu código manualmente:

- Ejecuta tu programa con `python einstein.py`. Escribe `1` y presiona Enter. Tu programa debería mostrar:

      90000000000000000

- Ejecuta tu programa con `python einstein.py`. Escribe `14` y presiona Enter. Tu programa debería mostrar:

      1260000000000000000

- Ejecuta tu programa con `python einstein.py`. Escribe `50` y presiona Enter. Tu programa debería mostrar:

      4500000000000000000

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/einstein

¡Las caritas verdes significan que tu programa ha superado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, qué salida esperaba y qué salida realmente dio tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/einstein