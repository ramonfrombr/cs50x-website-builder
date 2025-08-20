// Implémente la recherche linéaire de noms en utilisant !

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Un tableau de noms
    string names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    // Recherche EMMA
    for (int i = 0; i < 4; i++)
    {
        if (!strcmp(names[i], "EMMA"))
        {
            printf("Trouvé\n");
            return 0;
        }
    }
    printf("Non trouvé\n");
    return 1;
}