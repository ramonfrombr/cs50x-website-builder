// Implementa una lista de números con un array de tamaño fijo

#include <stdio.h>

int main(void)
{
    // Lista del tamaño 3
    int list[3];

    // Inicializa lista con números
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Imprimir lista
    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
}