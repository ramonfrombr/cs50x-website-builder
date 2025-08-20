// Implémente une liste de nombres avec une liste chaînée

#include <stdio.h>
#include <stdlib.h>

// Représente un noeud
typedef struct noeud
{
    int nombre;
    struct noeud *suivant;
}
noeud;

int main(void)
{
    // Liste de taille 0
    noeud *liste = NULL;

    // Ajoute un nombre à la liste
    noeud *n = malloc(sizeof(noeud));
    if (n == NULL)
    {
        return 1;
    }
    n->nombre = 1;
    n->suivant = NULL;
    liste = n;

    // Ajoute un nombre à la liste
    n = malloc(sizeof(noeud));
    if (n == NULL)
    {
        return 1;
    }
    n->nombre = 2;
    n->suivant = NULL;
    liste->suivant = n;

    // Ajoute un nombre à la liste
    n = malloc(sizeof(noeud));
    if (n == NULL)
    {
        return 1;
    }
    n->nombre = 3;
    n->suivant = NULL;
    liste->suivant->suivant = n;

    // Affiche la liste
    for (noeud *tmp = liste; tmp != NULL; tmp = tmp->suivant)
    {
        printf("%i\n", tmp->nombre);
    }

    // Libère la liste
    while (liste != NULL)
    {
        noeud *tmp = liste->suivant;
        free(liste);
        liste = tmp;
    }
}