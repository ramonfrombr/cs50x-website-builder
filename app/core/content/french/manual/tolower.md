# [NOM](#nom)

tolower - convertit un `char` en minuscule

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <ctype.h>

## Prototypage

    int tolower(char c);

Pensez à cette fonction comme prenant un `char` en entrée.

# [DESCRIPTION](#description)

Cette fonction convertit `c` en minuscule.

# [VALEUR DE RETOUR](#valeur-de-retour)

Si `c` est une lettre majuscule (`A` à `Z`), cette fonction renvoie son équivalent en minuscule (`a` à `z`). Si `c` n'est pas une lettre majuscule, cette fonction renvoie `c` lui-même.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>

    int main(void)
    {
        char c = get_char("Entrée : ");
        printf("Sortie : %c\n", tolower(c));
    }