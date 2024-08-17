// Almacena nombres usando un arreglo

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Nombres
    string names[4];
    names[0] = "EMMA";
    names[1] = "RODRIGO";
    names[2] = "BRIAN";
    names[3] = "DAVID";

    // Imprime el nombre de Emma
    printf("%s\n", names[0]);
    printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);
}