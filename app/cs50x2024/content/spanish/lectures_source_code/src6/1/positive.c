// Abstracción y alcance

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// Le pide al usuario un entero positivo
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Entero Positivo: ");
    }
    while (n < 1);
    return n;
}