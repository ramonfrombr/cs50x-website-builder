# [NOM](#nom)

time - obtenir le temps en secondes

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <time.h>

## Prototype

    long time(NULL);

Considérez cette fonction comme renvoyant un `long` en sortie et prenant seulement `NULL` en entrée.

# [DESCRIPTION](#description)

Cette fonction récupère la date et l'heure actuelles en secondes depuis le 1er janvier 1970, 00:00:00 UTC, également connu sous le nom d'Époque.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre de secondes depuis le 1er janvier 1970, 00:00:00 UTC.

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        printf("Il est maintenant %li.\n", time(NULL));
    }