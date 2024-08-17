# [NOMBRE](#nombre)

fscanf - obtener entrada de un archivo

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    int fscanf(FILE *stream, const char *formato, ...);

Tenga en cuenta que `...` representa cero o más argumentos adicionales.

# [DESCRIPCIÓN](#descripción)

Esta función "escanea" un archivo en busca de valores de tipos específicos. Espera como entrada el puntero a un `FILE` que fue devuelto por [fopen](fopen), una "cadena de formato" que especifica qué esperar y cero o más argumentos posteriores, cada uno de los cuales debe ser una ubicación en la memoria. La cadena de formato debe contener típicamente "especificaciones de conversión", marcadores de posición que comienzan con `%` y que especifican qué tipos de valores esperar. Los argumentos siguientes serán asignados a esos valores. Por ejemplo, si `n` es un `int`, esta función puede obtener un `int` de un usuario usando `%i`:

    scanf("%i", &n);

Entre las especificaciones de conversión admitidas por esta función se encuentran:

| Especificación de conversión | Tipo     |
| ---------------------------- | -------- |
| `%c`                         | `char`   |
| `%f`                         | `double` |
| `%f`                         | `float`  |
| `%i`                         | `int`    |
| `%li`                        | `long`   |

Para obtener una sola palabra (es decir, una secuencia de caracteres sin espacios en blanco), use `%s`. Pero solo es seguro usar esta función para obtener una palabra de un archivo usando `%s` si esa palabra tiene una longitud máxima determinada. Por ejemplo, si `file` es un puntero a un `FILE` que fue devuelto por [fopen](fopen) y `buffer` es un arreglo de 3 bytes, esta función podría usarse para obtener `"hi"`, incluyendo su `'\0'`, pero no `"hi!"`, de la siguiente manera:

    fscanf(file, "%s", buffer);

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de argumentos a los que se les asignaron valores o `EOF`, una constante definida en `stdio.h`, si se ha alcanzado el final del archivo.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("hi.txt", "r");
        if (file != NULL)
        {
            char buffer[3];
            fscanf(file, "%s", buffer);
            fclose(file);
            printf("%s\n", buffer);
        }
    }