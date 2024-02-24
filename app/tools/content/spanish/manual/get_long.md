# [NOMBRE](#nombre)

get_long - solicita al usuario un `long`

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <cs50.h>

## Prototipo

    long get_long(string prompt, ...);

# [DESCRIPCIÓN](#descripción)

Esta función solicita al usuario un `long`. Si el usuario ingresa cualquier otro tipo de dato que no sea un `long` (o un valor que no quepa en un `long`), la función solicitará nuevamente al usuario.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene algún código de formato, al estilo de [printf](printf), esta función aceptará argumentos adicionales, uno por cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario como un `long`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        long l = get_long("Input:  ");
        printf("Output: %li\n", l);
    }

# [VER TAMBIÉN](#ver-también)

>     get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
>     printf(3)