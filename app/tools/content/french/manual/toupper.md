# [NOM](#nom)

toupper - convertit un `char` en majuscule

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototype

    int toupper(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction convertit `c` en majuscule.

# [VALEUR DE RETOUR](#valeur-de-retour)

Si `c` est une lettre minuscule (`a` à `z`), cette fonction retourne son équivalent en majuscule (`A` à `Z`). Si `c` n'est pas une lettre minuscule, cette fonction retourne `c` lui-même.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée:  ");
        printf("Sortie: %c\n", toupper(c));
    }