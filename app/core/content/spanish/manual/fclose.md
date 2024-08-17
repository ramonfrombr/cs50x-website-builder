# [NOMBRE](#nombre)

fclose: cierra un archivo

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    int fclose(FILE *stream);

# [DESCRIPCIÓN](#descripción)

Esta función cierra un archivo que ha sido abierto a través de [fopen](fopen). Espera como entrada un puntero a `FILE` que fue devuelto por [fopen](fopen).

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve `0` si tiene éxito y `EOF`, una constante, en casos de error.

# [EJEMPLO](#ejemplo)

    #inclue <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file != NULL)
        {
            fprintf(file, "Esto es CS50\n");
            fclose(file);
        }
    }