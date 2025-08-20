// Condiciones y operadores relacionales

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Solicita a los usuarios el número x
    int x = get_int("x: ");

    // Solicita a los usuarios el número y
    int y = get_int("y: ");

    // Compara x e y
    if (x < y)
    {
        printf("x es menor que y\n");
    }
    else if (x > y)
    {
        printf("x es mayor que y\n");
    }
    else
    {
        printf("x es igual a y\n");
    }
}