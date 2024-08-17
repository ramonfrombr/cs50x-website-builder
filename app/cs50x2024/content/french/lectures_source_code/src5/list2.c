// Implémente une liste de nombres avec un tableau de taille dynamique en utilisant realloc

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

    // Initialise liste de taille 3 avec des nombres
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Redimensionne la liste pour qu'elle ait une taille 4
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }
    list = tmp;

    // Ajoute un nombre à la liste
    list[3] = 4;

    // Affiche la liste
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Libère la liste
    free(list);
}