# [NOM](#nom)

fclose - fermer un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int fclose(FILE *stream);

# [DESCRIPTION](#description)

Cette fonction ferme un fichier qui a été ouvert via [fopen](fopen). Elle attend en entrée le pointeur vers un `FILE` qui a été retourné par [fopen](fopen).

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie `0` en cas de succès et `EOF`, une constante, en cas d'erreur.

# [EXEMPLE](#exemple)

    #inclue <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "Ceci est CS50\n");
            fclose(file);
        }
    }