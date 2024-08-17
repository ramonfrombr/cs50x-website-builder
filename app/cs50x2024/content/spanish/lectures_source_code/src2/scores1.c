// Promedio de tres números utilizando un array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Calificaciones
    int calificaciones[3];
    calificaciones[0] = 72;
    calificaciones[1] = 73;
    calificaciones[2] = 33;

    // Imprime promedio
    printf("Promedio: %i\n", (calificaciones[0] + calificaciones[1] + calificaciones[2]) / 3);
}