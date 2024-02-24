# [NOMBRE](#nombre)

get_float - solicita al usuario un `float`

# [SINOPSIS](#sinopsis)

## Archivo de Cabecera

    #include <cs50.h>

## Prototipo

    float get_float(string prompt, ...);

# [DESCRIPCIÓN](#descripcion)

Esta función solicita al usuario un `float`. Si el usuario ingresa cualquier cosa que no sea un `float` (o un valor que no pueda caber en un `float`), la función solicitará al usuario nuevamente.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene algún código de formato, al estilo de [printf](printf), esta función también acepta argumentos adicionales, uno por código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario lo más precisamente posible como un `float`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        float f = get_float("Entrada:  ");
        printf("Salida: %f\n", f);
    }

# [VER TAMBIÉN](#ver-tambien)

>     get_char(3), get_double(3), get_int(3), get_long(3),
>     get_string(3)