# [NOM](#nom)

get_int - demande à l'utilisateur un `int`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototype

    int get_int(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction demande à l'utilisateur un `int`. Si l'utilisateur entre autre chose qu'un `int` (ou une valeur qui ne peut pas tenir dans un `int`), la fonction demande à nouveau à l'utilisateur.

Cette fonction attend au moins un argument, `prompt`. Si `prompt` contient des codes de format, à la manière de [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de format.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie l'entrée de l'utilisateur sous forme d'un `int`.

# [EXEMPLE](#exemple)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        int i = get_int("Entrée :  ");
        printf("Sortie : %i\n", i);
    }

# [VOIR AUSSI](#voir-aussi)

>     get_char(3), get_double(3), get_float(3), get_long(3),
>     get_string(3), printf(3)