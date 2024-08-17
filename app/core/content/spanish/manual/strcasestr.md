# [NOMBRE](#nombre)

strstr, strcasestr - localizar una subcadena

# [SINOPSIS](#sinopsis)

strcasestr - localizar una subcadena

## Archivos de cabecera

    #include <cs50.h>

    #define _GNU_SOURCE
    #include <string.h>

## Prototipo

    string strcasestr(string haystack, string needle);

La definición de `_GNU_SOURCE` de esta manera permite el uso de [strcasestr](strcasestr) dentro de `string.h`.

# [DESCRIPCIÓN](#descripción)

Esta función busca `needle` (la primera aparición) en `haystack`, sin tener en cuenta las mayúsculas y minúsculas. En otras palabras, determina si y dónde `needle` es una subcadena de `haystack`, ignorando las mayúsculas y minúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Si se encuentra `needle` en `haystack`, ignorando las mayúsculas y minúsculas, esta función retorna la subcadena de `haystack` que comienza con `needle`. (Por ejemplo, si `haystack` es `"FOO BAR BAR BAZ"` y `needle` es `"bar"`, esta función retorna `"BAR BAR BAZ"`.) Si no se encuentra `needle` en `haystack`, ignorando las mayúsculas y minúsculas, esta función retorna `NULL`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <stdio.h>

    #define _GNU_SOURCE
    #include <string.h>

    int main(void)
    {
        string haystack = "FOO BAR BAR BAZ";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }