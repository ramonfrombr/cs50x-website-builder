

# Interprete de Matemáticas

Python ya tiene soporte para matemáticas, de manera que _tú_ puedes escribir código para sumar, restar, multiplicar o dividir valores e incluso variables. Pero vamos a escribir un programa que permita a los _usuarios_ hacer matemáticas, incluso sin saber Python.

En un archivo llamado `interpreter.py`, implementa un programa que solicite al usuario una expresión aritmética y luego calcule y muestre el resultado como un valor de punto flotante formateado a un decimal. Supón que la entrada del usuario tendrá el formato `x y z`, con un espacio entre `x` e `y` y un espacio entre `y` y `z`, donde:

- `x` es un número entero
- `y` es `+`, `-`, `*` o `/`
- `z` es un número entero

Por ejemplo, si el usuario ingresa `1 + 1`, tu programa deberá mostrar `2.0`. Supón que, si `y` es `/`, entonces `z` no será `0`.

Ten en cuenta que, así como `python` en sí es un intérprete para Python, tu `interpreter.py` será un intérprete para matemáticas.

Sugerencias

Recuerda que una `str` tiene muchos métodos, según [docs.python.org/es/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluyendo `split`, que separa una `str` en una secuencia de valores, todos los cuales se pueden asignar a variables al mismo tiempo. Por ejemplo, si `expression` es una `str` como `1 + 1`, entonces

    x, y, z = expression.split(" ")

asignará `1` a `x`, `+` a `y` y `1` a `z`.

## Demostración

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu terminal se parece al siguiente:

    $

Luego ejecuta

    mkdir interpreter

para crear una carpeta llamada `interpreter` en tu espacio de código.

Después ejecuta

    cd interpreter

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de tu terminal como `interpreter/ $`. Ahora puedes ejecutar

    code interpreter.py

para crear un archivo llamado `interpreter.py` donde escribirás tu programa.

## Cómo Probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python interpreter.py`. Escribe `1 + 1` y presiona Enter. Tu programa deberá mostrar:

      2.0

- Ejecuta tu programa con `python interpreter.py`. Escribe `2 - 3` y presiona Enter. Tu programa deberá mostrar:

      -1.0

- Ejecuta tu programa con `python interpreter.py`. Escribe `2 * 2` y presiona Enter. Tu programa deberá mostrar:

      4.0

- Ejecuta tu programa con `python interpreter.py`. Escribe `50 / 5` y presiona Enter. Tu programa deberá mostrar:

      10.0

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/interpreter

¡Caritas verdes significan que tu programa ha pasado una prueba! Caritas rojas indicarán que tu programa mostró algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` entregó a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/interpreter