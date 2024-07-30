## Recuperar

![Imagen recuperada](https://cs50.harvard.edu/x/2024/psets/4/recover/recovered_image.png)

## Problema a resolver

Anticipándonos a este problema, hemos pasado los últimos días tomando fotos por el campus, todas las cuales se guardaron en una cámara digital como JPEG en una tarjeta de memoria. Por desgracia, las borramos todas de algún modo. Afortunadamente, en el mundo de la informática "borrar" no suele significar "borrar" sino más bien "olvidar". Aunque la cámara insista en que la tarjeta está ahora vacía, estamos seguros de que no es del todo cierto. De hecho, ¡esperamos (es más, exigimos!) que puedas escribir un programa que recupere las fotos para nosotros!

En un archivo llamado `recover.c` dentro de la carpeta `recover`, escribe un programa para recuperar JPEG de una tarjeta de memoria.

## Código de distribución

Para este problema, ampliarás la funcionalidad del código proporcionado por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana del terminal y ejecuta `cd` solo. Verás que el indicador de la ventana del terminal se parece a lo siguiente:

    $

Ahora ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/4/recover.zip

para descargar en tu espacio de códigos un ZIP llamado `recover.zip`.

A continuación, ejecuta

    unzip recover.zip

para crear una carpeta llamada `recover`. Ya no necesitas el archivo ZIP, así que puedes ejecutar

    rm recover.zip

y responder con "y" seguido de Intro en el indicador para eliminar el archivo ZIP que has descargado.

Ahora escribe

    cd recover

seguido de Intro para moverte (es decir, abrir) a ese directorio. Ahora el indicador debería parecerse a lo siguiente.

    recover/ $

Ejecuta `ls` solo y deberías ver dos archivos: `recover.c` y `card.raw`.

## Antecedentes

Aunque los JPEG son más complicados que los BMP, los JPEG tienen "firmas", patrones de bytes que pueden distinguirlos de otros formatos de archivo. Concretamente, los tres primeros bytes de los JPEG son

    0xff 0xd8 0xff

del primer byte al tercer byte, de izquierda a derecha. El cuarto byte, por su parte, es `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee` o `0xef`. Dicho de otro modo, los cuatro primeros bits del cuarto byte son `1110`.

Lo más probable es que si encuentras este patrón de cuatro bytes en un medio conocido por almacenar fotos (por ejemplo, mi tarjeta de memoria), demarquen el inicio de un JPEG. Para ser justos, es posible que encuentres estos patrones en algún disco por pura casualidad, así que la recuperación de datos no es una ciencia exacta.

Afortunadamente, las cámaras digitales suelen almacenar las fotografías de forma contigua en las tarjetas de memoria, por lo que cada foto se almacena inmediatamente después de la foto tomada anteriormente. Por consiguiente, el inicio de un JPEG suele demarcar el final de otro. Sin embargo, las cámaras digitales suelen inicializar las tarjetas con un sistema de archivos FAT cuyo "tamaño de bloque" es de 512 bytes (B). Esto implica que estas cámaras solo escriben en esas tarjetas en unidades de 512 B. Una foto de 1 MB (es decir, 1.048.576 B) ocupa, por tanto, 1048576 ÷ 512 = 2048 "bloques" en una tarjeta de memoria. ¡Pero también lo hace una foto que es, por ejemplo, un byte más pequeña (es decir, 1.048.575 B)! El espacio desperdiciado en el disco se llama "espacio libre". Los investigadores forenses suelen buscar en el espacio libre restos de datos sospechosos.

La implicación de todos estos detalles es que tú, el investigador, probablemente puedas escribir un programa que itere sobre una copia de mi tarjeta de memoria, buscando las firmas de los JPEG. Cada vez que encuentres una firma, puedes abrir un nuevo archivo para escribir y empezar a rellenar ese archivo con bytes de mi tarjeta de memoria, cerrando ese archivo solo cuando encuentres otra firma. Además, en lugar de leer los bytes de mi tarjeta de memoria uno por uno, puedes leer 512 de ellos a la vez en un búfer por razones de eficiencia. Gracias a FAT, puedes confiar en que las firmas de los JPEG estarán "alineadas con los bloques". Es decir, solo tienes que buscar esas firmas en los cuatro primeros bytes de un bloque.

Por supuesto, ten en cuenta que los JPEG pueden abarcar bloques contiguos. De lo contrario, ningún JPEG podría ser mayor de 512 B. Pero el último byte de un JPEG podría no caer al final de un bloque. Recuerda la posibilidad de espacio libre. Pero no te preocupes. Como esta tarjeta de memoria era nueva cuando empecé a hacer fotos, lo más probable es que el fabricante la haya "puesto a cero" (es decir, la haya llenado de 0), en cuyo caso cualquier espacio libre se llenará de 0. No pasa nada si esos 0 finales acaban en los JPEG que recuperes; deberían seguir siendo visibles.

Ahora bien, solo tengo una tarjeta de memoria, ¡pero sois muchos! Así que he creado una "imagen forense" de la tarjeta, almacenando su contenido, byte a byte, en un archivo llamado `card.raw`. Para que no pierdas tiempo iterando sobre millones de 0 innecesariamente, solo he creado una imagen de los primeros megabytes de la tarjeta de memoria. Pero al final deberías encontrar que la imagen contiene 50 JPEG.

## Especificación

Implementa un programa llamado `recover` que recupere JPEG de una imagen forense.

- Implementa el programa en un archivo llamado `recover.c` en un directorio llamado `recover`.
- El programa debe aceptar exactamente un argumento de línea de comandos, el nombre de una imagen forense de la que recuperar JPEG.
- Si el programa no se ejecuta con exactamente un argumento de línea de comandos, debe recordar al usuario el uso correcto y `main` debe devolver `1`.
- Si la imagen forense no se puede abrir para su lectura, el programa debe informar al usuario y `main` debe devolver `1`.
- Cada uno de los archivos que generes debe llamarse `###.jpg`, donde `###` es un número decimal de tres dígitos, empezando por `000` para la primera imagen y contando hacia arriba.
- El programa, si utiliza `malloc`, no debe tener fugas de memoria.

## Sugerencias

### Escribe un pseudocódigo antes de escribir más código

Si no estás seguro de cómo resolver el problema general, divídelo en problemas más pequeños que probablemente puedas resolver primero. Por ejemplo, este problema es en realidad solo un puñado de problemas:

1.  Aceptar un único argumento de línea de comandos: el nombre de una tarjeta de memoria
2.  Abrir la tarjeta de memoria
3.  Mientras queden datos por leer en la tarjeta de memoria

    1.  Crear JPEG a partir de los datos

Vamos a escribir un pseudocódigo como comentarios para recordarte que hagas precisamente eso:

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceptar un único argumento de línea de comandos

        // Abrir la tarjeta de memoria

        // Mientras queden datos por leer en la tarjeta de memoria

            // Crear JPEG a partir de los datos
    }

### Convertir el pseudocódigo en código

Primero, considera cómo aceptar un único argumento en la línea de comandos. Si el usuario usa mal el programa, debes decirle el uso correcto del programa.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceptar un único argumento en la línea de comandos
        if (argc != 2)
        {
            printf("Uso: ./recover ARCHIVO\n");
            return 1;
        }

        // Abrir la tarjeta de memoria

        // Mientras queden datos para leer de la tarjeta de memoria

            // Crear JPEG a partir de los datos
    }

Ahora que has comprobado el uso correcto, puedes abrir la tarjeta de memoria. Ten en cuenta que puedes abrir `card.raw` mediante programación con `fopen`, como se muestra a continuación.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceptar un único argumento en la línea de comandos
        if (argc != 2)
        {
            printf("Uso: ./recover ARCHIVO\n");
            return 1;
        }

        // Abrir la tarjeta de memoria
        FILE *card = fopen(argv[1], "r");

        // Mientras queden datos para leer de la tarjeta de memoria

            // Crear JPEG a partir de los datos
    }

Por supuesto, debes comprobar si el archivo se ha abierto correctamente. De lo contrario, informa al usuario y sal del programa; te dejamos a ti esta parte.

A continuación, tu programa debe leer los datos de la tarjeta que has abierto, hasta que no queden más datos para leer. A lo largo del proceso, tu programa debe recuperar todos los JPEG de `card.raw` y almacenar cada uno como un archivo independiente en tu directorio de trabajo actual.

Primero, considera cómo leer `card.raw` hasta el final. Recuerda que, para leer datos de un archivo, debes almacenar temporalmente esos datos en un "búfer". Y recuerda también que `card.raw` almacena datos en bloques de 512 bytes. Como tal, es probable que desees crear un búfer de 512 bytes para almacenar bloques de datos a medida que los lees secuencialmente. Una forma de hacerlo es usar el tipo `uint8_t` de `stdint.h`, que almacena exactamente 8 bits (1 byte). El tipo se llama `uint8_t` porque almacena un número entero sin signo/positivo/no negativo que requiere 8 bits de espacio (es decir, un byte).

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceptar un único argumento en la línea de comandos
        if (argc != 2)
        {
            printf("Uso: ./recover ARCHIVO\n");
            return 1;
        }

        // Abrir la tarjeta de memoria
        FILE *card = fopen(argv[1], "r");

        // Crear un búfer para un bloque de datos
        uint8_t buffer[512];

        // Mientras queden datos para leer de la tarjeta de memoria

            // Crear JPEG a partir de los datos
    }

Sin embargo, probablemente no sea la mejor idea usar 512 como un [“número mágico”](../../../shorts/magic_numbers/) aquí. ¡Es probable que puedas mejorar aún más este diseño!

Ahora, considera cómo leer datos de la tarjeta de memoria. Según su [página de manual](https://man.cs50.io/3/fread), `fread` devuelve el número de bytes que ha leído, en cuyo caso debería devolver `512` o `0`, dado que `card.raw` contiene un cierto número de bloques de 512 bytes. Para leer todos los bloques de `card.raw`, después de abrirlo con `fopen`, debería ser suficiente usar un bucle como este.

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceptar un único argumento en la línea de comandos
        if (argc != 2)
        {
            printf("Uso: ./recover ARCHIVO\n");
            return 1;
        }

        // Abrir la tarjeta de memoria
        FILE *card = fopen(argv[1], "r");

        // Crear un búfer para un bloque de datos
        uint8_t buffer[512];

        // Mientras queden datos para leer de la tarjeta de memoria
        while (fread(buffer, 1, 512, card) == 512)
        {
            // Crear JPEG a partir de los datos

        }
    }

De esa manera, tan pronto como `fread` devuelva `0` (que es efectivamente `false`), tu bucle terminará.

Finalmente, depende de ti determinar cómo crear JPEG mediante programación a medida que continúas leyendo desde `card.raw`. Para ello, la siguiente [explicación detallada](#explicación detallada) puede resultarte útil.

Ten en cuenta que tu programa debe numerar los archivos que genera nombrando cada uno `###.jpg`, donde `###` es un número decimal de tres dígitos desde `000` en adelante. Familiarízate con [`sprintf`](https://man.cs50.io/3/sprintf) y ten en cuenta que `sprintf` almacena una cadena formateada en una ubicación de la memoria. Dado el formato prescrito `###.jpg` para el nombre de archivo de un JPEG, ¿cuántos bytes debes asignar para esa cadena? (¡No olvides el carácter NUL!)

Para comprobar si los JPEG que produce tu programa son correctos, simplemente haz doble clic y échales un vistazo. Si cada foto aparece intacta, ¡es probable que tu operación haya sido un éxito!

Y, por supuesto, recuerda `fclose` todos los archivos que hayas abierto con `fopen`.

### Mantén tu directorio de trabajo limpio

Es probable que los JPEG que genere el primer borrador de tu código no sean correctos. (¡Si los abres y no ves nada, probablemente no sean correctos!) Ejecuta el siguiente comando para eliminar todos los JPEG de tu directorio de trabajo actual.

    rm *.jpg

Si prefieres no tener que confirmar cada eliminación, ejecuta el siguiente comando en su lugar.

    rm -f *.jpg

Solo ten cuidado con el argumento `-f`, ya que "fuerza" la eliminación sin pedirte confirmación.

## Explicación detallada

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar

### Ejecución del programa

    ./recover card.raw

### Corrección

    check50 cs50/problems/2024/x/recover

### Estilo

    style50 recover.c

## Cómo enviar

    submit50 cs50/problems/2024/x/recover

