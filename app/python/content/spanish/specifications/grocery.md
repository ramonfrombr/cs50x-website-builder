

# Lista de compras

Suponga que tiene la costumbre de hacer una lista de los artículos que necesita del supermercado.

En un archivo llamado `grocery.py`, implemente un programa que solicite al usuario los artículos, uno por línea, hasta que el usuario ingrese control-d (que es una forma común de terminar la entrada del usuario en un programa). Luego, muestre la lista de compras del usuario en mayúsculas, ordenada alfabéticamente por artículo, prefijando cada línea con el número de veces que el usuario ingresó ese artículo. No es necesario pluralizar los artículos. Trate la entrada del usuario sin distinguir entre mayúsculas y minúsculas.

Sugerencias

- Tenga en cuenta que puede detectar cuándo el usuario ha ingresado control-d capturando una [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) con un código como:

      try:
          item = input()
      except EOFError:
          ...

- Es probable que desee almacenar su lista de compras como un `dict`.
- Tenga en cuenta que un `dict` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), entre ellos `get`, y admite operaciones como:

      d[key]

  y

      if key in d:
          ...

  donde `d` es un `dict` y `key` es una `str`.

- Asegúrese de evitar o capturar cualquier [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## Demostración

## Antes de comenzar

Inicie sesión en [cs50.dev](https://cs50.dev/), haga clic en la ventana de su terminal y ejecute `cd` por sí solo. Debería ver que el indicador de su ventana de terminal se parece a esto:

    $

A continuación, ejecute

    mkdir grocery

para crear una carpeta llamada "grocery" en su espacio de códigos.

Luego, ejecute

    cd grocery

para cambiar de directorio a esa carpeta. Ahora debería ver el indicador de su terminal como `grocery/ $`. Ahora puede ejecutar

    code grocery.py

para crear un archivo llamado "grocery.py" donde escribirá su programa.

## Cómo probar

Así es como se puede probar su código manualmente:

- Ejecute su programa con `python grocery.py`. Escriba `mango` y presione Enter, luego escriba `strawberry` y presione Enter, seguido de control-d. Su programa debería mostrar:

      1 MANGO
      1 STRAWBERRY

- Ejecute su programa con `python grocery.py`. Escriba `milk` y presione Enter, luego escriba `milk` nuevamente y presione Enter, seguido de control-d. Su programa debería mostrar:

      2 MILK

- Ejecute su programa con `python grocery.py`. Escriba `tortilla` y presione Enter, luego escriba `sweet potato` y presione Enter, seguido de control-d. Su programa debería mostrar:

      1 SWEET POTATO
      1 TORTILLA

Puede ejecutar lo siguiente para verificar su código utilizando `check50`, un programa que CS50 utilizará para probar su código cuando lo envíe. ¡Pero asegúrese de probarlo usted mismo también!

    check50 cs50/problems/2022/python/grocery

¡Las caritas verdes significan que su programa ha pasado una prueba! Las caritas rojas indicarán que su programa ha producido algo inesperado. Visite la URL que `check50` muestra para ver la entrada que `check50` le entregó a su programa, qué salida esperaba y qué salida dio su programa.

## Cómo enviar

En su terminal, ejecute el siguiente comando para enviar su trabajo.

    submit50 cs50/problems/2022/python/grocery