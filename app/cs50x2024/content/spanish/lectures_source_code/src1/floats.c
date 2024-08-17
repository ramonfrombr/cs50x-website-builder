// Aritmética de punto flotante con float

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Solicita al usuario que introduzca x
    float x = get_float("x: ");

    // Solicita al usuario que introduzca y
    float y = get_float("y: ");

    // Realiza la división
    printf("x / y = %.50f\n", x / y);
}