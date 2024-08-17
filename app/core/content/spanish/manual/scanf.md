# [NOMBRE](#nombre)

scanf - obtener la entrada de un usuario

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <stdio.h>

## Prototipo

    int scanf(const char *format, ...);

Tenga en cuenta que `...` representa cero o más argumentos adicionales.

# [DESCRIPCIÓN](#descripción)

Esta función "escanea" la entrada del teclado de un usuario en busca de valores de tipos especificados. Espera como entrada una "cadena de formato" que especifica qué esperar y cero o más argumentos posteriores, cada uno de los cuales debe ser una ubicación en la memoria. La cadena de formato debe contener típicamente "especificaciones de conversión", marcadores de posición que empiezan con `%` que especifican qué tipos de valores esperar. Los argumentos posteriores se asignarán a esos valores. Por ejemplo, si `n` es un `int`, esta función puede obtener un `int` de un usuario usando `%i`:

    scanf("%i", &n);

Entre las especificaciones de conversión admitidas por esta función se encuentran:

| Especificación de conversión | Tipo     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |

No es seguro utilizar esta función para obtener una cadena de un usuario usando `%s`, ya que la entrada del usuario podría exceder la capacidad del argumento al que se asignaría ese valor.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de argumentos a los que se les asignaron valores o `EOF`, una constante definida en `stdio.h`, en caso de errores.

# [EJEMPLOS](#ejemplos)

    #include <stdio.h>

    int main(void)
    {
        int i;
        printf("Entrada: ");
        scanf("%i", &i);
        printf("Salida: %i\n", i);
    }