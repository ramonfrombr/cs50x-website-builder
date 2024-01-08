# [NOM](#nom)

fread - lit des octets à partir d'un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);

Pensez à `void *` comme représentant l'adresse du premier octet de n'importe quel type de données. Pensez à `size_t` comme un `long`.

# [DESCRIPTION](#description)

Cette fonction lit des données à partir d'un fichier qui a été ouvert via [fopen](fopen). Elle attend en entrée :

- `ptr`, qui est l'adresse (du premier octet) de la mémoire dans laquelle lire les données,
- `size`, qui est la taille (en octets) du type de données à lire,
- `nmemb`, qui est le nombre de ces types à lire en une fois, et
- `stream`, qui est un pointeur vers un `FILE` retourné par [fopen](fopen).

Par exemple, si vous lisez un `char` à la fois, `size` serait `sizeof(char)` (c'est-à-dire `1`), et `nmemb` serait `1`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre d'éléments lus, ce qui correspond au nombre d'octets lus lorsque `size` vaut `1`.

Si une erreur se produit, ou si la fin du fichier est atteinte, cette fonction peut renvoyer une valeur inférieure à `nmemb` ou même `0`.

Le fichier ouvert "se souvient" du nombre d'octets qui ont été lus avec succès, de sorte que les appels ultérieurs à cette fonction pour `stream` renverront des octets après ceux déjà lus.

# [EXEMPLES](#exemples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "r");
        if (file != NULL)
        {
            char c;
            while (fread(&c, sizeof(char), 1, file))
            {
                printf("%c", c);
            }
            fclose(file);
        }
    }