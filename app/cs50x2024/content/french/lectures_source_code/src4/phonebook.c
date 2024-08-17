// Enregistre les noms et les numéros dans un fichier CSV

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Ouvrir le fichier CSV
    FILE *file = fopen("phonebook.csv", "a");
    if (!file)
    {
        return 1;
    }

    // Obtenir le nom et le numéro
    string name = get_string("Nom : ");
    string number = get_string("Numéro : ");

    // Imprimer dans le fichier
    fprintf(file, "%s,%s\n", name, number);

    // Fermer le fichier
    fclose(file);
}