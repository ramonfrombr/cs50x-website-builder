// Affiche une chaîne de caractères un par ligne, en utilisant strlen, en mémorisant la longueur de la chaîne

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Entree : ");
    printf("Sortie : ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}