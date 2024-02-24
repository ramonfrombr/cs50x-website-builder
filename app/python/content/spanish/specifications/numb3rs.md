

# NUMB3RS

En la Temporada 5, Episodio 23 de [NUMB3RS](<https://en.wikipedia.org/wiki/Numbers_(TV_series)>), aparece en pantalla una supuesta [dirección IP](https://en.wikipedia.org/wiki/IP_address), `275.3.6.28`, que en realidad no es una dirección [IPv4](https://en.wikipedia.org/wiki/IPv4) (o [IPv6](https://en.wikipedia.org/wiki/IPv6)) válida.

Una dirección IPv4 es un identificador numérico que un dispositivo (o, en la televisión, un hacker) utiliza para comunicarse en Internet, similar a una dirección postal en el mundo real, generalmente formateada en una [notación decimal con puntos](https://en.wikipedia.org/wiki/Dot-decimal_notation) como `#.#.#.#`. Pero cada `#` debe ser un número entre `0` y `255`, inclusive. ¡Sobra decir que `275` no está en ese rango! ¡Si tan solo NUMB3RS hubiera validado la dirección en esa escena!

En un archivo llamado `numb3rs.py`, implementa una función llamada `validate` que espera una dirección IPv4 como entrada en forma de `str`, y luego devuelve `True` o `False`, respectivamente, si esa entrada es una dirección IPv4 válida o no.

Estructura `numb3rs.py` de la siguiente manera, en la cual puedes modificar `main` e implementar otras funciones según consideres necesario, pero no puedes importar ninguna otra biblioteca. Siéntete libre de utilizar `re` o `sys`, aunque no es obligatorio.

    import re
    import sys


    def main():
        print(validate(input("Dirección IPv4: ")))


    def validate(ip):
        ...


    ...


    if __name__ == "__main__":
        main()

Ya sea antes o después de implementar `validate` en `numb3rs.py`, adicionalmente implementa, en un archivo llamado `test_numb3rs.py`, **dos o más** funciones que prueben exhaustivamente tu implementación de `validate`, cuyos nombres deben comenzar con `test_` para que puedas ejecutar tus pruebas con:

    pytest test_numb3rs.py

Pistas

- Recuerda que el módulo `re` viene con muchas funciones, según [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html), incluyendo `search`.
- Recuerda que las expresiones regulares admiten muchos caracteres especiales, según [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).
- Debido a que las barras invertidas en las expresiones regulares podrían confundirse con secuencias de escape (como `\n`), es mejor usar la [notación de cadena cruda de Python para patrones de expresiones regulares](https://docs.python.org/3/library/re.html#module-re), de lo contrario, `pytest` mostrará una advertencia `DeprecationWarning: invalid escape sequence`. Al igual que las cadenas de formato que se prefijan con `f`, las cadenas crudas se prefijan con `r`. Por ejemplo, en lugar de `"harvard\.edu"`, usa `r"harvard\.edu"`.
- Ten en cuenta que `re.search`, si se le pasa un patrón con "grupos de captura" (es decir, paréntesis), devuelve un "objeto de coincidencia", según [docs.python.org/3/library/re.html#match-objects](https://docs.python.org/3/library/re.html#match-objects), donde las coincidencias se numeran a partir de 1, a las que se puede acceder individualmente con `group`, según [docs.python.org/3/library/re.html#re.Match.group](https://docs.python.org/3/library/re.html#re.Match.group), o en conjunto con `groups`, según [docs.python.org/3/library/re.html#re.Match.groups](https://docs.python.org/3/library/re.html#re.Match.groups).

## Demo

## Antes de comenzar

Ingresa a [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que la línea de comandos de tu terminal se ve como la siguiente:

    $

A continuación, ejecuta

    mkdir numb3rs

para crear una carpeta llamada `numb3rs` en tu espacio de códigos.

Luego, ejecuta

    cd numb3rs

para cambiar al directorio de esa carpeta. Ahora deberías ver que la línea de comandos de tu terminal es `numb3rs/ $`. Ahora puedes ejecutar

    code numb3rs.py

para crear un archivo llamado `numb3rs.py` donde escribirás tu programa. Asegúrate también de ejecutar

    code test_numb3rs.py

para crear un archivo llamado `test_numb3rs.py` donde escribirás las pruebas para tu programa.

## Cómo realizar pruebas

#### Cómo probar `numb3rs.py`

Así es cómo puedes probar `numb3rs.py` manualmente:

- Ejecuta tu programa con `python numb3rs.py`. Asegúrate de que el programa te solicite una dirección IPv4. Escribe `127.0.0.1` y presiona Enter. Tu función `validate` debería devolver `True`.
- Ejecuta tu programa con `python numb3rs.py`. Escribe `255.255.255.255` y presiona Enter. Tu función `validate` debería devolver `True`.
- Ejecuta tu programa con `python numb3rs.py`. Escribe `512.512.512.512` y presiona Enter. Tu función `validate` debería devolver `False`.
- Ejecuta tu programa con `python numb3rs.py`. Escribe `1.2.3.1000` y presiona Enter. Tu función `validate` debería devolver `False`.
- Ejecuta tu programa con `python numb3rs.py`. Escribe `cat` y presiona Enter. Tu función `validate` debería devolver `False`.

#### Cómo probar `test_numb3rs.py`

Para probar tus pruebas, ejecuta `pytest test_numb3rs.py`. Intenta usar versiones correctas e incorrectas de `numb3rs.py` para determinar qué tan bien detectan tus pruebas los errores:

- Asegúrate de tener una versión correcta de `numb3rs.py`. Ejecuta tus pruebas ejecutando `pytest test_numb3rs.py`. `pytest` debería mostrar que todas tus pruebas han pasado.
- Modifica la función `validate` en la versión correcta de `numb3rs.py`. Por ejemplo, `validate` podría verificar únicamente si el primer byte de la dirección IPv4 es válido. Ejecuta tus pruebas ejecutando `pytest test_numb3rs.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.
- Modifica nuevamente la versión correcta de `numb3rs.py`. Por ejemplo, `validate` podría devolver erróneamente `True` cuando el usuario ingresa un formato de dirección IPv4 incorrecto. Ejecuta tus pruebas ejecutando `pytest test_numb3rs.py`. `pytest` debería mostrar que al menos una de tus pruebas ha fallado.

¡Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. Pero asegúrate de probarlo tu mismo también!

    check50 cs50/problems/2022/python/numb3rs

¡Las caritas verdes significan que tu programa ha aprobado una prueba! Los rostros tristes rojos indicarán que tu programa ha mostrado algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` pasó a tu programa, cuál era la salida esperada y cuál fue la salida que tu programa realmente dio.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/numb3rs