

# Desactualizado

En Estados Unidos, las fechas suelen formatearse en el orden [mes-día-año](https://es.wikipedia.org/wiki/Formato_horario#Estados_Unidos_de_Am%C3%A9rica) (MM/DD/YYYY), también conocido como orden [medio-endiano](https://es.wikipedia.org/wiki/Endian#Medio-endiano), lo cual se considera un mal diseño. Las fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha viene al final en lugar de al principio. Intenta ordenar, por ejemplo, `2/2/1800`, `3/3/1900` y `1/1/2000` cronológicamente en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son ambiguas. Harvard fue [fundada](https://www.harvard.edu/about/history/) el 8 de septiembre de 1636, ¡pero 9/8/1636 también podría interpretarse como el 9 de agosto de 1636!

Afortunadamente, las computadoras tienden a utilizar [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601), un estándar internacional que prescribe que las fechas deben formatearse en el orden año-mes-día (YYYY-MM-DD), independientemente del país, formateando los años con cuatro dígitos, los meses con dos dígitos y los días con dos dígitos, "rellenándolos" con ceros a la izquierda según sea necesario.

En un archivo llamado `outdated.py`, implementa un programa que solicite al usuario una fecha, anno Domini, en el orden mes-día-año, formateado como `9/8/1636` o `8 de septiembre de 1636`, donde el mes en este último podría ser cualquiera de los valores en la `lista` a continuación:

```
[
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre"
]
```

Luego, muestra esa misma fecha en formato `YYYY-MM-DD`. Si la entrada del usuario no es una fecha válida en ninguno de los formatos, solicita al usuario nuevamente. Asume que cada mes tiene como máximo 31 días; no es necesario validar si un mes tiene 28, 29, 30 o 31 días.

Pistas:

- Recuerda que un `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluido `split`.
- Recuerda que un `list` viene con varios métodos, según [docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), entre los cuales se encuentra `index`.
- Ten en cuenta que puedes formatear un `int` con ceros a la izquierda con código como

  ```python
  print(f"{n:02}")
  ```

  donde, si `n` es un solo dígito, se le agrega un `0` como prefijo, según [docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax).

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que la indicación de tu terminal se parece a la siguiente:

```
$
```

Luego, ejecuta

```
mkdir outdated
```

para crear una carpeta llamada `outdated` en tu espacio de códigos.

A continuación, ejecuta

```
cd outdated
```

para cambiar de directorio a esa carpeta. Ahora deberías ver la indicación de tu terminal como `outdated/ $`. Ahora puedes ejecutar

```
code outdated.py
```

para crear un archivo llamado `outdated.py` donde escribirás tu programa.

## Cómo probar

Así es cómo puedes probar tu código manualmente:

- Ejecuta tu programa con `python outdated.py`. Escribe `9/8/1636` y presiona Enter. Tu programa debería mostrar:

  ```
  1636-09-08
  ```

- Ejecuta tu programa con `python outdated.py`. Escribe `8 de septiembre de 1636` y presiona Enter. Tu programa debería mostrar:

  ```
  1636-09-08
  ```

- Ejecuta tu programa con `python outdated.py`. Escribe `23/6/1912` y presiona Enter. Tu programa debería solicitar nuevamente al usuario.
- Ejecuta tu programa con `python outdated.py`. Escribe `80 de diciembre de 1980` y presiona Enter. Tu programa debería solicitar nuevamente al usuario.

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```
check50 cs50/problems/2022/python/outdated
```

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```
submit50 cs50/problems/2022/python/outdated
```