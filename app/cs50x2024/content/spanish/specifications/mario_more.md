## Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problema a resolver

Hacia el principio del Mundo 1-1 de Super Mario Bros. de Nintendo, Mario debe saltar sobre pirámides adyacentes de bloques, como se muestra a continuación.

![Captura de pantalla de Mario saltando sobre pirámides adyacentes](https://cs50.harvard.edu/x/2024/psets/1/mario/more/pyramids.png)

En un archivo llamado `mario.c` en una carpeta llamada `mario-more`, implementa un programa en C que recrea esa pirámide, usando almohadillas (`#`) para los ladrillos, como se muestra a continuación:

       #  #
      ##  ##
     ###  ###
    ####  ####

Y permitamos que el usuario decida qué tan altas deben ser las pirámides pidiéndoles primero un `int` positivo entre, digamos, 1 y 8, inclusive.

#### Ejemplos

Así es como podría funcionar el programa si el usuario ingresa `8` cuando se le solicite:

    $ ./mario
    Altura: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Así es como podría funcionar el programa si el usuario ingresa `4` cuando se le solicite:

    $ ./mario
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Así es como podría funcionar el programa si el usuario ingresa `2` cuando se le solicite:

    $ ./mario
    Altura: 2
     #  #
    ##  ##

Y así es como podría funcionar el programa si el usuario ingresa `1` cuando se le solicite:

    $ ./mario
    Altura: 1
    #  #

Si el usuario no ingresa, de hecho, un número entero positivo entre 1 y 8, inclusive, cuando se le solicite, el programa debe volver a preguntar al usuario hasta que coopere:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Tenga en cuenta que el ancho de la "brecha" entre pirámides adyacentes es igual al ancho de dos almohadillas, independientemente de la altura de las pirámides.

### Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Cómo probar tu código

¿Funciona tu código como se prescribe cuando ingresas

- `-1` (u otros numeros negativos)?
- `0`?
- `1` a `8`?
- `9` u otros numeros positivos?
- letras o palabras?
- ninguna entrada, cuando solo presionas Enter?

También puedes ejecutar lo siguiente para evaluar la exactitud de tu código usando `check50`. ¡Pero asegúrate de compilarlo y probarlo tú mismo también!

### Corrección

En tu terminal, ejecuta lo siguiente para verificar la exactitud de tu trabajo.

    check50 cs50/problems/2024/x/mario/more

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código utilizando `style50`.

    style50 mario.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/mario/more