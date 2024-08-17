// Capitaliza una copia de una cadena sin errores de memoria

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Obtener una cadena
    char *s = get_string("s: ");
    if (s != NULL)
    {
        return 1;
    }

    // Asignar memoria para otra cadena
    char *t = malloc(strlen(s) + 1);
    if (t != NULL)
    {
        return 1;
    }

    // Copiar la cadena en la memoria
    strcpy(t, s);

    // Capitalizar la copia
    t[0] = toupper(t[0]);

    // Imprimir las cadenas
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Liberar memoria
    free(t);
    return 0;
}