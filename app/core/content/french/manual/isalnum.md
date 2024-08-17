# [NOM](#nom)

isalnum - vérifie si un caractère est alphanumérique

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isalnum(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est alphanumérique (c'est-à-dire une lettre ou un chiffre) ou non.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie un `int` non nul si `c` est alphanumérique et `0` si `c` n'est pas alphanumérique.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isalnum(c))
        {
            printf("Votre entrée est alphanumérique.\n");
        }
        else
        {
            printf("Votre entrée n'est pas alphanumérique.\n");
        }
    }