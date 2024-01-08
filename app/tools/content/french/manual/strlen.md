# [NOM](#nom)

strlen - calculer la longueur d'une chaîne de caractères

# [SYNOPSIS](#synopsis)

strlen - calculer la longueur d'une chaîne de caractères

## Fichiers d'en-tête

    #include <cs50.h>
    #include <string.h>

## Prototype

    int strlen(string s);

# [DESCRIPTION](#description)

Cette fonction calcule la longueur de `s`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre de caractères dans `s`, en excluant le caractère de fin de chaîne NUL (c'est-à-dire `'\0'`).

# [EXEMPLE](#exemples)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s = get_string("Entrée:  ");
        printf("Sortie: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", s[i]);
        }
        printf("\n");
    }