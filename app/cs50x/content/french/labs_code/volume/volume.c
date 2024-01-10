// Modifie le volume d'un fichier audio

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Nombre d'octets dans l'en-tête .wav
const int TAILLE_EN_TETE = 44;

int main(int argc, char *argv[])
{
    // Vérifie les arguments de la ligne de commande
    if (argc != 4)
    {
        printf("Utilisation: ./volume input.wav output.wav facteur\n");
        return 1;
    }

    // Ouvre les fichiers et détermine le facteur d'échelle
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Impossible d'ouvrir le fichier.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Impossible d'ouvrir le fichier.\n");
        return 1;
    }

    float facteur = atof(argv[3]);

    // TODO: Copier l'en-tête du fichier d'entrée dans le fichier de sortie

    // TODO: Lire les échantillons du fichier d'entrée et écrire les données mises à jour dans le fichier de sortie

    // Ferme les fichiers
    fclose(input);
    fclose(output);
}