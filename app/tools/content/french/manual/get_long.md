# [NOM](#nom)

get_long - demande à l'utilisateur un `long`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototype

    long get_long(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction demande à l'utilisateur un `long`. Si l'utilisateur entre autre chose qu'un `long` (ou une valeur qui ne rentre pas dans un `long`), la fonction redemande à l'utilisateur.

Cette fonction attend au moins un argument, `prompt`. Si `prompt` contient des codes de formatage, à la [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de formatage.

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie l'entrée de l'utilisateur sous forme de `long`.

# [EXEMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        long l = get_long("Entrée : ");
        printf("Sortie : %li\n", l);
    }

# [VOIR AUSSI](#see-also)

>     get_char(3), get_double(3), get_float(3), get_int(3), get_string(3),
>     printf(3)