# Fiftyville

## Problema a resolver

¡El pato de CS50 fue robado! La ciudad de Fiftyville ha pedido tu ayuda para resolver el misterio del pato robado. Las autoridades creen que el ladrón robó el pato y, poco después, salió de la ciudad en un vuelo con la ayuda de un cómplice. Tu objetivo es identificar:

- Quién es el ladrón,
- A qué ciudad escapó el ladrón y
- Quién es el cómplice del ladrón que lo ayudó a escapar

Todo lo que sabes es que el robo **sucedió el 28 de julio de 2023** y que **sucedió en Humphrey Street**.

¿Cómo vas a resolver este misterio? Las autoridades de Fiftyville han tomado algunos de los registros de la ciudad de la época del robo y han preparado una base de datos SQLite para ti, `fiftyville.db`, que contiene tablas de datos de alrededor de la ciudad. Puedes consultar esa tabla usando consultas SQL `SELECT` para acceder a los datos que te interesan. Usando solo la información en la base de datos, tu tarea es resolver el misterio.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-YgI5fyTP939jINCZm7l3o7WCY" src="https://asciinema.org/a/YgI5fyTP939jINCZm7l3o7WCY.js"></script>

## Comenzando

Para este problema, utilizarás una base de datos que te proporcionará el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí mismo. Deberías encontrar que el indicador de tu ventana de terminal se asemeja al siguiente:

    $

Luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/7/fiftyville.zip

para descargar un ZIP llamado `fiftyville.zip` en tu codespace.

Luego ejecuta

    unzip fiftyville.zip

para crear una carpeta llamada `fiftyville`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm fiftyville.zip

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd fiftyville

seguido de Enter para moverte a (es decir, abrir) ese directorio. Tu indicador ahora debería parecerse al siguiente.

    fiftyville/ $

Ejecuta `ls` por sí mismo y deberías ver algunos archivos:

    answers.txt  fiftyville.db  log.sql

Si tienes algún problema, sigue estos mismos pasos nuevamente y observa si puedes determinar dónde te equivocaste.

## Especificación

Para este problema, tan importante como resolver el misterio en sí es el proceso que utilizas para resolver el misterio. En `log.sql`, mantén un registro de todas las consultas SQL que ejecutas en la base de datos. Encima de cada consulta, etiqueta cada una con un comentario (en SQL, los comentarios son cualquier línea que comienza con `--`) que describa por qué estás ejecutando la consulta y/o qué información esperas obtener de esa consulta en particular. Puedes utilizar comentarios en el archivo de registro para agregar notas adicionales sobre tu proceso de pensamiento a medida que resuelves el misterio: en última instancia, este archivo debería servir como evidencia del proceso que utilizaste para identificar al ladrón.

A medida que escribes tus consultas, puedes notar que algunas de ellas pueden volverse bastante complejas. Para ayudar a que tus consultas sean legibles, consulta los principios de buen estilo en [sqlstyle.guide](https://www.sqlstyle.guide). ¡La sección [sangría](https://www.sqlstyle.guide/#indentation) puede ser particularmente útil!

Una vez que resuelvas el misterio, completa cada una de las líneas en `answers.txt` completando el nombre del ladrón, la ciudad a la que escapó el ladrón y el nombre del cómplice del ladrón que lo ayudó a escapar de la ciudad. (¡Asegúrate de no cambiar el texto existente en el archivo ni agregar ninguna otra línea al archivo!)

Finalmente, debes enviar tus archivos `log.sql` y `answers.txt`.

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YHhgEoJMDnU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Sugerencias

- Ejecuta `sqlite3 fiftyville.db` para comenzar a ejecutar consultas en la base de datos.
  - Mientras ejecutas `sqlite3`, ejecutando `.tables` se mostrarán todas las tablas en la base de datos.
  - Mientras ejecutas `sqlite3`, ejecutando `.schema TABLE_NAME`, donde `TABLE_NAME` es el nombre de una tabla en la base de datos, te mostrará el comando `CREATE TABLE` utilizado para crear la tabla. ¡Esto puede ser útil para saber qué columnas consultar!
- Puede resultarte útil comenzar con la tabla `crime_scene_reports`. Comienza buscando un informe de escena del crimen que coincida con la fecha y el lugar del crimen.
- Consulta [esta referencia de palabras clave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para conocer algunas sintaxis SQL que pueden ser útiles.

## Cómo probar

### Corrección

    check50 cs50/problems/2024/x/fiftyville

## Cómo enviar

    submit50 cs50/problems/2024/x/fiftyville

## Reconocimientos

Inspirado en otro caso en [SQL City](https://mystery.knightlab.com/).