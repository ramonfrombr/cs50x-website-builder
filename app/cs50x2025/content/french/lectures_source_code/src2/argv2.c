// Affichage de caractères dans un tableau de chaînes

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    pour (int i = 0 ; i < argc ; i++)
    {
        pour (int j = 0, n = strlen(argv[i]) ; j < n ; j++)
        {
            printf("%c\n", argv[i][j]);
        }
        printf("\n");
    }
}