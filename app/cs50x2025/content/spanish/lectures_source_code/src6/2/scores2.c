// Promedio de tres números usando un arreglo y una constante.

#include <cs50.h>
#include <stdio.h>

const int N = 3;

int main(void)
{
    // Puntajes
    int puntajes[N];
    puntajes[0] = 72;
    puntajes[1] = 73;
    puntajes[2] = 33;

    // Imprimir el promedio
    printf("Promedio: %i\n", (puntajes[0] + puntajes[1] + puntajes[2]) / N);
}