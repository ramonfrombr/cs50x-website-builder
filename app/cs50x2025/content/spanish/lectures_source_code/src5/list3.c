// Implementa una lista de números con lista ligada

#include <stdio.h>
#include <stdlib.h>

// Representa un nodo (elemento)
typedef struct nodo
{
    int numero;
    struct nodo *siguiente;
}
nodo;

int main(void)
{
    // Lista de tamaño 0
    nodo *lista = NULL;

    // Agrega un número a la lista
    nodo *n = malloc(sizeof(nodo));
    if (n == NULL)
    {
        return 1;
    }
    n->numero = 1;
    n->siguiente = NULL;
    lista = n;

    // Agrega un número a la lista
    n = malloc(sizeof(nodo));
    if (n == NULL)
    {
        return 1;
    }
    n->numero = 2;
    n->siguiente = NULL;
    lista->siguiente = n;

    // Agrega un número a la lista
    n = malloc(sizeof(nodo));
    if (n == NULL)
    {
        return 1;
    }
    n->numero = 3;
    n->siguiente = NULL;
    lista->siguiente->siguiente = n;

    // Imprime la lista
    for (nodo *tmp = lista; tmp != NULL; tmp = tmp->siguiente)
    {
        printf("%i\n", tmp->numero);
    }

    // Libera la lista
    while (lista != NULL)
    {
        nodo *tmp = lista->siguiente;
        free(lista);
        lista = tmp;
    }
}