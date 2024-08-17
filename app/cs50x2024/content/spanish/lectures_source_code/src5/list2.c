// Implementa una lista de números con un array de tamaño dinámico usando realloc

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Lista de tamaño 3
    int *lista = malloc(3 * sizeof(int));
    if (lista == NULL)
    {
        return 1;
    }

    // Inicializa lista de tamaño 3 con números
    lista[0] = 1;
    lista[1] = 2;
    lista[2] = 3;

    // Redimensiona lista para que sea de tamaño 4
    int *tmp = realloc(lista, 4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }
    lista = tmp;

    // Añade número a lista
    lista[3] = 4;

    // Imprime lista
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", lista[i]);
    }

    // Libera lista
    free(lista);
}