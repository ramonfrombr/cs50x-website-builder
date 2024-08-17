// Devuelve valor explícito de main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("argumento de la línea de comandos faltante\n");
        return 1;
    }
    printf("hola, %s\n", argv[1]);
    return 0;
}