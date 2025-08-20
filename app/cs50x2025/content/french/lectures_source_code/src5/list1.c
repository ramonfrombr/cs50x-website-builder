// Implémente une liste de nombres grâce à un tableau à taille dynamique
//
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Liste de taille 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Initialisation de la liste de taille 3 avec des nombres
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Liste de taille 4
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }

    // Copie de la liste de taille 3 dans la liste de taille 4
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    // Ajout d'un nombre à la liste de taille 4
    tmp[3] = 4;

    // Libération de la liste de taille 3
    free(list);

    // Mémorisation de la liste de taille 4
    list = tmp;

    // Affichage de la liste
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Libération de la liste
    free(list);
}