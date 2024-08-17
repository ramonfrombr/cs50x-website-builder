// Imprime dos strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Obtener dos strings
    string s = get_string("s: ");
    string t = get_string("t: ");

    // Imprimir strings
    printf("%s\n", s);
    printf("%s\n", t);
}