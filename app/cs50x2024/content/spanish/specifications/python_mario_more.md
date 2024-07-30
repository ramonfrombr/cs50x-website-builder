## Mario

![captura de pantalla de Mario saltando en una pirámide](https://cs50.harvard.edu/x/2024/psets/6/mario/more/pyramids.png)

## Problema a resolver

En un archivo llamado `mario.py` en una carpeta llamada `sentimental-mario-more`, escribe un programa que recree una semi-pirámide usando almohadillas (`#`) como bloques, tal como lo hiciste en [la tarea 1](../../../1/). ¡Esta vez tu programa debería estar escrito en Python!

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-B0CE4bjPGR19PoRKUe5ZF9VoM" src="https://asciinema.org/a/B0CE4bjPGR19PoRKUe5ZF9VoM.js"></script>

## Especificaciones

- Para que sea más interesante, primero pídele altura de la semi-pirámide al usuario con `get_int`, debe ser un entero positivo entre `1` y `8`, inclusive. (La altura de la semi-pirámide en la imagen es `4`, el ancho de la semi-pirámide es `4` y el espacio que separa las pirámides es `2`).
- Si el usuario no provee un entero positivo menor a `8`, debes volver a pedirle lo mismo.
- Luego, genera (con `print` y uno o más bucles) la semi-pirámide deseada.
- Asegúrate de alinear la esquina inferior izquierda de tu pirámide con el borde izquierdo de la ventana de tu terminal, y asegura que haya dos espacios entre las dos pirámides, y que no haya espacios adicionales después del último grupo de almohadillas en cada fila.

## Cómo probar

Si bien `check50` está disponible para este problema, te recomendamos probar primero tu código por cuenta propia siguiendo los siguientes pasos.

- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `-1` y presiona enter. Tu programa debería rechazar esta entrada como no válida, pidiéndole al usuario ingresar otro número.
- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `0` y presiona enter. Tu programa debería rechazar esta entrada como no válida, pidiéndole al usuario ingresar otro número.
- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `1` y presiona enter. Tu programa debería generar el siguiente resultado. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de la terminal y que no haya espacios adicionales al final de cada línea.

        #  #

- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `2` y presiona enter. Tu programa debería generar el siguiente resultado. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de la terminal y que no haya espacios adicionales al final de cada línea.

         #  #
        ##  ##

- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `8` y presiona enter. Tu programa debería generar el siguiente resultado. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de la terminal y que no haya espacios adicionales al final de cada línea.

               #  #
              ##  ##
             ###  ###
            ####  ####
           #####  #####
          ######  ######
         #######  #######
        ########  ########

- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `9` y presiona enter. Tu programa debería rechazar esta entrada como invalida, pidiéndole al usuario que ingrese otro número. Luego, escribe `2` y presiona enter. Tu programa debería generar el siguiente resultado. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de la terminal y que no haya espacios adicionales al final de cada línea.

         #  #
        ##  ##

- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. Escribe `foo` y presiona enter. Tu programa debería rechazar esta entrada como invalida, pidiéndole al usuario que ingrese otro número.
- Ejecuta tu programa con `python mario.py` y espera la solicitud de ingreso. No escribas nada y presiona enter. Tu programa debería rechazar esta entrada como invalida, pidiéndole al usuario que ingrese otro número.

### Corrección

    check50 cs50/problems/2024/x/sentimental/mario/more

### Estilo

    style50 mario.py

## Cómo enviar

    submit50 cs50/problems/2024/x/sentimental/mario/more