# [NOMBRE](#nombre)

sprintf - imprimir en una cadena

# [SINOPSIS](#sinopsis)

## Archivo de cabecera

    #include <stdio.h>

## Prototipo

    int sprintf(char *str, const char *format, ...);

Se debe tener en cuenta que `...` representa cero o más argumentos adicionales.

# [DESCRIPCIÓN](#descripción)

Esta función imprime una "cadena formateada" en una ubicación de memoria. Espera como entrada la dirección de un búfer (que debe ser lo suficientemente grande como para contener la cadena, incluyendo su `\0`), una "cadena de formato" que especifica qué imprimir, y cero o más argumentos posteriores. La cadena de formato puede contener opcionalmente "conversiones de formato", marcadores de posición que comienzan con `%` y que especifican cómo formatear los argumentos siguientes de la función, si los hay. Por ejemplo, si `buffer` es una matriz de (al menos) 13 bytes e `i` es `50`, esta función podría formatear una cadena de la siguiente manera:

    sprintf(buffer, "hola, %s\n", i);

Entre las conversiones de formato admitidas por esta función se encuentran:

| Conversión de formato | Tipo     |
| --------------------- | -------- |
| `%c`                  | `char`   |
| `%f`                  | `double` |
| `%f`                  | `float`  |
| `%i`                  | `int`    |
| `%li`                 | `long`   |
| `%s`                  | `char *` |

Para imprimir el signo de porcentaje real, use `%%`.

Para especificar la "precisión" de un `float` o un `double`, `%f` puede contener opcionalmente un `.` después del `%` seguido de un número de decimales. Por ejemplo, esta función podría formatear el valor de un tercio con un decimal usando `%.1f`, suponiendo que `buffer` es una matriz de tamaño 4 (al menos):

    sprintf(buffer, "%.1f\n", 1.0 / 3.0);

# [VALOR DEVUELTO](#valor-devuelto)

Esta función devuelve el número de caracteres impresos.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        char buffer[13];

        int i = 50;
        sprintf(buffer, "Esto es CS%i", i);
        printf("%s\n", buffer);

        float f = 50.0;
        sprintf(buffer, "Esto es CS%.0f", f);
        printf("%s\n", buffer);
    }