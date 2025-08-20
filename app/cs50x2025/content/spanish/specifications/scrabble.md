# Scrabble

![Tablero de Scrabble](https://cs50.harvard.edu/x/2024/psets/2/scrabble/scrabble.png)

## Problema a resolver

En el juego de [Scrabble](https://scrabble.hasbro.com/en-us/rules), los jugadores crean palabras para obtener puntos, y el número de puntos es la suma de los valores de puntos de cada letra en la palabra.

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 3   | 3   | 2   | 1   | 4   | 2   | 4   | 1   | 8   | 5   | 1   | 3   | 1   | 1   | 3   | 10  | 1   | 1   | 1   | 1   | 4   | 4   | 8   | 4   | 10  |

Por ejemplo, si quisiéramos puntuar la palabra “CODE”, notaríamos que la ‘C’ vale 3 puntos, la ‘O’ vale 1 punto, la ‘D’ vale 2 puntos y la ‘E’ vale 1 punto. Sumando, obtenemos que “CODE” vale 7 puntos.

En un archivo llamado `scrabble.c` en una carpeta llamada `scrabble`, implementa un programa en C que determine el ganador de un juego corto similar al Scrabble. Tu programa debe solicitar la entrada dos veces: una para el “Jugador 1” para que ingrese su palabra y otra para que el “Jugador 2” ingrese su palabra. Luego, según qué jugador obtenga más puntos, tu programa debe imprimir “¡Jugador 1 gana!”, “¡Jugador 2 gana!” o “¡Empate!” (en caso de que ambos jugadores obtengan la misma cantidad de puntos).

## Demostración

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-74B4kq3ftleKe6AdN0NxFV8CN" src="https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN.js"></script>

## Recomendaciones

### Escribe código que sepas que se compilará

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Ten en cuenta que has incluido algunos archivos de encabezado que te darán acceso a funciones que pueden ayudarte a resolver este problema.

### Escribe pseudocódigo antes de escribir más código

Si no estás seguro de cómo resolver el problema en sí, divídelo en problemas más pequeños que probablemente puedas resolver primero. Por ejemplo, este problema es en realidad solo un puñado de problemas:

1. Solicitar al usuario dos palabras
2. Calcular la puntuación de cada palabra
3. Imprimir al ganador

Escribamos un pseudocódigo como comentarios para recordarte que hagas precisamente eso:

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicitar al usuario dos palabras

        // Calcular la puntuación de cada palabra

        // Imprimir al ganador
    }

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Algunos problemas en conjuntos de problemas, como este, pueden contener spoilers (como el siguiente) que finalmente te guían a través de toda la solución. Si bien tienes permitido usar este código, ¡te recomendamos encarecidamente que primero pruebes las cosas por ti mismo! Los demás problemas del conjunto de problemas no tendrán este tipo de tutorial y, por lo general, el problema que contiene el “spoiler completo” es una versión de calentamiento del problema más grande que luego deberás abordar.</p></div>

### Convierte el pseudocódigo a código

Primero, considera cómo podrías solicitar al usuario dos palabras. Recuerda que `get_string`, una función de la biblioteca CS50, puede solicitar al usuario una string.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicitar al usuario dos palabras
        string palabra1 = get_string("Jugador 1: ");
        string palabra2 = get_string("Jugador 2: ");

        // Calcular la puntuación de cada palabra

        // Imprimir al ganador
    }

A continuación, considera cómo calcular la puntuación de cada palabra. Como se aplica el mismo algoritmo de puntuación a ambas palabras, tienes una buena oportunidad de _abstracción_. Aquí definiremos una función llamada `compute_score` que toma una string, llamada `word`, como entrada y luego devuelve la puntuación de `word` como `int`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int compute_score(string word);

    int main(void)
    {
        // Solicitar al usuario dos palabras
        string palabra1 = get_string("Jugador 1: ");
        string palabra2 = get_string("Jugador 2: ");

        // Calcular la puntuación de cada palabra
        int punctuation1 = compute_score(palabra1);
        int punctuation2 = compute_score(palabra2);

        // Imprimir al ganador
    }

    int compute_score(string word)
    {
        // Calcular y devolver puntuación para palabra
    }

Ahora pase a implementar `compute_score`. Para calcular la puntuación de una palabra, necesita conocer el valor en puntos de cada letra de la palabra. Puede asociar las letras y sus valores en puntos con un _array_. Imagine un array de 26 `int` llamados `POINTS`, en el que el primer número es el valor en puntos para 'A', el segundo número es el valor en puntos para 'B' y así sucesivamente. Al declarar e inicializar un array de este tipo fuera de cualquier función particular, puede asegurarse de que este array sea accesible para cualquier función, incluido `compute_score`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Puntos asignados a cada letra del alfabeto
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Solicite al usuario dos palabras
        string word1 = get_string("Jugador 1: ");
        string word2 = get_string("Jugador 2: ");

        // Calcule la puntuación de cada palabra
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Imprima el ganador
    }

    int compute_score(string word)
    {
        // Calcule y devuelva la puntuación de la palabra
    }

Para implementar `compute_score`, primero intente encontrar el valor en puntos de una sola letra en `word`.

- Recuerde que para encontrar el carácter en el n-ésimo índice de una cadena, `s`, puede escribir `s[n]`. Por lo tanto, `word[0]`, por ejemplo, le dará el primer carácter de `word`.
- Ahora, recuerde que las computadoras representan caracteres usando [ASCII](http://asciitable.com/), un estándar que representa cada carácter como un número.
- Recuerde también que el índice 0 de `POINTS`, `POINTS[0]`, le da el valor en puntos de 'A'. Piense en cómo podría transformar la representación numérica de 'A' en el índice de su valor en puntos. Ahora, ¿qué pasa con 'a'? Necesitará aplicar diferentes transformaciones a letras mayúsculas y minúsculas, por lo que puede encontrar útiles las funciones [`isupper`](https://manual.cs50.io/3/isupper) y [`islower`](https: //manual.cs50.io/3/islower) para ti.
- Tenga en cuenta que los caracteres que _no_ son letras deben recibir cero puntos. Por ejemplo, `!` vale 0 puntos.

Si puede calcular correctamente el valor de _un_ carácter en `words`, es probable que pueda usar un bucle para sumar los puntos de los demás caracteres. Una vez que haya probado lo anterior por su cuenta, considere esta sugerencia (¡bastante reveladora!) a continuación.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Puntos asignados a cada letra del alfabeto
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Solicite al usuario dos palabras
        string word1 = get_string("Jugador 1: ");
        string word2 = get_string("Jugador 2: ");

        // Calcule la puntuación de cada palabra
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Imprima el ganador
    }

    int compute_score(string word)
    {
        // Mantenga un registro de la puntuación
        int score = 0;

        // Calcule la puntuación para cada carácter
        for (int i = 0, len = strlen(word); i < len; i++)
        {
            if (isupper(word[i]))
            {
                score += POINTS[word[i] - 'A'];
            }
            else if (islower(word[i]))
            {
                score += POINTS[word[i] - 'a'];
            }
        }

        return score;
    }

Finalmente, termina el último paso de tu seudo código: imprime al ganador. Recuerda que una declaración `if` puede usarse para verificar si una condición es verdadera, y que el uso adicional de `else if` o `else` puede verificar otras condiciones (exclusivas).

    if (/* El Jugador 1 gana */)
    {
        // ...
    }
    else if (/* El Jugador 2 gana */)
    {
        // ...
    }
    else
    {
        // ...
    }

Y una vez que lo hayas intentado, siéntete libre de echar un vistazo a la pista (o, mejor dicho, ¡a la solución completa!) a continuación.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Puntos asignados a cada letra del alfabeto
    int PUNTOS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int calcula_puntuacion(string palabra);

    int main(void)
    {
        // Solicita al usuario dos palabras
        string palabra1 = get_string("Jugador 1: ");
        string palabra2 = get_string("Jugador 2: ");

        // Calcula la puntuación de cada palabra
        int puntuacion1 = calcula_puntuacion(palabra1);
        int puntuacion2 = calcula_puntuacion(palabra2);

        // Imprime el ganador
        if (puntuacion1 > puntuacion2)
        {
            printf("¡El Jugador 1 gana!\n");
        }
        else if (puntuacion1 < puntuacion2)
        {
            printf("¡El Jugador 2 gana!\n");
        }
        else
        {
            printf("¡Empate!\n");
        }
    }

    int calcula_puntuacion(string palabra)
    {
        // Lleva un registro de la puntuación
        int puntuacion = 0;

        // Calcula la puntuación de cada caracter
        for (int i = 0, longitud = strlen(palabra); i < longitud; i++)
        {
            if (isupper(palabra[i]))
            {
                puntuacion += PUNTOS[palabra[i] - 'A'];
            }
            else if (islower(palabra[i]))
            {
                puntuacion += PUNTOS[palabra[i] - 'a'];
            }
        }

        return puntuacion;
    }

## Cómo probar

Tu programa debe comportarse según los ejemplos a continuación.

    $ ./scrabble
    Jugador 1: Question?
    Jugador 2: Question!
    ¡Empate!


    $ ./scrabble
    Jugador 1: red
    Jugador 2: wheelbarrow
    ¡El Jugador 2 gana!


    $ ./scrabble
    Jugador 1: COMPUTER
    Jugador 2: science
    ¡El Jugador 1 gana!


    $ ./scrabble
    Jugador 1: Scrabble
    Jugador 2: wiNNeR
    ¡El Jugador 1 gana!

### Corrección

En tu terminal, ejecuta lo siguiente para verificar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/scrabble

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 scrabble.c

## Cómo entregar

En tu terminal, ejecuta lo siguiente para entregar tu trabajo.

    submit50 cs50/problems/2024/x/scrabble

