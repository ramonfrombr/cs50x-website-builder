# [NOMBRE](#nombre)

strcpy - copia una cadena

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <string.h>

## Prototipo

    char *strcpy(char *dest, char *src);

# [DESCRIPCIÓN](#descripción)

Esta función copia la cadena en `src`, incluyendo su terminación `'\0'`, en la memoria en `dest`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve `dest`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = get_string("s: ");
        if (s != NULL)
        {
            char *t = malloc(strlen(s) + 1);
            if (t != NULL)
            {
                strcpy(t, s);
                printf("s: %s\n", s);
                printf("t: %s\n", t);
            }
        }
    }