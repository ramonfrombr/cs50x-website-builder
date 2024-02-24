# [NOMBRE](#nombre)

strstr - localizar una subcadena

# [SINOPSIS](#sinopsis)

## Archivos de Encabezado

    #include <cs50.h>
    #include <string.h>

## Prototipo

    string strstr(string haystack, string needle);

# [DESCRIPCIÓN](#descripción)

Esta función busca `needle` en `haystack` (la primera aparición). En otras palabras, determina si (y dónde) `needle` es una subcadena de `haystack`.

# [VALOR DE RETORNO](#valor-de-retorno)

Si se encuentra `needle` en `haystack`, esta función devuelve la subcadena de `haystack` que comienza con `needle`. (Por ejemplo, si `haystack` es "`foo bar bar baz`" y `needle` es "`bar`", esta función devuelve "`bar bar baz`".) Si no se encuentra `needle` en `haystack`, esta función devuelve `NULL`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <string.h>
    #include <stdio.h>

    int main(void)
    {
        string haystack = "foo bar bar baz";
        string needle = "bar";

        string match = strstr(haystack, needle);
        if (match)
        {
            printf("%s\n", match);
        }
    }