// Hace un promedio de tres números usando un arreglo y una constante

#include <cs50.h>
#include <stdio.h>

int const N = 3;

int main(void)
{
    // Puntuaciones
    int scores[N];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    // Imprime el promedio
    printf("Promedio: %i\n", (scores[0] + scores[1] + scores[2]) / N);
}