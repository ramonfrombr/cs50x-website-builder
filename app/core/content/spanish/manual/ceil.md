# [NOMBRE](#nombre)

ceil - calcular el techo de un número

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <math.h>

## Prototipo

    double ceil(double x);

# [DESCRIPCIÓN](#descripción)

Esta función devuelve el techo de `x`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve, como `double`, el entero más pequeño que no es menor que `x`. Puede convertir de forma segura ese valor a `long` (o a `int` si cabe).

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Esto es CS%i\n", (int) ceil(49.9));
    }