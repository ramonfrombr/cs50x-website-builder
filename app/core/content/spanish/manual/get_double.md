# [NOMBRE](#nombre)

get_double - solicita al usuario un `double`

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <cs50.h>

## Prototipo

    double get_double(string prompt, ...);

# [DESCRIPCIÓN](#descripción)

Esta función solicita al usuario un `double`. Si el usuario ingresa algo que no sea un `double` (o un valor que no puede caber en un `double`), la función solicita nuevamente al usuario.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene algún código de formato, al estilo de [printf](printf), esta función también acepta argumentos adicionales, uno por cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario lo más precisamente posible como un `double`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <stdio.h>
    int main(void)
    {
        double d = get_double("Entrada:  ");
        printf("Salida: %f\n", d);
    }

# [VER TAMBIÉN](#ver-también)

>     get_char(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)