# [NOMBRE](#nombre)

sqrt - calcular la raíz cuadrada de un número

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <math.h>

## Prototipo

    double sqrt(double x);

# [DESCRIPCIÓN](#descripción)

Esta función calcula la raíz cuadrada de `x`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve, como un `double`, la raíz cuadrada de `x`.

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Esto es CS%i\n", (int) sqrt(2500));
    }