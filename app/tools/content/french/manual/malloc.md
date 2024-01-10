# [NOM](#nom)

malloc - allouer de la mémoire dynamiquement

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    void *malloc(size_t size);

Pensez à `void *` comme signifiant l'adresse de n'importe quel type de valeur en mémoire. Pensez à `size_t` comme un `long`.

# [DESCRIPTION](#description)

Cette fonction alloue dynamiquement `size` octets de mémoire contigus (sur le tas) qui peuvent être utilisés pour stocker n'importe quel type de valeurs.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie l'adresse du premier octet de mémoire alloué ou `NULL` en cas d'erreur (comme lorsque la mémoire disponible est insuffisante).

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(4);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }