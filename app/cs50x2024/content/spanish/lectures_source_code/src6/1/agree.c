// Operadores lógicos

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Indicador de acuerdo del usuario
    char c = get_char("¿Estás de acuerdo?\n");

    // Verifica si está de acuerdo
    if (c == 'Y' || c == 'y')
    {
        printf("De acuerdo.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("No estoy de acuerdo.\n");
    }
}