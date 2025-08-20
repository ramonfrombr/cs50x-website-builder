// Dessine une pyramide à l'aide de récursivité

#include <cs50.h>
#include <stdio.h>

void dessiner(int h);

int main(void)
{
    // Obtient la hauteur de la pyramide
    int hauteur = get_int("Hauteur : ");

    // Dessine la pyramide
    dessiner(hauteur);
}

void dessiner(int h)
{
    // Si rien à dessiner
    if (h == 0)
    {
        return ;
    }

    // Dessine une pyramide de hauteur h - 1
    dessiner(h - 1);

    // Dessine une ligne supplémentaire de largeur h
    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}