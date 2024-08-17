# [NOM](#nom)

isblank - vérifie si un caractère est vide (c'est-à-dire un espace ou une tabulation)

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isblank(char c);

Considérez cette fonction comme prenant une entrée de type `char`.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est vide (c'est-à-dire `' '` ou `'\t'`) ou non.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie une valeur `int` non nulle si `c` est vide et `0` si `c` n'est pas vide.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isblank(c))
        {
            printf("Votre entrée est vide.\n");
        }
        else
        {
            printf("Votre entrée n'est pas vide.\n");
        }
    }