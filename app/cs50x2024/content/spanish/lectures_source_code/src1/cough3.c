//Abstracción con parámetro

#include <stdio.h>

void Cough(int n);

int main(void)
{
    cough(3);
}

// Tos algunas cuantas veces
void cough(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("cough\n");
    }
}