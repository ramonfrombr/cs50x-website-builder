# [NOM](#nom)

strcpy - copier une chaîne de caractères

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <string.h>

## Prototype

    char *strcpy(char *dest, char *src);

# [DESCRIPTION](#description)

Cette fonction copie la chaîne de caractères à `src`, y compris son caractère de fin `'\0'`, dans la mémoire à `dest`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie `dest`.

# [EXEMPLE](#exemple)

    #include <cs50.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = get_string("s : ");
        if (s != NULL)
        {
            char *t = malloc(strlen(s) + 1);
            if (t != NULL)
            {
                strcpy(t, s);
                printf("s : %s\n", s);
                printf("t : %s\n", t);
            }
        }
    }