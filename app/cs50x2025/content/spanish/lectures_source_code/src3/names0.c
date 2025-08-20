// Implementa búsqueda lineal de nombres

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Un arreglo de nombres
    string names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    // Buscar a EMMA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "EMMA") == 0)
        {
            printf("Encontrada\n");
            return 0;
        }
    }
    printf("No encontrada\n");
    return 1;
}