// Imprime una columna de n bloques con un bucle

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Altura: ");
    }
    while (n < 1);
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}