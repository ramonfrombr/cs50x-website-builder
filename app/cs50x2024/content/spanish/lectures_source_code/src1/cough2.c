// Abstracción

#include <stdio.h>

void cough(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        cough();
    }
}

// Toser una vez
void cough(void)
{
    printf("cough\n");
}