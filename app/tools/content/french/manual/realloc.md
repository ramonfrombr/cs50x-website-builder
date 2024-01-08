# [NOM](#nom)

realloc - réalloue dynamiquement la mémoire

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdlib.h>

## Prototype

    void *realloc(void *ptr, size_t size);

Pensez à `void *` comme signifiant l'adresse de n'importe quel type de valeur en mémoire. Pensez à `size_t` comme à une valeur `long`.

# [DESCRIPTION](#description)

Cette fonction redimensionne dynamiquement un bloc de mémoire qui a été alloué par `malloc`, dont l'adresse du premier octet est `ptr`, pour qu'il contienne `size` octets contigus au lieu de la taille d'origine, déplaçant (et copiant) les octets d'origine en mémoire si nécessaire.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie l'adresse du premier octet du bloc réalloué (qui peut être ou non la même que `ptr`) ou `NULL` en cas d'erreur (par exemple lorsque la mémoire disponible est insuffisante).

# [EXEMPLE](#exemple)

    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *s = malloc(3);
        if (s == NULL)
        {
            return 1;
        }

        s[0] = 'h';
        s[1] = 'i';
        s[2] = '\0';
        printf("%s\n", s);

        char *tmp = realloc(s, 4);
        if (tmp == NULL)
        {
            free(s);
            return 1;
        }
        s = tmp;

        s[2] = '!';
        s[3] = '\0';
        printf("%s\n", s);

        free(s);
        return 0;
    }