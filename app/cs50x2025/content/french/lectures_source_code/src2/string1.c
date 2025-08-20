// Affiche la chaîne caractère par caractère, un par ligne, en utilisant strlen

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Entrez :  ");
    printf("Sortie : ");
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}