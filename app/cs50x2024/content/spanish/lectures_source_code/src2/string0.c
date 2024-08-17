// Imprime cadena de caracteres por caracter, una por línea

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Entrada:  ");
    printf("Salida: ");
    for (int i = 0; s[i] != '\0'; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}