// Guarda nombres y números en un archivo CSV

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Abre el archivo CSV
    FILE *file = fopen("phonebook.csv", "a");
    if (!file)
    {
        return 1;
    }

    // Obtener nombre y número
    string name = get_string("Nombre: ");
    string number = get_string("Número: ");

    // Imprimir en el archivo
    fprintf(file, "%s,%s\n", name, number);

    // Cerrar archivo
    fclose(file);
}