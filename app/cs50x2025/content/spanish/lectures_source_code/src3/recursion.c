// Dibuja una pirámide usando recursión

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
    // Si no hay nada que dibujar
    if (h == 0)
    {
        return;
    }

    // Dibujar pirámide de altura h - 1
    draw(h - 1);

    // Dibujar una fila de ancho h más
    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}