// Implémente la recherche linéaire pour des nombres

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Un tableau de nombres
    int nombres[]= {4, 8, 15, 16, 23, 42};

    // Recherche de 50
    for (int i = 0; i < 6; i++)
    {
        if (nombres[i] == 50)
        {
            printf("Trouvé\n");
            return 0;
        }
    }
    printf("Pas trouvé\n");
    return 1;
}