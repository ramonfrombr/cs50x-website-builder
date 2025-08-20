// Promedia números utilizando una función auxiliar

#include <cs50.h>
#include <stdio.h>

float average(int length, int array[]);

int main(void)
{
    // Obtener el número de calificaciones
    int n = get_int("Calificaciones:  ");

    // Obtener las calificaciones
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Calificación %i: ", i + 1);
    }

    // Imprimir el promedio
    printf("Promedio: %.1f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}