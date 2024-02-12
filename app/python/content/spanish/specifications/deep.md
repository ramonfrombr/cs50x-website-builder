

# Pensamiento Profundo

> "Está bien," dijo la computadora y volvió al silencio. Los dos hombres se impacientaron. La tensión era insoportable.  
> "Realmente no te va a gustar," observó Pensamiento Profundo.  
> "¡Dinos!"  
> "Está bien," dijo Pensamiento Profundo. "La respuesta a la Gran Pregunta..."  
> "¡Sí...!"  
> "De la Vida, el Universo y Todo..." dijo Pensamiento Profundo.  
> "¡Sí...!"  
> "Es..." dijo Pensamiento Profundo, y se detuvo.  
> "¡Sí...!"  
> "Es..."  
> "¡¡Sí...!!!...?"  
> "Cuarenta y dos," dijo Pensamiento Profundo, con infinita majestuosidad y calma."
>
> - _La Guía del Autoestopista Galáctico_, Douglas Adams

En `deep.py`, implementa un programa que solicite al usuario la respuesta a la Gran Pregunta de la Vida, el Universo y Todo, y muestre `Sí` si el usuario ingresa `42` o (sin distinguir mayúsculas y minúsculas) `cuarenta y dos` o `cuarenta dos`. De lo contrario, mostrar `No`.

Pistas

- No es necesario convertir la entrada del usuario a un `int` si se verifica la igualdad con `"42"`, una `str`, en lugar de `42`, un `int`!
- Está bien que la salida de tu programa o la entrada del usuario se divida en varias líneas.

## Demo

## Antes de comenzar

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías ver que el prompt de tu ventana de terminal se parece a lo siguiente:

    $

A continuación, ejecuta

    mkdir deep

para crear una carpeta llamada `deep` en tu codespace.

Luego ejecuta

    cd deep

para cambiar de directorio a esa carpeta. Deberías ver ahora tu prompt de terminal como `deep/ $`. Ahora puedes ejecutar

    code deep.py

para crear un archivo llamado `deep.py` en el que escribirás tu programa.

## Cómo probar

Aquí te mostramos cómo probar tu código manualmente:

- Ejecuta tu programa con `python deep.py`. Escribe `42` y presiona Enter. Tu programa debería mostrar:

      Sí

- Ejecuta tu programa con `python deep.py`. Escribe `Cuarenta Dos` y presiona Enter. Tu programa debería mostrar:

      Sí

- Ejecuta tu programa con `python deep.py`. Escribe `cuarenta-dos` y presiona Enter. Tu programa debería mostrar:

      Sí

- Ejecuta tu programa con `python deep.py`. Escribe `50` y presiona Enter. Tu programa debería mostrar:

      No

Asegúrate de variar las mayúsculas y minúsculas de tu entrada y "accidentalmente" agregar espacios a cada lado de tu entrada antes de presionar Enter. Tu programa debería comportarse como se espera, sin importar mayúsculas y minúsculas ni espacios.

Puedes ejecutar lo siguiente para verificar tu código usando `check50`, un programa que CS50 utilizará para probar tu código cuando lo envíes. ¡Pero asegúrate de probarlo tú mismo también!

    check50 cs50/problems/2022/python/deep

¡Las caritas verdes significan que tu programa ha pasado una prueba! Las caritas rojas indicarán que tu programa produjo algo inesperado. Visita la URL que `check50` muestra para ver la entrada que `check50` le entregó a tu programa, qué salida esperaba y qué salida dio tu programa.

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2022/python/deep