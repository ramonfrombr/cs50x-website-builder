// Implémente un annuaire téléphonique sans structures

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string prénoms[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};
    string numéros[] = {"617-555-0100", "617-555-0101", "617-555-0102", "617-555-0103"};

    for (int i = 0; i < 4; i++)
    {
        if (!strcmp(prénoms[i], "EMMA"))
        {
            printf("Trouvé %s\n", numéros[i]);
            return 0;
        }
    }
    printf("Non trouvé\n");
    return 1;
}