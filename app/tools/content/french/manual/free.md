# [NOM](#nom)

free - libère la mémoire allouée dynamiquement

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    void free(void *ptr);

Considérez `void *` comme signifiant l'adresse de n'importe quel type de valeur en mémoire.

# [DESCRIPTION](#description)

Cette fonction libère la mémoire qui a été allouée dynamiquement avec `malloc`. Elle attend en entrée le pointeur qui a été renvoyé par [malloc](malloc).

# [VALEUR DE RENVOI](#valeur-de-renvoi)

Cette fonction ne renvoie pas de valeur.

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main(void)
    {
        char *s = "hello, world\n";
        char *t = malloc(strlen(s) + 1);
        if (t != NULL)
        {
            strcpy(t, s);
            printf("%s\n", t);
            free(t);
        }
    }