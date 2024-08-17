// Abstraction

#include <stdio.h>

void tousser (void);

int main (void)
{
    for (int i = 0; i < 3; i++)
    {
        tousser();
    }
}

// Tousser une fois
void tousser (void)
{
    printf("toux\n");
}