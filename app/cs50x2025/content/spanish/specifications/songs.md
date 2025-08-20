# Canciones

![Logotipo de Spotify Wrapped '22](https://cs50.harvard.edu/x/2024/psets/7/songs/wrapped.png)

## Problema a resolver

Escribe consultas SQL para responder preguntas sobre una base de datos de las 100 canciones más reproducidas en [Spotify](https://es.wikipedia.org/wiki/Spotify) en 2018.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DsiNSGFrMq2J6t9aDYhIQUQHy" src="https://asciinema.org/a/DsiNSGFrMq2J6t9aDYhIQUQHy.js"></script>

## Primeros pasos

Para este problema, usarás una base de datos proporcionada por el equipo de CS50.

Abre [VS Code](https://cs50.dev/).

Comienza haciendo clic dentro de la ventana del terminal y, luego, ejecuta `cd` solo. Deberías ver que el "indicador" sea el siguiente:

    $

Haz clic dentro de esa ventana del terminal y, luego, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/7/songs.zip

y presiona Enter para descargar un código postal denominado `songs.zip` en tu espacio de códigos. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL ni ningún otro carácter!

Ahora ejecuta

    unzip songs.zip

para crear una carpeta denominada `songs`. Ya no necesitas el archivo ZIP, entonces puedes ejecutar

    rm songs.zip

y responder con "y" y presionar Enter en el indicador para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd songs

y presiona Enter para ingresar (o abrir) esa carpeta. Tu indicador ahora debería verse como el siguiente:

    songs/ $

Si todo fue bien, debes ejecutar

    ls

y deberías ver 8 archivos .sql, `songs.db` y `answers.txt`.

Si tienes algún problema, sigue estos mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste.

## Comprensión

Te proporcionamos un archivo denominado `songs.db`, una base de datos SQLite que almacena datos de [Spotify](https://developer.spotify.com/documentation/web-api/) sobre canciones y sus artistas. Este conjunto de datos contiene las 100 canciones más transmitidas en Spotify en 2018. En una ventana de terminal, ejecuta `sqlite3 songs.db` para que puedas comenzar a ejecutar consultas en la base de datos.

En primer lugar, cuando `sqlite3` te solicite que proporciones una consulta, escribe `.schema` y presiona enter. Esto emitirá las sentencias `CREATE TABLE` que se utilizaron para generar cada una de las tablas en la base de datos. Al examinar esas sentencias, puedes identificar las columnas presentes en cada tabla.

Observa que cada `artista` tiene un `id` y un `nombre`. Observa también que cada canción tiene un `nombre`, un `artist_id` (que corresponde al `id` del artista de la canción) y valores para la bailabilidad, la energía, la clave, el volumen, la locuacidad (presencia de palabras habladas en una pista), la valencia, el tempo y la duración de la canción (medida en milisegundos).

El desafío que tienes por delante es escribir consultas SQL para responder una variedad de preguntas diferentes seleccionando datos de una o más de estas tablas. Después de hacerlo, reflexionarás sobre las formas en que Spotify podría usar estos mismos datos en su campaña anual [Spotify Wrapped](https://es.wikipedia.org/wiki/Spotify_Wrapped) para caracterizar los hábitos de los oyentes.

## Detalles de implementación

Para cada uno de los siguientes problemas, debes escribir una sola consulta SQL que genere los resultados especificados en cada problema. Tu respuesta debe tomar la forma de una sola consulta SQL, aunque puedes anidar otras consultas dentro de tu consulta. **No debes** asumir nada sobre los `id` de ninguna canción o artista en particular: tus consultas deben ser precisas, incluso si el `id` de alguna canción o persona en particular fuera diferente. Por último, cada consulta debería regresar solo los datos necesarios para responder la pregunta: si el problema solo te pide que generes los nombres de las canciones, por ejemplo, tu consulta no debería generar también el tempo de cada canción.

1. En `1.sql`, escribe una consulta SQL para enumerar los nombres de todas las canciones en la base de datos.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.
2. En `2.sql`, escribe una consulta SQL para enumerar los nombres de todas las canciones en orden de tempo creciente.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.
3. En `3.sql`, escribe una consulta SQL para enumerar los nombres de las 5 canciones más largas, en orden descendente de duración.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.
4. En `4.sql`, escribe una consulta SQL que enumere los nombres de las canciones que tienen bailabilidad, energía y valencia superiores a 0,75.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.
5. En `5.sql`, escribe una consulta SQL que devuelva el promedio de energía de todas las canciones.
   - Tu consulta debería generar una tabla con una sola columna y una sola fila que contenga el promedio de energía.
6. En `6.sql`, escribe una consulta SQL que enumere los nombres de las canciones que son de Post Malone.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.
   - No debes hacer ninguna suposición sobre cuál es el `artist_id` de Post Malone.
7. En `7.sql`, escribe una consulta SQL que devuelva el promedio de energía de las canciones de Drake.
   - Tu consulta debería generar una tabla con una sola columna y una sola fila que contenga el promedio de energía.
   - No debes hacer ninguna suposición sobre cuál es el `artist_id` de Drake.
8. En `8.sql`, escribe una consulta SQL que enumere los nombres de las canciones que cuentan con otros artistas.
   - Las canciones que cuentan con otros artistas incluirán "feat." en el nombre de la canción.
   - Tu consulta debería generar una tabla con una sola columna para el nombre de cada canción.

## Sugerencias

¡Consulta [esta referencia de palabras clave de SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para ver algo de sintaxis de SQL que puede ser útil!

¡Haz clic en los siguientes botones para leer algunos consejos!

### Enumerar los nombres de todas las canciones en la base de datos

Recuerda que, para seleccionar todos los valores en la columna de una tabla, puedes usar la palabra clave `SELECT` de SQL. `SELECT` va seguida de la columna (o columnas) que te gustaría seleccionar, que a su vez va seguida de `FROM table` donde `table` es el nombre de la tabla de la que te gustaría seleccionar.

En `1.sql`, entonces, intenta escribir lo siguiente:

    -- Todas las canciones en la base de datos.
    SELECT name
    FROM songs;

### Enumerar los nombres de todas las canciones en orden de tempo creciente

Recuerda que SQL tiene una palabra clave `ORDER BY`, por la cual puedes ordenar los resultados de tu consulta por el valor en una determinada columna. Por ejemplo, `ORDER BY tempo` ordenará los resultados por la columna `tempo`.

En `2.sql`, entonces, intenta escribir lo siguiente:

    -- Todas las canciones en orden de tempo creciente.
    SELECT name
    FROM songs
    ORDER BY tempo;

### Enumerar los nombres de las 5 canciones más largas, en orden descendente de duración

Recuerda que `ORDER BY` no siempre debe ordenar en orden ascendente. Puedes especificar que tus resultados se ordenen en orden _descendente_ adjuntando `DESC`. Por ejemplo, `ORDER BY duration_ms DESC` enumerará los resultados en orden descendente, por duración.

Y recuerda también que `LIMIT n` puede especificar que solo quieres las primeras \\(n\\) filas que coincidan con una consulta específica. Por ejemplo, `LIMIT 5` devolverá solo los primeros cinco resultados de la consulta.

En `3.sql`, entonces, intenta escribir lo siguiente:

    -- Los nombres de las 5 canciones más largas, en orden descendente de duración.
    SELECT name
    FROM songs
    ORDER BY duration_ms DESC
    LIMIT 5;

### Enumere los nombres de cualquier canción que tenga una bailabilidad, energía y valencia mayores a 0,75

Recuerde que puede filtrar los resultados en SQL con cláusulas `WHERE`, las cuales son seguidas de alguna condición que típicamente prueba los valores en las columnas de una fila.

Recuerde también que los operadores de SQL funcionan de manera muy similar a los operadores de C. Por ejemplo, `>` se evalúa como "verdadero" cuando el valor en el lado izquierdo es mayor que el valor en el lado derecho. Puede encadenar estas expresiones, usando `AND` u `OR`, para formar una condición más grande.

Entonces, en `4.sql`, intente escribir lo siguiente:

    -- Los nombres de cualquier canción que tenga bailabilidad, energía y valencia mayores a 0,75.
    SELECT name
    FROM songs
    WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;

### Encuentre la energía promedio de todas las canciones

Recuerde que SQL admite palabras clave no solo para seleccionar filas particulares, sino también para _agregar_ los datos en esas filas. En particular, la palabra clave `AVG` (para calcular promedios) puede resultarle útil. Para agregar los resultados de una columna, simplemente aplique la función de agregación a esa columna. Por ejemplo, `SELECT AVG(energy)` encontrará el promedio de los valores en la columna de energía para la consulta dada.

Entonces, en `5.sql`, intente escribir lo siguiente:

    -- La energía promedio de todas las canciones.
    SELECT AVG(energy)
    FROM songs;

### Enumere los nombres de las canciones que son de Post Malone

Observe que, si ejecuta `.schema songs` en el símbolo del sistema de sqlite, la tabla `songs` tiene nombres de canciones pero no nombres de artistas. En su lugar, `songs` tiene una columna `artist_id`. Entonces, para enumerar los nombres de las canciones de Post Malone, primero deberá identificar el id de artista de Post Malone.

    -- Identifique el id de artista de Post Malone.
    SELECT id
    FROM artists
    WHERE name = "Post Malone";

Esta consulta devuelve 54. Ahora, podría consultar la tabla `songs` para cualquier canción con el id de Post Malone.

    SELECT name
    FROM songs
    WHERE artist_id = 54;

Pero, según la especificación, debe tener cuidado de no asumir el conocimiento de ninguna identificación. Podría mejorar el diseño de esta consulta _anidando_ sus dos consultas.

En `6.sql`, intente escribir lo siguiente:

    -- Los nombres de las canciones que son de Post Malone.
    SELECT name
    FROM songs
    WHERE artist_id =
    (
        SELECT id
        FROM artists
        WHERE name = "Post Malone"
    );

### Encuentre la energía promedio de las canciones que son de Drake

Observe que, similar a la consulta anterior, deberá combinar varias tablas para ejecutar esta consulta correctamente. Nuevamente podría usar subconsultas anidadas, ¡pero considere otro enfoque también!

Recuerde que puede usar la palabra clave `JOIN` de SQL para combinar varias tablas en una, siempre que especifique qué columnas a través de esas tablas deben coincidir en última instancia. Por ejemplo, la siguiente consulta une las tablas `songs` y `artists`, indicando que la columna `artist_id` en la tabla `songs` y la columna `id` en la tabla `artists` deben coincidir:

    SELECT *
    FROM songs
    JOIN artists ON songs.artist_id = artists.id

Con estas dos tablas combinadas, es solo cuestión de filtrar su selección para encontrar la energía promedio de las canciones de Drake.

Entonces, en `7.sql`, intente escribir lo siguiente:

    -- La energía promedio de las canciones que son de Drake
    SELECT AVG(energy)
    FROM songs
    JOIN artists ON songs.artist_id = artists.id
    WHERE artists.name = "Drake";

### Enumere los nombres de las canciones que presentan a otros artistas.

Para esta consulta, tenga en cuenta que las canciones que presentan a otros artistas suelen tener alguna mención de "feat." en su título. Recuerde que la palabra clave `LIKE` de SQL se puede utilizar para hacer coincidir cadenas con ciertas frases (¡como "feat."!). Para hacerlo, puede utilizar `%`: un carácter comodín que coincide con cualquier secuencia de caracteres.

Entonces, en `8.sql`, intente escribir lo siguiente:

    -- Los nombres de las canciones que presentan a otros artistas.
    SELECT name
    FROM songs
    WHERE name LIKE "%feat.%";

## Tutorial

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>

<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) es una función que presenta las 100 canciones más reproducidas de los usuarios de Spotify del año pasado. En 2021, Spotify Wrapped calculó un [“Aura de audio”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) para cada usuario, una "lectura de \[sus\] dos estados de ánimo más destacados según \[sus\] mejores canciones y artistas del año". Supongamos que Spotify determina un aura de audio observando la energía, la valencia y la bailabilidad promedio de las 100 mejores canciones de una persona del año pasado. En `answers.txt`, reflexione sobre las siguientes preguntas:

- Si `songs.db` contiene las 100 mejores canciones de un oyente de 2018, ¿cómo caracterizaría su aura de audio?
- Suponga por qué la forma en que ha calculado esta aura podría _no_ ser muy representativa del oyente. ¿Qué mejores formas de calcular esta aura propondría?

Asegúrese de enviar `answers.txt` junto con cada uno de sus archivos `.sql`.

## Cómo probar

### Corrección

    check50 cs50/problems/2024/x/songs

## Cómo enviar

    submit50 cs50/problems/2024/x/songs

## Reconocimientos

Conjunto de datos de [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).

