// Arithmétique en virgule flottante avec double

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Demander à l'utilisateur x
    double x = get_double("x: ");

    // Demander à l'utilisateur y
    double y = get_double("y: ");

    // Faire une division
    printf("x / y = %.50f\n", x / y);
}