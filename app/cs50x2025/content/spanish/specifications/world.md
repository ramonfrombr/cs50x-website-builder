# Hola, mundo

## Problema a resolver

Gracias al profesor [David Malan](https://en.wikipedia.org/wiki/David_J._Malan) (¡quien impartía la clase CS50 cuando Ramón la tomó!), “Hola, mundo” se ha implementado en cientos de lenguajes. ¡Agreguemos tu implementación a la lista!

En un archivo llamado `hola.c`, dentro de una carpeta llamada `mundo`, implementa un programa en C que imprima `hola, mundo\n` ¡y eso es todo!

#### Pista

¡Este es el código que debes escribir! (Es una gran pista, ¿eh?) Sin embargo, es mejor que lo escribas tú mismo en lugar de copiarlo y pegarlo, para que comiences a desarrollar algo de “memoria muscular” para escribir código.

    #include <stdio.h>

    int main(void)
    {
        printf("hola, mundo\n");
    }

## Demostración

Esta es una demostración de qué debe pasar cuando compilas y ejecutas tu programa.

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-C5rag3703OZpKxGJ6dSwHnUEF" src="https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF.js"></script>

## Cómo empezar

Abre [VS Code](https://cs50.dev/).

Comienza dando clic dentro de la ventana de tu terminal y luego ejecuta `cd` por sí solo. Deberías ver que su “prompt” se parece al siguiente.

    $

Después ejecuta

    mkdir mundo

para crear una carpeta llamada `mundo` en tu espacio de trabajo.

Luego ejecuta

    cd mundo

para cambiar directorios a esa carpeta. Ahora deberías ver tu prompt de terminal como `mundo/ $`. Ahora puedes ejecutar

    code hola.c

para crear un archivo llamado `hola.c` en el que puedas escribir tu código.

## Cómo probar

Recuerda que puedes compilar `hola.c` con:

    make hola

¡Si no ves un mensaje de error, se compiló con éxito! Puedes confirmarlo con

    ls

que debe mostrar no solo `hola.c` (que es el código fuente) sino también `hola` (que es código máquina).

Si ves un mensaje de error, intenta arreglar tu código y vuelve a compilarlo. Sin embargo, si no entiendes el mensaje de error, intenta ejecutar

    help50 make hola

para buscar asesoría.

Una vez que tu código se compile con éxito, puedes ejecutar tu programa con:

    ./hola

### Corrección

Ejecuta lo siguiente para evaluar la corrección de tu código usando `check50`, ¡un programa de línea de comandos que mostrará caritas felices cuando tu código pase las pruebas automáticas de CS50 y caritas tristes cuando no lo haga!

    check50 cs50/problems/2024/x/mundo

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`, un programa de línea de comandos que mostrará adiciones (en verde) y eliminaciones (en rojo) que debes hacer a tu programa para mejorar su estilo. ¡Si tienes problemas para ver esos colores, `style50` también admite otros [modos](https://cs50.readthedocs.io/style50/)!

    style50 hola.c

## Cómo enviar

¡No necesitas enviar este!