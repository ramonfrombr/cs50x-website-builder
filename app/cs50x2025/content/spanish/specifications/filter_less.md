# Filtro

![Harvard Yard en escala de grises](https://cs50.harvard.edu/x/2024/psets/4/filter/less/yard-grayscale.bmp)

## Problema a Resolver

Quizás la forma más simple de representar una imagen sea con una cuadrícula de píxeles (es decir, puntos), cada uno de los cuales puede tener un color diferente. Para imágenes en blanco y negro, necesitamos 1 bit por píxel, donde 0 podría representar negro y 1 podría representar blanco, como se muestra a continuación.

![un mapa de bits simple](https://cs50.harvard.edu/x/2024/psets/4/filter/less/bitmap.png)

En este sentido, una imagen es simplemente un mapa de bits (bitmap). Para imágenes más coloridas, se necesitan más bits por píxel. Un formato de archivo (como [BMP](https://es.wikipedia.org/wiki/BMP), [JPEG](https://es.wikipedia.org/wiki/JPEG) o [PNG](https://es.wikipedia.org/wiki/Portable_Network_Graphics)) que soporta "color de 24 bits" utiliza 24 bits por píxel. (BMP en realidad soporta colores de 1, 4, 8, 16, 24 y 32 bits).

Un BMP de 24 bits utiliza 8 bits para indicar la cantidad de rojo en el color de un píxel, 8 bits para indicar la cantidad de verde y 8 bits para indicar la cantidad de azul. Si alguna vez has oído hablar del color RGB, bueno, aquí lo tienes: rojo, verde, azul.

Si los valores R, G y B de algún píxel en un BMP son, por ejemplo, `0xff`, `0x00` y `0x00` en hexadecimal, ese píxel es completamente rojo, ya que `0xff` (también conocido como `255` en decimal) implica "mucho rojo", mientras que `0x00` y `0x00` implican "ningún verde" y "ningún azul", respectivamente. En este problema, manipularás estos valores R, G y B de los píxeles individuales, creando tus propios filtros de imagen.

En un archivo llamado `helpers.c` en una carpeta llamada `filter-less`, escribe un programa para aplicar filtros a BMPs.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QnLel70SPmbW9nswXTb9Yu9ZD" src="https://asciinema.org/a/QnLel70SPmbW9nswXTb9Yu9ZD.js"></script>

## Código de Distribución

Para este problema, extenderás la funcionalidad del código proporcionado por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el indicador de tu ventana de terminal se parece al siguiente:

    $

Luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-less.zip

para descargar un archivo ZIP llamado `filter-less.zip` en tu espacio de trabajo.

Después ejecuta

    unzip filter-less.zip

para crear una carpeta llamada `filter-less`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm filter-less.zip

y responde "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd filter-less

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu prompt ahora debería parecerse al siguiente:

    filter-less/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` y `Makefile`. También deberías ver una carpeta llamada `images/` con cuatro archivos BMP. Si encuentras algún problema, sigue estos mismos pasos nuevamente y trata de determinar dónde te equivocaste.

## Antecedentes

### Un Poco Más Técnico Acerca de los Bit(mapas)

Recuerda que un archivo es simplemente una secuencia de bits organizados de alguna manera. Un archivo BMP de 24 bits, entonces, es esencialmente una secuencia de bits, donde casi cada 24 bits representan el color de algún píxel. Pero un archivo BMP también contiene algunos "metadatos", información como la altura y anchura de una imagen. Estos metadatos se almacenan al principio del archivo en forma de dos estructuras de datos generalmente conocidas como "encabezados", no deben confundirse con los archivos de encabezado de C. (Por cierto, estos encabezados han evolucionado con el tiempo. Este problema utiliza la versión más reciente del formato BMP de Microsoft, 4.0, que debutó con Windows 95.)

El primero de estos encabezados, llamado `BITMAPFILEHEADER`, tiene una longitud de 14 bytes. (Recuerda que 1 byte equivale a 8 bits.) El segundo de estos encabezados, llamado `BITMAPINFOHEADER`, tiene una longitud de 40 bytes. Inmediatamente después de estos encabezados está el mapa de bits real: un array de bytes, triples de los cuales representan el color de un píxel. Sin embargo, BMP almacena estos triples al revés (es decir, como BGR), con 8 bits para azul, seguidos de 8 bits para verde, y finalmente 8 bits para rojo. (Algunos BMP también almacenan todo el mapa de bits al revés, con la fila superior de una imagen al final del archivo BMP. Pero hemos almacenado los BMP de este conjunto de problemas como se describe aquí, con la primera fila de cada mapa de bits al principio y la última fila al final.) En otras palabras, si convirtiéramos el smiley de 1 bit anterior a un smiley de 24 bits, sustituyendo el negro por rojo, un BMP de 24 bits almacenaría este mapa de bits de la siguiente manera, donde `0000ff` representa rojo y `ffffff` representa blanco; hemos resaltado en rojo todas las instancias de `0000ff`.

![sonrisa roja](https://cs50.harvard.edu/x/2024/psets/4/filter/less/red_smile.png)

Debido a que hemos presentado estos bits de izquierda a derecha, de arriba hacia abajo, en 8 columnas, puedes ver realmente la sonrisa roja si das un paso atrás.

Para ser claro, recuerda que un dígito hexadecimal representa 4 bits. Por lo tanto, `ffffff` en hexadecimal realmente significa `111111111111111111111111` en binario.

Observa que podrías representar un mapa de bits como una matriz bidimensional de píxeles: donde la imagen es un array de filas, cada fila es un array de píxeles. De hecho, así es como hemos elegido representar imágenes de mapa de bits en este problema.

### Filtrado de Imágenes

¿Qué significa filtrar una imagen? Puedes pensar en filtrar una imagen como tomar los píxeles de una imagen original y modificar cada píxel de tal manera que un efecto particular sea evidente en la imagen resultante.

## Comprensión

Ahora veamos algunos de los archivos proporcionados como código de distribución para entender qué contienen.

### `bmp.h`

Abre `bmp.h` (doble clic en él en el navegador de archivos) y échale un vistazo.

Verás las definiciones de los encabezados que mencionamos (`BITMAPINFOHEADER` y `BITMAPFILEHEADER`). Además, este archivo define `BYTE`, `DWORD`, `LONG` y `WORD`, tipos de datos que normalmente se encuentran en el mundo de la programación de Windows. Observa cómo son simplemente alias para los tipos primitivos con los que ya estás (esperamos) familiarizado. Parece que `BITMAPFILEHEADER` y `BITMAPINFOHEADER` utilizan estos tipos.

Quizás lo más importante para ti, este archivo también define una `struct` llamada `RGBTRIPLE` que, simplemente, "encapsula" tres bytes: uno azul, uno verde y uno rojo (el orden, recuerda, en el que esperamos encontrar triples RGB en disco).

¿Por qué son útiles estas `struct`s? Bueno, recuerda que un archivo es simplemente una secuencia de bytes (o, en última instancia, bits) en disco. Pero esos bytes generalmente están ordenados de tal manera que los primeros representan algo, los siguientes representan otra cosa y así sucesivamente. Los "formatos de archivo" existen porque el mundo ha estandarizado qué bytes significan qué cosas. Ahora, podríamos leer un archivo desde el disco en RAM como un gran array de bytes. Y podríamos recordar que el byte en `array[i]` representa una cosa, mientras que el byte en `array[j]` representa otra. Pero ¿por qué no darle nombres a algunos de esos bytes para que podamos recuperarlos de la memoria más fácilmente? Eso es precisamente lo que permiten hacer las `struct`s en `bmp.h`. En lugar de pensar en un archivo como una larga secuencia de bytes, podemos pensar en él como una secuencia de `struct`s.

### `filter.c`

Ahora, abre `filter.c`. Este archivo ya ha sido escrito para ti, pero hay algunos puntos importantes que vale la pena destacar aquí.

Primero, observa la definición de `filters` en la línea 10. Esa cadena le dice al programa cuáles son los argumentos permitidos desde la línea de comandos: `b`, `g`, `r` y `s`. Cada uno de ellos especifica un filtro diferente que podemos aplicar a nuestras imágenes: desenfoque, escala de grises, reflexión y sepia.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea realmente un archivo BMP y leen toda la información de píxeles en una matriz bidimensional llamada `image`.

Desplázate hacia abajo hasta la declaración `switch` que comienza en la línea 101. Observa que, dependiendo del `filtro` que hayamos elegido, se llama a una función diferente: si el usuario elige el filtro `b`, el programa llama a la función `blur`; si es `g`, llama a `grayscale`; si es `r`, llama a `reflect`; y si es `s`, llama a `sepia`. Además, cada una de estas funciones recibe como argumentos la altura de la imagen, la anchura de la imagen y la matriz bidimensional de píxeles.

Estas son las funciones que implementarás pronto. Como puedes imaginar, el objetivo es que cada una de estas funciones edite la matriz bidimensional de píxeles de tal manera que se aplique el filtro deseado a la imagen.

Las líneas restantes del programa toman la imagen resultante y la escriben en un nuevo archivo de imagen.

### `helpers.h`

A continuación, echa un vistazo a `helpers.h`. Este archivo es bastante corto y simplemente proporciona los prototipos de las funciones que viste anteriormente.

Aquí, ten en cuenta que cada función toma como argumento una matriz bidimensional llamada `image`, donde `image` es un array de `height` filas y cada fila es a su vez otro array de `width` estructuras `RGBTRIPLE`. Por lo tanto, si `image` representa toda la imagen, entonces `image[0]` representa la primera fila y `image[0][0]` representa el píxel en la esquina superior izquierda de la imagen.

### `helpers.c`

Ahora, abre `helpers.c`. Aquí es donde pertenece la implementación de las funciones declaradas en `helpers.h`. Pero ten en cuenta que ¡las implementaciones actualmente faltan! Esta parte depende de ti.

### `Makefile`

Finalmente, echemos un vistazo a `Makefile`. Este archivo especifica qué debe ocurrir cuando ejecutamos un comando en la terminal como `make filter`. Mientras que los programas que podrías haber escrito antes estaban confinados a un solo archivo, `filter` parece usar varios archivos: `filter.c` y `helpers.c`. Por lo tanto, debemos decirle a `make` cómo compilar este archivo.

Intenta compilar `filter` por ti mismo yendo a tu terminal y ejecutando

    $ make filter

Luego, puedes ejecutar el programa escribiendo:

    $ ./filter -g images/yard.bmp out.bmp

lo cual toma la imagen en `images/yard.bmp` y genera una nueva imagen llamada `out.bmp` después de pasar los píxeles a través de la función `grayscale`. Aunque la función `grayscale` aún no hace nada, por lo que la imagen de salida debería lucir igual que la imagen original del jardín.

## Especificación

Implementa las funciones en `helpers.c` de manera que el usuario pueda aplicar filtros de escala de grises, sepia, reflexión o desenfoque a sus imágenes.

- La función `grayscale` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma.
- La función `sepia` debe tomar una imagen y convertirla en una versión sepia de la misma.
- La función `reflect` debe tomar una imagen y reflejarla horizontalmente.
- Finalmente, la función `blur` debe tomar una imagen y convertirla en una versión desenfocada.

No debes modificar ninguna de las firmas de las funciones, ni tampoco debes modificar otros archivos aparte de `helpers.c`.

## Pistas

### Implementar `grayscale`

Un filtro común es el filtro de "escala de grises", donde tomamos una imagen y queremos convertirla a blanco y negro. ¿Cómo funciona esto?

- Recuerda que si los valores de rojo, verde y azul están todos configurados en `0x00` (hexadecimal para `0`), entonces el píxel es negro. Y si todos los valores están configurados en `0xff` (hexadecimal para `255`), entonces el píxel es blanco. Mientras más altos sean los valores de rojo, verde y azul, más claro será el tono de gris (más cercano al blanco) y mientras más bajos sean, más oscuro será el tono de gris (más cercano al negro).
- Entonces, para convertir un píxel a escala de grises, solo necesitas asegurarte de que los valores de rojo, verde y azul sean todos iguales. Pero ¿cómo sabes qué valor hacerles? Bueno, probablemente sea razonable esperar que si los valores originales de rojo, verde y azul eran bastante altos, entonces el nuevo valor también debería ser bastante alto. Y si los valores originales eran bajos, entonces el nuevo valor también debería ser bajo.
- De hecho, para asegurarte de que cada píxel de la nueva imagen tenga la misma luminosidad o oscuridad general que la imagen original, puedes tomar el **promedio** de los valores de rojo, verde y azul para determinar qué tono de gris hacer el nuevo píxel.

Si aplicas el algoritmo anterior a cada píxel de la imagen, el resultado será una imagen convertida a escala de grises. Escribe un pseudocódigo para ayudarte a resolver este problema.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Recorrer todos los píxeles

            // Tomar el promedio de rojo, verde y azul

            // Actualizar los valores del píxel
    }

Primero, ¿cómo podrías recorrer todos los píxeles? Recuerda que los píxeles de la imagen están almacenados en el array bidimensional `image`. Para iterar sobre un array bidimensional, necesitarás dos bucles, uno dentro del otro.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Recorrer todos los píxeles
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Tomar el promedio de rojo, verde y azul

                // Actualizar los valores del píxel
            }
        }
    }

Ahora, puedes usar `image[i][j]` para acceder a cualquier píxel individual de la imagen. Pero ¿cómo tomar el promedio de los elementos rojo, verde y azul? Recuerda que cada elemento de `image` es un `RGBTRIPLE`, que es la `struct` definida en `bmp.h` para representar un píxel. La sintaxis usual para acceder a los miembros de una `struct` se aplica aquí, donde `image[i][j].rgbtRed` te dará acceso al valor rojo de `RGBTRIPLE`, `image[i][j].rgbtGreen` te dará acceso a su valor verde, y así sucesivamente.

Cuando calcules el promedio de los valores de rojo, verde y azul del píxel en un color gris resultante, ten en cuenta que los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos enteros. ¡Así que asegúrate de [redondear](https://manual.cs50.io/3/round) cualquier número de punto flotante al entero más cercano al asignarlos al valor del píxel! Y ¿por qué podrías querer dividir la suma de estos enteros por 3.0 y no por 3?

Una vez que hayas promediado los valores de rojo, verde y azul del píxel en un color gris resultante, procede y actualiza los valores de rojo, verde y azul del píxel. ¡A estas alturas, ya estás familiarizado con la sintaxis para la asignación!

### Implementar `sepia`

La mayoría de los programas de edición de imágenes soportan un filtro de "sepia", que hace que las imágenes luzcan antiguas al teñir toda la imagen de un tono marrón rojizo.

- Una imagen se puede convertir a sepia al tomar cada píxel y calcular nuevos valores de rojo, verde y azul basados en los valores originales de los tres.
- Hay varios algoritmos para convertir una imagen a sepia, pero para este problema, te pediremos que uses el siguiente algoritmo. Para cada píxel, los valores de color sepia deben calcularse basados en los valores de color originales según los siguientes.
  sepiaRed = .393 _ originalRed + .769 _ originalGreen + .189 _ originalBlue
  sepiaGreen = .349 _ originalRed + .686 _ originalGreen + .168 _ originalBlue
  sepiaBlue = .272 _ originalRed + .534 _ originalGreen + .131 \* originalBlue

- Por supuesto, el resultado de cada una de estas fórmulas podría no ser un entero, pero cada valor podría redondearse al entero más cercano. También es posible que el resultado de la fórmula sea un número más grande que 255, el valor máximo para un valor de color de 8 bits. En ese caso, los valores de rojo, verde y azul deben limitarse a 255. Como resultado, podemos garantizar que los valores resultantes de rojo, verde y azul serán números enteros entre 0 y 255, inclusive.

Escribe un pseudocódigo para ayudarte a resolver este problema y recuerda el uso de bucles `for` anidados para visitar cada píxel.

    void sepia(int height, int width, RGBTRIPLE image[height][width])
    {
        // Recorrer todos los pixeles
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Calcular los valores sepia

                // Actualizar el píxel con los valores sepia
            }
        }
    }

Para calcular los valores `sepia`, revisa los puntos anteriores. Tienes una fórmula para calcular los valores sepia, pero todavía hay algunos detalles. En particular, necesitarás...

- Redondear el resultado de cada cálculo al entero más cercano
- Asegurar que el valor resultante no sea superior a 255

¿Cómo podría ser útil una función que devuelve el menor de dos enteros al implementar `sepia`, particularmente cuando necesitas asegurarte de que el valor de un color no sea superior a 255? ¡Eres bienvenido, pero no es obligatorio, a escribir una función auxiliar propia para hacer eso!

### Implementar `reflect`

Algunos filtros también podrían mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro donde la imagen resultante es lo que se obtendría al colocar la imagen original frente a un espejo.

- Cualquier píxel en el lado izquierdo de la imagen debe terminar en el derecho, y viceversa.
- Ten en cuenta que todos los píxeles originales de la imagen original todavía estarán presentes en la imagen reflejada, solo que esos píxeles pueden haber sido reorganizados para estar en un lugar diferente en la imagen.

Entonces, en la función `reflect`, necesitarás intercambiar los valores de los píxeles en lados opuestos de una fila. Escribe un pseudocódigo para ayudarte a comenzar:

    void reflect(int height, int width, RGBTRIPLE image[height][width])
    {
        // Recorrer todos los pixeles
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Intercambiar pixeles
            }
        }
    }

Recuerda de la clase cómo implementamos el intercambio de dos valores con una variable temporal. ¡No es necesario usar una función separada para el intercambio a menos que lo desees!

Y ahora es un buen momento para pensar en tus bucles `for` anidados. El bucle `for` externo itera sobre cada fila, mientras que el bucle `for` interno itera sobre cada píxel en esa fila. Sin embargo, para reflejar con éxito una fila, ¿necesitas iterar sobre cada píxel en ella?

### Implementa `blur`

Hay varias formas de crear el efecto de desenfoque o suavizar una imagen. Para este problema, utilizaremos el "desenfoque por caja", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor al promediar los valores de color de píxeles vecinos.

- Considera la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.
  ![una cuadrícula de píxeles](grid.png)
- El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando una caja de 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores de color originales de píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (ten en cuenta que el propio píxel 6 está incluido en el promedio). Del mismo modo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.
- Para un píxel a lo largo del borde o esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.

Al implementar la función `blur`, es posible que descubras que el desenfoque de un píxel termina afectando el desenfoque de otro píxel. Podría ser mejor crear una copia de `image` declarando una nueva matriz bidimensional con código como `RGBTRIPLE copy[height][width];`. Luego copia `image` en `copy`, píxel por píxel, con bucles `for` anidados, como se muestra a continuación:

    void blur(int height, int width, RGBTRIPLE image[height][width])
    {
        // Crea una copia de image
        RGBTRIPLE copy[height][width];
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                copy[i][j] = image[i][j];
            }
        }
    }

¡Ahora, puedes leer los colores de los píxeles desde `copy` pero escribir (es decir, cambiar) los colores de los píxeles en `image`!

## Tutorial

**Ten en cuenta que hay 5 videos en esta lista de reproducción.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>

## Cómo probar

¡Asegúrate de probar todos tus filtros en los archivos de mapa de bits de muestra proporcionados!

### Corrección

    check50 cs50/problems/2024/x/filter/less

### Estilo

    style50 helpers.c

## Cómo enviar

    submit50 cs50/problems/2024/x/filter/less
