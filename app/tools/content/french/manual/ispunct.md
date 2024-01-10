# [NOM](#nom)

ispunct - vérifie si un caractère est de la ponctuation

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int ispunct(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est un signe de ponctuation (par exemple, `'.'`, ou `','`, ou `'!'`, etc.) ou non.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie un `int` non nul si `c` est de la ponctuation et `0` si `c` n'est pas de la ponctuation.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (ispunct(c))
        {
            printf("Votre entrée est de la ponctuation.\n");
        }
        else
        {
            printf("Votre entrée n'est pas de la ponctuation.\n");
        }
    }