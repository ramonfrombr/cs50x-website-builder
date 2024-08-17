// Abstracción y alcance

#include <cs50.h>
#include <stdio.h>

int obtener_int_positivo(void);

int main(void)
{
    int i = obtener_int_positivo();
    printf("%i\n", i);
}

// Solicita al usuario un entero positivo
int obtener_int_positivo(void)
{
    int n;
    do
    {
        n = get_int("Entero positivo: ");
    }
    while (n < 1);
    return n;
}