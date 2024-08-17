# [NOM](#nom)

strcmp - comparer deux chaînes de caractères

# [SYNOPSIS](#synopsis)

## Fichiers d'en-tête

    #include <cs50.h>
    #include <string.h>

## Prototype

    int strcmp(string s1, string s2);

# [DESCRIPTION](#description)

Cette fonction compare deux chaînes de caractères de manière sensible à la casse.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie

- un `int` inférieur à `0` si `s1` vient avant `s2`,
- `0` si `s1` est identique à `s2`,
- un `int` supérieur à `0` si `s1` vient après `s2`.

Les chaînes de caractères sont comparées en utilisant l'ordre "ASCIIbétique", basé sur les valeurs ASCII de leurs caractères. Par exemple, `"AAA"` viendrait avant `"BBB"`, et `"AAA"` viendrait également avant `"aaa"`.

# [EXEMPLES](#exemples)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s1 = get_string("s1 : ");
        string s2 = get_string("s2 : ");
        if (strcmp(s1, s2) == 0)
        {
            printf("Ce sont les mêmes.\n");
        }
        else
        {
            printf("Ce sont différentes.\n");
        }
    }