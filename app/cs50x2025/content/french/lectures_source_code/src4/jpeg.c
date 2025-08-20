// Détecte si un fichier est un JPEG

#include <stdio.h>

int main(int argc, char *argv[])
{
    // Vérifier l'usage
    if (argc != 2)
    {
        return 1;
    }

    // Ouvrir le fichier
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }

    // Lire les trois premiers octets
    unsigned char bytes[3];
    fread(bytes, 3, 1, file);

    // Vérifier les trois premiers octets
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Peut-être\n");
    }
    else
    {
        printf("Non\n");
    }

    // Fermer le fichier
    fclose(file);
}