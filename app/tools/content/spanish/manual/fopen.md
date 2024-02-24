# [NOMBRE](#nombre)

fopen - abrir un archivo

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    FILE *fopen(const char *nombreArchivo, const char *modo);

# [DESCRIPCIÓN](#descripción)

Esta función abre un archivo, `nombreArchivo`. Los valores admitidos para `modo` incluyen

- `"r"`, si se abre el archivo para leer,
- `"w"`, si se abre el archivo para escribir, y
- `"a"`, si se abre el archivo para agregar contenido.

# [VALOR DEVUELTO](#valor-devuelto)

Esta función devuelve un puntero a un `FILE` que representa el archivo abierto o, en caso de error (por ejemplo, cuando `nombreArchivo` no existe), `NULL`.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *archivo = fopen("cs50.txt", "w");
        if (archivo != NULL)
        {
            fprintf(archivo, "Esto es CS50\n");
            fclose(archivo);
        }
    }