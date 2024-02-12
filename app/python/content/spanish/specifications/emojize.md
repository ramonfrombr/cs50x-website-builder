

# Emojize

Debido a que los emoji no son tan fáciles de escribir como el texto, al menos en computadoras portátiles y de escritorio, algunos programas admiten "códigos", mediante los cuales puedes escribir, por ejemplo, `:thumbs_up:`, que se convertirá automáticamente en 👍. Algunos programas también admiten alias, mediante los cuales puedes escribir de manera más concisa, por ejemplo, `:thumbsup:`, que también se convertirá automáticamente en 👍.

Consulta [carpedm20.github.io/emoji/all.html?enableList=enable_list_alias](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias) para obtener una lista de códigos con alias.

En un archivo llamado `emojize.py`, implementa un programa que solicite al usuario una cadena de caracteres en inglés y luego genere la versión "emojizada" de esa cadena, convirtiendo cualquier código (o alias) en su emoji correspondiente.

Pistas

- Ten en cuenta que el módulo `emoji` incluye dos funciones, según [pypi.org/project/emoji](https://pypi.org/project/emoji/), una de las cuales es `emojize`, que admite un parámetro nombrado opcional llamado `language`. Puedes instalarlo con:

      pip install emoji

## Demo

## Antes de empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí mismo. Deberías ver que la línea de comandos de tu terminal se parece a lo siguiente:

    $

Luego, ejecuta

    mkdir emojize

para crear una carpeta llamada `emojize` en tu entorno de codificación.

A continuación, ejecuta

    cd emojize

para cambiar al directorio `emojize`. Ahora deberías ver la línea de comandos de tu terminal como `emojize/ $`. Ahora puedes ejecutar

    code emojize.py

para crear un archivo llamado `emojize.py` donde escribirás tu programa.

## Cómo realizar pruebas

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python emojize.py`. Escribe `:1st_place_medal:` y presiona Enter. Tu programa debería mostrar:

      Salida: 🥇

- Ejecuta tu programa con `python emojize.py`. Escribe `:money_bag:` y presiona Enter. Tu programa debería mostrar:

      Salida: 💰

- Ejecuta tu programa con `python emojize.py`. Escribe `:smile_cat:` y presiona Enter. Tu programa debería mostrar:

      Salida: 😸

Puedes ejecutar lo siguiente para verificar tu código con `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo por ti mismo también!

    check50 cs50/problems/2022/python/emojize

¡Caritas verdes significan que tu programa ha pasado una prueba! Caritas rojas indican que tu programa emitió algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le entregó a tu programa, cuál era la salida esperada y qué salida dio tu programa en realidad.

## Cómo enviarlo

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/emojize