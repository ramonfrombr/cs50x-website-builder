# [NOM](#nom)

fopen - ouvre un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    FILE *fopen(const char *chemin, const char *mode);

# [DESCRIPTION](#description)

Cette fonction ouvre un fichier, `chemin`. Les valeurs prises en charge pour `mode` sont les suivantes :

- `"r"`, si le fichier est ouvert pour le lire,
- `"w"`, si le fichier est ouvert pour l'écrire, et
- `"a"`, si le fichier est ouvert pour y ajouter du contenu.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction retourne un pointeur vers un `FILE` représentant le fichier ouvert ou, en cas d'erreur (par exemple si le fichier `chemin` n'existe pas), `NULL`.

# [EXEMPLES](#exemples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "This is CS50\n");
            fclose(file);
        }
    }