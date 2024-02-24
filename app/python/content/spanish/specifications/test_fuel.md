

# Recarga de combustible

En un archivo llamado `fuel.py`, reimplementa [Fuel Gauge](../../3/fuel/) del [Conjunto de Problemas 3](../../3/), reestructurando tu código de la siguiente manera:

- `convert` espera una cadena `str` en formato `X/Y` como entrada, donde `X` e `Y` son enteros, y devuelve esa fracción como un porcentaje redondeado al entero más cercano entre `0` y `100`, ambos inclusive. Si `X` e / o `Y` no son enteros, o si `X` es mayor que `Y`, entonces `convert` debe levantar una `ValueError`. Si `Y` es `0`, entonces `convert` debe levantar un `ZeroDivisionError`.
- `gauge` espera un entero `int` y devuelve una cadena `str` que es:

  - `"E"` si ese entero es menor o igual a `1`,
  - `"F"` si ese entero es mayor o igual a `99`,
  - y `"Z%"` en cualquier otro caso, donde `Z` es ese mismo entero.

  def main():
  ...

  def convert(fraccion):
  ...

  def gauge(porcentaje):
  ...

  if **name** == "**main**":
  main()

Luego, en un archivo llamado `test_fuel.py`, implementa **dos o más** funciones que prueben exhaustivamente tus implementaciones de `convert` y `gauge`, cada una de las cuales debe comenzar con `test_` para que puedas ejecutar tus pruebas con:

    pytest test_fuel.py

Pistas

- Asegúrate de incluir

      import fuel

  o

      from fuel import convert, gauge

  en la parte superior de `test_fuel.py` para que puedas llamar a `convert` y `gauge` en tus pruebas.

- Asegúrate de `return`, no `print`, un `int` en `convert` y una `str` en `gauge`. Solo `main` debe llamar a `print`.
- Ten en cuenta que puedes comprobar con `pytest` si una función ha generado una excepción, según [docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions](https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions).

## Antes de empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que la indicación de tu ventana de terminal se asemeja a lo siguiente:

    $

A continuación, ejecuta

    mkdir test_fuel

para crear una carpeta llamada `test_fuel` en tu espacio de código.

Luego ejecuta

    cd test_fuel

para cambiar de directorio a esa carpeta. Ahora deberías ver la indicación de tu terminal como `test_fuel/ $`. Ahora puedes ejecutar

    code test_fuel.py

para crear un archivo llamado `test_fuel.py` donde escribirás tus pruebas.

## Cómo probar

Para probar tus pruebas, ejecuta `pytest test_fuel.py`. Asegúrate de tener una copia del archivo `fuel.py` en la misma carpeta. Intenta usar versiones correctas e incorrectas de `fuel.py` para determinar qué tan bien tus pruebas encuentran errores:

- Asegúrate de tener una versión correcta de `fuel.py`. Ejecuta tus pruebas ejecutando `pytest test_fuel.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la versión correcta de `fuel.py`, cambiando los valores de retorno de `convert`. Por ejemplo, tu programa podría devolver erróneamente una cadena (`str`) en lugar de un entero (`int`). Ejecuta tus pruebas ejecutando `pytest test_fuel.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.
- De manera similar, modifica la versión correcta de `fuel.py`, cambiando los valores de retorno de `gauge`. Por ejemplo, tu programa podría omitir erróneamente un `%` en la cadena resultante (`str`). Ejecuta tus pruebas ejecutando `pytest test_fuel.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar lo siguiente para comprobar tus pruebas usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. (¡Ahora hay pruebas para probar tus pruebas!). Asegúrate de probar tus pruebas personalmente y determinar qué pruebas son necesarias para asegurarte de que `fuel.py` sea revisado exhaustivamente.

    check50 cs50/problems/2022/python/tests/fuel

¡Las caritas de color verde significan que tu programa ha pasado una prueba! Las caritas de color rojo indicarán que tu programa ha dado una salida inesperada. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, qué salida se esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/tests/fuel