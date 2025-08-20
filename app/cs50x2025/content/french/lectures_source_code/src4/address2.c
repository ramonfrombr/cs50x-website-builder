// Affiche un entier via son adresse

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
}