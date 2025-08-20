// Guarda nombres y números a un archivo CSV

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Abre archivo CSV
    FILE *file = fopen("phonebook.csv", "a");
    if (!file)
    {
        return 1;
    }

    // Obtiene nombre y número
    string name = get_string("Nombre: ");
    string number = get_string("Número: ");

    // Imprime a archivo
    fprintf(file, "%s,%s\n", name, number);

    // Cierra archivo
    fclose(file);
}