# [NOMBRE](#nombre)

fprintf - imprimir en un archivo

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    int fprintf(FILE *stream, const char *format, ...);

Se debe tener en cuenta que `...` representa cero o más argumentos adicionales.

# [DESCRIPCIÓN](#descripción)

Esta función imprime una "cadena de formato" en un archivo. Espera como entrada un puntero a un `FILE` que fue devuelto por [fopen](fopen), una "cadena de formato" que especifica qué imprimir y cero o más argumentos posteriores. La cadena de formato puede contener opcionalmente "especificaciones de conversión", marcadores de posición que comienzan con `%` que especifican cómo formatear los argumentos posteriores de la función, si los hay. Por ejemplo, si `file` es un puntero a un `FILE` y `c` es un `char`, esta función puede imprimir este último en el primero de la siguiente manera usando `%c`:

    fprintf(file, "%c\n", c);

Alternativamente, esta función también podría formatear ese mismo valor como un `int` usando `%i`, como en un gráfico ASCII:

    fprintf(file, "%c %i\n", c, c);

Y esta función también puede imprimir cadenas sin ninguna especificación de conversión:

    fprintf(file, "¡Hola, mundo!\n");

Entre las especificaciones de conversión admitidas por esta función se encuentran:

| Especificación de conversión | Tipo     |
| ---------------------------- | -------- |
| `%c`                         | `char`   |
| `%f`                         | `double` |
| `%f`                         | `float`  |
| `%i`                         | `int`    |
| `%li`                        | `long`   |
| `%s`                         | `char *` |

Para imprimir el signo de porcentaje real, use `%%`.

Para especificar la "precisión" de un `float` o un `double`, `%f` puede contener opcionalmente un `.` después de `%`, seguido de un número de decimales. Por ejemplo, esta función podría formatear el valor de un tercio con un decimal usando `%.1f`:

    fprintf(file, "%.1f\n", 1.0 / 3.0);

# [VALOR DEVUELTO](#valor-devuelto)

Esta función devuelve el número de caracteres impresos.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file == NULL)
        {
            return 0;
        }

        char *s = "Esto es CS50";
        fprintf(file, "%s\n", s);

        int i = 50;
        fprintf(file, "Esto es CS%i\n", i);

        float f = 50.0;
        fprintf(file, "Esto es CS%.0f\n", f);

        fclose(file);
        return 0;
    }