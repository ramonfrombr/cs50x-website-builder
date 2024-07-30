# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problema a resolver

Hacia el final del mundo 1-1 en [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.) de Nintendo, Mario debe ascender una pirámide de ladrillos alineada a la derecha, como en la imagen de abajo.

![captura de pantalla de Mario saltando sobre una pirámide alineada a la derecha](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

En un archivo llamado `mario.c` en una carpeta llamada `mario-less`, implementa un programa en C que recree esa pirámide, usando almohadillas (`#`) para los ladrillos, como en la imagen de abajo:

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Pero solicita al usuario un `int` para la altura real de la pirámide, de modo que el programa también pueda generar pirámides más pequeñas como la siguiente:

      #
     ##
    ###

Vuelve a solicitar al usuario, una y otra vez según sea necesario, si su entrada no es mayor que 0 o no es un `int` en su totalidad.

#### Sugerencias

- Recuerda que puedes obtener un `int` de un usuario con `get_int`, que se declara en `cs50.h`.
- Recuerda que puedes imprimir una `string` con `printf`, que se declara en `stdio.h`.

## Demostración

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-WPrv7PFVLaLkJ2BU96uTEQKuA" src="https://asc
iinema.org/a/WPrv7PFVLaLkJ2BU96uTEQKuA.js"></script>

## Consejo

### Escribe código que sepas que se compilará

Aunque este programa no haga nada, ¡al menos debería compilarse con `make`!

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

### Escribe pseudocódigo antes de escribir más código

Si no estás seguro de cómo resolver el problema en sí, divídelo en problemas más pequeños que probablemente puedas resolver primero. Por ejemplo, este problema son realmente dos problemas:

1. Pedirle al usuario la altura de la pirámide
2. Imprimir una pirámide de esa altura

Así que escribe un pseudocódigo como comentarios que te recuerden hacer eso:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide

        // Imprime una pirámide de esa altura
    }

### Convierte el pseudocódigo en código

Primero, considera cómo podrías pedirle al usuario la altura de la pirámide. Recuerda que un bucle `do while` es útil cuando quieres hacer algo al menos una vez, y posiblemente una y otra vez, como en el siguiente ejemplo:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
    }

En segundo lugar, considera cómo podrías imprimir una pirámide de esa altura, de arriba a abajo. Observa que la primera fila debe tener un ladrillo, la segunda fila debe tener dos ladrillos, y así sucesivamente. Lo más probable es que necesites un bucle, como en el siguiente ejemplo, aunque (¡todavía!) no estés seguro de qué poner en ese bucle. Así que añade más pseudocódigo como comentario por ahora:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
        for (int i = 0; i < n; i++)
        {
            // Imprime la fila de ladrillos
        }
    }

¿Cómo imprimir esa fila de ladrillos? Bueno, ¿no sería genial si hubiera una función llamada `print_row` que pudiera hacer eso? Supongamos que la hay:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
        for (int i = 0; i < n; i++)
        {
            // Imprime la fila de ladrillos
        }
    }

    void print_row(int bricks)
    {
        // Imprime la fila de ladrillos
    }

Luego podríamos llamar a esa función desde `main`, como en el siguiente ejemplo:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
        for (int i = 0; i < n; i++)
        {
            // Imprime la fila de ladrillos
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        // Imprime la fila de ladrillos
    }

¿Pero por qué `i + 1`?

Ahora vamos a implementar `print_row`:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
        for (int i = 0; i < n; i++)
        {
            // Imprime la fila de ladrillos
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        for (int i = 0; i < bricks; i++)
        {
            printf("#");
        }
        printf("\n");
    }

¿Pero por qué el `\n` al final?

Desafortunadamente, este código imprime una pirámide alineada a la izquierda, ¡pero tú necesitas una alineada a la derecha! ¿Quizás deberíamos imprimir algunos espacios en blanco antes de algunos de los ladrillos, para moverlos hacia la derecha? Vamos a cambiar `print_row` de la siguiente manera para que pueda imprimir ambas:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int spaces, int bricks);

    int main(void)
    {
        // Pídele al usuario la altura de la pirámide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprime una pirámide de esa altura
        for (int i = 0; i < n; i++)
        {
            // Imprime la fila de ladrillos
        }
    }

    void print_row(int spaces, int bricks)
    {
        // Imprime los espacios

        // Imprime los ladrillos
    }

Todavía queda algo de pseudocódigo en `main` y `print_row`, ¡así que te lo dejamos a ti!

Y considera si podrías factorizar parte del código en `main` en una función `get_height`, ¡que también devuelva el `int` que necesitas!

## Tutorial

<div class="alert alert-info" data-alert="info" role="alert"><p>Tenga en cuenta que este tutorial especifica que su programa debe pedirle al usuario la altura de una pirámide y <em>volver</em> a preguntar si el usuario ingresa un valor menor a 1 o mayor a 8. La especificación solo requiere que le vuelva a preguntar al usuario si ingresa un valor menor a 1.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar

¿Su código funciona según lo prescrito cuando ingresa:

- `-1` u otros números negativos?
- `0`?
- `1` u otros números positivos?
- ¿letras o palabras?
- ¿no ingresa nada, cuando solo presiona Enter?

### Corrección

En su terminal, ejecute lo siguiente para verificar la corrección de su trabajo.

    check50 cs50/problems/2024/x/mario/less

### Estilo

Ejecute lo siguiente para evaluar el estilo de su código usando `style50`.

    style50 mario.c

## Cómo enviar

En su terminal, ejecute lo siguiente para enviar su trabajo.

    submit50 cs50/problems/2024/x/mario/less

