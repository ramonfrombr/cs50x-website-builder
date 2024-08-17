# [NOM](#nom)

srandom - initialiser la génération de nombres pseudo-aléatoires

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #define _DEFAULT_SOURCE
    #include <stdlib.h>

## Prototype

    void srandom(unsigned int seed);

`unsigned int` doit être non négatif.

Définir `_DEFAULT_SOURCE` de cette manière permet d'utiliser [srandom](srandom) dans `stdlib.h`.

# [DESCRIPTION](#description)

Cette fonction modifie la séquence de nombres pseudo-aléatoires générés par [random](random). Elle doit être appelée (une fois) avant d'effectuer des appels à [random](random). En d'autres termes, si vous appelez d'abord [srandom](srandom) avec une valeur de `seed` égale à `1`, les appels ultérieurs à [random](random) renverront des valeurs différentes par rapport à un appel initial à [srandom](srandom) avec une valeur de `seed` égale à `2`.

Plutôt que de fixer une valeur pour `seed`, il est courant de passer la valeur de retour de [time](/2/time) (qui change chaque seconde) à [srandom](srandom).

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction ne renvoie pas de valeur.

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

Appeler `time` avec un argument de `NULL`, une constante définie dans `stdlib.h`, renvoie l'heure courante en secondes.