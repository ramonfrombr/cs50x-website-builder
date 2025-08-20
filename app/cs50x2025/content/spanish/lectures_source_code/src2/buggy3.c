// Ejemplo con errores para help50, debug50

#include <cs50.h>
#include <stdio.h>

int get_negative_int(void);

int main(void)
{
    int i = get_negative_int();
    printf("%i\n", i);
}

// Solicita al usuario un número entero positivo
int get_negative_int(void)
{
    do
    {
        int n = get_int("Número entero negativo: ");
    }
    while (n >= 0);
    return n;
}