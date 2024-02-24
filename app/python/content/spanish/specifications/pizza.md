

# Pizza Py

Quizás el lugar más popular para pizza en [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) es [Pinocchio’s Pizza & Subs](https://www.pinocchiospizza.net/), también conocido como Noch's, famoso por su [pizza siciliana](https://www.pinocchiospizza.net/sicilian_vs_regular.html), que es "una pizza de masa gruesa o estilo deep-dish".

Los estudiantes tienden a comprar pizza por porción, pero Pinocchio’s también tiene pizzas enteras en su [menú](https://www.pinocchiospizza.net/menu.html), que se muestra en el siguiente archivo CSV de pizzas sicilianas, [sicilian.csv](sicilian.csv):

    Pizza Siciliana,Pequeña,Grande
    Queso,$25.50,$39.95
    1 ingrediente,$27.50,$41.95
    2 ingredientes,$29.50,$43.95
    3 ingredientes,$31.50,$45.95
    Especial,$33.50,$47.95

Consulte [regular.csv](regular.csv) para obtener un archivo CSV de pizzas regulares también.

Por supuesto, un archivo CSV no es el formato más amigable para el cliente. Un formato más legible podría ser una tabla formateada como [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), como esta:

    +------------------+---------+---------+
    | Pizza Siciliana  | Pequeña | Grande  |
    +==================+=========+=========+
    | Queso            | $25.50  | $39.95  |
    +------------------+---------+---------+
    | 1 ingrediente    | $27.50  | $41.95  |
    +------------------+---------+---------+
    | 2 ingredientes   | $29.50  | $43.95  |
    +------------------+---------+---------+
    | 3 ingredientes   | $31.50  | $45.95  |
    +------------------+---------+---------+
    | Especial         | $33.50  | $47.95  |
    +------------------+---------+---------+

En un archivo llamado `pizza.py`, implementa un programa que espera exactamente un argumento de línea de comandos, el nombre (o ruta) de un archivo CSV en el formato de Pinocchio's, y muestra una tabla formateada como ASCII art utilizando `tabulate`, un paquete en PyPI en [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Formatea la tabla utilizando el formato `grid` de la biblioteca. Si el usuario no especifica exactamente un argumento de línea de comandos, o si el nombre del archivo especificado no termina en `.csv`, o si el archivo especificado no existe, el programa deberá finalizar con `sys.exit`.

Pistas

- Recuerda que el módulo `csv` viene con varios métodos, según [docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html), entre los que se encuentran `reader`, según [docs.python.org/3/library/csv.html#csv.reader](https://docs.python.org/3/library/csv.html#csv.reader), y `DictReader`, según [docs.python.org/3/library/csv.html#csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).
- Ten en cuenta que `open` puede `lanzar` un `FileNotFoundError`, según [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Ten en cuenta que el paquete `tabulate` viene con una sola función, según [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Puedes instalar el paquete con el siguiente comando:

      pip install tabulate

## Demo

## Antes de empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` sin ningún argumento. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

A continuación, ejecuta

    mkdir pizza

para crear una carpeta llamada `pizza` en tu espacio de código.

Luego ejecuta

    cd pizza

para cambiar a ese directorio. Ahora deberías ver el indicador de tu terminal como `pizza/ $`. Ahora puedes ejecutar

    code pizza.py

para crear un archivo llamado `pizza.py` donde escribirás tu programa. Asegúrate de ejecutar

    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv

para descargar [sicilian.csv](sicilian.csv) en tu carpeta. También ejecuta

    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

para descargar [regular.csv](regular.csv) en tu carpeta.

## Cómo probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python pizza.py`. Tu programa debería finalizar usando `sys.exit` y mostrar un mensaje de error:

      Demasiados pocos argumentos de línea de comandos

- Asegúrate de descargar [regular.csv](regular.csv) y [sicilian.csv](sicilian.csv), colocándolos en la misma carpeta que `pizza.py`. Ejecuta tu programa con `python pizza.py regular.csv sicilian.csv`. Tu programa debería mostrar:

      Demasiados argumentos de línea de comandos

- Ejecuta tu programa con `python pizza.py invalid_file.csv`. Suponiendo que `invalid_file.csv` no existe, tu programa debería finalizar usando `sys.exit` y mostrar un mensaje de error:

      Archivo no existe

- Crea un archivo llamado `sicilian.txt`. Ejecuta tu programa con `python pizza.py sicilian.txt`. Tu programa debería finalizar usando `sys.exit` y mostrar un mensaje de error:

      No es un archivo CSV

- Ejecuta tu programa con `python pizza.py regular.csv`. Suponiendo que hayas descargado [regular.csv](regular.csv), tu programa debería mostrar una tabla como la siguiente:

      +-----------------+---------+---------+
      | Pizza Regular   | Pequeña | Grande  |
      +=================+=========+=========+
      | Queso           | $13.50  | $18.95  |
      +-----------------+---------+---------+
      | 1 ingrediente   | $14.75  | $20.95  |
      +-----------------+---------+---------+
      | 2 ingredientes  | $15.95  | $22.95  |
      +-----------------+---------+---------+
      | 3 ingredientes  | $16.95  | $24.95  |
      +-----------------+---------+---------+
      | Especial        | $18.50  | $26.95  |
      +-----------------+---------+---------+

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utiliza para probar tu código cuando lo envías. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/pizza

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/pizza