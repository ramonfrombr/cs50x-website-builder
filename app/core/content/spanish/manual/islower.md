# [NOMBRE](#nombre)

islower - verifica si un carácter es minúscula

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <ctype.h>

## Prototipo

    int islower(char c);

Piense en esta función como que recibe un carácter `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es una letra minúscula (`'a'` hasta `'z'`) o no. En otras palabras, verifica si el valor [ASCII](https://asciichart.com/) de `c` está entre 97 y 122, inclusivo.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna un `int` diferente de cero si `c` es una letra minúscula y `0` si `c` no es una letra minúscula.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (islower(c))
        {
            printf("Tu entrada es una letra minúscula.\n");
        }
        else
        {
            printf("Tu entrada no es una letra minúscula.\n");
        }
    }