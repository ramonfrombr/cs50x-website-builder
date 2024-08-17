# [NOMBRE](#nombre)

srandom: inicializa la generación de números pseudoaleatorios con una semilla

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

## Prototipo

    void srandom(unsigned int semilla);

Un `unsigned int` debe ser no negativo.

Definiendo `DEFAULT_SOURCE` de esta manera permite utilizar el [srandom](srandom) dentro de `stdlib.h`.

# [DESCRIPCIÓN](#descripción)

Esta función altera la secuencia de números pseudoaleatorios generados por [random](random). Se debe llamar (una vez) antes de hacer cualquier llamada a [random](random). En otras palabras, si primero llamamos a [srandom](srandom) con una semilla `1`, las llamadas posteriores a [random](random) devolverán valores diferentes que si primero llamamos a [srandom](srandom) con una semilla `2`.

En lugar de codificar un valor para la semilla `seed`, es común pasar el valor de retorno de [time](/2/time) (que cambia cada segundo) a [srandom](srandom).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función no retorna ningún valor.

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

Llamar `time` con una entrada de `NULL`, una constante definida en `stdlib.h`, devuelve el tiempo actual en segundos.