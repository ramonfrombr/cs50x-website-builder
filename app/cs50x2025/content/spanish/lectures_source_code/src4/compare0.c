// Compara dos números enteros

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtén dos números enteros
    int i = get_int("i: ");
    int j = get_int("j: ");

    // Compara números enteros
    if (i == j)
    {
        printf("Igual\n");
    }
    else
    {
        printf("Diferente\n");
    }
}