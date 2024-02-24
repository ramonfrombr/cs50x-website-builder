# [NOMBRE](#nombre)

malloc - asignar memoria dinámicamente

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdlib.h>

## Prototipo

    void *malloc(size_t size);

Piense en `void *` como el significado de la dirección de cualquier tipo de valor en la memoria. Piense en `size_t` como un `long`.

# [DESCRIPCIÓN](#descripción)

Esta función asigna dinámicamente `size` bytes contiguos de memoria (en el montón) que se pueden usar para almacenar cualquier tipo de valores.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la dirección del primer byte de memoria asignada o `NULL` en casos de error (como cuando no hay suficiente memoria disponible).

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(4);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }