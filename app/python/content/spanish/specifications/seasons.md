

# Estaciones de Amor

> Quinientos veinticinco mil seiscientos minutos  
> Quinientos veinticinco mil momentos tan queridos  
> Quinientos veinticinco mil seiscientos minutos  
> ¿Cómo mides, mides un año?
>
> — "[Estaciones de Amor](https://en.wikipedia.org/wiki/Seasons_of_Love)," [_Rent_](<https://en.wikipedia.org/wiki/Rent_(musical)>)

Suponiendo que hay 365 días en un año, hay \\(365 \\times 24 \\times 60 = 525,600\\) minutos en ese mismo año (porque hay 24 horas en un día y 60 minutos en una hora). Pero, ¿cuántos minutos hay en dos o más años? Bueno, eso depende de cuántos de ellos sean [años bisiestos](https://en.wikipedia.org/wiki/Leap_year) con 366 días, según el [calendario gregoriano](https://en.wikipedia.org/wiki/Gregorian_calendar), ya que algunos podrían tener \\(1 \\times 24 \\times 60 = 1,440\\) minutos adicionales. De hecho, ¿cuántos minutos han pasado desde que naciste? Bueno, eso también depende de cuántos años bisiestos ha habido desde entonces. Hay un [algoritmo](https://en.wikipedia.org/wiki/Leap_year#Algorithm) para eso, pero no vamos a reinventar la rueda. Vamos a usar una biblioteca en su lugar. Afortunadamente, Python viene con un módulo llamado `datetime` que tiene una clase llamada `date` que puede ayudar, según la documentación de [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects).

En un archivo llamado `seasons.py`, implementa un programa que solicite al usuario su fecha de nacimiento en formato `AAAA-MM-DD` y luego imprima cuántos minutos tiene esa persona, redondeado al entero más cercano, usando palabras en inglés en lugar de números, tal como la canción de _Rent_, sin ninguna palabra `y` entre las palabras. Dado que un usuario podría no saber la hora en la que nació, supongamos, para simplificar, que el usuario nació a medianoche (es decir, 00:00:00) en esa fecha. Y supongamos que la hora actual también es la medianoche. En otras palabras, incluso si el usuario ejecuta el programa al mediodía, supongamos que en realidad es medianoche, en la misma fecha. Usa `datetime.date.today` para obtener la fecha de hoy, según la documentación de [docs.python.org/3/library/datetime.html#datetime.date.today](https://docs.python.org/3/library/datetime.html#datetime.date.today).

Estructura tu programa según se muestra a continuación, no solo con una función `main`, sino también con una o más funciones adicionales:

    from datetime import date


    def main():
        ...


    ...


    if __name__ == "__main__":
        main()

Puedes importar otras bibliotecas (integradas) o cualquier otra que se especifique en las pistas a continuación. Sal del programa a través de `sys.exit` si el usuario no ingresa una fecha en el formato `AAAA-MM-DD`. Asegúrate de que tu programa no genere ninguna excepción.

Antes o después de implementar `seasons.py`, además implementa, en un archivo llamado `test_seasons.py`, **una o más** funciones que prueben exhaustivamente tu implementación de todas las funciones, excepto `main`, en `seasons.py`, cada una cuyo nombre debe comenzar con `test_` para que puedas ejecutar tus pruebas con:

    pytest test_seasons.py

Pistas

- Ten en cuenta que la clase `date` viene con varios métodos y "operaciones admitidas", según [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects). En particular, la clase implementa `__sub__`, según [docs.python.org/3/library/operator.html#operator.\_\_sub\_\_](https://docs.python.org/3/library/operator.html#operator.__sub__), sobrecargando el operador `-` de tal manera que restar un objeto `date` de otro devuelve un objeto `timedelta`, que a su vez viene con varios "atributos de instancia" (de solo lectura), según [docs.python.org/3/library/datetime.html#timedelta-objects](https://docs.python.org/3/library/datetime.html#timedelta-objects).
- Ten en cuenta que el módulo `inflect` viene con varios métodos, según [pypi.org/project/inflect](https://pypi.org/project/inflect/). Puedes instalarlo con:

      pip install inflect

## Demostración

Supongamos que esta demostración fue grabada el 1 de enero de 2000.

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el símbolo del prompt de tu ventana de terminal se parece a lo siguiente:

    $

A continuación, ejecuta

    mkdir seasons

para crear una carpeta llamada `seasons` en tu espacio de trabajo.

Luego, ejecuta

    cd seasons

para cambiar al directorio de esa carpeta. Ahora verás que tu símbolo del terminal es `seasons/ $`. Ahora puedes ejecutar

    code seasons.py

para crear un archivo llamado `seasons.py` donde escribirás tu programa. Asegúrate también de ejecutar

    code test_seasons.py

para crear un archivo llamado `test_seasons.py` donde escribirás pruebas para tu programa.

## Cómo Probar

#### Cómo Probar `seasons.py`

Así es cómo puedes probar `seasons.py` manualmente:

- Ejecuta tu programa con `python seasons.py`. Asegúrate de que tu programa te solicite una fecha de nacimiento. Escribe una fecha de hace un año a partir de hoy, en el formato especificado, y luego presiona Enter. Tu programa deberá imprimir `Quinientos veinticinco mil seiscientos minutos`.
- Ejecuta tu programa con `python seasons.py`. Escribe una fecha de hace dos años a partir de hoy, en el formato especificado, y luego presiona Enter. Tu programa deberá imprimir `Un millón cincuenta y un mil doscientos minutos`.
- Ejecuta tu programa con `python seasons.py`. Escribe una fecha de tu elección, pero esta vez utiliza un formato no válido. Presiona Enter y tu programa deberá salir usando `sys.exit` sin generar una excepción.

#### Cómo Probar `test_seasons.py`

Para probar tus pruebas, ejecuta `pytest test_seasons.py`. Intenta usar versiones correctas e incorrectas de `seasons.py` para determinar qué tan bien tus pruebas detectan errores:

- Asegúrate de tener una versión correcta de `seasons.py`. Ejecuta tus pruebas ejecutando `pytest test_seasons.py`. `pytest` deberá mostrar que todas tus pruebas han pasado.
- Modifica una de las funciones que has implementado en `seasons.py` e importada en `test_seasons.py`. Por ejemplo, una de tus funciones podría no generar un `ValueError` cuando debería hacerlo. Ejecuta tus pruebas ejecutando `pytest test_seasons.py`. `pytest` deberá mostrar que al menos una de tus pruebas ha fallado.
- Continúa modificando el comportamiento de `seasons.py`, creando versiones incorrectas (previsibles) de tu implementación. Ejecuta tus pruebas ejecutando `pytest test_seasons.py`. ¿Las pruebas que esperas que fallen, fallan?

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/seasons

¡Caritas verdes significan que tu programa ha aprobado una prueba! Caritas rojas indicarán que tu programa generó algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, la salida esperada y la salida real que tu programa devolvió.

## Cómo Enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/seasons