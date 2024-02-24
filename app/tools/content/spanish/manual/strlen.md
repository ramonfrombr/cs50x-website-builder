# [NOMBRE](#nombre)

strlen - calcular la longitud de una cadena

# [SINOPSIS](#sinopsis)

strlen - calcular la longitud de una cadena

## Archivos de cabecera

    #include <cs50.h>
    #include <string.h>

## Prototipo

    int strlen(string s);

# [DESCRIPCIÓN](#descripción)

Esta función calcula la longitud de `s`.

# [VALOR DEVUELTO](#valor-devuelto)

Esta función devuelve el número de caracteres en `s`, excluyendo el byte terminador NUL (es decir, `'\0'`).

# [EJEMPLO](#ejemplo)

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        string s = get_string("Entrada:  ");
        printf("Salida: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            printf("%c", s[i]);
        }
        printf("\n");
    }