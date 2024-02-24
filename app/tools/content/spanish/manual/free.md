# [NOMBRE](#name)

free - libera la memoria asignada dinámicamente

# [SINOPSIS](#synopsis)

## Archivo de encabezado

```c
#include <stdlib.h>
```

## Prototipo

```c
void free(void *ptr);
```

Piense en `void *` como el significado de la dirección de cualquier tipo de valor en la memoria.

# [DESCRIPCIÓN](#description)

Esta función libera la memoria que ha sido asignada dinámicamente con `malloc`. Espera como entrada el puntero que fue retornado por [malloc](malloc).

# [VALOR DE RETORNO](#return-value)

Esta función no retorna ningún valor.

# [EJEMPLO](#example)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = "hello, world\n";
    char *t = malloc(strlen(s) + 1);
    if (t != NULL)
    {
        strcpy(t, s);
        printf("%s\n", t);
        free(t);
    }
}
```