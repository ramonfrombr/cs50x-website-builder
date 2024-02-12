

# Solo configurando mi twttr

> solo configurando mi twttr
>
> — jack⚡️ (@jack) [21 de marzo de 2006](https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw)

Cuando envías mensajes de texto o tweets, no es raro abreviar palabras para ahorrar tiempo o espacio, como omitiendo las vocales, al igual que Twitter fue llamado originalmente _twttr_. En un archivo llamado `twttr.py`, implementa un programa que solicite al usuario un `str` de texto y luego imprima ese mismo texto pero sin ninguna vocal (A, E, I, O y U), ya sea que se ingresen en mayúsculas o minúsculas.

Sugerencias

- Recuerda que un `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Al igual que una `list`, un `str` es "iterable", lo que significa que puedes iterar sobre cada uno de sus caracteres en un bucle. Por ejemplo, si `s` es un `str`, puedes imprimir cada uno de sus caracteres de uno en uno con código como este:

      for c in s:
          print(c, end="")

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece a lo siguiente:

    $

Luego ejecuta

    mkdir twttr

para crear una carpeta llamada `twttr` en tu espacio de código.

Luego ejecuta

    cd twttr

para cambiar al directorio de esa carpeta. Ahora deberías ver que el indicador de tu terminal es `twttr/ $`. Ahora puedes ejecutar

    code twttr.py

para crear un archivo llamado `twttr.py` donde escribirás tu programa.

## Cómo probar

Aquí te mostramos cómo probar tu código manualmente:

- Ejecuta tu programa con `python twttr.py`. Escribe `Twitter` y presiona Enter. Tu programa debería imprimir:

      Twttr

- Ejecuta tu programa con `python twttr.py`. Escribe `¿Cómo te llamas?` y presiona Enter. Tu programa debería imprimir:

      ¿Cóm t llms?

- Ejecuta tu programa con `python twttr.py`. Escribe `CS50` y presiona Enter. Tu programa debería imprimir:

      CS50

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/twttr

¡Caritas sonrientes verdes significan que tu programa ha pasado una prueba! Caritas tristes rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, qué salida esperaba y qué salida obtuvo tu programa en realidad.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/twttr