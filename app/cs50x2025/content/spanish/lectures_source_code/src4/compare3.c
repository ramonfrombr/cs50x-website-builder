// Imprime las direcciones de dos cadenas

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtener dos cadenas
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Imprimir las direcciones de las cadenas
    printf("%p\n", s);
    printf("%p\n", t);
}