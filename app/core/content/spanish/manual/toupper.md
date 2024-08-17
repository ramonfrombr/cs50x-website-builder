# [NOMBRE](#nombre)

toupper - convierte un `char` a mayúsculas

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <ctype.h>

## Prototipo

    int toupper(char c);

Piensa en esta función como si tomará un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función convierte `c` a mayúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Si `c` es una letra minúscula (`a` a `z`), esta función devuelve su equivalente en mayúscula (`A` a `Z`). Si `c` no es una letra minúscula, esta función devuelve `c` tal cual.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada:  ");
        printf("Salida: %c\n", toupper(c));
    }