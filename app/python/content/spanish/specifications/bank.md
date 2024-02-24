

# Home Federal Savings Bank

En [la temporada 7, episodio 24](https://en.wikipedia.org/wiki/The_Invitations) de [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visita un banco que promete dar $100 a cualquiera que no sea saludado con un "hola". En cambio, Kramer es saludado con un "hey", lo cual él insiste en que no es un "hola", y por eso pide los $100. El gerente del banco propone un compromiso: "Recibiste un saludo que empieza con una 'h', ¿qué te parece $20?" Kramer acepta.

En un archivo llamado `bank.py`, implementa un programa que solicite al usuario un saludo. Si el saludo empieza con "hola", muestra `$0`. Si el saludo empieza con una "h" (pero no con "hola"), muestra `$20`. De lo contrario, muestra `$100`. Ignora cualquier espacio en blanco al principio del saludo del usuario y trata el saludo del usuario sin tener en cuenta las mayúsculas y minúsculas.

Sugerencias

- Recuerda que un `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Asegúrate de dar $0 no solo para "hola" sino también para "hola allí", "hola, Newman", y similares.

## Demo

## Antes de Comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego ejecuta

    mkdir bank

para crear una carpeta llamada `bank` en tu espacio de codificación.

A continuación, ejecuta

    cd bank

para cambiar de directorio a esa carpeta. Ahora deberías ver tu indicador de terminal como `bank/ $`. Ahora puedes ejecutar

    code bank.py

para crear un archivo llamado `bank.py` donde escribirás tu programa.

## Cómo Probar

Aquí te mostramos cómo probar tu código manualmente:

- Ejecuta tu programa con `python bank.py`. Escribe `Hola` y presiona Enter. Tu programa debería mostrar:

      $0

- Ejecuta tu programa con `python bank.py`. Escribe `Hola, Newman` y presiona Enter. Tu programa debería mostrar:

      $0

- Ejecuta tu programa con `python bank.py`. Escribe `¿Cómo estás?` y presiona Enter. Tu programa debería mostrar:

      $20

- Ejecuta tu programa con `python bank.py`. Escribe `¿Qué está pasando?` y presiona Enter. Tu programa debería mostrar:

      $100

Puedes ejecutar lo siguiente para verificar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/bank

¡Los emoticonos verdes significan que tu programa ha pasado una prueba! Los emoticonos rojos indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/bank