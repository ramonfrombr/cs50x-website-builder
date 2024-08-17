# [NOMBRE](#nombre)

round: redondea un número al entero más cercano

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <math.h>

## Prototipo

    double round(double x);

# [DESCRIPCIÓN](#descripción)

Esta función redondea `x` al entero más cercano.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna, como `double`, `x` redondeado al entero más cercano. Puedes convertir seguramente ese valor a un `long` (o a un `int` si cabe).

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Esto es CS%i\n", (int) round(49.5));
    }