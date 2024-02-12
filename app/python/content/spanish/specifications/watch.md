

# Ver en YouTube

Resulta que la mayoría de los videos de YouTube se pueden incrustar en otros sitios web, al igual que el anterior. Por ejemplo, si visitas [https://youtu.be/xvFZjo5PgG0](https://youtu.be/xvFZjo5PgG0) en una computadora portátil o de escritorio, haz clic en **Compartir** y luego en **Insertar**, verás [HTML](https://en.wikipedia.org/wiki/HTML) (el lenguaje en el que se escriben las páginas web) como se muestra a continuación, que luego puedes copiar en el código fuente de tu propio sitio web, donde [`iframe`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) es un "elemento" HTML y `src` es uno de los varios "atributos" HTML en él, cuyo valor, entre comillas, es `https://www.youtube.com/embed/xvFZjo5PgG0`.

.html pre { white-space: pre-wrap; }

    <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Reproductor de video de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Debido a que algunos atributos HTML son opcionales, también podrías incrustar mínimamente solo lo siguiente.

    <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Supongamos que deseas extraer las URL de los videos de YouTube que están incrustados en páginas (por ejemplo, `https://www.youtube.com/embed/xvFZjo5PgG0`), convirtiéndolos nuevamente en URL más cortas y compartibles de `youtu.be` (por ejemplo, `https://youtu.be/xvFZjo5PgG0`) donde se pueden ver en YouTube directamente.

En un archivo llamado `watch.py`, implementa una función llamada `parse` que espera una `str` de HTML como entrada, extrae cualquier URL de YouTube que sea el valor de un atributo `src` de un elemento `iframe` en ella, y devuelve su equivalente más corto y compartible de `youtu.be` como una `str`. Supón que cualquier URL de este tipo estará en uno de los siguientes formatos. Asume que el valor de `src` estará rodeado de comillas. Y supón que la entrada no contendrá más de una URL de este tipo. Si la entrada no contiene ninguna URL de este tipo, devuelve `None`.

- `http://youtube.com/embed/xvFZjo5PgG0`
- `https://youtube.com/embed/xvFZjo5PgG0`
- `https://www.youtube.com/embed/xvFZjo5PgG0`

Estructura `watch.py` de la siguiente manera, en la cual puedes modificar `main` y/o implementar otras funciones según consideres necesario, pero no puedes importar ninguna otra biblioteca. Puedes utilizar `re` y/o `sys`, pero no es obligatorio.

    import re
    import sys


    def main():
        print(parse(input("HTML: ")))


    def parse(s):
        ...


    ...


    if __name__ == "__main__":
        main()

Sugerencias

- Recuerda que el módulo `re` viene con varias funciones, según se indica en [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html), incluyendo `search`.
- Recuerda que las expresiones regulares admiten varios caracteres especiales, según se indica en [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).
- Debido a que las barras invertidas en las expresiones regulares podrían confundirse con secuencias de escape (como `\n`), es mejor utilizar [la notación de cadena en bruto de Python para los patrones de expresiones regulares](https://docs.python.org/3/library/re.html#module-re). Al igual que las cadenas de formato, las cadenas en bruto se prefijan con `r`. Por ejemplo, en lugar de `"harvard\.edu"`, usa `r"harvard\.edu"`.
- Ten en cuenta que `re.search`, si se le pasa un patrón con "grupos de captura" (es decir, paréntesis), devuelve un "objeto de coincidencia", según se indica en [docs.python.org/3/library/re.html#match-objects](https://docs.python.org/3/library/re.html#match-objects), donde las coincidencias son indexadas en 1, a las cuales se puede acceder individualmente con `group`, según se indica en [docs.python.org/3/library/re.html#re.Match.group](https://docs.python.org/3/library/re.html#re.Match.group), o colectivamente con `groups`, según se indica en [docs.python.org/3/library/re.html#re.Match.groups](https://docs.python.org/3/library/re.html#re.Match.groups).
- Ten en cuenta que `*` y `+` son "codiciosos", en el sentido de que "coinciden con la mayor cantidad de texto posible", según se indica en [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax). Agregar `?` inmediatamente después de cualquiera de ellos, como `*?` o `+?`, "hace que la coincidencia se realice de manera no codiciosa o minimal; se coincidirán la menor cantidad posible de caracteres".

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece a lo siguiente:

    $

Luego ejecuta

    mkdir watch

para crear una carpeta llamada `watch` en tu espacio de codificación.

Luego ejecuta

    cd watch

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de tu terminal como `watch/ $`. Ahora puedes ejecutar

    code watch.py

para crear un archivo llamado `watch.py`, donde escribirás tu programa.

## Cómo probar

Aquí te mostramos cómo probar tu código manualmente:

- Ejecuta tu programa con `python watch.py`. Asegúrate de que tu programa te solicite el HTML, luego copia/pega lo siguiente:

      <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

  Presiona enter y tu programa debería mostrar `https://youtu.be/xvFZjo5PgG0`. Observa cómo, aunque el atributo `src` está precedido por `http://www.youtube.com/embed/`, el enlace resultante está precedido por `https://youtu.be/`.

- Ejecuta tu programa con `python watch.py`. Asegúrate de que tu programa te solicite el HTML, luego copia/pega lo siguiente:

      <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

  Presiona enter y tu programa debería seguir mostrando `https://youtu.be/xvFZjo5PgG0`.

- Ejecuta tu programa con `python watch.py`. Asegúrate de que tu programa te solicite el HTML, luego copia/pega lo siguiente:

      <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>

  Presiona enter y tu programa debería mostrar `None`. Observa que el atributo `src` no apunta a un enlace de YouTube.

Puedes ejecutar lo siguiente para verificar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo por ti mismo también!

    check50 cs50/problems/2022/python/watch

¡Las caritas sonrientes verdes significan que tu programa ha pasado una prueba! Las caritas tristes rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le pasó a tu programa, qué salida esperaba y qué salida realmente dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/watch