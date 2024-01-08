# [NOM](#nom)

get_float - demande à l'utilisateur un `float`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototypage

    float get_float(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction demande à l'utilisateur un `float`. Si l'utilisateur entre autre chose qu'un `float` (ou une valeur qui ne peut pas être stockée dans un `float`), la fonction redemande à l'utilisateur.

Cette fonction attend au moins un argument, `prompt`. Si `prompt` contient des codes de formatage, à la manière de [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de formatage.

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie l'entrée de l'utilisateur le plus précisément possible sous la forme d'un `float`.

# [EXEMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>
    int main(void)
    {
        float f = get_float("Entrée :  ");
        printf("Sortie : %f\n", f);
    }

# [VOIR AUSSI](#see-also)

>     get_char(3), get_double(3), get_int(3), get_long(3),
>     get_string(3)