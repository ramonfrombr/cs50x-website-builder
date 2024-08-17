# [NOMBRE](#nombre)

fread - leer bytes de un archivo

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <stdio.h>

## Prototipo

    size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);

Piensa en `void *` como la representación de la dirección del primer byte de cualquier tipo de dato. Piensa en `size_t` como un `long`.

# [DESCRIPCIÓN](#descripción)

Esta función lee datos de un archivo que ha sido abierto mediante [fopen](fopen). Espera como entrada:

- `ptr`, que es la dirección (del primer byte) de la memoria en la que se leerán los datos,
- `size`, que es el tamaño (en bytes) del tipo de dato a leer,
- `nmemb`, que es el número de esos tipos a leer a la vez, y
- `stream`, que es el puntero a un `FILE` devuelto por [fopen](fopen).

Por ejemplo, si se lee un `char` a la vez, `size` sería `sizeof(char)` (es decir, `1`), y `nmemb` sería `1`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de elementos leídos, que es igual al número de bytes leídos cuando `size` es `1`.

Si se produce un error o se alcanza el final del archivo, esta función podría devolver un valor menor que `nmemb` o incluso `0`.

El archivo abierto "recuerda" el número de bytes que se han leído correctamente, de modo que las llamadas posteriores a esta función para `stream` devolverán bytes después de los ya leídos.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "r");
        if (file != NULL)
        {
            char c;
            while (fread(&c, sizeof(char), 1, file))
            {
                printf("%c", c);
            }
            fclose(file);
        }
    }