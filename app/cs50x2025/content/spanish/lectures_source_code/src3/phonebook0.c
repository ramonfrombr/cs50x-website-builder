// Implementa una libreta telefónica sin estructuras

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string nombres[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};
    string números[] = {"617-555-0100", "617-555-0101", "617-555-0102", "617-555-0103"};

    for (int i = 0; i < 4; i++)
    {
        if (!strcmp(nombres[i], "EMMA"))
        {
            printf("Encontrado %s\n", números[i]);
            return 0;
        }
    }
    printf("No encontrado\n");
    return 1;
}