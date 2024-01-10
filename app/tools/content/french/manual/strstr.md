# [NOM](#nom)

strstr - localise une sous-chaîne

# [SYNOPSIS](#synopsis)

## Fichiers d'en-tête

    #include <cs50.h>
    #include <string.h>

## Prototype

    string strstr(string haystack, string needle);

# [DESCRIPTION](#description)

Cette fonction recherche `needle` dans `haystack` (la première occurrence). En d'autres termes, elle détermine si (et où) `needle` est une sous-chaîne de `haystack`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Si `needle` est trouvé dans `haystack`, cette fonction renvoie la sous-chaîne de `haystack` qui commence par `needle`. (Par exemple, si `haystack` est `"foo bar bar baz"` et `needle` est `"bar"`, cette fonction renvoie `"bar bar baz"`.) Si `needle` n'est pas trouvé dans `haystack`, cette fonction renvoie `NULL`.

# [EXEMPLE](#exemple)

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