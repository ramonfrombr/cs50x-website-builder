// Opérateurs logiques

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Invite l'utilisateur à répondre
    char c = get_char("Êtes-vous d'accord ?\n");

    // Vérifie s'il est d'accord
    if (c == 'Y' || c == 'y')
    {
        printf("D'accord.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("Pas d'accord.\n");
    }
}