# [NOM](#nom)

isspace - vérifie si un caractère est un espace (par exemple, un saut de ligne, un espace ou une tabulation)

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isspace(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est un espace (par exemple, `\n`, `' '`, ou `'\t'`) ou non.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie un `int` différent de zéro si `c` est un espace, et `0` si `c` n'est pas un espace.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isspace(c))
        {
            printf("Votre entrée est un espace.\n");
        }
        else
        {
            printf("Votre entrée n'est pas un espace.\n");
        }
    }