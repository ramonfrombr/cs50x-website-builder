

# Voz de Interior

ESCRIBIR TODO EN MAYÚSCULAS ES COMO GRITAR.

Es mejor usar tu "voz de interior" a veces, escribiendo completamente en minúsculas.

En un archivo llamado `indoor.py`, implementa un programa en Python que solicite al usuario una entrada y luego imprima esa misma entrada en minúsculas. La puntuación y los espacios en blanco deben imprimirse sin cambios. Eres bienvenido, pero no es necesario, para solicitar explícitamente al usuario, al pasar un `str` propio como argumento a `input`.

Pistas

- Recuerda que `input` devuelve una `str`, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que un `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Antes de Comenzar

Ejecuta `cd` solo en la ventana de tu terminal. Deberías encontrar que el indicador de tu ventana de terminal se parece a lo siguiente:

    $

A continuación, ejecuta

    mkdir indoor

para crear una carpeta llamada `indoor` en tu espacio de código.

Luego ejecuta

    cd indoor

para cambiar de directorio a esa carpeta. Ahora deberías ver tu indicador de terminal como `indoor/ $`. Ahora puedes ejecutar el comando

    code indoor.py

para crear un archivo llamado `indoor.py` donde escribirás tu programa.

## Demo

## Cómo Probar

Aquí tienes cómo probar tu código manualmente. En el indicador `indoor/ $` de tu terminal:

- Ejecuta tu programa con `python indoor.py`. Escribe `HELLO` y presiona Enter. Tu programa debería imprimir `hello`.
- Ejecuta tu programa con `python indoor.py`. Escribe `THIS IS CS50` y presiona Enter. Tu programa debería imprimir `this is cs50`.
- Ejecuta tu programa con `python indoor.py`. Escribe `50` y presiona Enter. Tu programa debería imprimir `50`.

Si encuentras un error que dice que tu archivo no se puede abrir, retrocede tus pasos para asegurarte de que estás dentro de tu carpeta `indoor` y has guardado tu archivo `indoor.py` allí. ¿Recuerdas cómo?

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/indoor

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/indoor