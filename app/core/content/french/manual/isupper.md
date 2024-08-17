# [NOM](#nom)

isupper - vérifie si un caractère est en majuscule

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isupper(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est une lettre majuscule (`'A'` à `'Z'`) ou pas. En d'autres termes, elle vérifie si la valeur [ASCII](https://asciichart.com/) de `c` est comprise entre 65 et 90 inclus.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne un `int` différent de zéro si `c` est une lettre majuscule et `0` si `c` n'est pas une lettre majuscule.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isupper(c))
        {
            printf("Votre entrée est une lettre majuscule.\n");
        }
        else
        {
            printf("Votre entrée n'est pas une lettre majuscule.\n");
        }
    }