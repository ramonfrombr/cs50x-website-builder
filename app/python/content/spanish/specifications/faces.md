

# Haciendo Caras

Antes de los emoji, existían los [emoticonos](https://es.wikipedia.org/wiki/Anexo:Emoticonos), donde el texto como `:)` era una cara feliz y el texto como `:(` era una cara triste. ¡Hoy en día, los programas tienden a convertir los emoticonos automáticamente en emoji!

En un archivo llamado `faces.py`, implementa una función llamada `convert` que acepte una `str` como entrada y devuelva la misma entrada con cualquier `:)` convertido en 🙂 (conocido como una [cara ligeramente sonriente](https://emojipedia.org/slightly-smiling-face/)) y cualquier `:(` convertido en 🙁 (conocido como una [cara ligeramente fruncida](https://emojipedia.org/slightly-frowning-face/)). Todo el texto debe ser devuelto sin cambios.

Luego, en ese mismo archivo, implementa una función llamada `main` que solicite al usuario una entrada, llame a `convert` en esa entrada e imprima el resultado. Puedes, pero no es obligatorio, solicitar explícitamente al usuario ingresando una `str` propia como argumento de `input`. Asegúrate de llamar a `main` al final de tu archivo.

Pistas

- Recuerda que `input` devuelve una `str`, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que una `str` tiene varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Un emoji es simplemente un carácter, por lo que puedes citarlo como cualquier `str`, como `"😐"`. Y puedes copiar y pegar el emoji de esta página en tu propio código según sea necesario.

## Antes de empezar

Ejecuta `cd` por sí solo en la ventana de tu terminal. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego, ejecuta

    mkdir faces

para crear una carpeta llamada `faces` en tu espacio de trabajo de código.

A continuación, ejecuta

    cd faces

para cambiar de directorio a esa carpeta. Ahora deberías ver tu prompt de terminal como `faces/ $`. Ahora puedes ejecutar

    code faces.py

para crear un archivo llamado `faces.py` donde escribirás tu programa.

## Demostración

## Cómo probar

Así es como puedes probar tu código manualmente:

- Ejecuta tu programa con `python faces.py`. Escribe `Hola :)` y presiona Enter. Tu programa debería imprimir:

      Hola 🙂

- Ejecuta tu programa con `python faces.py`. Escribe `Adiós :(` y presiona Enter. Tu programa debería imprimir:

      Adiós 🙁

- Ejecuta tu programa con `python faces.py`. Escribe `Hola :) Adiós :(` y presiona Enter. Tu programa debería imprimir:

      Hola 🙂 Adiós 🙁

Puedes ejecutar lo siguiente para verificar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. Pero asegúrate de probarlo tú mismo también.

    check50 cs50/problems/2022/python/faces

¡Caritas verdes significan que tu programa ha pasado una prueba! Caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, qué salida esperaba y qué salida realmente dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/faces