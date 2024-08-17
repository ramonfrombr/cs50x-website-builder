// Affiche le char  de la chaîne caractère par caractère, un par ligne

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Entrée:  ");
    printf("Sortie: ");
    for (int i = 0; s[i] != '\0'; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}