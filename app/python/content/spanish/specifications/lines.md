

# Líneas de código

Una forma de medir la complejidad de un programa es contar el número de [líneas de código](https://es.wikipedia.org/wiki/L%C3%ADneas_de_c%C3%B3digo) (LOC), excluyendo las líneas en blanco y los comentarios. Por ejemplo, un programa como:

    # Decir hola

    nombre = input("¿Cuál es tu nombre? ")
    print(f"hola, {nombre}")

tiene solo dos líneas de código, no cuatro, ya que la primera línea es un comentario y la segunda línea está en blanco (es decir, solo contiene espacios en blanco). Eso no es muchas, por lo que es probable que el programa no sea tan complejo. Por supuesto, el hecho de que un programa (o incluso una función) tenga más líneas de código que otro no necesariamente significa que sea más complejo. Por ejemplo, una función como:

    def es_par(n):
        if n % 2 == 0:
            return True
        else:
            return False

no es realmente el doble de compleja que una función como:

    def es_par(n):
        return n % 2 == 0

aunque la primera tiene (más de) el doble de líneas de código. De hecho, la primera podría argumentarse que es más simple si es más fácil de leer. Por lo tanto, las líneas de código deben tomarse con un [grano de sal](https://es.wikipedia.org/wiki/Grano_de_sal).

Aun así, en un archivo llamado `lines.py`, implementa un programa que espera exactamente un argumento de línea de comandos, el nombre (o ruta) de un archivo Python, y muestra el número de líneas de código en ese archivo, excluyendo los comentarios y las líneas en blanco. Si el usuario no especifica exactamente un argumento de línea de comandos, o si el nombre del archivo especificado no termina en `.py`, o si el archivo especificado no existe, el programa debería finalizar mediante `sys.exit`.

Supón que cualquier línea que comienza con `#`, opcionalmente precedida por espacios en blanco, es un comentario. (Un [docstring](https://peps.python.org/pep-0257/) no se considera un comentario) Supón que cualquier línea que solo contiene espacios en blanco está en blanco.

Pistas

- Recuerda que un `str` viene con bastantes métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluyendo `lstrip` y `startswith`.
- Ten en cuenta que `open` puede `lanzar` un `FileNotFoundError`, según [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Puede que te resulte útil probar tu programa, por ejemplo, en algunos de los [códigos fuente de la Semana 6](https://cdn.cs50.net/python/2022/x/lectures/6/src6/) y en algunos programas propios.

## Demostración

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` sin agregar nada. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego, ejecuta

    mkdir lines

para crear una carpeta llamada `lines` en tu espacio de código.

Luego, ejecuta

    cd lines

para cambiar al directorio de esa carpeta. Ahora deberías ver tu indicador de terminal como `lines/ $`. Ahora puedes ejecutar

    code lines.py

para crear un archivo llamado `lines.py` donde escribirás tu programa.

## Cómo Probar

Aquí te mostraremos cómo probar tu código manualmente:

- Ejecuta tu programa con `python lines.py`. Tu programa debería finalizar con `sys.exit` y mostrar un mensaje de error:

      Argumentos de línea de comandos insuficientes

- Crea dos programas en Python llamados `hello.py` y `goodbye.py`. Ejecuta `python lines.py hello.py goodbye.py`. Tu programa debería finalizar con `sys.exit` y mostrar un mensaje de error:

      Demasiados argumentos de línea de comandos

- Crea un archivo de texto llamado `invalid_extension.txt`. Ejecuta tu programa con `python lines.py invalid_extension.txt`. Tu programa debería finalizar con `sys.exit` y mostrar un mensaje de error:

      No es un archivo de Python

- Ejecuta tu programa con `python lines.py non_existent_file.py`. Suponiendo que `non_existent_file.py` no existe, tu programa debería finalizar con `sys.exit` y mostrar un mensaje de error:

      El archivo no existe

- Crea otros programas en Python que varíen en complejidad: crea algunos con comentarios, algunos con docstrings y algunos con espacios en blanco. Para cada uno de estos archivos, ejecuta `python lines.py NOMBRE_DE_ARCHIVO`, donde `NOMBRE_DE_ARCHIVO` es el nombre del archivo. `lines.py` debería mostrar el número de líneas, excluyendo los comentarios y el espacio en blanco, presentes en el archivo dado.

Puedes ejecutar lo siguiente para verificar tu código utilizando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/lines

¡Las caras sonrientes verdes significan que tu programa ha pasado una prueba! Las caras tristes rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le dio a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/lines