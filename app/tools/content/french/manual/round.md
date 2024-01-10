# [NOM](#nom)

round - arrondir un nombre à l'entier le plus proche

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double round(double x);

# [DESCRIPTION](#description)

Cette fonction arrondit `x` à l'entier le plus proche.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne, en tant que `double`, `x` arrondi à l'entier le plus proche. Vous pouvez ensuite convertir cette valeur en `long` en toute sécurité (ou en `int` si elle rentre dans la plage).

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Ceci est CS%i\n", (int) round(49.5));
    }