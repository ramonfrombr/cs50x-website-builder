## Crédito

## Problema a resolver

En un archivo llamado `crédito.py` en una carpeta llamada `sentimental-crédito`, escribe un programa que le pida al usuario un numero de tarjeta de crédito y luego informe (a través de `print`) si es un número válido de American Express, MasterCard o Visa, exactamente como lo hiciste en [Problema Establecido 1](../../1/). ¡Esta vez, tu programa debe estar escrito en Python!

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QYLr1R1RDLO9QkPF2XFODLkq4" src="https://asciinema.org/a/QYLr1R1RDLO9QkPF2XFODLkq4.js"></script>

## Especificaciones

- Para que podamos automatizar algunas pruebas de tu código, solicitamos que la última línea de salida de tu programa sea `AMEX\n` o `MASTERCARD\n` o `VISA\n` o `INVÁLIDO\n`, nada más ni nada menos.
- Para simplificar, puedes asumir que la entrada del usuario será completamente numérica (es decir, sin guiones, como podría estar impresa en una tarjeta real).
- Es mejor utilizar `get_int` o `get_string` de la librería de CS50 para obtener la entrada de los usuarios, dependiendo de cómo decidas implementar ésta.

## Sugerencias

- Es posible utilizar expresiones regulares para validar la entrada del usuario. Puedes utilizar el módulo [`re`](https://docs.python.org/3/library/re.html) de Python, por ejemplo, para verificar si la entrada del usuario es, de hecho, una secuencia de dígitos de la longitud correcta.

## Cómo probar

Si bien `check50` está disponible para este problema, te recomendamos que primero pruebes tu código por tu cuenta para cada uno de los siguientes elementos:
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `378282246310005` y presiona enter. Tu programa debe mostrar como salida `AMEX`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `371449635398431` y presiona enter. Tu programa debe mostrar como salida `AMEX`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `5555555555554444` y presiona enter. Tu programa debe mostrar como salida `MASTERCARD`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `5105105105105100` y presiona enter. Tu programa debe mostrar como salida `MASTERCARD`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `4111111111111111` y presiona enter. Tu programa debe mostrar como salida `VISA`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `4012888888881881` y presiona enter. Tu programa debe mostrar como salida `VISA`.
- Ejecuta tu programa como `python crédito.py` y espera una indicación de entrada. Escribe `1234567890` y presiona enter. Tu programa debe mostrar como salida `INVÁLIDO`.

### Corrección

    check50 cs50/problems/2024/x/sentimental/crédito

### Estilo

    style50 crédito.py

## Cómo enviar

    submit50 cs50/problems/2024/x/sentimental/crédito