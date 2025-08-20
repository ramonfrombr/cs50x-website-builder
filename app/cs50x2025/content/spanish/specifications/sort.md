# Ordenar

## Problema a resolver

Recuerda que en clase vimos algunos algoritmos para ordenar una secuencia de números: ordenación por selección, ordenación por burbuja y ordenación por fusión.

- La ordenación por selección itera sobre las partes no ordenadas de una lista, seleccionando el elemento más pequeño cada vez y moviéndolo a su ubicación correcta.
- La ordenación por burbuja compara pares de valores adyacentes uno a la vez y los intercambia si están en el orden incorrecto. Esto continúa hasta que la lista esté ordenada.
- La ordenación por fusión divide recursivamente la lista en dos repetidamente y luego fusiona las listas más pequeñas en una más grande en el orden correcto.

En este problema, analizarás tres programas de ordenación (¡compilados!) para determinar qué algoritmos utilizan. En un archivo llamado `answers.txt` en una carpeta llamada `sort`, registra tus respuestas, junto con una explicación para cada programa, rellenando los espacios en blanco marcados con `TODO`.

## Código de distribución

Para este problema, necesitarás un "código de distribución", es decir, código escrito por el personal de CS50. Se te proporcionan tres programas C ya compilados, `sort1`, `sort2` y `sort3`, así como varios archivos `.txt` para la entrada y otro archivo, `answers.txt`, en el que escribir tus respuestas. Cada uno de los programas `sort1`, `sort2` y `sort3` implementa un algoritmo de ordenación diferente: ordenación por selección, ordenación por burbuja u ordenación por fusión (¡aunque no necesariamente en ese orden!). Tu tarea es determinar qué algoritmo de ordenación utiliza cada archivo. Comienza descargando estos archivos.

### Descarga los archivos de distribución

Abre [VS Code](https://cs50.dev/).

Comienza haciendo clic dentro de la ventana de tu terminal, luego ejecuta `cd` por sí mismo. Deberías encontrar que su "indicación" se asemeja a la siguiente.

    $

Haz clic dentro de esa ventana de terminal y luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/3/sort.zip

seguido de Enter para descargar un ZIP llamado `sort.zip` en tu codespace. ¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, ni ningún otro carácter!

Ahora ejecuta

    unzip sort.zip

para crear una carpeta llamada `sort`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm sort.zip

y responde con "y" seguido de Enter en la indicación para eliminar el archivo ZIP que descargaste.

## Sugerencias

### Explora los archivos `.txt`

- Se te proporcionan varios archivos `.txt`. Estos archivos contienen `n` líneas de valores, invertidos, mezclados u ordenados.
    - Por ejemplo, `reversed10000.txt` contiene 10000 líneas de números que se invierten desde `10000`, mientras que `random50000.txt` contiene 50000 líneas de números en orden aleatorio.
- Los diferentes tipos de archivos `.txt` pueden ayudarte a determinar qué orden es cuál. Considera cómo se comporta cada algoritmo con una lista ya ordenada. ¿Qué tal una lista invertida? ¿O una lista mezclada? Puede resultar útil trabajar con una lista más pequeña de cada tipo y recorrer cada proceso de ordenación.

### Mide el tiempo de cada ordenación con diferentes entradas

- Para ejecutar las ordenaciones en los archivos de texto, en el terminal, ejecuta `./[nombre_programa] [archivo_texto.txt]`. ¡Asegúrate de haber utilizado `cd` para desplazarte al directorio `sort`!
    - Por ejemplo, para ordenar `reversed10000.txt` con `sort1`, ejecuta `./sort1 reversed10000.txt`.
- Puede resultarte útil medir el tiempo de tus ordenaciones. Para hacerlo, ejecuta `time ./[archivo_clasificación] [archivo_texto.txt]`.
    - Por ejemplo, podrías ejecutar `time ./sort1 reversed10000.txt` para ejecutar `sort1` en 10.000 números invertidos. Al final de la salida de tu terminal, puedes consultar el tiempo `real` para ver cuánto tiempo transcurrió realmente mientras se ejecutaba el programa.

## Tutorial

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>

<details><summary>¿No estás seguro de cómo resolverlo?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>

## Cómo probar

### Corrección

    check50 cs50/problems/2024/x/sort

## Cómo enviar

    submit50 cs50/problems/2024/x/sort