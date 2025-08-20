// Abstraction avec paramétrisation

#include <stdio.h>

void tousser(int n);

int main(void)
{
    tousser(3);
}

// Tousser un certain nombre de fois
void tousser(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("toux\n");
    }
}