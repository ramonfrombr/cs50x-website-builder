// Implementa la búsqueda lineal de nombres usando !

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Un array de nombres
    string names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    // Buscar por EMMA
    for (int i = 0; i < 4; i++)
    {
        if (!strcmp(names[i], "EMMA"))
        {
            printf("Encontrado\n");
            return 0;
        }
    }
    printf("No encontrado\n");
    return 1;
}