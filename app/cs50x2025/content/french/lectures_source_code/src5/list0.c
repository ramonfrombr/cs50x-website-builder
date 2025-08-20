// Implémente une liste de nombres avec un tableau de taille fixe

#include <stdio.h>

int main(void)
{
    // Liste de taille 3
    int liste[3];

    // Initialise une liste avec des nombres
    liste[0] = 1;
    liste[1] = 2;
    liste[2] = 3;

    // Imprime la liste
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", liste[i]);
    }
}