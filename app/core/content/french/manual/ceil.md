# [NOM](#nom)

ceil - calculer le plafond d'un nombre

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double ceil(double x);

# [DESCRIPTION](#description)

Cette fonction renvoie le plafond de `x`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie, en tant que `double`, le plus petit entier qui n'est pas inférieur à `x`. Vous pouvez tranquillement convertir cette valeur en un `long` (ou un `int` si elle correspond).

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Ceci est CS%i\n", (int) ceil(49.9));
    }