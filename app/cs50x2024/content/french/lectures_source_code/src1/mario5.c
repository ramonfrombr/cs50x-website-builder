// Affiche une colonne de n briques avec une boucle

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Hauteur : ");
    }
    while (n < 1);
    for (int i = 0; i < n; i++)
    {
        printf("#\n");
    }
}