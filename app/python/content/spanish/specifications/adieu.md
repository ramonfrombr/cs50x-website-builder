

# Adieu, Adieu

En [The Sound of Music](<https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)>), hay una canción cantada en su mayoría en inglés, [So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU), con estas [letras](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell), en las que "adieu" significa "adiós" en francés:

> Adieu, adieu, a ti y a ti y a ti

Por supuesto, la frase no es gramaticalmente correcta, ya que típicamente se escribiría (con una [coma de Oxford](https://en.wikipedia.org/wiki/Serial_comma)) de la siguiente manera:

> Adieu, adieu, a ti, a ti y a ti

Para ser justos, "tú" ni siquiera es una palabra; simplemente rima con "you" en inglés.

En un archivo llamado `adieu.py`, implementa un programa que solicite al usuario nombres, uno por línea, hasta que el usuario introduzca control-d (o control-z en Windows). Supongamos que el usuario ingresará al menos un nombre. Luego, despídete de esos nombres, separando dos nombres con un `and`, tres nombres con dos comas y un `and`, y \\(n\\) nombres con \\(n-1\\) comas y un `and`, como se muestra a continuación:

> Adieu, adieu, a Liesl  
> Adieu, adieu, a Liesl y Friedrich  
> Adieu, adieu, a Liesl, Friedrich y Louisa  
> Adieu, adieu, a Liesl, Friedrich, Louisa y Kurt  
> Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt y Brigitta  
> Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt, Brigitta y Marta  
> Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta y Gretl

Pistas

- Ten en cuenta que el módulo `inflect` viene con bastantes métodos, según [pypi.org/project/inflect](https://pypi.org/project/inflect/). Puedes instalarlo con:

      pip install inflect

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir adieu

para crear una carpeta llamada `adieu` en tu espacio de trabajo.

Luego ejecuta

    cd adieu

para cambiar de directorio a esa carpeta. Ahora deberías ver el prompt de tu terminal como `adieu/ $`. Ahora puedes ejecutar

    code adieu.py

para crear un archivo llamado `adieu.py` en el que escribirás tu programa.

## Cómo Probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python adieu.py`. Escribe `Liesl` y presiona Enter, seguido de control-d. Tu programa debería mostrar:

      Adieu, adieu, a Liesl

- Ejecuta tu programa con `python adieu.py`. Escribe `Liesl` y presiona Enter, luego escribe `Friedrich` y presiona Enter, seguido de control-d. Tu programa debería mostrar:

      Adieu, adieu, a Liesl y Friedrich

- Ejecuta tu programa con `python adieu.py`. Escribe `Liesl` y presiona Enter, luego escribe `Friedrich` y presiona Enter. Ahora escribe `Louisa` y presiona Enter, seguido de control-d. Tu programa debería mostrar:

      Adieu, adieu, a Liesl, Friedrich y Louisa

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/adieu

¡Las caritas verdes significan que tu programa ha superado una prueba! Las tristes caritas rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, la salida esperada y la salida real de tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/adieu