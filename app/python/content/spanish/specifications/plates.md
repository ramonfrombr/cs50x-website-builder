

# Placas personalizadas

![Placa de CS50](plate.png)

En Massachusetts, hogar de la Universidad de Harvard, es posible [solicitar una placa de matrícula personalizada](https://www.mass.gov/how-to/request-a-vanity-license-plate) para tu auto, con tu elección de letras y números en lugar de los aleatorios. Sin embargo, entre los requisitos se encuentran:

- "Todas las placas personalizadas deben comenzar con al menos dos letras".
- "... las placas personalizadas pueden contener un máximo de 6 caracteres (letras o números) y un mínimo de 2 caracteres".
- "No se pueden usar números en el medio de una placa; deben ir al final. Por ejemplo, AAA222 sería una placa personalizada aceptable; AAA22A no sería aceptable. El primer número utilizado no puede ser un '0'".
- "No se permiten puntos, espacios ni signos de puntuación".

En `plates.py`, implementa un programa que solicite al usuario una placa personalizada y luego imprima `Válida` si cumple con todos los requisitos o `Inválida` si no lo hace. Asume que todas las letras ingresadas por el usuario estarán en mayúscula. Estructura tu programa según lo siguiente, donde `is_valid` devuelve `Verdadero` si `s` cumple con todos los requisitos y `Falso` si no. Puedes implementar funciones adicionales para que `is_valid` llame (por ejemplo, una función por requisito).

    def main():
        plate = input("Placa: ")
        if is_valid(plate):
            print("Válida")
        else:
            print("Inválida")


    def is_valid(s):
        ...


    main()

Sugerencias

- Recuerda que un `str` tiene varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Al igual que una `list`, un `str` es una "secuencia" (de caracteres), lo que significa que se puede "cortar" en cadenas más cortas con una sintaxis como `s[i:j]`. Por ejemplo, si `s` es `"CS50"`, entonces `s[0:2]` sería `"CS"`.

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` sin agregar nada más. Verás que la ventana de tu terminal se asemeja a lo siguiente:

    $

A continuación, ejecuta

    mkdir plates

para crear una carpeta llamada `plates` en tu área de trabajo.

Luego ejecuta

    cd plates

para cambiar al directorio de esa carpeta. Ahora deberías ver tu indicador de terminal como `plates/ $`. A continuación, puedes ejecutar

    code plates.py

para crear un archivo llamado `plates.py` donde escribirás tu programa.

## Cómo probar

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `python plates.py`. Escribe `CS50` y presiona Enter. Tu programa debería imprimir:

      Válida

- Ejecuta tu programa con `python plates.py`. Escribe `CS05` y presiona Enter. Tu programa debería imprimir:

      Inválida

- Ejecuta tu programa con `python plates.py`. Escribe `CS50P` y presiona Enter. Tu programa debería imprimir:

      Inválida

- Ejecuta tu programa con `python plates.py`. Escribe `PI3.14` y presiona Enter. Tu programa debería imprimir:

      Inválida

- Ejecuta tu programa con `python plates.py`. Escribe `H` y presiona Enter. Tu programa debería imprimir:

      Inválida

- Ejecuta tu programa con `python plates.py`. Escribe `OUTATIME` y presiona Enter. Tu programa debería imprimir:

      Inválida

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/plates

¡Las caritas verdes significan que tu programa ha aprobado una prueba! Las caritas rojas indicarán que tu programa ha producido algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le proporcionó a tu programa, qué salida se esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/plates