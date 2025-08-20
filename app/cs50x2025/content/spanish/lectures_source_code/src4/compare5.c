// Compara dos strings usando strcmp y !

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtener dos cadenas de caracteres
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Comparar cadenas
    if (strcmp(s, t) == 0)
    {
        printf("Mismo\n");
    }
    else
    {
        printf("Diferente\n");
    }
}