// Bibliothèque Math

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    double base = get_double("Base : ");
    double exposant = get_double("Exposant : ");
    printf("Sortie : %.0f\n", pow(base, exposant));
}