# [NOM](#nom)

get_char - invite l'utilisateur à entrer un « char »

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototype

    char get_char(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction invite l'utilisateur à entrer un « char ». Si l'utilisateur entre plus ou moins d'un « char », la fonction lui demande à nouveau.

Cette fonction attend au moins un argument, « prompt ». Si « prompt » contient des codes de formatage, à la [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de formatage.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie en sortie la saisie de l'utilisateur sous forme de « char ».

# [EXEMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        char c = get_char("Input:  ");
        printf("Output: %c.\n", c);
    }

# [VOIR AUSSI](#see-also)

>     get_double(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)