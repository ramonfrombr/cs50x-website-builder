# [NOMBRE](#nombre)

fwrite - escribe bytes en un archivo

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);

Piensa en `void *` como representando la dirección del primer byte de cualquier tipo de datos. Piensa en `size_t` como un `long`.

# [DESCRIPCIÓN](#descripción)

Esta función escribe datos en un archivo que ha sido abierto a través de [fopen](fopen). Espera como entrada:

- `ptr`, que es la dirección (del primer byte) de la memoria desde donde leer los datos,
- `size`, que es el tamaño (en bytes) del tipo de datos a escribir,
- `nmemb`, que es el número de esos tipos para escribir de una vez, y
- `stream`, que es el puntero a un `FILE` devuelto por [fopen](fopen).

Por ejemplo, si se va a escribir un `char` a la vez, `size` sería `sizeof(char)` (es decir, `1`), y `nmemb` sería `1`.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de elementos escritos, que es igual al número de bytes escritos cuando `size` es `1`.

Si ocurre un error o se alcanza el final del archivo, esta función puede devolver un valor menor que `nmemb` o incluso `0`.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *input = fopen("input.txt", "r");
        if (input == NULL)
        {
            return 1;
        }

        FILE *output = fopen("output.txt", "w");
        if (output == NULL)
        {
            fclose(input);
            return 1;
        }

        char c;
        while (fread(&c, sizeof(char), 1, input))
        {
            fwrite(&c, sizeof(char), 1, output);
        }

        fclose(input);
        fclose(output);
    }