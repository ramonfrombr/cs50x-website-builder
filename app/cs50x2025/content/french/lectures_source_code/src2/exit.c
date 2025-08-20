// Renvoi la valeur explicite depuis main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("argument de ligne de commande manquant\n");
        return 1;
    }
    printf("bonjour, %s\n", argv[1]);
    return 0;
}