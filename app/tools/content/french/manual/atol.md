# [NOM](#nom)

atol - convertit une `string` en un `long`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    long atol(string s);

# [DESCRIPTION](#description)

Cette fonction convertit un entier (positif ou négatif) d'une `string` (par exemple, `"50"`) en un `long` (par exemple, `50`).

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne son entrée, `s`, en tant que `long`.

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("Ceci est CS%li\n", atol("50"));
    }