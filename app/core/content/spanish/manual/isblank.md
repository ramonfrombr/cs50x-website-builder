# [NOMBRE](#nombre)

isblank: comprueba si un carácter está en blanco (es decir, un espacio o una tabulación).

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <ctype.h>

## Prototipo

    int isblank(char c);

Piensa en esta función como si recibiera un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función comprueba si `c` está en blanco (es decir, `' '` o `'\t'`) o no.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve un `int` distinto de cero si `c` está en blanco y `0` si no lo está.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isblank(c))
        {
            printf("Tu entrada está en blanco.\n");
        }
        else
        {
            printf("Tu entrada no está en blanco.\n");
        }
    }