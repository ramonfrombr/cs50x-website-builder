# [NOMBRE](#nombre)

isspace - verifica si un carácter es un espacio en blanco (por ejemplo, un salto de línea, un espacio o una tabulación)

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <ctype.h>

## Prototipo

    int isspace(char c);

Piensa en esta función como si tomara un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función verifica si `c` es un espacio en blanco (por ejemplo, `\n`, `' '`, o `'\t'`) o no.

# [VALOR DEVUELTO](#valor-devuelto)

Esta función devuelve un `int` distinto de cero si `c` es un espacio en blanco y devuelve `0` si `c` no es un espacio en blanco.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        if (isspace(c))
        {
            printf("Tu entrada es un espacio en blanco.\n");
        }
        else
        {
            printf("Tu entrada no es un espacio en blanco.\n");
        }
    }