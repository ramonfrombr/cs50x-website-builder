# [NOM](#nom)

atof - convertit une `chaîne de caractères` en `float`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    float atof(chaine s);

# [DESCRIPTION](#description)

Cette fonction convertit une valeur à virgule flottante (positive ou négative) d'une `chaîne de caractères` (par exemple, `"50.0"`) en `float` (par exemple, `50.0`).

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie son entrée, `s`, en tant que `float`.

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        printf("This is CS%.0f\n", atof("50.0"));
    }