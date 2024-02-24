

# Hora de las comidas

Supongamos que estás en un país donde es costumbre desayunar entre las 7:00 y las 8:00, almorzar entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00. ¿No sería bueno tener un programa que te diga qué comer y cuándo?

En `meal.py`, implementa un programa que solicite al usuario una hora y muestre si es `hora de desayunar`, `hora de almorzar` o `hora de cenar`. Si no es hora de ninguna comida, no muestres nada en absoluto. Supón que la entrada del usuario estará formateada en formato de 24 horas como `#:##` o `##:##`. Y supón que el rango de tiempo para cada comida es inclusivo. Por ejemplo, ya sea que sean las 7:00, las 7:01, las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

Estructura tu programa de la siguiente manera, donde `convert` es una función (que puede ser llamada por `main`) que convierte `time`, una cadena en formato de 24 horas, al número correspondiente de horas como un número decimal. Por ejemplo, dado un `time` como `"7:30"` (es decir, 7 horas y 30 minutos), `convert` debería devolver `7.5` (es decir, 7.5 horas).

    def main():
        ...


    def convert(time):
        ...


    if __name__ == "__main__":
        main()

Sugerencias:

- Recuerda que una cadena (str) viene con varios métodos, según [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluyendo `split`, que separa una cadena en una secuencia de valores, los cuales pueden asignarse a variables de una vez. Por ejemplo, si `time` es una cadena como `"7:30"`, entonces

      hours, minutes = time.split(":")

  asignará `"7"` a `hours` y `"30"` a `minutes`.

- Ten en cuenta que hay 60 minutos en una hora.

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` solo. Deberías ver que el indicador de tu ventana de terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    mkdir meal

para crear una carpeta llamada `meal` en tu espacio de código.

Luego, ejecuta

    cd meal

para cambiar al directorio de esa carpeta. Ahora deberías ver tu indicador de terminal como `meal/ $`. Ahora puedes ejecutar

    code meal.py

para crear un archivo llamado `meal.py` donde escribirás tu programa.

## Desafío

Si estás interesado en un desafío, puedes agregar opcionalmente soporte para horarios de 12 horas, permitiendo al usuario ingresar horarios en los siguientes formatos:

- `#:## a.m.` y `##:## a.m.`
- `#:## p.m.` y `##:## p.m.`

## Cómo probar el programa

Aquí tienes cómo probar tu código manualmente:

- Ejecuta tu programa con `python meal.py`. Escribe `7:00` y presiona Enter. Tu programa debería mostrar:

      hora de desayunar

- Ejecuta tu programa con `python meal.py`. Escribe `7:30` y presiona Enter. Tu programa debería mostrar:

      hora de desayunar

- Ejecuta tu programa con `python meal.py`. Escribe `12:42` y presiona Enter. Tu programa debería mostrar:

      hora de almorzar

- Ejecuta tu programa con `python meal.py`. Escribe `18:32` y presiona Enter. Tu programa debería mostrar:

      hora de cenar

- Ejecuta tu programa con `python meal.py`. Escribe `11:11` y presiona Enter. Tu programa no debería mostrar nada.

Puedes ejecutar el siguiente comando para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/meal

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa mostró algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` pasó a tu programa, la salida esperada y la salida que tu programa realmente dio.

Si no estás aprobando las pruebas pero estás seguro de que tu programa se comporta correctamente, asegúrate de no haber eliminado la línea

    if __name__ == "__main__":
        main()

de la estructura del código que te dieron. Eso permite que `check50` pruebe tu función `convert` por separado. Aprenderás más sobre esto en las próximas semanas.

## Cómo enviar tu trabajo

En tu terminal, ejecuta el siguiente comando para enviar tu trabajo.

    submit50 cs50/problems/2022/python/meal