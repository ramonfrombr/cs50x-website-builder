# [NOM](#nom)

sqrt - calculer la racine carrée d'un nombre

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double sqrt(double x);

# [DESCRIPTION](#description)

Cette fonction calcule la racine carrée de `x`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne la racine carrée de `x`, en tant que `double`.

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Ceci est CS%i\n", (int) sqrt(2500));
    }