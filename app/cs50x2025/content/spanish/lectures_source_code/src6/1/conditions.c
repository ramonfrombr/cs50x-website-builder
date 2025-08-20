// Condiciones y operadores relacionales

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Solicitar al usuario x
    int x = get_int("x: ");

    // Solicitar al usuario y
    int y = get_int("y: ");

    // Comparar x e y
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