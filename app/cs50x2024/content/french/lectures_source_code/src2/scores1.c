// Calcule la moyenne de trois nombres en utilisant un tableau

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Scores
    int scores[3];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    // Affichage de la moyenne
    printf("Moyenne : %i\n", (scores[0] + scores[1] + scores[2]) / 3);
}