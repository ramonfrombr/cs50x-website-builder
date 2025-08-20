// Renvoie une valeur explicite de main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("argument de ligne de commande manquant\n");
        return 1;
    }
    printf("bonjour à toi, %s\n", argv[1]);
    return 0;
}