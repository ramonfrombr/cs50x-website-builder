// Mettre en majuscule une copie d'une chaîne en utilisant strcpy

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Obtenir une chaîne
    char *s = get_string("s: ");

    // Allouer de la mémoire pour une autre chaîne
    char *t = malloc(strlen(s) + 1);

    // Copier la chaîne en mémoire
    strcpy(t, s);

    // Mettre la copie en majuscule
    t[0] = toupper(t[0]);

    // Imprimer les chaînes
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}