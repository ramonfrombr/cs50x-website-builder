# [NOMBRE](#nombre)

tolower - convierte un `char` a minúsculas

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <ctype.h>

## Prototipo

    int tolower(char c);

Piensa en esta función como si tomara un `char` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función convierte `c` a minúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Si `c` es una letra mayúscula (`A` a `Z`), esta función devuelve su equivalente en minúsculas (`a` a `z`). Si `c` no es una letra mayúscula, esta función devuelve `c` en sí.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrada: ");
        printf("Salida: %c\n", tolower(c));
    }