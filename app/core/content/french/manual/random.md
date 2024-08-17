# [NOM](#nom)

random - générer un nombre pseudo-aléatoire

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #define _DEFAULT_SOURCE#include <stdlib.h>

## Prototype

    long random(void);

Le fait de définir `_DEFAULT_SOURCE` de cette manière permet d'utiliser `random` dans `stdlib.h`.

# [DESCRIPTION](#description)

Cette fonction génère un nombre pseudo-aléatoire entre `0` et `RAND_MAX`, inclusivement, où `RAND_MAX` est une constante définie dans `stdlib.h`.

Pour obtenir une valeur pseudo-aléatoire en virgule flottante entre `0.0` et `1.0`, exclusivement, il est courant de diviser la valeur de retour de [random](random) par `(double) RAND_MAX + 1`, comme suit :

    float nombre = random() / ((double) RAND_MAX + 1);

Pour obtenir un nombre pseudo-aléatoire entier entre `0` et `N`, exclusivement, où `N` est un entier donné, il est courant de diviser la valeur de retour de [random](random) par `(double) RAND_MAX + 1` puis de multiplier le quotient par `N`, comme suit :

    int nombre = (random() / ((double) RAND_MAX + 1)) * N;

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre généré de manière pseudo-aléatoire sous forme d'un `long`.

# [EXEMPLE](#exemple)

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        srandom(time(NULL));
        printf("%lu\n", random());
        printf("%lu\n", random());
        printf("%lu\n", random());
    }

L'appel de la fonction `time` avec une entrée de `NULL`, une constante définie dans `stdlib.h`, renvoie l'heure actuelle en secondes.