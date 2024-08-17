# [NOMBRE](#nombre)

isalnum - verifica si un carácter es alfanumérico

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <ctype.h>

## Prototipo

    int isalnum(char c);

Piensa en esta función como si recibiera un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es alfanumérico (es decir, una letra o un número) o no.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna un entero no nulo si `c` es alfanumérico y `0` si `c` no es alfanumérico.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isalnum(c))
        {
            printf("Tu entrada es alfanumérica.\n");
        }
        else
        {
            printf("Tu entrada no es alfanumérica.\n");
        }
    }