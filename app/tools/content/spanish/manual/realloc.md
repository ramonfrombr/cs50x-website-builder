# [NOMBRE](#nombre)

realloc: reallocar memoria dinámicamente

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdlib.h>

## Prototipo

    void *realloc(void *ptr, size_t size);

Piensa en `void *` como la dirección de cualquier tipo de valor en memoria. Piensa en `size_t` como un `long`.

# [DESCRIPCIÓN](#descripción)

Esta función redimensiona dinámicamente un bloque de memoria que fue devuelto por `malloc`. La dirección del primer byte de este bloque es `ptr` y se redimensiona para tener `size` bytes contiguos, moviendo (y copiando) los bytes originales en memoria según sea necesario.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve la dirección del primer byte del bloque realocado (que puede o no ser igual a `ptr`) o `NULL` en casos de error (como cuando no hay suficiente memoria disponible).

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(3);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '\0';
        printf("%s\n", s);

        char *tmp = realloc(s, 4);
        if (tmp == NULL)
        {
            free(s);
            return 1;
        }
        s = tmp;

        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }