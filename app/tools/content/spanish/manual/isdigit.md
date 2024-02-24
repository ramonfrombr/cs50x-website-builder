# [NOMBRE](#nombre)

isdigit - verifica si un carácter es un dígito

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <ctype.h>

## Prototipo

    int isdigit(char c);

Puedes pensar en esta función como una función que toma un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es un dígito decimal (`'0'` a `'9'`) o no. En otras palabras, verifica si el valor [ASCII](https://asciichart.com/) de `c` está entre 48 y 57, inclusive.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve un `int` distinto de cero si `c` es un dígito decimal y `0` si `c` no es un dígito decimal.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isdigit(c))
        {
            printf("Tu entrada es un dígito.\n");
        }
        else
        {
            printf("Tu entrada no es un dígito.\n");
        }
    }