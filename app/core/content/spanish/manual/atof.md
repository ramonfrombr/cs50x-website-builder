# [NOMBRE](#nombre)

atof - convierte una `cadena` a un `float`

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <stdlib.h>

## Prototipo

    float atof(cadena s);

# [DESCRIPCIÓN](#descripción)

Esta función convierte un valor de punto flotante (positivo o negativo) de una `cadena` (por ejemplo, `"50.0"`) a un `float` (por ejemplo, `50.0`).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve su entrada, `s`, como un `float`.

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Esto es CS%.0f\n", atof("50.0"));
    }