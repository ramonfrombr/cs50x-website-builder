

# Solicitando de nuevo una placa personalizada

En un archivo llamado `plates.py`, vuelve a implementar [Vanity Plates](../../2/plates/) del [Problem Set 2](../../2/), reestructurando tu código de la siguiente manera, en la que `is_valid` todavía espera una `str` como entrada y devuelve `True` si esa `str` cumple con todos los requisitos y `False` si no lo hace, pero `main` solo se llama si el valor de `__name__` es `"__main__"`:

    def main():
        ...


    def is_valid(s):
        ...


    if __name__ == "__main__":
        main()

Luego, en un archivo llamado `test_plates.py`, implementa **cuatro o más** funciones que prueben exhaustivamente tu implementación de `is_valid`, cada una de cuyos nombres debe comenzar con `test_` para que puedas ejecutar tus pruebas usando:

    pytest test_plates.py

Sugerencias

- Asegúrate de incluir

      import plates

  o

      from plates import is_valid

  en la parte superior de `test_plates.py` para que puedas llamar a `is_valid` en tus pruebas.

- Ten cuidado de `return`ar, no imprimir, un `bool` en `is_valid`. Solo `main` debe llamar a `print`.

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana del terminal y ejecuta `cd` por sí solo. Deberías ver que la línea de comandos en tu ventana del terminal se parece a esto:

    $

A continuación, ejecuta

    mkdir test_plates

para crear una carpeta llamada `test_plates` en tu espacio de trabajo.

Luego ejecuta

    cd test_plates

para cambiar de directorio a esa carpeta. Ahora deberías ver el indicador de la línea de comandos como `test_plates/ $`. Ahora puedes ejecutar

    code test_plates.py

para crear un archivo llamado `test_plates.py` donde escribirás tus pruebas.

## Cómo probar

Para probar tus pruebas, ejecuta `pytest test_plates.py`. Asegúrate de tener una copia de un archivo `plates.py` en la misma carpeta. Intenta usar versiones correctas e incorrectas de `plates.py` para determinar qué tan bien tus pruebas detectan los errores:

- Asegúrate de tener una versión correcta de `plates.py`. Ejecuta tus pruebas ejecutando `pytest test_plates.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la versión correcta de `plates.py`, eliminando quizás algunas de sus restricciones. ¡Tu programa podría imprimir erróneamente "Válido" para una placa de cualquier longitud! Ejecuta tus pruebas ejecutando `pytest test_plates.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar lo siguiente para verificar tus pruebas usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. (¡Ahora hay pruebas para probar tus pruebas!). Asegúrate de probar tus pruebas tú mismo y determina qué pruebas son necesarias para garantizar que `plates.py` se revise exhaustivamente.

    check50 cs50/problems/2022/python/tests/plates

¡Caras sonrientes verdes significan que tu programa ha aprobado una prueba! ¡Caras tristes rojas indicarán que tu programa emitió algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` entregó a tu programa, la salida que esperaba y la salida que tu programa dio realmente.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/tests/plates