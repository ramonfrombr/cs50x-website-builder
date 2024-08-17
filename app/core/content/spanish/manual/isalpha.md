# [NOMBRE](#nombre)

isalpha - comprueba si un carácter es alfabético

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <ctype.h>

## Prototipo

    int isalpha(char c);

Piense en esta función como si tomara un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función comprueba si `c` es alfabético (es decir, una letra) o no.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve un `int` distinto de cero si `c` es alfabético y `0` si `c` no es alfabético.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isalpha(c))
        {
            printf("Su entrada es alfabética.\n");
        }
        else
        {
            printf("Su entrada no es alfabética.\n");
        }
    }