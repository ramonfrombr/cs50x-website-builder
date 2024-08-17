# [NOM](#nom)

isdigit - vérifie si un caractère est un chiffre

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int isdigit(char c);

Pensez à cette fonction comme prenant un `char` en tant qu'entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est un chiffre décimal (`'0'` à `'9'`) ou non. En d'autres termes, elle vérifie si la valeur [ASCII](https://asciichart.com/) de `c` est comprise entre 48 et 57, inclus.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie un `int` non nul si `c` est un chiffre décimal et `0` si `c` n'est pas un chiffre décimal.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (isdigit(c))
        {
            printf("Votre entrée est un chiffre.\n");
        }
        else
        {
            printf("Votre entrée n'est pas un chiffre.\n");
        }
    }