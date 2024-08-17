// Cette fonction calcule la moyenne à l'aide d'une fonction d'assistance

#include <cs50.h>
#include <stdio.h>

float moyenne(int length, int array[]);

int main(void)
{
    // Obtient le nombre de scores
    int n = get_int("Scores : ");

    // Obtient les scores
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score %i : ", i + 1);
    }

    // Affiche la moyenne
    printf("Moyenne : %.1f\n", moyenne(n, scores));
}

float moyenne(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}