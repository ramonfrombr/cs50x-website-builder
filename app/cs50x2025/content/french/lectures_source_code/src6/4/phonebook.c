// Sauvegarde le nom et le numéro dans un fichier CSV.

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Ouverture du fichier CSV
    FILE *file = fopen("répertoire.csv", "a");
    if (!file)
    {
        return 1;
    }

    // Récupération du nom et du numéro
    string name = get_string("Nom : ");
    string number = get_string("Numéro : ");

    // Écriture dans le fichier
    fprintf(file, "%s,%s\n", name, number);

    // Fermeture du fichier
    fclose(file);
}