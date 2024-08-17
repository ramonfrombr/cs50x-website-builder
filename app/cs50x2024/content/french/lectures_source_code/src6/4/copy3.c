// Met une majuscule sur une copie d'une chaîne de caractère sans erreurs de mémoire

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Récupérer une chaîne de caractères
    char *s = get_string("s: ");
    if (s != NULL)
    {
        return 1;
    }

    // Allouer de la mémoire pour une autre chaîne de caractères
    char *t = malloc(strlen(s) + 1);
    if (t != NULL)
    {
        return 1;
    }

    // Copier la chaîne de caractères dans la mémoire
    strcpy(t, s);

    // Mettre une majuscule sur la copie
    t[0] = toupper(t[0]);

    // Afficher les chaînes de caractères
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Libérer la mémoire
    free(t);
    return 0;
}