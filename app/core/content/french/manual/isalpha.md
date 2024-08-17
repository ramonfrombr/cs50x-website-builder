# [NOM](#nom)

isalpha - vérifier si un caractère est alphabétique

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isalpha(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est alphabétique (c'est-à-dire une lettre) ou non.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne un `int` non nul si `c` est alphabétique et `0` si `c` n'est pas alphabétique.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isalpha(c))
        {
            printf("Votre entrée est alphabétique.\n");
        }
        else
        {
            printf("Votre entrée n'est pas alphabétique.\n");
        }
    }