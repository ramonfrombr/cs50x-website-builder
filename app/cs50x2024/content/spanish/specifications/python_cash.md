## Efectivo

## Problema a resolver

En un archivo llamado `cash.py` en una carpeta llamada `sentimental-cash`, escribe un programa que le pida al usuario cuánto cambio se le debe y luego arroje el número mínimo de monedas con las que se puede hacer dicho cambio. Puedes hacer esto exactamente como lo hiciste en [Serie de problemas 1](../../1/), excepto que esta vez tu programa debe escribirse en Python y debes asumir que el usuario ingresará su cambio en dólares (por ejemplo, 0,50 dólares en lugar de 50 centavos).

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-eoFGGVR2gwl2jvyj7sHchxUmW" src="https://asciinema.org/a/eoFGGVR2gwl2jvyj7sHchxUmW.js"></script>

## Especificación

- Usa `get_float` de la biblioteca CS50 para obtener la entrada del usuario e `imprimir` para generar tu respuesta. Asume que las únicas monedas disponibles son cuartos (25¢), monedas de diez centavos (10¢), monedas de cinco centavos (5¢) y centavos (1¢).
 - Te pedimos que uses `get_float` para que puedas manejar dólares y centavos, aunque sin el signo de dólar. En otras palabras, si a algún cliente se le deben $9.75 (como en el caso de que un periódico cueste 25¢ pero el cliente pague con un billete de $10), asume que la entrada de tu programa será `9.75` y no `$9.75` o `975`. Sin embargo, si a algún cliente se le deben $9 exactamente, asume que la entrada de tu programa será `9.00` o solo `9` pero, nuevamente, no `$9` o `900`. Por supuesto, por la naturaleza de los valores de punto flotante, es probable que tu programa también funcione con entradas como `9.0` y `9.000`; no necesitas preocuparte por verificar si la entrada del usuario está "formateada" como debería ser el dinero.
 - Si el usuario no proporciona un valor no negativo, tu programa debe solicitarle nuevamente al usuario una cantidad válida una y otra vez hasta que el usuario la proporcione.
 - Por cierto, para que podamos automatizar algunas pruebas de tu código, pedimos que la última línea de salida de tu programa sea solo el número mínimo de monedas posible: un número entero seguido de un salto de línea.

## Cómo realizar la prueba

Aunque `check50` está disponible para este problema, te recomendamos que primero pruebes tu código por tu cuenta para cada uno de los siguientes casos.

- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `0.41` y presiona enter. Tu programa debe generar `4`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `0.01` y presiona enter. Tu programa debe generar `1`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `0.15` y presiona enter. Tu programa debe generar `2`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `1.60` y presiona enter. Tu programa debe generar `7`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `23` y presiona enter. Tu programa debe generar `92`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `4.2` y presiona enter. Tu programa debe generar `18`.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `-1` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a solicitarle al usuario que escriba otro número.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. Escribe `foo` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a solicitarle al usuario que escriba otro número.
- Ejecuta tu programa como `python cash.py` y espera una solicitud de entrada. No escribas nada y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a solicitarle al usuario que escriba otro número.

### Precisión

    check50 cs50/problems/2024/x/sentimental/cash

### Estilo

    style50 cash.py

## Cómo enviar

    submit50 cs50/problems/2024/x/sentimental/cash