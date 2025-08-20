// Calcule la moyenne de trois nombres à l'aide d'un tableau et d'une constante

#include <cs50.h>
#include <stdio.h>

const int N = 3;

int main(void)
{
    // Scores
    int scores[N];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    // Affiche la moyenne
    printf("Moyenne : %i\n", (scores[0] + scores[1] + scores[2]) / N);
}