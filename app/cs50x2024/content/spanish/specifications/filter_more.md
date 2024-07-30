# Filtro

![Harvard Yard con detección de bordes](https://cs50.harvard.edu/x/2024/psets/4/filter/more/yard-edges.bmp)

## Problema a Resolver

Quizás la forma más simple de representar una imagen es con una cuadrícula de píxeles (es decir, puntos), cada uno de los cuales puede tener un color diferente. Para imágenes en blanco y negro, necesitamos 1 bit por píxel, donde 0 podría representar negro y 1 podría representar blanco, como se muestra a continuación.

![un simple mapa de bits](https://cs50.harvard.edu/x/2024/psets/4/filter/more/bitmap.png)

En este sentido, una imagen es simplemente un mapa de bits (bitmap). Para imágenes más coloridas, simplemente necesitas más bits por píxel. Un formato de archivo (como [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG) o [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) que soporta "color de 24 bits" utiliza 24 bits por píxel. (BMP de hecho soporta colores de 1, 4, 8, 16, 24 y 32 bits.)

Un BMP de 24 bits utiliza 8 bits para significar la cantidad de rojo en el color de un píxel, 8 bits para significar la cantidad de verde y 8 bits para significar la cantidad de azul. Si alguna vez has oído hablar del color RGB, ahí lo tienes: rojo, verde, azul.

Si los valores de R, G y B de algún píxel en un BMP son, digamos, `0xff`, `0x00` y `0x00` en hexadecimal, ese píxel es puramente rojo, ya que `0xff` (también conocido como `255` en decimal) implica "mucho rojo", mientras que `0x00` e `0x00` implican "ningún verde" y "ningún azul", respectivamente. En este problema, manipularás estos valores de R, G y B de píxeles individuales, creando tus propios filtros de imágenes.

En un archivo llamado `helpers.c` en una carpeta llamada `filter-more`, escribe un programa para aplicar filtros a archivos BMP.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DC5vtWOatmXC3Ff825YxHE0CZ" src="https://asciinema.org/a/DC5vtWOatmXC3Ff825YxHE0CZ.js"></script>

## Código de Distribución

Para este problema, ampliarás la funcionalidad del código proporcionado por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu ventana de terminal se asemeja al siguiente:

    $

Luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-more.zip

para descargar un archivo ZIP llamado `filter-more.zip` en tu espacio de trabajo.

Después ejecuta

    unzip filter-more.zip

para crear una carpeta llamada `filter-more`. Ya no necesitas el archivo ZIP, así que ejecuta

    rm filter-more.zip

y responde "y" seguido de Enter en el prompt para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd filter-more

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu prompt debería parecerse al siguiente.

    filter-more/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` y `Makefile`. También deberías ver una carpeta llamada `images` con cuatro archivos BMP. Si encuentras algún problema, sigue estos mismos pasos nuevamente y determina dónde te equivocaste.

## Antecedentes

### Un Poco Más Técnico de un Mapa de Bits

Recuerda que un archivo es simplemente una secuencia de bits, organizados de alguna manera. Un archivo BMP de 24 bits, entonces, es esencialmente solo una secuencia de bits, casi cada 24 de los cuales representan el color de un píxel. Pero un archivo BMP también contiene metadatos, como la altura y anchura de una imagen. Esa información se almacena al inicio del archivo en forma de dos estructuras de datos generalmente denominadas "encabezados", que no deben confundirse con los archivos de encabezado de C. (Por cierto, estos encabezados han evolucionado con el tiempo. Este problema utiliza la versión más reciente del formato BMP de Microsoft, 4.0, que debutó con Windows 95.)

El primero de estos encabezados, llamado `BITMAPFILEHEADER`, tiene una longitud de 14 bytes. (Recuerda que 1 byte equivale a 8 bits.) El segundo de estos encabezados, llamado `BITMAPINFOHEADER`, tiene una longitud de 40 bytes. Inmediatamente después de estos encabezados está el mapa de bits real: una matriz de bytes, triples de los cuales representan el color de un píxel. Sin embargo, BMP almacena estos triples al revés (es decir, como BGR), con 8 bits para azul, seguidos de 8 bits para verde, seguidos de 8 bits para rojo. (Algunos BMP también almacenan el mapa de bits completo al revés, con la fila superior de una imagen al final del archivo BMP. Pero hemos almacenado los BMP de este conjunto de problemas como se describe aquí, con la primera fila superior de cada mapa de bits y la última fila inferior.) En otras palabras, si convirtiéramos el emoticono de 1 bit anterior a un emoticono de 24 bits, sustituyendo el negro por rojo, un BMP de 24 bits almacenaría este mapa de bits de la siguiente manera, donde `0000ff` significa rojo y `ffffff` significa blanco; hemos resaltado en rojo todas las instancias de `0000ff`.

![sonrisa roja](https://cs50.harvard.edu/x/2024/psets/4/filter/more/red_smile.png)

Dado que hemos presentado estos bits de izquierda a derecha, de arriba hacia abajo, en 8 columnas, realmente puedes ver la sonrisa roja si das un paso atrás.

Para ser claro, recuerda que un dígito hexadecimal representa 4 bits. En consecuencia, `ffffff` en hexadecimal realmente significa `111111111111111111111111` en binario.

Observa que podrías representar un mapa de bits como una matriz bidimensional de píxeles: donde la imagen es una matriz de filas, cada fila es una matriz de píxeles. De hecho, así es como hemos elegido representar las imágenes de mapa de bits en este problema.

### Filtrado de Imágenes

¿Qué significa filtrar una imagen? Puedes pensar en filtrar una imagen como tomar los píxeles de alguna imagen original y modificar cada píxel de tal manera que un efecto particular sea evidente en la imagen resultante.

#### Escala de Grises

Un filtro común es el filtro "escala de grises", donde tomamos una imagen y queremos convertirla a blanco y negro. ¿Cómo funciona esto?

Recuerda que si los valores de rojo, verde y azul están todos establecidos en `0x00` (hexadecimal para `0`), entonces el píxel es negro. Y si todos los valores están establecidos en `0xff` (hexadecimal para `255`), entonces el píxel es blanco. Siempre y cuando los valores de rojo, verde y azul sean iguales, el resultado será diferentes tonos de gris a lo largo del espectro de blanco y negro, con valores más altos significando tonos más claros (más cerca del blanco) y valores más bajos significando tonos más oscuros (más cerca del negro).

Por lo tanto, para convertir un píxel a escala de grises, solo necesitamos asegurarnos de que los valores de rojo, verde y azul sean todos iguales. Pero, ¿cómo sabemos qué valor asignarles? Bueno, probablemente sea razonable esperar que si los valores originales de rojo, verde y azul eran bastante altos, entonces el nuevo valor también debería ser alto. Y si los valores originales eran bajos, entonces el nuevo valor también debería ser bajo.

De hecho, para asegurar que cada píxel de la nueva imagen tenga el mismo brillo o oscuridad general que la imagen original, podemos tomar el promedio de los valores de rojo, verde y azul para determinar qué tono de gris asignar al nuevo píxel.

Si aplicas eso a cada píxel en la imagen, el resultado será una imagen convertida a escala de grises.

#### Reflejo

Algunos filtros también podrían mover los píxeles. Reflejar una imagen, por ejemplo, es un filtro donde la imagen resultante es lo que obtendrías al colocar la imagen original frente a un espejo. Entonces, cualquier píxel en el lado izquierdo de la imagen debería terminar en el lado derecho, y viceversa.

Nota que todos los píxeles originales de la imagen original seguirán presentes en la imagen reflejada, solo que esos píxeles pueden haberse reorganizado a un lugar diferente en la imagen.

#### Desenfoque

Hay varias formas de crear el efecto de desenfoque o suavizado en una imagen. Para este problema, utilizaremos el "desenfoque de caja", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles vecinos.

Considera la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.

![una cuadrícula de píxeles](https://cs50.harvard.edu/x/2024/psets/4/filter/more/grid.png)

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando una caja 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores originales de color de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (nota que el píxel 6 en sí mismo está incluido en el promedio). Del mismo modo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel a lo largo del borde o esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.

#### Bordes

En los algoritmos de inteligencia artificial para el procesamiento de imágenes, a menudo es útil detectar bordes en una imagen: líneas en la imagen que crean un límite entre un objeto y otro. Una forma de lograr este efecto es aplicando el [operador Sobel](https://en.wikipedia.org/wiki/Sobel_operator) a la imagen.

Al igual que el desenfoque de imágenes, la detección de bordes también funciona tomando cada píxel y modificándolo basándose en la cuadrícula 3x3 de píxeles que rodea ese píxel. Pero en lugar de simplemente tomar el promedio de los nueve píxeles, el operador Sobel calcula el nuevo valor de cada píxel tomando una suma ponderada de los valores de los píxeles circundantes. Y dado que los bordes entre objetos pueden ocurrir tanto en dirección vertical como horizontal, realmente calcularás dos sumas ponderadas: una para detectar bordes en la dirección x y otra para detectar bordes en la dirección y. En particular, utilizarás los siguientes dos "núcleos":

![núcleos Sobel](https://cs50.harvard.edu/x/2024/psets/4/filter/more/sobel.png)

¿Cómo interpretar estos núcleos? En resumen, para cada uno de los tres valores de color para cada píxel, calcularemos dos valores `Gx` y `Gy`. Para calcular `Gx` para el valor del canal rojo de un píxel, por ejemplo, tomaremos los valores originales de rojo de los nueve píxeles que forman una caja 3x3 alrededor del píxel, los multiplicaremos cada uno por el valor correspondiente en el núcleo `Gx` y tomaremos la suma de los valores resultantes.

¿Por qué estos valores particulares para el núcleo? En la dirección `Gx`, por ejemplo, estamos multiplicando los píxeles a la derecha del píxel objetivo por un número positivo, y multiplicando los píxeles a la izquierda del píxel objetivo por un número negativo. Cuando tomamos la suma, si los píxeles a la derecha son de un color similar a los píxeles a la izquierda, el resultado será cercano a 0 (los números se cancelan). Pero si los píxeles a la derecha son muy diferentes de los píxeles a la izquierda, entonces el valor resultante será muy positivo o muy negativo, indicando un cambio de color que probablemente sea el resultado de un límite entre objetos. Y un argumento similar es válido para calcular bordes en la dirección `y`.

Usando estos núcleos, podemos generar un valor `Gx` y `Gy` para cada uno de los canales rojo, verde y azul de un píxel. Pero cada canal solo puede tomar un valor, no dos: así que necesitamos alguna manera de combinar `Gx` y `Gy` en un solo valor. El algoritmo del filtro Sobel combina `Gx` y `Gy` en un valor final calculando la raíz cuadrada de `Gx^2 + Gy^2`. Y dado que los valores de los canales solo pueden ser valores enteros de 0 a 255, asegúrate de que el valor resultante esté redondeado al entero más cercano y limitado a 255.

¿Y qué hay de manejar píxeles en el borde o en la esquina de la imagen? Hay muchas formas de manejar píxeles en el borde, pero para los propósitos de este problema, te pediremos que trates la imagen como si hubiera un borde sólido negro de 1 píxel alrededor del borde de la imagen: por lo tanto, intentar acceder a un píxel más allá del borde de la imagen debería tratarse como un píxel negro sólido (valores de 0 para cada uno de rojo, verde y azul). Esto efectivamente ignorará esos píxeles en nuestros cálculos de `Gx` y `Gy`.

## Especificación

Implementa las funciones en `helpers.c` de modo que un usuario pueda aplicar filtros de escala de grises, reflejo, desenfoque o detección de bordes a sus imágenes.

- La función `grayscale` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
- La función `reflect` debe tomar una imagen y reflejarla horizontalmente.
- La función `blur` debe tomar una imagen y convertirla en una versión desenfocada tipo caja de la misma imagen.
- La función `edges` debe tomar una imagen y resaltar los bordes entre objetos, según el operador Sobel.

No debes modificar las firmas de las funciones ni tampoco modificar otros archivos aparte de `helpers.c`.

## Entendimiento

Vamos a echar un vistazo a algunos de los archivos proporcionados como código de distribución para entender qué hay dentro de ellos.

### `bmp.h`

Abre `bmp.h` (dando doble clic en él en el explorador de archivos) y observa.

Verás definiciones de los encabezados que mencionamos (`BITMAPINFOHEADER` y `BITMAPFILEHEADER`). Además, ese archivo define `BYTE`, `DWORD`, `LONG` y `WORD`, tipos de datos que normalmente se encuentran en la programación de Windows. Observa cómo son simplemente alias para primitivos con los que ya deberías estar familiarizado. Parece que `BITMAPFILEHEADER` y `BITMAPINFOHEADER` utilizan estos tipos.

Quizás lo más importante para ti, este archivo también define una `struct` llamada `RGBTRIPLE` que encapsula tres bytes: uno azul, uno verde y uno rojo (en ese orden, el orden en el que esperamos encontrar los triples RGB en disco).

¿Por qué son útiles estas `structs`? Bueno, recuerda que un archivo es simplemente una secuencia de bytes (o, en última instancia, bits) en disco. Pero esos bytes generalmente están ordenados de tal manera que los primeros representan algo, los siguientes representan otra cosa, y así sucesivamente. Los "formatos de archivo" existen porque el mundo ha estandarizado qué bytes significan qué. Ahora, podríamos simplemente leer un archivo de disco en RAM como una gran matriz de bytes. Y podríamos recordar que el byte en `array[i]` representa una cosa, mientras que el byte en `array[j]` representa otra. Pero ¿por qué no dar nombres a algunos de esos bytes para que podamos recuperarlos de la memoria más fácilmente? Eso es precisamente lo que permiten hacer las structs en `bmp.h`. En lugar de pensar en un archivo como una larga secuencia de bytes, podemos pensar en él como una secuencia de `structs`.

### `filter.c`

Ahora, abre `filter.c`. Este archivo ya está escrito para ti, pero hay algunos puntos importantes que vale la pena destacar.

Primero, nota la definición de `filters` en la línea 10. Esa cadena le dice al programa cuáles son los argumentos permitidos desde la línea de comandos: `b`, `e`, `g` y `r`. Cada uno especifica un filtro diferente que podríamos aplicar a nuestras imágenes: desenfoque, detección de bordes, escala de grises y reflejo.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea realmente un archivo BMP y leen toda la información de píxeles en una matriz 2D llamada `image`.

Desplázate hasta la declaración `switch` que comienza en la línea 101. Observa que, dependiendo del filtro que hayamos elegido, se llama a una función diferente: si el usuario elige el filtro `b`, el programa llama a la función `blur`; si `e`, entonces llama a `edges`; si `g`, llama a `grayscale`; y si `r`, llama a `reflect`. Además, cada una de estas funciones recibe como argumentos la altura de la imagen, el ancho de la imagen y la matriz 2D de píxeles.

Estas son las funciones que implementarás pronto. Como puedes imaginar, el objetivo es que cada una de estas funciones edite la matriz 2D de píxeles de tal manera que se aplique el filtro deseado a la imagen.

Las líneas restantes del programa toman la `image` resultante y la escriben en un nuevo archivo de imagen.

### `helpers.h`

Luego, echa un vistazo a `helpers.h`. Este archivo es bastante corto y solo proporciona los prototipos de funciones para las funciones que viste anteriormente.

Aquí, ten en cuenta que cada función toma una matriz 2D llamada `image` como argumento, donde `image` es una matriz de tantas filas como `height`, y cada fila es a su vez otra matriz de tantos `RGBTRIPLEs` como `width`. Entonces, si `image` representa toda la imagen, entonces `image[0]` representa la primera fila y `image[0][0]` representa el píxel en la esquina superior izquierda de la imagen.

### `helpers.c`

Ahora, abre `helpers.c`. Aquí es donde pertenece la implementación de las funciones declaradas en `helpers.h`. Pero nota que, ¡las implementaciones actualmente faltan! Esta parte depende de ti.

### `Makefile`

Finalmente, echemos un vistazo a `Makefile`. Este archivo especifica qué debería ocurrir cuando ejecutamos un comando en terminal como `make filter`. Mientras que los programas que podrías haber escrito antes estaban confinados a un solo archivo, `filter` parece usar múltiples archivos: `filter.c` y `helpers.c`. Así que necesitaremos decirle a `make` cómo compilar este archivo.

Intenta compilar `filter` por ti mismo yendo a tu terminal y ejecutando

    $ make filter

Luego, puedes ejecutar el programa con:

    $ ./filter -g images/yard.bmp out.bmp

que toma la imagen en `images/yard.bmp` y genera una nueva imagen llamada `out.bmp` después de pasar los píxeles a través de la función `grayscale`. Sin embargo, `grayscale` no hace nada por ahora, así que la imagen de salida debería lucir igual que la imagen original del jardín.

## Sugerencias

- Los valores de los componentes `rgbtRed`, `rgbtGreen` y `rgbtBlue` de un píxel son todos enteros, así que asegúrate de redondear cualquier número de punto flotante al entero más cercano al asignarlo a un valor de píxel.

## Guía paso a paso

**Ten en cuenta que hay 5 videos en esta lista de reproducción.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>

## Cómo probar

¡Asegúrate de probar todos tus filtros en los archivos de imagen de ejemplo proporcionados!

### Correctitud

    check50 cs50/problems/2024/x/filter/more

### Estilo

    style50 helpers.c

## Cómo enviar

    submit50 cs50/problems/2024/x/filter/more
