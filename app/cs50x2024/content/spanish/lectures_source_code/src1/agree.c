// Operadores lógicos

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Invitar al usuario a asentir
    char c = get_char("¿Estás de acuerdo?\n");

    // Verificar si está de acuerdo
    if (c == 'Y' || c == 'y')
    {
        printf("De acuerdo.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("No está de acuerdo.\n");
    }
}