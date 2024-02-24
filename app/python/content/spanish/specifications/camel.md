

# camelCase

![camel](1024px-CamelCase_new.svg.png)

Fuente: [en.wikipedia.org/wiki/Camel_case](https://en.wikipedia.org/wiki/Camel_case)

En algunos lenguajes, es común utilizar [camel case](https://en.wikipedia.org/wiki/Camel_case) (también conocido como "mixed case") para los nombres de las variables cuando estos nombres están compuestos por varias palabras, donde la primera letra de la primera palabra es minúscula, pero la primera letra de cada palabra siguiente es mayúscula. Por ejemplo, mientras que una variable para el nombre de un usuario podría ser llamada `name`, una variable para el primer nombre de un usuario podría ser llamada `firstName`, y una variable para el primer nombre preferido de un usuario (por ejemplo, apodo) podría ser llamada `preferredFirstName`.

Por otro lado, Python [recomienda](https://peps.python.org/pep-0008/#function-and-variable-names) [snake case](https://en.wikipedia.org/wiki/Snake_case), donde las palabras se separan utilizando guiones bajos (`_`), con todas las letras en minúscula. Por ejemplo, esas mismas variables se llamarían `name`, `first_name` y `preferred_first_name`, respectivamente, en Python.

En un archivo llamado `camel.py`, implementa un programa que solicita al usuario el nombre de una variable en camel case y muestra el nombre correspondiente en snake case. Se asume que la entrada del usuario estará en camel case.

Sugerencias:

- Recuerda que un `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Al igual que una lista (`list`), un `str` es "iterable", lo que significa que se puede iterar sobre cada uno de sus caracteres en un bucle. Por ejemplo, si `s` es un `str`, puedes imprimir cada uno de sus caracteres, uno por uno, con código como:

      for c in s:
          print(c, end="")

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir camel

para crear una carpeta llamada `camel` en tu espacio de código.

Luego ejecuta

    cd camel

para cambiar de directorio a esa carpeta. Ahora deberías ver el prompt de tu terminal como `camel/ $`. Ahora puedes ejecutar

    code camel.py

para crear un archivo llamado `camel.py` donde escribirás tu programa.

## Cómo Probar

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `python camel.py`. Escribe `name` y presiona Enter. Tu programa debería mostrar:

      name

- Ejecuta tu programa con `python camel.py`. Escribe `firstName` y presiona Enter. Tu programa debería mostrar:

      first_name

- Ejecuta tu programa con `python camel.py`. Escribe `preferredFirstName` y presiona Enter. Tu programa debería mostrar:

      preferred_first_name

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando envíes la tarea. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/camel

¡Las caritas felices verdes significan que tu programa ha pasado una prueba! Las caritas tristes rojas indicarán que tu programa mostró algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/camel