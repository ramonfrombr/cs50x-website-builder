# [NOMBRE](#nombre)

pow - elevar un número a una potencia

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <math.h>

## Prototipo

    double pow(double x, double y);

# [DESCRIPCIÓN](#descripción)

Esta función eleva `x` a la potencia de `y`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve, como un `double`, `x` elevado a la potencia de `y`.

# [EJEMPLO](#ejemplo)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Un entero de 32 bits puede almacenar %li valores posibles.\n", (long) pow(2, 32));
    }