// Mettre en majuscule une chaîne

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Obtenir la chaîne
    string s = get_string("s: ");

    // Copier l'adresse de la chaîne
    string t = s;

    // Mettre en majuscule la première lettre de la chaîne
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Imprimer la chaîne deux fois
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}