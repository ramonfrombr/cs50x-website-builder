// Met en majuscules une copie d'une chaîne sans erreurs de mémoire

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Récupère une chaîne
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // Alloue de la mémoire pour une autre chaîne
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // Copie la chaîne en mémoire
    strcpy(t, s);

    // Met en majuscules la copie
    t[0] = toupper(t[0]);

    // Affiche les chaînes
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Libère la mémoire
    free(t);
    return 0;
}