# Películas

![Logo de IMDb](https://cs50.harvard.edu/x/2024/psets/7/movies/imdb.png)

## Problema a resolver

Se te proporciona un archivo llamado `movies.db`, una base de datos SQLite que almacena datos de [IMDb](https://www.imdb.com/) sobre películas, las personas que las dirigieron y protagonizaron, y sus puntuaciones. Escribe consultas SQL para responder preguntas sobre esta base de datos de películas.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-uPWDqSe0NjjqXLF3qxzpsMnfv" src="https://asciinema.org/a/uPWDqSe0NjjqXLF3qxzpsMnfv.js"></script>

## Primeros pasos

Para este problema, utilizarás una base de datos proporcionada por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías encontrar que el indicador de tu ventana de terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/7/movies.zip

para descargar un ZIP llamado `movies.zip` en tu espacio de códigos.

A continuación, ejecuta

    unzip movies.zip

para crear una carpeta llamada `movies`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm movies.zip

y responder con "y" seguido de Enter en el indicador para eliminar el archivo ZIP que has descargado.

Ahora escribe

    cd movies

seguido de Enter para moverte (es decir, abrir) en ese directorio. Tu indicador ahora debería parecerse al siguiente.

    movies/ $

Ejecuta `ls` por sí solo y deberías ver 13 archivos .sql, así como `movies.db`.

Si tienes algún problema, sigue estos mismos pasos de nuevo y observa si puedes determinar dónde te equivocaste.

## Especificaciones

Para cada uno de los siguientes problemas, debes escribir una única consulta SQL que genere los resultados especificados por cada problema. Tu respuesta debe tomar la forma de una única consulta SQL, aunque puedes anidar otras consultas dentro de tu consulta. **No debes** asumir nada sobre los `id` de películas o personas concretas: tus consultas deben ser precisas incluso si el `id` de una película o persona concreta fuera diferente. Por último, cada consulta debe devolver solo los datos necesarios para responder a la pregunta: si el problema solo te pide que generes los nombres de las películas, por ejemplo, tu consulta no debe generar también el año de estreno de cada película.

Puedes comprobar los resultados de tus consultas en [IMDb](https://www.imdb.com/), pero ten en cuenta que las puntuaciones del sitio web pueden diferir de las de `movies.db`, ya que es posible que se hayan emitido más votos desde que descargamos los datos.

1. En `1.sql`, escribe una consulta SQL para enumerar los títulos de todas las películas estrenadas en 2008.
    - Tu consulta debe generar una tabla con una única columna para el título de cada película.
2. En `2.sql`, escribe una consulta SQL para determinar el año de nacimiento de Emma Stone.
    - Tu consulta debe generar una tabla con una única columna y una única fila (sin contar la cabecera) que contenga el año de nacimiento de Emma Stone.
    - Puedes suponer que solo hay una persona en la base de datos con el nombre Emma Stone.
3. En `3.sql`, escribe una consulta SQL para enumerar los títulos de todas las películas con fecha de estreno a partir de 2018, en orden alfabético.
    - Tu consulta debe generar una tabla con una única columna para el título de cada película.
    - Deben incluirse las películas estrenadas en 2018, así como las películas con fechas de estreno en el futuro.
4. En `4.sql`, escribe una consulta SQL para determinar el número de películas con una puntuación IMDb de 10,0.
    - Tu consulta debe generar una tabla con una única columna y una única fila (sin contar la cabecera) que contenga el número de películas con una puntuación de 10,0.
5. En `5.sql`, escribe una consulta SQL para enumerar los títulos y años de estreno de todas las películas de Harry Potter, en orden cronológico.
    - Tu consulta debe generar una tabla con dos columnas, una para el título de cada película y otra para el año de estreno de cada película.
    - Puedes suponer que el título de todas las películas de Harry Potter comenzará con las palabras "Harry Potter" y que si el título de una película comienza con las palabras "Harry Potter", es una película de Harry Potter.
6. En `6.sql`, escribe una consulta SQL para determinar la puntuación media de todas las películas estrenadas en 2012.
    - Tu consulta debe generar una tabla con una única columna y una única fila (sin contar la cabecera) que contenga la puntuación media.
7. En `7.sql`, escribe una consulta SQL para enumerar todas las películas estrenadas en 2010 y sus puntuaciones, en orden descendente por puntuación. Para películas con la misma puntuación, ordénalas alfabéticamente por título.
    - Tu consulta debe generar una tabla con dos columnas, una para el título de cada película y otra para la puntuación de cada película.
    - Las películas que no tengan puntuación no deben incluirse en el resultado.
8. En `8.sql`, escribe una consulta SQL para enumerar los nombres de todas las personas que protagonizaron Toy Story.
    - Tu consulta debe generar una tabla con una única columna para el nombre de cada persona.
    - Puedes suponer que solo hay una película en la base de datos con el título Toy Story.
9. En `9.sql`, escribe una consulta SQL para enumerar los nombres de todas las personas que protagonizaron una película estrenada en 2004, ordenada por año de nacimiento.
    - Tu consulta debe generar una tabla con una única columna para el nombre de cada persona.
    - Las personas con el mismo año de nacimiento pueden aparecer en cualquier orden.
    - No es necesario preocuparse por las personas que no tengan un año de nacimiento registrado, siempre que las que sí lo tengan aparezcan en orden.
    - Si una persona apareció en más de una película en 2004, solo debe aparecer una vez en tus resultados.
10. En `10.sql`, escribe una consulta SQL para enumerar los nombres de todas las personas que han dirigido una película que recibió una puntuación de al menos 9,0.
    - Tu consulta debe generar una tabla con una única columna para el nombre de cada persona.
    - Si una persona dirigió más de una película que recibió una puntuación de al menos 9,0, solo debe aparecer una vez en tus resultados.
11. En `11.sql`, escribe una consulta SQL para enumerar los títulos de las cinco películas mejor puntuadas (en orden) en las que participó Chadwick Boseman, empezando por la mejor puntuada.
    - Tu consulta debe generar una tabla con una única columna para el título de cada película.
    - Puedes suponer que solo hay una persona en la base de datos con el nombre Chadwick Boseman.
12. En `12.sql`, escribe una consulta SQL para enumerar los títulos de todas las películas en las que participaron tanto Bradley Cooper como Jennifer Lawrence.
    - Tu consulta debe generar una tabla con una única columna para el título de cada película.
    - Puedes suponer que solo hay una persona en la base de datos con el nombre Bradley Cooper.
    - Puedes suponer que solo hay una persona en la base de datos con el nombre Jennifer Lawrence.
13. En `13.sql`, escribe una consulta SQL para enumerar los nombres de todas las personas que protagonizaron una película en la que también participó Kevin Bacon.
    - Tu consulta debe generar una tabla con una única columna para el nombre de cada persona.
    - Puede haber varias personas llamadas Kevin Bacon en la base de datos. Asegúrate de seleccionar solo al Kevin Bacon nacido en 1958.
    - El propio Kevin Bacon no debe incluirse en la lista resultante.

## Sugerencias

### Comprende el esquema de `movies.db`

Cuando trabajes con una nueva base de datos, lo mejor es comprender primero su _esquema_. En una ventana de terminal, ejecuta `sqlite3 movies.db` para empezar a ejecutar consultas en la base de datos.

Primero, cuando `sqlite3` te pida que proporciones una consulta, escribe `.schema` y presiona Enter. Esto mostrará las sentencias `CREATE TABLE` que se utilizaron para generar cada una de las tablas en la base de datos. Al examinar esas sentencias, puedes identificar las columnas presentes en cada tabla.

Observa que la tabla `movies` tiene una columna `id` que identifica de forma única cada película, así como columnas para el `title` de una película y el `year` en el que se estrenó la película. La tabla `people` también tiene una columna `id`, y también tiene columnas para el `name` de cada persona y el año de `birth`.

Las calificaciones de las películas, por su parte, se almacenan en la tabla `ratings`. La primera columna de la tabla es `movie_id`: una clave foránea que hace referencia al `id` de la tabla `movies`. El resto de la fila contiene datos sobre la `rating` de cada película y el número de `votes` que la película ha recibido en IMDb.

Finalmente, las tablas `stars` y `directors` relacionan a las personas con las películas en las que actuaron o dirigieron. (Solo se incluyen las estrellas y directores [principales](https://www.imdb.com/interfaces/).) Cada tabla tiene solo dos columnas: `movie_id` y `person_id`, que hacen referencia a una película y persona específica, respectivamente.

El desafío que tienes por delante es escribir consultas SQL para responder a una variedad de preguntas diferentes seleccionando datos de una o más de estas tablas.

### Da estilo a tus consultas de forma coherente

Consulta [sqlstyle.guide](https://www.sqlstyle.guide/) para obtener consejos sobre un buen estilo en SQL, ¡especialmente a medida que tus consultas se vuelven más complejas!

### Enumera los títulos de todas las películas estrenadas en 2008

Recuerda que puedes seleccionar una (o más) columnas de una base de datos usando `SELECT`, según el ejemplo siguiente:

    SELECT columna0, columna1 FROM tabla;

donde `columna0` es el título de una columna y `columna1` es el título de otra.

Y recuerda que puedes filtrar las filas devueltas en una consulta con la palabra clave `WHERE`, seguida de una condición. Puedes utilizar `=`, `>`, `<` y [otros operadores](https://www.w3schools.com/sql/sql_operators.asp) también.

    SELECT columna FROM tabla
    WHERE condicion;

¡Consulta [esta referencia de palabras clave de SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obtener una sintaxis SQL que puede ser útil!

### Determina el año de nacimiento de Emma Stone

Recuerda que una cláusula `WHERE` puede evaluar condiciones no solo con números, sino con cadenas.

### Enumera los títulos de todas las películas con una fecha de estreno en o después de 2018, en orden alfabético

Intenta dividir esta consulta en dos pasos. Primero, encuentra las películas con una fecha de estreno en o después de 2018. Luego, ordena alfabéticamente los títulos de esas películas.

Para encontrar las películas con una fecha de estreno en o después de 2018, recuerda que una condición en SQL admite el uso de muchos [operadores de comparación](https://www.w3schools.com/sql/sql_operators.asp) comunes, incluido `>=` para "mayor que o igual a". Verifica si tu consulta devuelve la cantidad correcta de películas, según [Cómo probar](#cómo-probar).

Finalmente, ordena alfabéticamente los resultados de la consulta por título. Recuerda que `ORDER BY` puede ordenar datos por una columna en tus resultados, según el ejemplo siguiente.

    ...
    ORDER BY columna;

### Determina el número de películas con una calificación IMDb de 10.0

Observa que esta pregunta no te pide _películas individuales_ con una calificación de 10.0, sino el _número_ de películas con dicha calificación. En otras palabras, debes recopilar ("agregar") los resultados de tu consulta en un solo número (el número de filas). Recuerda que SQL admite una "función de agregación" llamada `COUNT`, que puedes usar en una columna según el ejemplo siguiente.

    SELECT COUNT(columna)
    FROM tabla;

### Enumera los títulos y años de estreno de todas las películas de Harry Potter, en orden cronológico

Para esta consulta, es probable que desees hacer uso de la palabra clave `LIKE` de SQL. Recuerda que `LIKE` puede hacer uso de los llamados "caracteres comodín", como `%`, que coincidirán con cualquier carácter (o secuencia de los mismos).

    SELECT columna0, columna1
    FROM tabla
    WHERE columna1 LIKE patrón;

### Determina la calificación promedio de todas las películas estrenadas en 2012

Aquí tienes otro ejemplo de una consulta en la que necesitarás agregar datos. Considera la función de agregación `AVG` de SQL para calcular un promedio.

Considera también que esta consulta utiliza datos almacenados en dos tablas separadas: `ratings` y `movies`. Recuerda que, siempre que una tabla tenga una clave foránea que coincida con una columna en otra tabla, puedes combinar dos tablas usando la palabra clave `JOIN` de SQL. Para usar la palabra clave `JOIN`, debes especificar la tabla a la que te gustaría unir y la columna por la cual hacerlo.

    SELECT columna0
    FROM tabla0
    JOIN tabla1 ON tabla0.columna1 = tabla1.columna2

### Enumera todas las películas estrenadas en 2010 y sus calificaciones, en orden descendente por calificación

Recuerda que `ORDER BY` no siempre tiene que ordenar en orden ascendente. Puedes especificar que los resultados se ordenen en orden _descendente_ agregando `DESC`.

    ...
    ORDER BY columna DESC;

### Listar los nombres de todas las personas que protagonizaron Toy Story

Cuando ve una consulta más compleja como esta, es mejor dividirla en partes más pequeñas. Finalmente, su consulta debe llegar a una lista de nombres, según lo siguiente a continuación.

    -- Seleccionar nombres
    SELECT name
    FROM people
    WHERE ...

Pero, ¿cuál es la mejor manera de llegar a los nombres de quienes protagonizaron Toy Story? Tenga en cuenta que la tabla `gente` por sí sola no tiene esta información (¡pero la tabla `estrellas` podría tenerla!). De hecho, la tabla `estrellas` combina dos columnas, `person_id` y `movie_id`: cualquier persona con un `person_id` que esté asociado con el `movie_id` de Toy Story protagonizó Toy Story.

    -- Seleccionar nombres
    SELECT name
    FROM people
    WHERE ...

    -- Seleccionar ID de personas
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

Entonces, un siguiente paso natural es encontrar el ID de la película de Toy Story.

    -- Seleccionar nombres
    SELECT name
    FROM people
    WHERE ...

    -- Seleccionar ID de personas
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

    -- Buscar ID de Toy Story
    SELECT id
    FROM movies
    WHERE title = 'Toy Story';

Por supuesto, actualmente has escrito tres consultas _separadas_. Pero observe que algunas consultas (las dos primeras) estarían completas al incluir los resultados de la consulta directamente debajo de ellas. El proceso de realizar una consulta que depende de los resultados de una "subconsulta" se denomina "anidar" consultas. ¡Es una gran pista, pero aquí tienes una forma de anidar las consultas anteriores!

    -- Seleccionar nombres
    SELECT name
    FROM people
    WHERE id IN
    (
        -- Seleccionar ID de personas
        SELECT person_id
        FROM stars
        WHERE movie_id = (

            -- Seleccionar ID de Toy Story
            SELECT id
            FROM movies
            WHERE title = 'Toy Story'
        )
    );

### Listar los nombres de todas las personas que protagonizaron una película estrenada en 2004, ordenados por año de nacimiento

Observe que esta consulta, como la anterior, requiere que utilice datos de varias tablas. Recuerde que puede "anidar" consultas en SQL, lo que le permite dividir una consulta más grande en otras más pequeñas. Quizás podrías escribir consultas para...

1. Encontrar los ID de las películas estrenadas en 2004
2. Encontrar los ID de las personas que protagonizaron esas películas
3. Encontrar los nombres de las personas con esos ID de personas

Luego, intente anidar esas consultas para llegar a una sola consulta que devuelva todas las personas que protagonizaron una película estrenada en 2004. Considere cómo podría entonces ordenar los resultados de su consulta.

### Listar los nombres de todas las personas que han dirigido una película que recibió una calificación de al menos 9.0

Observe que esta consulta, como la anterior, requiere que utilice datos de varias tablas. Recuerde que puede "anidar" consultas en SQL, lo que le permite dividir una consulta más grande en otras más pequeñas. Quizás podrías escribir consultas para...

1. Encontrar los ID de las películas con una calificación de al menos 9.0
2. Encontrar los ID de las personas que dirigieron esas películas
3. Encontrar los nombres de las personas con esos ID de personas

Luego, intente anidar esas consultas para llegar a una sola consulta que devuelva los nombres de todas las personas que han dirigido una película que recibió una calificación de al menos 9.0.

### Listar los títulos de las cinco películas mejor calificadas (en orden) que protagonizó Chadwick Boseman, comenzando con la mejor calificada

Observe que esta consulta, como la anterior, requiere que utilice datos de varias tablas. Recuerde que puede "anidar" consultas en SQL, lo que le permite dividir una consulta más grande en otras más pequeñas. Quizás podrías escribir consultas para...

1. Encontrar el ID de Chadwick Boseman
2. Encontrar los ID de las películas asociadas con el ID de Chadwick Boseman
3. Encontrar los títulos de las películas con esos ID de películas

Luego, intente anidar esas consultas para llegar a una consulta única que devuelva los títulos de las películas de Chadwick Boseman.

A partir de ahí, deberá determinar las calificaciones de esos títulos y ordenarlos por calificación, en orden descendente. Considere cómo podría combinar una tabla relevante (¡probablemente `calificaciones`!) y ordenar los resultados por una columna relevante.

Finalmente, lee sobre la palabra clave [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) de SQL, que devolverá las \\(n\\) filas principales en una consulta.

### Enumere los títulos de todas las películas en las que Bradley Cooper y Jennifer Lawrence hayan actuado.

Tenga en cuenta que esta consulta, como la anterior, requiere que utilice datos de varias tablas. Recuerde que puede "anidar" consultas en SQL, lo que le permite dividir una consulta más grande en otras más pequeñas. Quizás podría escribir consultas para...

1. Encontrar el ID de Bradley Cooper
2. Encontrar el ID de Jennifer Lawrence
3. Encontrar los ID de las películas asociadas con el ID de Bradley Cooper
4. Encontrar los ID de las películas asociadas con el ID de Jennifer Lawrence
5. Encontrar títulos de películas a partir de los ID de películas asociadas con _tanto_ Bradley Cooper como Jennifer Lawrence

Así, intente anidar las consultas para obtener una consulta única que devuelva las películas en las que actuaron Bradley Cooper y Jennifer Lawrence.

Recuerde que puede crear condiciones compuestas en SQL mediante `AND` y `OR`.

### Enumere los nombres de todas las personas que actuaron en una película en la que también actuó Kevin Bacon.

Tenga en cuenta que esta consulta, como la anterior, requiere que utilice datos de varias tablas. Recuerde que puede "anidar" consultas en SQL, lo que le permite dividir una consulta más grande en otras más pequeñas. Quizás podría escribir consultas para...

1. Encontrar el ID de Kevin Bacon (¡el nacido en 1958!)
2. Encontrar los ID de las películas asociadas con el ID de Kevin Bacon
3. Encontrar los ID de las personas asociadas con esos ID de películas
4. Encontrar los nombres de personas con esos ID de personas

Así, intente anidar las consultas para obtener una consulta única que devuelva los nombres de todas las personas que actuaron en una película en la que también actuó Kevin Bacon. **¡Tenga en cuenta que querrá excluir al propio Kevin Bacon de los resultados!**

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Uso

Para probar sus consultas en VS Code, puede consultar la base de datos ejecutando

    $ cat filename.sql | sqlite3 movies.db

donde `filename.sql` es el archivo que contiene su consulta SQL.

También puede ejecutar

    $ cat filename.sql | sqlite3 movies.db > output.txt

para redirigir la salida de la consulta a un archivo de texto llamado `output.txt`. (¡Esto puede ser útil para verificar cuántas filas devuelve su consulta!)

## Cómo probar

Si bien `check50` está disponible para este problema, se le recomienda que pruebe su código por su cuenta para cada una de las siguientes acciones. Puede ejecutar `sqlite3 movies.db` para ejecutar consultas adicionales en la base de datos y asegurarse de que su resultado sea correcto.

Si está utilizando la base de datos `movies.db` proporcionada en la distribución de este set de problemas, debería encontrar que

- La ejecución de `1.sql` da como resultado una tabla con 1 columna y 10,276 filas.
- La ejecución de `2.sql` da como resultado una tabla con 1 columna y 1 fila.
- La ejecución de `3.sql` da como resultado una tabla con 1 columna y 110,014 filas.
- La ejecución de `4.sql` da como resultado una tabla con 1 columna y 1 fila.
- La ejecución de `5.sql` da como resultado una tabla con 2 columnas y 11 filas.
- La ejecución de `6.sql` da como resultado una tabla con 1 columna y 1 fila.
- La ejecución de `7.sql` da como resultado una tabla con 2 columnas y 7,192 filas.
- La ejecución de `8.sql` da como resultado una tabla con 1 columna y 4 filas.
- La ejecución de `9.sql` da como resultado una tabla con 1 columna y 19,325 filas.
- La ejecución de `10.sql` da como resultado una tabla con 1 columna y 3,854 filas.
- La ejecución de `11.sql` da como resultado una tabla con 1 columna y 5 filas.
- La ejecución de `12.sql` da como resultado una tabla con 1 columna y 4 filas.
- La ejecución de `13.sql` da como resultado una tabla con 1 columna y 182 filas.

Tenga en cuenta que los conteos de filas no incluyen las filas de encabezado que solo muestran nombres de columna.

Si su consulta devuelve un número de filas ligeramente diferente al resultado esperado, asegúrese de que está manejando los duplicados correctamente. En el caso de las consultas que solicitan una lista de nombres, ninguna persona debe aparecer dos veces, pero dos personas diferentes con el mismo nombre deben aparecer cada una.

### Corrección

    check50 cs50/problems/2024/x/movies

## Cómo enviar

    submit50 cs50/problems/2024/x/movies

## Agradecimientos

Información cortesía de IMDb ([imdb.com](https://www.imdb.com)). Usado con permiso.

