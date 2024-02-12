

# Taquería de Felipe

¡Ten en cuenta que, a partir del [2023-10-25T11:59:00-04:00](https://time.cs50.io/20231025T115900-0400), ¡los precios de Felipe's han sido actualizados!

![Taquería de Felipe](felipes-logo.png)

Uno de los lugares más populares para comer en [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) es la [Taquería de Felipe](https://www.felipesboston.com/), que ofrece un [menú](https://www.felipesboston.com/menu) de platos principales, según el `dict` a continuación, donde el valor de cada clave es un precio en dólares:

    {
        "Taco Baja": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Ensalada de Tortilla": 8.00
    }

En un archivo llamado `taqueria.py`, implementa un programa que permita al usuario realizar un pedido, solicitándole los elementos, uno por línea, hasta que el usuario ingrese control-d (que es una forma común de finalizar la entrada a un programa). Después de cada elemento ingresado, muestra el costo total de todos los elementos ingresados hasta el momento, precedido de un signo de dólar (`$`) y formateado con dos decimales. Trata la entrada del usuario sin distinguir mayúsculas y minúsculas. Ignora cualquier entrada que no sea un elemento. Asume que cada elemento del menú estará en mayúscula y minúscula.

Sugerencias:

- Ten en cuenta que puedes detectar cuando el usuario haya ingresado control-d capturando una excepción [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) con el siguiente código:

      try:
          item = input()
      except EOFError:
          ...

  Es posible que desees imprimir una nueva línea para que el cursor del usuario (y el siguiente indicador) no permanezca en la misma línea que el indicador de tu propio programa.

- No es necesario ingresar Enter después de control-d, por lo que el cursor del usuario (y el siguiente indicador) puede permanecer en la misma línea que el indicador de tu propio programa. ¡Puedes mover el cursor del usuario a una nueva línea imprimiendo `\n` tú mismo!
- Ten en cuenta que un `dict` tiene varios métodos, según [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), incluidos `get`, y admite operaciones como:

      d[key]

  y

      if key in d:
          ...

  donde `d` es un `dict` y `key` es una cadena (`str`).

- Asegúrate de evitar o capturar cualquier [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## Demo

## Antes de Comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta el comando `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego ejecuta

    mkdir taqueria

para crear una carpeta llamada `taqueria` en tu entorno de desarrollo.

Después ejecuta

    cd taqueria

para cambiar de directorio a esa carpeta. Ahora deberías ver el indicador de tu terminal como `taqueria/ $`. Ahora puedes ejecutar

    code taqueria.py

para crear un archivo llamado `taqueria.py` donde escribirás tu programa.

## Cómo Probar

Aquí te explicamos cómo probar tu código manualmente:

- Ejecuta tu programa con `python taqueria.py`. Escribe `Taco` y presiona Enter, luego escribe `Taco` nuevamente y presiona Enter. Tu programa debería mostrar:

      Total: $6.00

  y continuar solicitando al usuario hasta que ingrese control-d.

- Ejecuta tu programa con `python taqueria.py`. Escribe `Taco Baja` y presiona Enter, luego escribe `Ensalada de Tortilla` y presiona Enter. Tu programa debería mostrar:

      Total: $12.25

  y continuar solicitando al usuario hasta que ingrese control-d.

- Ejecuta tu programa con `python taqueria.py`. Escribe `Hamburguesa` y presiona Enter. Tu programa debería volver a solicitar al usuario.

Asegúrate de probar con otros alimentos y variar las mayúsculas y minúsculas de tu entrada. Tu programa debería comportarse como se espera, sin distinguir mayúsculas y minúsculas.

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo por ti mismo también!

    check50 cs50/problems/2022/python/taqueria

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` entregó a tu programa, la salida esperada y la salida que tu programa realmente produjo.

## Cómo Enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo:

    submit50 cs50/problems/2022/python/taqueria