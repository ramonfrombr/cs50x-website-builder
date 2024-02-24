# [NOMBRE](#nombre)

get_string - solicita al usuario una `cadena`  

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <cs50.h>

## Prototipo

    string get_string(string prompt, ...);

# [DESCRIPCIÓN](#descripción)

Esta función solicita al usuario una `cadena`.

Esta función espera al menos un argumento, `prompt`. Si `prompt` contiene algún código de formato, al estilo de [printf](printf), esta función acepta argumentos adicionales, uno por cada código de formato.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la entrada del usuario como una `cadena`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        string s = get_string("Entrada:  ");
        printf("Salida: %s\n", s);
    }

# [VER TAMBIÉN](#ver-también)

>     get_char(3), get_double(3), get_float(3), get_int(3),
>     get_long(3), printf(3)