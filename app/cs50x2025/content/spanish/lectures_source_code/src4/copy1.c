// Capitaliza una copia de una cadena

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Obtener una cadena
    char *s = get_string("s: ");

    // Asignar memoria para otra cadena
    char *t = malloc(strlen(s) + 1);

    // Copiar la cadena en la memoria
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }

    // Capitalizar la copia
    t[0] = toupper(t[0]);

    // Imprimir cadenas
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}