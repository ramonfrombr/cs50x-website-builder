

# CS50 Shirtificate

[![CS50 Shirtificate de John Harvard](jharvard.png)](jharvard.pdf)

Supongamos que deseas implementar un "shritificado" de CS50, un PDF con una imagen de una camiseta [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt), [shirtificate.png](shirtificate.png), personalizada con el nombre del usuario.

En un archivo llamado `shirtificate.py`, implementa un programa que solicite al usuario su nombre y genere, utilizando [fpdf2](https://pypi.org/project/fpdf2/), un CS50 shirtificate en un archivo llamado `shirtificate.pdf` similar a [este ejemplo para John Harvard](jharvard.pdf), con las siguientes especificaciones:

- La [orientación](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) del PDF debe ser Portrait (vertical).
- El [formato](https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html) del PDF debe ser A4, que es de 210 mm de ancho por 297 mm de alto.
- La parte superior del PDF debe decir "CS50 Shirtificate" como [texto](https://py-pdf.github.io/fpdf2/Text.html), centrado horizontalmente.
- La imagen de la camiseta debe estar centrada horizontalmente.
- El nombre del usuario debe estar sobre la camiseta, en [texto](https://py-pdf.github.io/fpdf2/TextStyling.html) blanco.

Dejamos todos los demás detalles a tu elección. Incluso puedes agregar bordes, colores y [líneas](https://py-pdf.github.io/fpdf2/Shapes.html#lines). Tu shirtificate no necesita ser idéntico al de John Harvard. Y no es necesario ajustar nombres largos en varias líneas.

Antes de escribir cualquier código, lee el [tutorial](https://py-pdf.github.io/fpdf2/Tutorial.html) de fpdf2 para aprender cómo usarlo. Luego, examina la [API](https://py-pdf.github.io/fpdf2/fpdf/) (interfaz de programación de aplicaciones) de fpdf2 para ver todas sus funciones y parámetros.

No es necesario enviar ningún PDF con tu código. Pero si quieres, puedes compartir un shirtificate con tu nombre en alguna de las [comunidades de CS50](https://cs50.harvard.edu/python/communities) (¡pero no es obligatorio!).

Sugerencias:

- Ten en cuenta que fpdf2 incluye una `clase` llamada `FPDF`, que tiene varios métodos, según [py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF](https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF). Puedes instalarlo con:

      pip install fpdf2

- Ten en cuenta que puedes extender `FPDF` e instanciar tu propia subclase para agregar un encabezado a cada página de un PDF, según [py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image](https://py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image). O puedes agregarlo como texto tú mismo.
- Ten en cuenta que puedes desactivar los saltos de página automáticos, que de otro modo podrían hacer que tu PDF desborde desde una página a dos, con `set_auto_page_break`, según [py-pdf.github.io/fpdf2/Margins.html](https://py-pdf.github.io/fpdf2/Margins.html).
- Ten en cuenta que la altura de una [celda](https://py-pdf.github.io/fpdf2/Text.html#cell) puede ser negativa para moverla hacia arriba.
- Puedes abrir `shirtificate.pdf`, una vez generado, al hacer clic en él en el explorador de archivos de VS Code.

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que la indicación de tu ventana de terminal se parece a la siguiente:

    $

Luego ejecuta

    mkdir shirtificate

para crear una carpeta llamada `shirtificate` en tu espacio de trabajo.

Luego ejecuta

    cd shirtificate

para cambiar de directorio a esa carpeta. Ahora deberías ver que tu indicación de terminal es `shirtificate/ $`. Ahora ejecuta

    wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png

para obtener una copia de la imagen `shirtificate.png` para tu certificado. Por último, ejecuta

    code shirtificate.py

para crear un archivo llamado `shirtificate.py` donde escribirás tu programa.

## Cómo probar

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `shirtificate.py`. Asegúrate de que tu programa te solicite un nombre. Ingresa tu propio nombre y presiona Enter. Tu programa debe crear un archivo llamado `shirtificate.pdf` que contenga el nombre que has ingresado superpuesto en una representación de `shirtificate.png`.
- ¡Prueba también con algunos otros nombres para mayor seguridad!

Puedes ejecutar lo siguiente para comprobar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/shirtificate

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, la salida esperada y la salida real de tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/shirtificate