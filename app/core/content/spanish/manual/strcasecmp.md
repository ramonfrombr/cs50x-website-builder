# [NOMBRE](#nombre)

strcasecmp: compara dos cadenas de caracteres sin hacer distinción entre mayúsculas y minúsculas.

# [SINOPSIS](#sinopsis)

## Archivos de cabecera

    #include <cs50.h>#include <strings.h>

## Prototipo

    int strcasecmp(string s1, string s2);

# [DESCRIPCIÓN](#descripción)

Esta función compara dos cadenas de caracteres sin hacer distinción entre mayúsculas y minúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna:

- un `int` menor que `0` si `s1` viene antes que `s2`, sin importar las mayúsculas y minúsculas,
- `0` si `s1` es igual a `s2`, sin importar las mayúsculas y minúsculas, o
- un `int` mayor que `0` si `s1` viene después que `s2`, sin importar las mayúsculas y minúsculas.

Las cadenas se comparan utilizando el orden "ASCIIbetical", basado en los valores ASCII de sus caracteres. Por ejemplo, `"AAA"` vendría antes que `"BBB"`.

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <strings.h>

    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcasecmp(s1, s2) == 0)
        {
            printf("Esas son iguales, incluso ignorando las mayúsculas y minúsculas.\n");
        }
        else
        {
            printf("Esas son diferentes, incluso ignorando las mayúsculas y minúsculas.\n");
        }
    }