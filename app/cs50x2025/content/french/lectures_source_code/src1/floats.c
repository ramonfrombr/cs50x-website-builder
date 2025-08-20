// Arithmétique à virgule flottante avec float

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Demander à l'utilisateur x
    float x = get_float("x: ");

    // Demander à l'utilisateur y
    float y = get_float("y: ");

    // Effectuer la division
    printf("x / y = %.50f\n", x / y);
}