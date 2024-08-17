// Implementa una búsqueda lineal de nombres

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Un array de nombres
    string nombres[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    // Búsqueda de EMMA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(nombres[i], "EMMA") == 0)
        {
            printf("Encontrado\n");
            return 0;
        }
    }
    printf("No encontrado\n");
    return 1;
}