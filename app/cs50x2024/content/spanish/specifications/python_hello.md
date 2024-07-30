# Hola, de nuevo

## Problema a resolver

En un archivo llamado `hello.py` en una carpeta llamada `sentimental-hello`, implementa un programa que le pregunte a un usuario su nombre y luego imprima `hola, fulanito`, donde `fulanito` es el nombre proporcionado, exactamente como lo hiciste en [Conjunto de problemas 1](../../1/). ¡Excepto que tu programa esta vez debe estar escrito en Python!

### Sugerencias

- Recuerda que puedes obtener una cadena de un usuario con `get_string`, que se declara en la biblioteca `cs50`.
- Recuerda que puedes imprimir una cadena con `print`.
- Recuerda que puedes crear cadenas formateadas en Python anteponiendo `f` a una cadena en sí. Por ejemplo, `f"{name}"` sustituirá ("interpolará") el valor de la variable `name` donde hayas escrito `{name}`.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-gqi2voQFzbKlna6WkQR0G2W93" src="https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93.js"></script>

## Cómo probar

Si bien `check50` está disponible para este problema, te recomendamos que primero pruebes tu código por tu cuenta en cada uno de los siguientes casos.

- Ejecuta tu programa como `python hello.py` y espera que aparezca un aviso para ingresar datos. Escribe `David` y presiona Enter. Tu programa debe generar `hola, David`.
- Ejecuta tu programa como `python hello.py` y espera que aparezca un aviso para ingresar datos. Escribe `Inno` y presiona Enter. Tu programa debe generar `hola, Inno`.
- Ejecuta tu programa como `python hello.py` y espera que aparezca un aviso para ingresar datos. Escribe `Kamryn` y presiona Enter. Tu programa debe generar `hola, Kamryn`.

### Corrección

    check50 cs50/problems/2024/x/sentimental/hello

### Estilo

    style50 hello.py

## Cómo enviar

    submit50 cs50/problems/2024/x/sentimental/hello