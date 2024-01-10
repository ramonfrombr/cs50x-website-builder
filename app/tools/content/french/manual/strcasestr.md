# [NOM](#nom)

strstr, strcasestr - localiser une sous-chaîne

# [SYNOPSIS](#synopsis)

strcasestr - localiser une sous-chaîne

## Fichiers d'en-tête

    #include <cs50.h>

    #define _GNU_SOURCE
    #include <string.h>

## Prototype

    string strcasestr(string haystack, string needle);

Définir `_GNU_SOURCE` de cette manière permet d'utiliser [strcasestr](strcasestr) dans `string.h`.

# [DESCRIPTION](#description)

Cette fonction recherche `haystack` pour (la première occurrence de) `needle` sans tenir compte de la casse. En d'autres termes, elle détermine si (et où) `needle` est une sous-chaîne de `haystack`, en ignorant la casse.

# [VALEUR DE RETOUR](#valeur-de-retour)

Si `needle` est trouvé dans `haystack`, en ignorant la casse, cette fonction renvoie la sous-chaîne de `haystack` qui commence par `needle`. (Par exemple, si `haystack` est `"FOO BAR BAR BAZ"` et `needle` est `"bar"`, cette fonction renvoie `"BAR BAR BAZ"`.) Si `needle` n'est pas trouvé dans `haystack`, en ignorant la casse, cette fonction renvoie `NULL`.

# [EXEMPLE](#exemple)

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