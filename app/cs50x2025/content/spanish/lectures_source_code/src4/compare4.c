// Compara dos cadenas utilizando strcmp

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtener dos cadenas
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparar cadenas
    if (strcmp(s, t) == 0)
    {
        printf("Igual\n");
    }
    else
    {
        printf("Diferente\n");
    }
}