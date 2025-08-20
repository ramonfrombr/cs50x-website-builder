# Sustitución

## Problema a resolver

En un cifrado por sustitución, “encriptamos” (es decir, ocultamos de forma reversible) un mensaje al reemplazar cada letra por otra. Para hacer esto, usamos una _clave_: en este caso, una asignación de cada una de las letras del alfabeto a la letra a la que debe corresponder cuando la encriptamos. Para “desencriptar” el mensaje, el receptor del mensaje debe conocer la clave, a fin de que pueda revertir el proceso: traducir el texto encriptado (generalmente llamado _texto cifrado_) al mensaje original (generalmente llamado _texto simple_).

Una clave, por ejemplo, podría ser la cadena `NQXPOMAFTRHLZGECYJIUWSKDVB`. Esta clave de 26 caracteres significa que `A` (la primera letra del alfabeto) debe convertirse en `N` (el primer carácter de la clave), `B` (la segunda letra del alfabeto) debe convertirse en `Q` (el segundo carácter de la clave), y así sucesivamente.

Un mensaje como `HELLO`, entonces, se encriptaría como `FOLLE`, reemplazando cada una de las letras según la asignación determinada por la clave.

Crea un programa en un archivo llamado `substitution.c` en una carpeta llamada `substitution` que permita encriptar mensajes con un cifrado por sustitución. En el momento en que el usuario ejecuta el programa, debe decidir, proporcionando un argumento de línea de comandos, cuál debe ser la clave en el mensaje secreto que proporcionará en tiempo de ejecución.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script>

## Especificación

Diseña e implementa un programa, `substitution`, que encripte mensajes con un cifrado por sustitución.

- Implementa el programa en un archivo llamado `substitution.c` en un directorio llamado `substitution`.
- El programa debe aceptar un único argumento de línea de comandos, la clave que se usará para la sustitución. La clave en sí debe ser insensible a mayúsculas y minúsculas, por lo que si algún carácter en la clave está en mayúscula o minúscula, no debería afectar el comportamiento del programa.
- Si el programa se ejecuta sin argumentos de línea de comando o con más de un argumento de línea de comando, el programa debe imprimir un mensaje de error de tu elección (con `printf`) y regresar desde `main` con un valor de `1` (que tiende a significar un error) de inmediato.
- Si la clave es inválida (por no contener 26 caracteres, contener algún carácter que no sea alfabético o no contener cada letra exactamente una vez), el programa debe imprimir un mensaje de error de tu elección (con `printf`) y regresar desde `main` con un valor de `1` de inmediato.
- El programa debe mostrar `texto simple:` (sin salto de línea) y luego pedir al usuario un `string` de texto simple (usando `get_string`).
- El programa debe mostrar `texto cifrado:` (sin salto de línea) seguido del texto cifrado correspondiente al texto simple, con cada carácter alfabético en el texto simple sustituido por el carácter correspondiente en el texto cifrado; los caracteres no alfabéticos deben mostrarse sin cambios.
- El programa debe conservar las mayúsculas y minúsculas: las letras mayúsculas deben seguir siendo letras mayúsculas; las letras minúsculas deben seguir siendo letras minúsculas.
- Después de mostrar el texto cifrado, debes imprimir un salto de línea. Luego, el programa debe salir regresando `0` desde `main`.

Podrías encontrar una o más funciones declaradas en `ctype.h` que te resulten útiles, según [manual.cs50.io](https://manual.cs50.io/).

## Explicación detallada

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo realizar la prueba

### Corrección

En la terminal, ejecuta lo siguiente para verificar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/substitution

#### Cómo usar `debug50`

¿Quieres ejecutar `debug50`? Puedes hacerlo de la siguiente manera, después de compilar tu código exitosamente con `make`,

    debug50 ./substitution CLAVE

donde `CLAVE` es la clave que entregas como argumento de línea de comandos para tu programa. Ten en cuenta que al ejecutar

    debug50 ./substitution

¡lo ideal es que tu programa termine pidiendo al usuario una clave!

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 substitution.c

## Cómo enviar

En la terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/substitution