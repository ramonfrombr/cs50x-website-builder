# [NOM](#nom)

log2 - calcule le logarithme en base 2 d'un nombre

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double log2(double x);

# [DESCRIPTION](#description)

Cette fonction calcule le logarithme en base 2 de `x`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie, sous forme de `double`, le logarithme en base 2 de `x`.

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Ceci est CS%i\n", (int) log2(1125899906842624));
    }