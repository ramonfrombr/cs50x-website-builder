// Échange deux entiers à l'aide de pointeurs

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x vaut %i, y vaut %i\n", x, y);
    swap(&x, &y);
    printf("x vaut %i, y vaut %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}