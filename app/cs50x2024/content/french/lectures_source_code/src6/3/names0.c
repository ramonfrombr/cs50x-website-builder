// Implémente une recherche linéaire pour des noms

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Un tableau de noms
    string noms[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    // Recherche EMMA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(noms[i], "EMMA") == 0)
        {
            printf("Trouvé\n");
            return 0;
        }
    }
    printf("Non trouvé\n");
    return 1;
}