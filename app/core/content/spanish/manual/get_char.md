# [NOMBRE](#nombre)

get_char - solicitar al usuario un `char`

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <cs50.h>

## Prototipo

    char get_char(string prompt, ...);

# [DESCRIPCIÓN](#descripción)

Esta función solicita al usuario un `char`. Si el usuario ingresa más o menos de un `char`, la función solicita al usuario nuevamente.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene códigos de formato, al estilo de [printf](printf), esta función acepta argumentos adicionales también, uno por cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario como un `char`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Entrada:  ");
        printf("Salida: %c.\n", c);
    }

# [VER TAMBIÉN](#ver-también)

>     get_double(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)