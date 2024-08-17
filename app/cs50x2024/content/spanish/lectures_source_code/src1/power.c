// Librería matemática

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    double base = get_double("Base: ");
    double exponent = get_double("Exponente: ");
    printf("Resultado: %.0f\n", pow(base, exponent));
}