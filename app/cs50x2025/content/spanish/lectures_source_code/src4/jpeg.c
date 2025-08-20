// Detecta si un archivo es JPEG

#include <stdio.h>

int main(int argc, char *argv[])
{
    // Comprobar uso
    if (argc != 2)
    {
        return 1;
    }

    // Abrir archivo
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }

    // Leer primeros tres bytes
    unsigned char bytes[3];
    fread(bytes, 3, 1, file);

    // Comprobar primeros tres bytes
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Quizá\n");
    }
    else
    {
        printf("No\n");
    }

    // Cerrar archivo
    fclose(file);
}