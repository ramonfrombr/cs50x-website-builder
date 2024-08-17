# [NOMBRE](#nombre)

get_int - solicita al usuario un `int`

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <cs50.h>

## Prototipo

    int get_int(string prompt, ...);

# [DESCRIPCIÓN](#descripción)

Esta función solicita al usuario un `int`. Si el usuario ingresa cualquier cosa que no sea un `int` (o un valor que no quepa en un `int`), la función solicita al usuario nuevamente.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene algún código de formato, al estilo de [printf](printf), esta función también acepta argumentos adicionales, uno por cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario como un `int`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        int i = get_int("Entrada:  ");
        printf("Salida: %i\n", i);
    }

# [VER TAMBIÉN](#ver-también)

>     get_char(3), get_double(3), get_float(3), get_long(3),
>     get_string(3), printf(3)