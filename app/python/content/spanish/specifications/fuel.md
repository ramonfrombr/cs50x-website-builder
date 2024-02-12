

# Indicador de combustible

![indicador de combustible](51-hsJaA+SL._SL1000_.jpg)  
Fuente: [amazon.com/dp/B09C4FL56G](https://www.amazon.com/dp/B09C4FL56G)

Los indicadores de combustible indican, a menudo con fracciones, cuánto combustible hay en un tanque. Por ejemplo, 1/4 indica que un tanque está lleno en un 25%, 1/2 indica que un tanque está lleno en un 50%, y 3/4 indica que un tanque está lleno en un 75%.

En un archivo llamado `fuel.py`, implemente un programa que solicite al usuario una fracción, formateada como `X/Y`, donde tanto `X` como `Y` son enteros, y luego muestre como resultado, como un porcentaje redondeado al entero más cercano, cuánto combustible hay en el tanque. Sin embargo, si queda un 1% o menos, muestre `E` en su lugar para indicar que el tanque está prácticamente vacío. Y si queda un 99% o más, muestre `F` en su lugar para indicar que el tanque está prácticamente lleno.

Si, sin embargo, `X` o `Y` no es un entero, `X` es mayor que `Y`, o `Y` es `0`, solicite al usuario de nuevo. (No es necesario que `Y` sea `4`.) Asegúrese de capturar cualquier excepción como [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) o [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

Pistas

- Recuerde que una `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluido `split`.
- Tenga en cuenta que puede manejar dos excepciones por separado con código como:

      try:
          ...
      except ValueError:
          ...
      except ZeroDivisionError:
          ...

  O puede manejar dos excepciones juntas con código como:

      try:
          ...
      except (ValueError, ZeroDivisionError):
          ...

## Demostración

## Antes de comenzar

Inicie sesión en [cs50.dev](https://cs50.dev/), haga clic en la ventana de su terminal y ejecute `cd` por sí solo. Debería ver que el indicador de su ventana de terminal se parece al siguiente:

    $

A continuación, ejecute

    mkdir fuel

para crear una carpeta llamada `fuel` en su espacio de código.

Luego, ejecute

    cd fuel

para cambiar al directorio de esa carpeta. Ahora debería ver el indicador de su terminal como `fuel/ $`. Ahora puede ejecutar

    code fuel.py

para crear un archivo llamado `fuel.py` donde escribirá su programa.

## Cómo probar

Así es cómo probar su código manualmente:

- Ejecute su programa con `python fuel.py`. Escriba `3/4` y presione Enter. Su programa debería mostrar:

      75%

- Ejecute su programa con `python fuel.py`. Escriba `1/4` y presione Enter. Su programa debería mostrar:

      25%

- Ejecute su programa con `python fuel.py`. Escriba `4/4` y presione Enter. Su programa debería mostrar:

      F

- Ejecute su programa con `python fuel.py`. Escriba `0/4` y presione Enter. Su programa debería mostrar:

      E

- Ejecute su programa con `python fuel.py`. Escriba `4/0` y presione Enter. Su programa debería manejar un [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) y solicitar al usuario de nuevo.
- Ejecute su programa con `python fuel.py`. Escriba `three/four` y presione Enter. Su programa debería manejar un [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) y solicitar al usuario de nuevo.
- Ejecute su programa con `python fuel.py`. Escriba `1.5/3` y presione Enter. Su programa debería manejar un [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) y solicitar al usuario de nuevo.
- Ejecute su programa con `python fuel.py`. Escriba `5/4` y presione Enter. Su programa debería solicitar al usuario de nuevo.

Puede ejecutar el siguiente comando para verificar su código usando `check50`, un programa que CS50 utilizará para probar su código cuando lo envíe. ¡Pero asegúrese de probarlo usted mismo también!

    check50 cs50/problems/2022/python/fuel

¡Las caritas verdes significan que su programa ha superado una prueba! Las caritas rojas indicarán que su programa ha producido algo inesperado. Visite la URL que `check50` muestra para ver la entrada que `check50` proporcionó a su programa, la salida que esperaba y la salida que su programa realmente dio.

## Cómo enviar

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2022/python/fuel