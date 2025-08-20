// Retourner la valeur

#include <cs50.h>
#include <stdio.h>

int carre(int n);

int main(void)
{
    int input = get_int("Entrée : ");
    printf("Sortie : %i\n", carre(input));
}

// Carré de n
int carre(int n)
{
    return n * n;
}