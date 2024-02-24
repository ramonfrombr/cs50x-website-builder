# [NOMBRE](#nombre)

atoi: convierte una `string` a un `int`

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdlib.h>

## Prototipo

    int atoi(string s);

# [DESCRIPCIÓN](#descripción)

Esta función convierte un número entero (positivo o negativo) de una `string` (por ejemplo, `"50"`) a un `int` (por ejemplo, `50`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve su entrada, `s`, como un `int`.

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Esto es CS%i\n", atoi("50"));
    }