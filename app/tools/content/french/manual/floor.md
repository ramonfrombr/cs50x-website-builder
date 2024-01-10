# [NOM](#nom)

floor - calcule l'arrondi inférieur d'un nombre

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <math.h>

## Prototype

    double floor(double x);

# [DESCRIPTION](#description)

Cette fonction retourne l'arrondi inférieur de `x`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne, en tant que `double`, le plus grand entier qui n'est pas supérieur à `x`. Vous pouvez en toute sécurité convertir cette valeur en un `long` (ou un `int` s'il le permet).

# [EXEMPLE](#exemple)

    #include <math.h>
    #include <stdio.h>

    int main(void)
    {
        printf("Ceci est CS%i\n", (int) floor(50.1));
    }