# [NAME](#name)

islower - vérifie si un caractère est en minuscule

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int islower(char c);

Considérez cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction vérifie si `c` est une lettre minuscule (`'a'` à `'z'`) ou non. En d'autres termes, elle vérifie si la valeur [ASCII](https://asciichart.com/) de `c` est comprise entre 97 et 122, inclus.

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie un `int` non nul si `c` est une lettre minuscule et `0` si `c` n'est pas une lettre minuscule.

# [EXEMPLE](#example)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        if (islower(c))
        {
            printf("Votre entrée est une lettre minuscule.\n");
        }
        else
        {
            printf("Votre entrée n'est pas une lettre minuscule.\n");
        }
    }