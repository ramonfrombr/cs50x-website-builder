## Mario

![Captura de pantalla de Mario saltando sobre una pirámide](https://cs50.harvard.edu/x/2024/psets/6/mario/less/pyramid.png)

### Problema a resolver

Escribe un programa en un archivo llamado `mario.py` en una carpeta llamada `sentimental-mario-less` que recree una media pirámide usando llaves (`#`) para los bloques, exactamente como lo hiciste en el [Conjunto de problemas 1](../../../1/). ¡Esta vez, tu programa debe estar escrito en Python!

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-sUSilCTveD7JTV2lOZ7eIqKbo" src="https://asciinema.org/a/sUSilCTveD7JTV2lOZ7eIqKbo.js"></script>

## Especificaciones

- Para hacerlo más interesante, primero solicita al usuario con `get_int` la altura de la media pirámide, un número entero positivo entre `1` y `8`, inclusive.
- Si el usuario no proporciona un número entero positivo no mayor que `8`, debes volver a solicitar el número.
- Luego, genera (con ayuda de `print` y uno o más bucles) la media pirámide deseada.
- Ten cuidado de alinear la esquina inferior izquierda de tu media pirámide con el borde izquierdo de tu ventana de terminal.

### Modo de prueba

Aunque puedes usar `check50` para este problema, te recomendamos que primero pruebes tu código por tu cuenta para cada uno de los siguientes casos:

- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `-1` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a pedirle al usuario que escriba otro número.
- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `0` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a pedirle al usuario que escriba otro número.
- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `1` y presiona enter. Tu programa debe generar la siguiente salida. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

        #

- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `2` y presiona enter. Tu programa debe generar la siguiente salida. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

         #
        ##

- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `8` y presiona enter. Tu programa debe generar la siguiente salida. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

               #
              ##
             ###
            ####
           #####
          ######
         #######
        ########

- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `9` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a pedirle al usuario que escriba otro número. Luego, escribe `2` y presiona enter. Tu programa debe generar la siguiente salida. Asegúrate de que la pirámide esté alineada con la esquina inferior izquierda de tu terminal y que no haya espacios adicionales al final de cada línea.

         #
        ##

- Ejecuta tu programa como `python mario.py` y espera que se te pida información. Escribe `foo` y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a pedirle al usuario que escriba otro número.
- Ejecuta tu programa como `python mario.py` y espera que se te pida información. No escribas nada y presiona enter. Tu programa debe rechazar esta entrada como no válida y volver a pedirle al usuario que escriba otro número.

### Corrección

    check50 cs50/problems/2024/x/sentimental/mario/less

### Estilo

    style50 mario.py

### Modo de envío

    submit50 cs50/problems/2024/x/sentimental/mario/less