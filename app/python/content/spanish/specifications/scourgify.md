

# Scourgify

> "Bueno", dijo Tonks, cerrando de un portazo la tapa del baúl, "al menos todo está adentro. Esto también podría necesitar un poco de limpieza". Señaló con su varita la jaula de Hedwig. "[Scourgify](https://harrypotter.fandom.com/wiki/Scouring_Charm)." Algunas plumas y excrementos desaparecieron.
> 
> - _Harry Potter y la Orden del Fénix_

También es común que los datos necesiten ser "limpiados", por ejemplo, reformateándolos para que los valores estén en un formato consistente y conveniente. Considera, por ejemplo, este archivo CSV de estudiantes, [before.csv](before.csv), a continuación:

    nombre,casa
    "Abbott, Hannah",Hufflepuff
    "Bell, Katie",Gryffindor
    "Bones, Susan",Hufflepuff
    "Boot, Terry",Ravenclaw
    "Brown, Lavender",Gryffindor
    "Bulstrode, Millicent",Slytherin
    "Chang, Cho",Ravenclaw
    "Clearwater, Penelope",Ravenclaw
    "Crabbe, Vincent",Slytherin
    "Creevey, Colin",Gryffindor
    "Creevey, Dennis",Gryffindor
    "Diggory, Cedric",Hufflepuff
    "Edgecombe, Marietta",Ravenclaw
    "Finch-Fletchley, Justin",Hufflepuff
    "Finnigan, Seamus",Gryffindor
    "Goldstein, Anthony",Ravenclaw
    "Goyle, Gregory",Slytherin
    "Granger, Hermione",Gryffindor
    "Johnson, Angelina",Gryffindor
    "Jordan, Lee",Gryffindor
    "Longbottom, Neville",Gryffindor
    "Lovegood, Luna",Ravenclaw
    "Lupin, Remus",Gryffindor
    "Malfoy, Draco",Slytherin
    "Malfoy, Scorpius",Slytherin
    "Macmillan, Ernie",Hufflepuff
    "McGonagall, Minerva",Gryffindor
    "Midgen, Eloise",Gryffindor
    "McLaggen, Cormac",Gryffindor
    "Montague, Graham",Slytherin
    "Nott, Theodore",Slytherin
    "Parkinson, Pansy",Slytherin
    "Patil, Padma",Gryffindor
    "Patil, Parvati",Gryffindor
    "Potter, Harry",Gryffindor
    "Riddle, Tom",Slytherin
    "Robins, Demelza",Gryffindor
    "Scamander, Newt",Hufflepuff
    "Slughorn, Horace",Slytherin
    "Smith, Zacharias",Hufflepuff
    "Snape, Severus",Slytherin
    "Spinnet, Alicia",Gryffindor
    "Sprout, Pomona",Hufflepuff
    "Thomas, Dean",Gryffindor
    "Vane, Romilda",Gryffindor
    "Warren, Myrtle",Ravenclaw
    "Weasley, Fred",Gryffindor
    "Weasley, George",Gryffindor
    "Weasley, Ginny",Gryffindor
    "Weasley, Percy",Gryffindor
    "Weasley, Ron",Gryffindor
    "Wood, Oliver",Gryffindor
    "Zabini, Blaise",Slytherin

Fuente: [en.wikipedia.org/wiki/List_of_Harry_Potter_characters](https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters)

Aunque cada "fila" en el archivo tiene tres valores (apellido, nombre y casa), los dos primeros están combinados en una "columna" (nombre), encerrados entre comillas dobles, con el apellido y el nombre separados por una coma y un espacio. Esto no es ideal si [Hogwarts](https://en.wikipedia.org/wiki/Hogwarts) quiere enviar una [carta modelo](https://en.wikipedia.org/wiki/Form_letter) a cada estudiante, como a través de una [fusión de correspondencia](https://en.wikipedia.org/wiki/Mail_merge), ya que sería extraño comenzar una carta con:

> Estimado Potter, Harry,

En lugar de, por ejemplo:

> Estimado Harry,

En un archivo llamado `scourgify.py`, implementa un programa que:

- Espera que el usuario proporcione dos argumentos en la línea de comandos:
  - el nombre de un archivo CSV existente que se leerá como entrada, asumiendo que las columnas son, en orden, `nombre` y `casa`, y
  - el nombre de un nuevo archivo CSV que se escribirá como salida, cuyas columnas deben ser, en orden, `nombre`, `apellido` y `casa`.
- Convierte esa entrada en la salida correspondiente, dividiendo cada `nombre` en un `nombre` y un `apellido`. Supón que cada estudiante tendrá tanto un nombre como un apellido.

Si el usuario no proporciona exactamente dos argumentos en la línea de comandos, o si no se puede leer el primero, el programa debería salir usando `sys.exit` con un mensaje de error.

Pistas

- Ten en cuenta que el módulo `csv` viene con varios métodos, según [docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html), entre los cuales están `DictReader`, según [docs.python.org/3/library/csv.html#csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader), y `DictWriter`, según [docs.python.org/3/library/csv.html#csv.DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter).
- Ten en cuenta que puedes indicarle a un `DictWriter` que escriba los `fieldnames` en un archivo usando `writeheader` sin argumentos, según [docs.python.org/3/library/csv.html#csv.DictWriter.writeheader](https://docs.python.org/3/library/csv.html#csv.DictWriter.writeheader).

## Ejemplo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    mkdir scourgify

para crear una carpeta llamada `scourgify` en tu espacio de códigos.

Luego ejecuta

    cd scourgify

para cambiar al directorio de esa carpeta. Ahora deberías ver el indicador de la terminal como `scourgify/ $`. Ahora puedes ejecutar

    code scourgify.py

para crear un archivo llamado `scourgify.py` donde escribirás tu programa. Asegúrate de ejecutar

    wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

para descargar el archivo [before.csv](before.csv) en tu carpeta.

## Cómo Probar

Así es como puedes probar tu código manualmente:

- Ejecuta tu programa con `python scourgify.py`. Tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Too few command-line arguments

- Crea archivos vacíos `1.csv`, `2.csv` y `3.csv`. Ejecuta tu programa con `python scourgify.py 1.csv 2.csv 3.csv`. Tu programa debería mostrar:

      Too many command-line arguments

- Ejecuta tu programa con `python scourgify.py invalid_file.csv output.csv`. Suponiendo que `invalid_file.csv` no existe, tu programa debería salir usando `sys.exit` y mostrar un mensaje de error:

      Could not read invalid_file.csv

- Ejecuta tu programa con `python scourgify.py before.csv after.csv`. Suponiendo que `before.csv` existe, tu programa debería crear un nuevo archivo, `after.csv`, cuyas columnas deben ser, en orden, `nombre`, `apellido` y `casa`.

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/scourgify

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` envió a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/scourgify