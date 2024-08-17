// Implementa la búsqueda lineal para números

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // A un array de números
    int numbers[] = {4, 8, 15, 16, 23, 42};

    // Busca 50
    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Encontrado\n");
            return 0;
        }
    }
    printf("No encontrado\n");
    return 1;
}