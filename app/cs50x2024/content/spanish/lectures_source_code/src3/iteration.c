// Dibuja una pirámide usando iteración

#include <cs50.h>
#include <stdio.h>

void draw(int h);

int main(void)
{
    // Obtener la altura de la pirámide
    int height = get_int("Altura: ");

    // Dibujar pirámide
    draw(height);
}

void draw(int h)
{
    // Dibujar pirámide de altura h
    for (int i = 1; i <= h; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}