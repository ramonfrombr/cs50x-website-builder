// Capitaliza una cadena

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Obtener una cadena
    string s = get_string("s: ");

    // Copiar dirección de cadena
    string t = s;

    // Capitalizar primera letra de la cadena
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Imprimir cadena dos veces
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}