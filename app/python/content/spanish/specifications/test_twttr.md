

# Probando mi twttr

En un archivo llamado `twttr.py`, reimplenta [Configurando mi twttr](../../2/twttr/) desde el [Problema 2](../../2/), reestructurando tu código de la siguiente manera, donde `shorten` espera una cadena (`str`) como entrada y devuelve esa misma cadena sin ninguna vocal (A, E, I, O y U), ya sea ingresadas en mayúsculas o minúsculas.

    def main():
        ...


    def shorten(palabra):
        ...


    if __name__ == "__main__":
        main()

Luego, en un archivo llamado `test_twttr.py`, implementa **una o más** funciones que prueben exhaustivamente tu implementación de `shorten`, cada una de las cuales debería comenzar con `test_` para que puedas ejecutar tus pruebas con:

    pytest test_twttr.py

Sugerencias

- Asegúrate de incluir

      import twttr

  o

      from twttr import shorten

  en la parte superior de `test_twttr.py` para poder llamar a `shorten` en tus pruebas.

- Ten cuidado de `return`, no `print`, una cadena (`str`) en `shorten`. Solo `main` debería llamar a `print`.

## Antes de Comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece a lo siguiente:

    $

A continuación, ejecuta

    mkdir test_twttr

para crear una carpeta llamada `test_twttr` en tu espacio de trabajo.

Luego ejecuta

    cd test_twttr

para cambiar el directorio a esa carpeta. Ahora deberías ver el indicador de tu terminal como `test_twttr/ $`. Ahora puedes ejecutar

    code test_twttr.py

para crear un archivo llamado `test_twttr.py` donde escribirás tus pruebas.

## Cómo Probar

Para probar tus pruebas, ejecuta `pytest test_twttr.py`. Asegúrate de tener una copia del archivo `twttr.py` en la misma carpeta. Intenta usar versiones correctas e incorrectas de `twttr.py` para determinar qué tan bien detectan errores tus pruebas:

- Asegúrate de tener una versión correcta de `twttr.py`. Ejecuta tus pruebas ejecutando `pytest test_twttr.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la versión correcta de `twttr.py` de tal manera que se cree un error. Por ejemplo, ¡tu programa podría omitir por error solo las vocales minúsculas! Ejecuta tus pruebas ejecutando `pytest test_twttr.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar lo siguiente para verificar tus pruebas usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. (¡Ahora hay pruebas para probar tus pruebas!). Asegúrate de probar tus pruebas tú mismo y determinar qué pruebas son necesarias para asegurar que `twttr.py` sea revisado exhaustivamente.

    check50 cs50/problems/2022/python/tests/twttr

¡Las caritas verdes significan que tu programa ha superado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver qué inputs le ha proporcionado `check50` a tu programa, qué salida esperaba y qué salida ha dado tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/tests/twttr