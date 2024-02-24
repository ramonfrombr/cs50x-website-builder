# [NOMBRE](#nombre)

floor - calcular el piso de un número

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <math.h>

## Prototipo

    double floor(double x);

# [DESCRIPCIÓN](#descripción)

Esta función devuelve el piso de `x`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve, como un `double`, el entero más grande que no es mayor que `x`. Puede convertir ese valor de forma segura a un `long` (o un `int` si cabe).

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Esto es CS%i\n", (int) floor(50.1));
    }