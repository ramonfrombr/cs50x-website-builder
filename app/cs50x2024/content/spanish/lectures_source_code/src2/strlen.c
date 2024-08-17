// Determina la longitud de una cadena

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Solicita el nombre del usuario
    string s = get_string("Nombre: ");

    // Cuenta el número de caracteres hasta '\0' (también conocido como NUL)
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}