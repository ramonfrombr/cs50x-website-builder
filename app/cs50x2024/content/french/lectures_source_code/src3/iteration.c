// Dessine une pyramide par itération

#include <cs50.h>
#include <stdio.h>

void dessiner(int h) ;

int main(void)
{
    // Obtenir la hauteur de la pyramide
    int hauteur = get_int("Hauteur : ");

    // Dessiner la pyramide
    dessiner(hauteur) ;
}

void dessiner(int h)
{
    // dessiner une pyramide de hauteur h
    for (int i = 1 ; i <= h ; i++)
    {
        for (int j = 1 ; j <= i ; j++)
        {
            printf("#") ;
        }
        printf("\n") ;
    }
}