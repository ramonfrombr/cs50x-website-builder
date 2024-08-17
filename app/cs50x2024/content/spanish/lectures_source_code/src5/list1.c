// Implementa una lista de números con un array de tamaño dinámico
//
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Lista de tamaño 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Inicializa lista de tamaño 3 con números
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Lista de tamaño 4
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }

    // Copia la lista de tamaño 3 a la lista de tamaño 4
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    // Añade un número a la lista de tamaño 4
    tmp[3] = 4;

    // Libera la lista de tamaño 3
    free(list);

    // Recuerda la lista de tamaño 4
    list = tmp;

    // Imprime la lista
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Libera la lista
    free(list);
}