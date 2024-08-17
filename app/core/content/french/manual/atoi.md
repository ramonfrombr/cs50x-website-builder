# [NOM](#nom)

atoi - convertit une `chaine de caractères` en un `entier`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    int atoi(string s);

# [DESCRIPTION](#description)

Cette fonction convertit un entier (positif ou négatif) d'une `chaine de caractères` (par exemple, `"50"`) en un `entier` (par exemple, `50`).

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie son entrée, `s`, en tant qu'`entier`.

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("C'est CS%i\n", atoi("50"));
    }