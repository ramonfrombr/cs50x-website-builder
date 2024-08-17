// Calcul de modulo

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Demande à l'utilisateur de saisir un entier
    int n = get_int("n: ");

    // Vérifie la parité de l'entier
    if (n % 2 == 0)
    {
        printf("pair\n");
    }
    else
    {
        printf("impair\n");
    }
}