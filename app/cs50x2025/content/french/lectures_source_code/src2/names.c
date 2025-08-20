// Stocke les noms en utilisant un tableau

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Noms
    string noms[4];
    noms[0] = "EMMA";
    noms[1] = "RODRIGO";
    noms[2] = "BRIAN";
    noms[3] = "DAVID";

    // Affiche le nom d'Emma
    printf("%s\n", noms[0]);
    printf("%c%c%c%c\n", noms[0][0], noms[0][1], noms[0][2], noms[0][3]);
}