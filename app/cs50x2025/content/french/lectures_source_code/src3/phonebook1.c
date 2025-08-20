// Implémente un répertoire téléphonique avec des structures

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string nom;
    string numéro;
}
personne;

int main(void)
{
    personne personnes[4];

    personnes[0].nom = "EMMA";
    personnes[0].numéro = "617-555-0100";

    personnes[1].nom = "RODRIGO";
    personnes[1].numéro = "617-555-0101";

    personnes[2].nom = "BRIAN";
    personnes[2].numéro = "617-555-0102";

    personnes[3].nom = "DAVID";
    personnes[3].numéro = "617-555-0103";

    // Chercher EMMA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(personnes[i].nom, "EMMA") == 0)
        {
            printf("Trouvé %s\n", personnes[i].numéro);
            return 0;
        }
    }
    printf("Pas trouvé\n");
    return 1;
}