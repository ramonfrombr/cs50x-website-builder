# [NOMBRE](#nombre)

random - genera un número pseudoaleatorio

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #define _DEFAULT_SOURCE#include <stdlib.h>

## Prototipo

    long random(void);

Definir `_DEFAULT_SOURCE` de esta manera habilita `random` dentro de `stdlib.h`.

# [DESCRIPCIÓN](#descripción)

Esta función genera un número pseudoaleatorio entre `0` y `RAND_MAX`, inclusive, donde `RAND_MAX` es una constante definida en `stdlib.h`.

Para devolver un valor de punto flotante pseudoaleatorio entre `0.0` y `1.0`, exclusivo, en su lugar, es común dividir el valor de retorno de [random](random) por `(double) RAND_MAX + 1`, como en:

    float number = random() / ((double) RAND_MAX + 1);

Para devolver un número entero pseudoaleatorio entre `0` y `N`, exclusivo, donde `N` es algún entero, es común dividir el valor de retorno de [random](random) por `(double) RAND_MAX + 1` y luego multiplicar el cociente por `N`, como en:

    int number = (random() / ((double) RAND_MAX + 1)) * N;

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número generado pseudoaleatoriamente como un `long`.

# [EJEMPLO](#ejemplo)

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        srandom(time(NULL));
        printf("%lu\n", random());
        printf("%lu\n", random());
        printf("%lu\n", random());
    }

Llamar a `time` con una entrada de `NULL`, una constante definida en `stdlib.h`, devuelve el tiempo actual en segundos.