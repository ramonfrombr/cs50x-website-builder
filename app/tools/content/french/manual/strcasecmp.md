# [NOM](#nom)

strcasecmp - compare deux chaînes de caractères en ignorant la casse

# [SYNOPSIS](#synopsis)

## Fichiers d'entête

    #include <cs50.h>#include <strings.h>

## Prototype

    int strcasecmp(string s1, string s2);

# [DESCRIPTION](#description)

Cette fonction compare deux chaînes de caractères sans tenir compte de la casse.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne

- un `int` inférieur à `0` si `s1` est avant `s2`, en ignorant la casse,
- `0` si `s1` est identique à `s2`, en ignorant la casse, ou
- un `int` supérieur à `0` si `s1` est après `s2`, en ignorant la casse.

Les chaînes de caractères sont comparées en utilisant un ordre "ASCIIbélique", basé sur les valeurs ASCII de leurs caractères. Par exemple, `"AAA"` serait avant `"BBB"`.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <stdio.h>
    #include <strings.h>

    int main(void)
    {
        string s1 = get_string("s1 : ");
        string s2 = get_string("s2 : ");
        if (strcasecmp(s1, s2) == 0)
        {
            printf("Ce sont les mêmes, en ignorant la casse.\n");
        }
        else
        {
            printf("Ce sont différentes, même en ignorant la casse.\n");
        }
    }