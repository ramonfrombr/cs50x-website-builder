# [NOMBRE](#nombre)

ispunct - verifica si un carácter es un signo de puntuación

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <ctype.h>

## Prototipo

    int ispunct(char c);

Piensa en esta función como si tomara un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es un signo de puntuación (por ejemplo, `'.'`, `'.'` o `'!'`, etc.) o no.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve un `int` diferente de cero si `c` es un signo de puntuación y `0` si `c` no es un signo de puntuación.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (ispunct(c))
        {
            printf("Tu entrada es un signo de puntuación.\n");
        }
        else
        {
            printf("Tu entrada no es un signo de puntuación.\n");
        }
    }