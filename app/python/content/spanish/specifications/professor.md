

# Pequeño profesor

Uno de los primeros juguetes de David cuando era niño, curiosamente, fue el [Pequeño profesor](https://es.wikipedia.org/wiki/Little_Professor), una "calculadora" que generaba diez diferentes problemas matemáticos para que David resolviera. Por ejemplo, si el juguete mostraba `4 + 0 =`, David respondería (con suerte) `4`. Si el juguete mostrara `4 + 1 =`, David respondería (con suerte) `5`. Si David respondía incorrectamente, el juguete mostraría `EEE`. Después de tres respuestas incorrectas para el mismo problema, el juguete simplemente mostraría la respuesta correcta (por ejemplo, `4 + 0 = 4` o `4 + 1 = 5`).

En un archivo llamado `professor.py`, implementa un programa que:

- Solicite al usuario un nivel, \\(n\\). Si el usuario no ingresa `1`, `2` o `3`, el programa debe pedir nuevamente.
- Genere aleatoriamente diez (10) problemas matemáticos formateados como `X + Y =`, donde cada `X` e `Y` son enteros no negativos con \\(n\\) dígitos. No es necesario admitir operaciones distintas a la suma (`+`).
- Solicite al usuario que resuelva cada uno de esos problemas. Si una respuesta no es correcta (o ni siquiera es un número), el programa debe mostrar `EEE` y solicitar nuevamente al usuario, permitiendo hasta tres intentos en total para ese problema. Si el usuario aún no ha respondido correctamente después de tres intentos, el programa debe mostrar la respuesta correcta.
- El programa debe mostrar finalmente la puntuación del usuario: el número de respuestas correctas de un total de 10.

Estructura tu programa de la siguiente manera, donde `get_level` solicita (y, si es necesario, solicita de nuevo) al usuario un nivel y devuelve `1`, `2` o `3`, y `generate_integer` devuelve un entero no negativo generado aleatoriamente con `level` dígitos o genera una excepción `ValueError` si `level` no es `1`, `2` o `3`:

    import random


    def main():
        ...


    def get_level():
        ...


    def generate_integer(level):
        ...


    if __name__ == "__main__":
        main()

Sugerencias

- Ten en cuenta que puedes generar una excepción como `ValueError` con código como:

      raise ValueError

- Ten en cuenta que el módulo `random` viene con varias funciones, según [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demostración

## Antes de empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana del terminal y ejecuta `cd` por sí solo. Deberías ver que el símbolo de tu ventana del terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    mkdir professor

para crear una carpeta llamada `professor` en tu área de trabajo.

Luego, ejecuta

    cd professor

para cambiar al directorio de esa carpeta. Ahora deberías ver el símbolo del terminal como `professor/ $`. Ahora puedes ejecutar

    code professor.py

para crear un archivo llamado `professor.py` donde escribirás tu programa.

## Cómo probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python professor.py`. Ingresa `-1` y presiona Enter. Tu programa debería pedirte de nuevo:

      Nivel:

- Ejecuta tu programa con `python professor.py`. Ingresa `4` y presiona Enter. Tu programa debería pedirte de nuevo:

      Nivel:

- Ejecuta tu programa con `python professor.py`. Ingresa `1` y presiona Enter. Tu programa debería comenzar a plantear problemas de suma con enteros positivos de un solo dígito. Por ejemplo:

      6 + 6 =

  Tu programa debería mostrar 10 problemas distintos antes de imprimir el número de preguntas a las que has respondido correctamente y salir.

- Ejecuta tu programa con `python professor.py`. Ingresa `1` y presiona Enter. Responde incorrectamente a la primera pregunta. Tu programa debería mostrar:

      EEE

  antes de solicitarte de nuevo la misma pregunta.

- Ejecuta tu programa con `python professor.py`. Ingresa `1` y presiona Enter. Responde incorrectamente a la primera pregunta tres veces. Tu programa debería mostrar la respuesta correcta. Por ejemplo:

      6 + 6 = 12

  y luego pasar a otra pregunta. Responde correctamente a las preguntas restantes. Tu programa debería mostrar una puntuación de `9`.

- Ejecuta tu programa con `python professor.py`. Ingresa `1` y presiona Enter. Responde correctamente a las 10 preguntas. Tu programa debería mostrar una puntuación de `10`.

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/professor

Las caras sonrientes verdes significan que tu programa ha pasado una prueba. Las caras tristes rojas indicarán que tu programa ha emitido algo inesperado. Visita la dirección web que `check50` muestra para ver la entrada que `check50` envió a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/professor