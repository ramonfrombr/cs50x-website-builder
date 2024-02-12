

# Expresiones Regulares

No es raro decir "um" en inglés cuando se intenta, digamos, pensar en una palabra. Sin embargo, cuanto más se hace, más notorio tiende a ser.

En un archivo llamado `um.py`, implementa una función llamada `count` que espera recibir como entrada una línea de texto como una cadena (`str`) y devuelve, como entero (`int`), el número de veces que aparece "um" en ese texto, sin tener en cuenta las mayúsculas y minúsculas, como una palabra única, no como una subcadena de otra palabra. Por ejemplo, dado un texto como `hello, um, world`, la función debe devolver `1`. Sin embargo, dado un texto como `yummy`, la función debe devolver `0`.

Estructura tu archivo `um.py` de la siguiente manera, en la cual puedes modificar `main` e implementar otras funciones según consideres necesario, pero no puedes importar ninguna otra librería. Puedes usar `re` y/o `sys` si lo deseas, pero no es obligatorio.

```python
import re
import sys


def main():
    print(count(input("Texto: ")))


def count(s):
    ...


...


if __name__ == "__main__":
    main()
```

Antes o después de implementar la función `count` en `um.py`, adicionalmente implementa, en un archivo llamado `test_um.py`, **tres o más** funciones que prueben exhaustivamente tu implementación de `count`, cada una de ellas cuyos nombres deben comenzar con `test_`, de manera que puedas ejecutar tus pruebas con:

```python
pytest test_um.py
```

Sugerencias:

- Recuerda que el módulo `re` viene con bastantes funciones, según [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html), incluyendo `findall`.
- Recuerda que las expresiones regulares admiten varios caracteres especiales, según [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).
- Debido a que las barras invertidas en las expresiones regulares podrían confundirse con secuencias de escape (como `\n`), es mejor usar [la notación de cadena sin formato de Python para los patrones de expresiones regulares](https://docs.python.org/3/library/re.html#module-re). Al igual que las cadenas de formato, las cadenas sin formato se anteponen con una `r`. Por ejemplo, en lugar de `"harvard\.edu"`, usa `r"harvard\.edu"`.
- Ten en cuenta que `\b` está "definido como el límite entre un carácter `\w` y un carácter `\W` (o viceversa), o entre `\w` al principio/final de la cadena", según [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).
- Puedes encontrar útil utilizar [regex101.com](https://regex101.com/) o [regexr.com](https://regexr.com/) para probar expresiones regulares (y visualizar coincidencias).
- Consulta [thefreedictionary.com/words-containing-um](https://www.thefreedictionary.com/words-containing-um) para encontrar algunas palabras que contengan "um".

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí mismo. Deberías ver que la línea de comandos de tu terminal se asemeja a la siguiente:

```
$
```

A continuación, ejecuta

```
mkdir um
```

para crear una carpeta llamada `um` en tu espacio de código.

Luego ejecuta

```
cd um
```

para cambiar a ese directorio. Ahora deberías ver la línea de comandos de tu terminal como `um/ $`. Ahora puedes ejecutar

```
code um.py
```

para crear un archivo llamado `um.py` donde escribirás tu programa. Asegúrate también de ejecutar

```
code test_um.py
```

para crear un archivo llamado `test_um.py` donde, digamos, escribirás pruebas para tu programa.

## Cómo Probar

#### Cómo Probar `um.py`

Aquí se explica cómo probar `um.py` manualmente:

- Ejecuta tu programa con `python um.py`. Asegúrate de que tu programa solicite una entrada. Escribe `um`, seguido de Enter. Tu función `count` debería devolver `1`.
- Ejecuta tu programa con `python um.py`. Escribe `um?`, seguido de Enter. Tu función `count` debería devolver `1`.
- Ejecuta tu programa con `python um.py`. Escribe `Um, thanks for the album.`, seguido de Enter. Tu función `count` debería devolver `1`.
- Ejecuta tu programa con `python um.py`. Escribe `Um, thanks, um...`, seguido de Enter. Tu función `count` debería devolver `2`.

#### Cómo Probar `test_um.py`

Para probar tus pruebas, ejecuta `pytest test_um.py`. Intenta utilizar versiones correctas e incorrectas de `um.py` para determinar qué tan bien detectan errores tus pruebas:

- Asegúrate de tener una versión correcta de `um.py`. Ejecuta tus pruebas ejecutando `pytest test_um.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la función `count` en la versión correcta de `um.py`. Podría ser que `count` cuente erróneamente cualquier "um" que sea parte de una palabra. Ejecuta tus pruebas ejecutando `pytest test_um.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.
- Modifica nuevamente la función `count` en la versión correcta de `um.py`. Podría ser que `count` cuente erróneamente solo un "um" que esté rodeado por espacios a ambos lados. Ejecuta tus pruebas ejecutando `pytest test_um.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

Puedes ejecutar lo siguiente para revisar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

```
check50 cs50/problems/2022/python/um
```

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, la salida que esperaba y la salida que tu programa realmente dio.

## Cómo Enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

```
submit50 cs50/problems/2022/python/um
```