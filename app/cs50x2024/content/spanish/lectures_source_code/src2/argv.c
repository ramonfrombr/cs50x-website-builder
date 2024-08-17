// Escribiendo un argumento de línea de comando

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hola, %s\n", argv[1]);
    }
    else
    {
        printf("hola, mundo\n");
    }
}