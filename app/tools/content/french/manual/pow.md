# [NOM](#nom)

pow - élever un nombre à une puissance

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double pow(double x, double y);

# [DESCRIPTION](#description)

Cette fonction élève `x` à la puissance de `y`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne, en tant que `double`, `x` élevé à la puissance de `y`.

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Un entier 32 bits peut stocker %li valeurs possibles.\n", (long) pow(2, 32));
    }