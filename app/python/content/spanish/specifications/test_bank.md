

# De vuelta al banco

En un archivo llamado `bank.py`, reemplaza la implementación de [Home Federal Savings Bank](../../1/bank/) del [Problem Set 1](../../1/), reestructurando tu código de la siguiente manera: el parámetro `value` espera una cadena (`str`) como entrada y devuelve un entero (`int`), específicamente `0` si esa cadena comienza con "hello", `20` si esa cadena comienza con una "h" (pero no con "hello"), o `100` en cualquier otro caso, considerando la cadena sin distinguir mayúsculas y minúsculas. Puedes asumir que la cadena pasada a la función `value` no contendrá ningún espacio al inicio. Solo la función `main` debe llamar a `print`.

    def main():
        ...


    def value(saludo):
        ...


    if __name__ == "__main__":
        main()

Luego, en un archivo llamado `test_bank.py`, implementa **tres o más** funciones que prueben exhaustivamente tu implementación de `value`, cada una de las cuales debe comenzar con `test_` para que puedas ejecutar tus pruebas de la siguiente manera:

    pytest test_bank.py

Pistas

- Asegúrate de incluir

      import bank

  o

      from bank import value

  al principio de `test_bank.py` para poder llamar a `value` en tus pruebas.

- Ten cuidado de hacer `return`, no `print`, de un entero (`int`) en `value`. Solo `main` debe llamar a `print`.

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que la ruta de tu terminal se muestra como sigue:

    $

Luego ejecuta

    mkdir test_bank

para crear una carpeta llamada `test_bank` en tu espacio de trabajo.

Luego ejecuta

    cd test_bank

para cambiar al directorio de esa carpeta. Ahora deberías ver que tu terminal muestra `test_bank/ $` como prompt. Ahora puedes ejecutar

    code test_bank.py

para crear un archivo llamado `test_bank.py` donde escribirás tus pruebas.

## Cómo probar

Para probar tus pruebas, ejecuta `pytest test_bank.py`. Asegúrate de tener una copia del archivo `bank.py` en la misma carpeta. Intenta usar versiones correctas e incorrectas de `bank.py` para determinar qué tan bien tus pruebas detectan errores:

- Asegúrate de tener una versión correcta de `bank.py`. Ejecuta tus pruebas ejecutando `pytest test_bank.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la versión correcta de `bank.py`, cambiando los valores proporcionados para cada saludo. Por ejemplo, tu programa podría proporcionar incorrectamente $100 a un cliente saludado con "Hello" y $0 a un cliente saludado con "What's up"! Ahora, ejecuta tus pruebas ejecutando `pytest test_bank.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar lo siguiente para verificar tus pruebas utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. (¡Ahora hay pruebas para probar tus pruebas!). Asegúrate de probar tus pruebas tú mismo y determinar qué pruebas son necesarias para asegurar que `bank.py` sea evaluado exhaustivamente.

    check50 cs50/problems/2022/python/tests/bank

¡Caritas verdes sonrientes significan que tu programa ha pasado una prueba! Caritas rojas tristes indicarán que tu programa ha producido una salida inesperada. Visita la URL que `check50` muestra para ver la entrada que `check50` le dio a tu programa, la salida esperada y la salida real de tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/tests/bank