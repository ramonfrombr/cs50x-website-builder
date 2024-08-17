// Aritmética de punto flotante con double

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Solicitar x al usuario
    double x = get_double("x: ");

    // Solicitar y al usuario
    double y = get_double("y: ");

    // Realizar la división
    printf("x / y = %.50f\n", x / y);
}