// Implementa una agenda telefónica con structs

#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string nombre;
    string número;
}
persona;

int main(void)
{
    persona personas[4];

    personas[0].nombre = "EMMA";
    personas[0].número = "617-555-0100";

    personas[1].nombre = "RODRIGO";
    personas[1].número = "617-555-0101";

    personas[2].nombre = "BRIAN";
    personas[2].número = "617-555-0102";

    personas[3].nombre = "DAVID";
    personas[3].número = "617-555-0103";

    // Buscar a EMMA
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(personas[i].nombre, "EMMA") == 0)
        {
            printf("Encontrado %s\n", personas[i].número);
            return 0;
        }
    }
    printf("No encontrado\n");
    return 1;
}