# [NOMBRE](#nombre)

atol - convierte una `string` a un `long`

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdlib.h>

## Prototipo

    long atol(string s);

# [DESCRIPCIÓN](#descripción)

Esta función convierte un entero (positivo o negativo) de una `string` (por ejemplo, `"50"`) a un `long` (por ejemplo, `50`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve su entrada, `s`, como un `long`.

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Esto es CS%li\n", atol("50"));
    }