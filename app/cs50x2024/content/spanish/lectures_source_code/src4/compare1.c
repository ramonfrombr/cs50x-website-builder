// Compara dos direcciones de cadenas

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtener dos cadenas
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparar direcciones de cadenas
    if (s == t)
    {
        printf("Mismas\n");
    }
    else
    {
        printf("Distintas\n");
    }
}