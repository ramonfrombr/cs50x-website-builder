// Calcula un residuo

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Pedir un entero al usuario
    int n = get_int("n: ");

    // Revisar la paridad del entero
    if (n % 2 == 0)
    {
        printf("par\n");
    }
    else
    {
        printf("impar\n");
    }
}