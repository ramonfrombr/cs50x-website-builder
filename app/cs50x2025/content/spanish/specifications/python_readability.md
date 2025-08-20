# Legibilidad

## Problema a resolver

Escribe, en un archivo llamado `readability.py` en una carpeta llamada `sentimental-readability`, un programa que primero le pida al usuario que escriba algún texto y luego muestre el nivel educativo para el texto, de acuerdo con la fórmula de Coleman-Liau, exactamente como lo hiciste en [Conjunto de problemas 2](../../2/), excepto que esta vez tu programa debe estar escrito en Python.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-WnE6pZNnDkDm8NtuxrTqY1Nu4" src="https://asciinema.org/a/WnE6pZNnDkDm8NtuxrTqY1Nu4.js"></script>

## Especificaciones

- Recuerda que el índice de Coleman-Liau se calcula como `0.0588 * L - 0.296 * S - 15.8`, donde `L` es el número promedio de letras por cada 100 palabras en el texto y `S` es el número promedio de oraciones por cada 100 palabras en el texto.
- Usa `get_string` de la biblioteca CS50 para obtener la entrada del usuario y `print` para mostrar tu respuesta.
- Tu programa debe contar el número de letras, palabras y oraciones en el texto. Puedes asumir que una letra es cualquier carácter en minúsculas de `a` a `z` o cualquier carácter en mayúsculas de `A` a `Z`, cualquier secuencia de caracteres separada por espacios debe contar como una palabra y que cualquier aparición de un punto, un signo de exclamación o un signo de interrogación indican el final de una oración.
- Tu programa debe imprimir como resultado `"Grado X"` donde `X` es el nivel educativo calculado mediante la fórmula de Coleman-Liau, redondeado al entero más cercano.
- Si el número del índice resultante es 16 o superior (equivalente a un nivel educativo de licenciatura avanzada o superior), tu programa debe mostrar `"Grado 16+"` en lugar de dar el número exacto del índice. Si el número del índice es menor que 1, tu programa debe mostrar `"Antes del Grado 1"`.

## Cómo probar

Mientras que `check50` está disponible para este problema, te recomendamos que primero pruebes tu código por tu cuenta para cada uno de los siguientes.

- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `One fish. Two fish. Red fish. Blue fish.` y presiona enter. Tu programa debe mostrar `Before Grade 1`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` y presiona enter. Tu programa debe mostrar `Grade 2`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Congratulations! Today is your day. You're off to Great Places! You're off and away!` y presiona enter. Tu programa debe mostrar `Grade 3`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` y presiona enter. Tu programa debe mostrar `Grade 5`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` y presiona enter. Tu programa debe mostrar `Grade 7`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` y presiona enter. Tu programa debe mostrar `Grade 8`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` y presiona enter. Tu programa debe mostrar `Grade 8`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` y presiona enter. Tu programa debe mostrar `Grade 9`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` y presiona enter. Tu programa debe mostrar `Grade 10`.
- Ejecuta tu programa como `python readability.py` y espera una solicitud de entrada. Escribe `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` y presiona enter. Tu programa debe mostrar `Grade 16+`.

### Corrección

    check50 cs50/problems/2024/x/sentimental/readability

### Estilo

    style50 readability.py

## Cómo enviar

    submit50 cs50/problems/2024/x/sentimental/readability