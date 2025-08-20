// Intento fallido de intercambio de dos enteros

#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x es %i, y es %i\n", x, y);
    swap(x, y);
    printf("x es %i, y es %i\n", x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}