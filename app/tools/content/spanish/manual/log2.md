# [NOMBRE](#nombre)

log2 - calcular el logaritmo en base 2 de un número

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <math.h>

## Prototipo

    double log2(double x);

# [DESCRIPCIÓN](#descripción)

Esta función calcula el logaritmo en base 2 de `x`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna, como un `double`, el logaritmo en base 2 de `x`.

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Esto es CS%i\n", (int) log2(1125899906842624));
    }