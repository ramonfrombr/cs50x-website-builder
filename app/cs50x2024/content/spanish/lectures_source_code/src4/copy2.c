// Capitalize la copia de una cadena usando strcpy

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Obtiene una cadena
    char *s = get_string("s: ");

    // Asigna la memoria para otra cadena
    char *t = malloc(strlen(s) + 1);

    // Copia la cadena en la memoria
    strcpy(t, s);

    // Capitaliza la copia
    t[0] = toupper(t[0]);

    // Imprime las cadenas
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}