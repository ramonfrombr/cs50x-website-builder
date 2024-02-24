# [NOMBRE](#nombre)

printf - imprime en la pantalla

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    int printf(cadena formato, ...);

Tenga en cuenta que `...` representa cero o más argumentos adicionales.

# [DESCRIPCIÓN](#descripción)

Esta función imprime una "cadena formateada" en la pantalla. Espera como entrada una "cadena de formato" que especifica qué imprimir y cero o más argumentos posteriores. La cadena de formato puede contener opcionalmente "especificaciones de conversión", marcadores de posición que comienzan con `%` que especifican cómo formatear los argumentos posteriores de la función, si los hay. Por ejemplo, si `c` es un `char`, esta función puede imprimirlo de la siguiente manera usando `%c`:

    printf("%c\n", c);

Alternativamente, esta función también podría formatear ese mismo valor como un `int` usando `%i`, como en una tabla ASCII:

    printf("%c %i\n", c, c);

Y esta función también puede imprimir cadenas sin ninguna especificación de conversión:

    printf("hola, mundo\n");

Entre las especificaciones de conversión admitidas por esta función se encuentran:

| Especificación de conversión | Tipo       |
| ---------------------------- | ---------- |
| `%c`                         | `char`     |
| `%f`                         | `double`   |
| `%f`                         | `float`    |
| `%i`                         | `int`      |
| `%li`                        | `long`     |
| `%s`                         | `string`   |

Para imprimir un signo de porcentaje real, use `%%`.

Para especificar la "precisión" de un `float` o un `double`, `%f` puede contener opcionalmente un `.` después del `%` seguido de un número de decimales. Por ejemplo, esta función podría formatear el valor de un tercio con una decimal utilizando `%.1f`:

    printf("%.1f\n", 1.0 / 3.0);

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de caracteres impresos.

# [EJEMPLOS](#ejemplos)

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        string s = "This is CS50";
        printf("%s\n", s);

        int i = 50;
        printf("This is CS%i\n", i);

        float f = 50.0;
        printf("This is CS%.0f\n", f);
    }