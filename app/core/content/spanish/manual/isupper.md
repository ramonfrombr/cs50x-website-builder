# [NOMBRE](#nombre)

isupper - verifica si un carácter está en mayúscula

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <ctype.h>

## Prototipo

    int isupper(char c);

Piense en esta función como si estuviera tomando un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es una letra en mayúscula (`'A'` a `'Z'`) o no. En otras palabras, verifica si el valor [ASCII](https://asciichart.com/) de `c` está entre 65 y 90, ambos inclusive.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve un `int` distinto de cero si `c` es una letra en mayúscula y `0` si `c` no es una letra en mayúscula.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isupper(c))
        {
            printf("Tu entrada es una letra en mayúscula.\n");
        }
        else
        {
            printf("Tu entrada no es una letra en mayúscula.\n");
        }
    }