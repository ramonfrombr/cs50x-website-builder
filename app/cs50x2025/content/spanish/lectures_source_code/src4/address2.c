// Imprime un entero por medio de su dirección

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
}