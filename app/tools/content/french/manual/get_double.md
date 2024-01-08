# [NOM](#name)

get_double - demander à l'utilisateur un `double`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototype

    double get_double(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction demande à l'utilisateur un `double`. Si l'utilisateur entre autre chose qu'un `double` (ou une valeur qui ne peut pas être stockée dans un `double`), la fonction demande à l'utilisateur à nouveau.

Cette fonction attend au moins un argument, `prompt`. Si `prompt` contient des codes de format, à la manière de [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de format.

# [VALEUR DE RÉTOUR](#return-value)

Cette fonction renvoie l'entrée de l'utilisateur aussi précisément que possible en tant que `double`.

# [EXEMPLE](#example)

    #include <cs50.h>#include <stdio.h>
    int main(void)
    {
        double d = get_double("Entrée:  ");
        printf("Sortie: %f\n", d);
    }

# [VOIR AUSSI](#see-also)

>     get_char(3), get_float(3), get_int(3), get_long(3),
>     get_string(3), printf(3)