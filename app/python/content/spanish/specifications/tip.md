

# Calculadora de Propinas

> Y ahora, mi calculadora de propinas mágica.
>
> - Morty Seinfeld

En los Estados Unidos, es costumbre dejar propina a tu camarero después de comer en un restaurante, generalmente una cantidad equivalente al 15% o más del costo de tu comida. ¡No te preocupes, sin embargo, hemos escrito una calculadora de propinas para ti, a continuación!

    def main():
        dollars = dollars_to_float(input("¿Cuánto fue la comida? "))
        percent = percent_to_float(input("¿Qué porcentaje te gustaría dejar como propina? "))
        tip = dollars * percent
        print(f"Dejar ${tip:.2f}")


    def dollars_to_float(d):
        # TODO


    def percent_to_float(p):
        # TODO


    main()

Bueno, hemos escrito _casi toda_ la calculadora de propinas para ti. Desafortunadamente, no tuvimos tiempo de implementar dos funciones:

- `dollars_to_float`, que debería aceptar una `str` como entrada (formateada como `$##.##`, donde cada `#` es un dígito decimal), eliminar el símbolo de `$` y devolver la cantidad como un `float`. Por ejemplo, dado `$50.00` como entrada, debería devolver `50.0`.
- `percent_to_float`, que debería aceptar una `str` como entrada (formateada como `##%`, donde cada `#` es un dígito decimal), eliminar el símbolo de `%` y devolver el porcentaje como un `float`. Por ejemplo, dado `15%` como entrada, debería devolver `0.15`.

Suponemos que el usuario ingresará los valores en los formatos esperados.

Pistas

- Recuerda que `input` devuelve una `str`, según [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recuerda que `float` puede convertir una `str` en un `float`, según [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float).
- Recuerda que una `str` viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demo

## Antes de Empezar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu terminal se parece al siguiente:

    $

Luego ejecuta

    mkdir tip

para crear una carpeta llamada `tip` en tu espacio de trabajo.

A continuación, ejecuta

    cd tip

para cambiar de directorio a esa carpeta. Ahora deberías ver el prompt de tu terminal como `tip/ $`. Ahora puedes ejecutar

    code tip.py

para crear un archivo llamado `tip.py`. Copia y pega el código anterior en un archivo y completa las implementaciones de `dollars_to_float` y `percent_to_float`, reemplazando cada `TODO` con una o más líneas de tu propio código.

## Cómo Probar

Así es cómo probar tu código manualmente:

- Ejecuta tu programa con `python tip.py`. Escribe `$50.00` y presiona Enter. Luego, escribe `15%` y presiona Enter. Tu programa debería imprimir:

      Dejar $7.50

- Ejecuta tu programa con `python tip.py`. Escribe `$100.00` y presiona Enter. Luego, escribe `18%` y presiona Enter. Tu programa debería imprimir:

      Dejar $18.00

- Ejecuta tu programa con `python tip.py`. Escribe `$15.00` y presiona Enter. Luego, escribe `25%` y presiona Enter. Tu programa debería imprimir:

      Dejar $3.75

Puedes ejecutar el siguiente comando para comprobar tu código usando `check50`, un programa que CS50 usará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/tip

¡Las caritas verdes significan que tu programa ha pasado la prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` proporcionó a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo Enviar

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/tip