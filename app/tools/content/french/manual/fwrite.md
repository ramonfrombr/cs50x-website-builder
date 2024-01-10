# [NOM](#nom)

fwrite - écrire des octets dans un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);

Considérez `void *` comme représentant l'adresse du premier octet de tout type de données. Considérez `size_t` comme un `long`.

# [DESCRIPTION](#description)

Cette fonction écrit des données dans un fichier qui a été ouvert via [fopen](fopen). Elle attend en entrée:

- `ptr`, qui est l'adresse (du premier octet) de la mémoire à partir de laquelle lire les données,
- `size`, qui est la taille (en octets) du type de données à écrire,
- `nmemb`, qui est le nombre de ces types à écrire en une seule fois, et
- `stream`, qui est le pointeur vers un `FILE` renvoyé par [fopen](fopen).

Par exemple, si vous écrivez un `char` à la fois, `size` serait `sizeof(char)` (c'est-à-dire `1`), et `nmemb` serait `1`.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre d'éléments écrits, qui est égal au nombre d'octets écrits lorsque `size` vaut `1`.

Si une erreur se produit, ou si la fin du fichier est atteinte, cette fonction peut renvoyer une valeur inférieure à `nmemb` ou même `0`.

# [EXEMPLES](#exemples)

    #include <stdio.h>

    int main(void)
    {
        FILE *input = fopen("input.txt", "r");
        if (input == NULL)
        {
            return 1;
        }

        FILE *output = fopen("output.txt", "w");
        if (output == NULL)
        {
            fclose(input);
            return 1;
        }

        char c;
        while (fread(&c, sizeof(char), 1, input))
        {
            fwrite(&c, sizeof(char), 1, output);
        }

        fclose(input);
        fclose(output);
    }