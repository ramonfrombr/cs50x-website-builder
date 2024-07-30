# Hola, Soy

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YQHsXMglC9A?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=74"></iframe></div>

## Problema a Resolver

En un archivo llamado `hello.c`, en una carpeta llamada `me`, implementa un programa en C que le pide al usuario su nombre y luego saluda a ese usuario. Por ejemplo, si el nombre del usuario es Adele, ¡tu programa debería imprimir `hello, Adele\n`!

#### Pistas

- Recuerda que puedes obtener una `cadena` de un usuario con `get_string`, que se declara en `cs50.h`.
- Recuerda que puedes imprimir una `cadena` con `printf`, que se declara en `stdio.h`.
- Recuerda que puedes dar formato a una `cadena` con `printf` con `%s`.

## Demo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-Jn4egWrG0Rvuzo9d2Rs0qpkcL" src="https://asc
iinema.org/a/Jn4egWrG0Rvuzo9d2Rs0qpkcL.js"></script>

## Cómo Empezar

Ejecuta `cd` por sí solo en tu ventana de terminal. Deberás encontrarte con que la ventana de terminal es similar a la siguiente:

    $

A continuación, ejecuta

    mkdir me

para crear una carpeta llamada `me` en tu codespace.

Luego, ejecuta

    cd me

para cambiar directorios a esa carpeta. Ahora deberías ver tu terminal como `me/ $`. Ahora puedes ejecutar

    code hello.c

para crear un archivo llamado `hello.c` en el que puedes escribir tu código.

## Tutorial

Aquí te presentamos un "tutorial" (es decir, un recorrido) de este problema, ¡por si te gustaría tener una visión verbal de lo que tienes que hacer!

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo Probar

### Corrección

En tu terminal, ejecuta lo siguiente para verificar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/me

### Estilo

    style50 hello.c

## Cómo Enviar

    submit50 cs50/problems/2024/x/me