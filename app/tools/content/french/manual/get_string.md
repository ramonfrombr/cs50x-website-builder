# [NOM](#name)

get_string - demande à l'utilisateur une `chaine de caractères`

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <cs50.h>

## Prototype

    string get_string(string prompt, ...);

# [DESCRIPTION](#description)

Cette fonction demande à l'utilisateur une `chaine de caractères`.

Cette fonction attend au moins un argument, `prompt`. Si `prompt` contient des codes de format, à la manière de [printf](printf), cette fonction accepte également des arguments supplémentaires, un par code de format.

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie la saisie de l'utilisateur sous la forme d'une `chaine de caractères`.

# [EXEMPLE](#example)

    #include <cs50.h>
    #include <stdio.h>
    int main(void)
    {
        string s = get_string("Entrée :  ");
        printf("Sortie : %s\n", s);
    }

# [VOIR AUSSI](#see-also)

>     get_char(3), get_double(3), get_float(3), get_int(3),
>     get_long(3), printf(3)