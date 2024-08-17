// Calcule la moyenne de trois nombres

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Les notes
    int note1 = 72;
    int note2 = 73;
    int note3 = 33;

    // Affiche la moyenne
    printf("Moyenne: %i\n", (note1 + note2 + note3) / 3);
}