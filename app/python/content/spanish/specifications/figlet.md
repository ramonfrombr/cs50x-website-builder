

# Letras de Frank, Ian y Glen

[FIGlet](https://en.wikipedia.org/wiki/FIGlet), llamado así por [las letras de Frank, Ian y Glen](http://www.figlet.org/faq.html), es un programa de principios de la década de 1990 que crea letras grandes a partir de texto común, una forma de [arte ASCII](https://en.wikipedia.org/wiki/ASCII_art):

     _ _ _          _   _     _
    | (_) | _____  | |_| |__ (_)___
    | | | |/ / _ \ | __| '_ \| / __|
    | | |   <  __/ | |_| | | | \__ \
    |_|_|_|\_\___|  \__|_| |_|_|___/

Entre las fuentes admitidas por FIGlet se encuentran las de [figlet.org/examples.html](http://www.figlet.org/examples.html).

FIGlet ha sido adaptado a Python como un módulo llamado [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

En un archivo llamado `figlet.py`, implementa un programa que:

- Espera cero o dos argumentos por línea de comandos:
  - Cero si el usuario desea mostrar el texto con una fuente aleatoria.
  - Dos si el usuario desea mostrar el texto con una fuente específica, en cuyo caso el primero de los dos debería ser `-f` o `--font`, y el segundo debería ser el nombre de la fuente.
- Solicita al usuario una cadena de texto (str).
- Muestra ese texto con la fuente deseada.

Si el usuario proporciona dos argumentos por línea de comandos y el primero no es `-f` o `--font`, o el segundo no es el nombre de una fuente, el programa debería salir mediante `sys.exit` con un mensaje de error.

Pistas

- Puedes instalar `pyfiglet` con:

      pip install pyfiglet

- La documentación de pyfiglet no es muy clara, pero puedes usar el módulo de la siguiente manera:

      from pyfiglet import Figlet

      figlet = Figlet()

  Luego puedes obtener una lista de fuentes disponibles con código como este:

      figlet.getFonts()

  Puedes establecer la fuente con código como este, donde `f` es el nombre de la fuente como cadena (str):

      figlet.setFont(font=f)

  Y puedes mostrar el texto con esa fuente usando código como este, donde `s` es ese texto como una cadena (str):

      print(figlet.renderText(s))

- Ten en cuenta que el módulo `random` viene con varias funciones, según [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demo

En esta demostración, la primera salida utiliza una fuente aleatoria. Tu salida puede variar.

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí mismo. Deberías ver que la ventana de tu terminal se parece a la siguiente:

    $

Luego ejecuta

    mkdir figlet

para crear una carpeta llamada `figlet` en tu espacio de trabajo.

Luego ejecuta

    cd figlet

para cambiar al directorio de esa carpeta. Ahora deberías ver el símbolo de tu terminal como `figlet/ $`. Ahora puedes ejecutar

    code figlet.py

para crear un archivo llamado `figlet.py` donde escribirás tu programa.

## Cómo Probar

Así es como puedes probar tu código manualmente:

- Ejecuta tu programa con `python figlet.py test`. Tu programa debería salir mediante `sys.exit` y mostrar un mensaje de error:

      Uso inválido

- Ejecuta tu programa con `python figlet.py -a slant`. Tu programa debería salir mediante `sys.exit` y mostrar un mensaje de error:

      Uso inválido

- Ejecuta tu programa con `python figlet.py -f invalid_font`. Tu programa debería salir mediante `sys.exit` y mostrar un mensaje de error:

      Uso inválido

- Ejecuta tu programa con `python figlet.py -f slant`. Escribe `CS50`. Tu programa debería mostrar lo siguiente:

         ___________ __________
        / ____/ ___// ____/ __ \
       / /    \__ \/___ \/ / / /
      / /___ ___/ /___/ / /_/ /
      \____//____/_____/\____/

- Ejecuta tu programa con `python figlet.py -f rectangles`. Escribe `Hello, world`. Tu programa debería mostrar lo siguiente:

       _____     _ _                        _   _
      |  |  |___| | |___      _ _ _ ___ ___| |_| |
      |     | -_| | | . |_   | | | | . |  _| | . |
      |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                        |_|

- Ejecuta tu programa con `python figlet.py -f alphabet`. Escribe `Moo`. Tu programa debería mostrar lo siguiente:

      M   M
      MM MM
      M M M ooo ooo
      M   M o o o o
      M   M ooo ooo

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/figlet

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` entregó a tu programa, cuál era la salida esperada y cuál fue la salida real de tu programa.

## Cómo Entregar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/figlet