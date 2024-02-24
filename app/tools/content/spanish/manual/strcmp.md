# [NOMBRE](#nombre)

strcmp - compara dos cadenas de caracteres

# [SINOPSIS](#sinopsis)

## Archivos de cabecera

    #include <cs50.h>
    #include <string.h>

## Prototipo

    int strcmp(string s1, string s2);

# [DESCRIPCIÓN](#descripción)

Esta función compara dos cadenas de caracteres de forma sensible a mayúsculas y minúsculas.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función retorna

- un `int` menor a `0` si `s1` viene antes que `s2`,
- `0` si `s1` es igual a `s2`,
- un `int` mayor a `0` si `s1` viene después que `s2`.

Las cadenas se comparan utilizando un orden "ASCIIbetico", basado en los valores ASCII de sus caracteres. Por ejemplo, `"AAA"` vendría antes que `"BBB"`, y `"AAA"` también vendría antes que `"aaa"`.

# [EJEMPLOS](#ejemplos)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s1 = get_string("s1: ");
        string s2 = get_string("s2: ");
        if (strcmp(s1, s2) == 0)
        {
            printf("Esas son iguales.\n");
        }
        else
        {
            printf("Esas son diferentes.\n");
        }
    }