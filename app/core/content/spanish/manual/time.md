# [NOMBRE](#nombre)

time - obtener tiempo en segundos

# [SINOPSIS](#sinopsis)

## Archivo de encabezado

    #include <time.h>

## Prototipo

    long time(NULL);

Piensa en esta función como devolviendo un `long` como salida y tomando solo `NULL` como entrada.

# [DESCRIPCIÓN](#descripción)

Esta función obtiene la fecha y hora actual en segundos desde el 1 de enero de 1970, 00:00:00 UTC, también conocido como el Época.

# [VALOR DE RETORNO](#valor-de-retorno)

Esta función devuelve el número de segundos desde el 1 de enero de 1970, 00:00:00 UTC.

# [EJEMPLO](#ejemplo)

    #include <stdio.h>
    #include <time.h>

    int main(void)
    {
        printf("La hora actual es %li.\n", time(NULL));
    }