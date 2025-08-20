## Legibilidad

![Portada de la telaraña de Charlotte](https://cs50.harvard.edu/x/2024/psets/2/readability/charlottes_web.jpg)

## Problema a resolver

Según [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _La telaraña de Charlotte_ de E.B. White está en un nivel de lectura entre segundo y cuarto grado, y _El dador_ de Lois Lowry está en un nivel de lectura entre octavo y duodécimo grado. ¿Qué significa, entonces, que un libro esté en un nivel de lectura particular?

Bueno, en muchos casos, un experto humano puede leer un libro y tomar una decisión sobre el grado (es decir, año escolar) para el que cree que el libro es más apropiado. ¡Pero un algoritmo también podría resolverlo!

En un archivo llamado `readability.c` en una carpeta llamada `readability`, implementarás un programa que calcula el nivel de grado aproximado necesario para comprender un texto. Tu programa debe imprimir como salida "Grado X" donde "X" es el nivel de grado calculado, redondeado al entero más cercano. Si el nivel de grado es 16 o mayor (equivalente a un nivel de lectura de un estudiante de pregrado de último año o superior), tu programa debe mostrar "Grado 16+" en lugar de dar el número de índice exacto. Si el nivel de grado es inferior a 1, tu programa debe mostrar "Antes del grado 1".

## Demostración

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script>

## Antecedentes

Entonces, ¿qué tipo de rasgos caracterizan los niveles de lectura más altos? Bueno, las palabras más largas probablemente se correlacionan con niveles de lectura más altos. Del mismo modo, las oraciones más largas probablemente también se correlacionen con niveles de lectura más altos.

Se han desarrollado varias "pruebas de legibilidad" a lo largo de los años que definen fórmulas para calcular el nivel de lectura de un texto. Una de esas pruebas de legibilidad es el _índice de Coleman-Liau_. El índice de Coleman-Liau de un texto está diseñado para generar el nivel de grado (estadounidense) que se necesita para comprender algún texto. La fórmula es:

    índice = 0,0588 * L - 0,296 * S - 15,8

donde `L` es el número promedio de letras por cada 100 palabras en el texto y `S` es el número promedio de oraciones por cada 100 palabras en el texto.

## Consejos

### Escribe algún código que sepas que compilará

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Ten en cuenta que ahora has incluido algunos archivos de encabezado que te darán acceso a las funciones que podrían ayudarte a resolver este problema.

### Escribe algún pseudocódigo antes de escribir más código

Si no estás seguro de cómo resolver el problema en sí, divídelo en problemas más pequeños que probablemente puedas resolver primero. Por ejemplo, este problema es en realidad solo un puñado de problemas:

1. Pídele al usuario algún texto
2. Cuenta la cantidad de letras, palabras y oraciones en el texto
3. Calcula el índice de Coleman-Liau
4. Imprime el nivel de grado

Escribamos algunos pseudocódigos como comentarios para recordarte que hagas именно eso:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Pídele al usuario algún texto

        // Cuenta la cantidad de letras, palabras y oraciones en el texto

        // Calcula el índice de Coleman-Liau

        // Imprime el nivel de grado
    }

### Convertir el pseudocódigo al código

En primer lugar, tenga en cuenta cómo le pediría algún texto al usuario. Recuerde que `get_string`, una función de la biblioteca CS50, puede pedirle una cadena al usuario.

```
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Pida algún texto al usuario
    string texto = get_string("Texto: ");

    // Cuente el número de letras, palabras y oraciones en el texto

    // Calcule el índice de Coleman-Liau

    // Imprima el nivel de grado
}
```

Ahora que ha recogido la aportación del usuario, puede comenzar a analizar dicha aportación. En primer lugar, intente contar el número de letras del texto. Considere que las letras son caracteres alfabéticos en mayúsculas o minúsculas, no puntuación, dígitos u otros símbolos.

Una forma de abordar este problema es crear una función llamada `count_letters` que toma una cadena de texto como entrada y luego devuelve el número de letras en ese texto como un `int`.

```
int count_letters(string texto)
{
    // Devuelva el número de letras en el texto
}
```

Tendrá que escribir su propio código para contar el número de letras del texto. Pero alguien con más experiencia que usted es posible que ya haya escrito una función para determinar si un carácter es alfabético. Esta es una buena oportunidad para utilizar el [manual de CS50](https://manual.cs50.io/), una colección de explicaciones de las funciones comunes en la biblioteca estándar de C.

Puede integrar `count_letters` en el código que ya ha escrito, como se indica a continuación.

```
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string texto);

int main(void)
{
    // Pida algún texto al usuario
    string texto = get_string("Texto: ");

    // Cuente el número de letras, palabras y oraciones en el texto
    int letras = count_letters(texto);

    // Calcule el índice de Coleman-Liau

    // Imprima el nivel de grado
}

int count_letters(string texto)
{
    // Devuelva el número de letras en el texto
}
```

A continuación, escriba una función para contar palabras.

```
int count_words(string texto)
{
    // Devuelva el número de palabras en el texto
}
```

Para los propósitos de este problema, consideraremos como palabra cualquier secuencia de caracteres separada por un espacio (por lo tanto, una palabra con guion como "cuñada" se debe considerar una palabra, no tres). Puede suponer que una oración:

- contendrá al menos una palabra;
- no comenzará ni terminará con un espacio; y
- no tendrá varios espacios seguidos.

Bajo estas suposiciones, es posible que pueda encontrar una relación entre el número de palabras y el número de espacios. Por supuesto, le invitamos a que intente una solución que tolere varios espacios entre palabras o, de hecho, ¡ninguna palabra!

Ahora puede integrar `count_words` en su programa como se indica a continuación:

```
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string texto);
int count_words(string texto);

int main(void)
{
    // Pida algún texto al usuario
    string texto = get_string("Texto: ");

    // Cuente el número de letras, palabras y oraciones en el texto
    int letras = count_letters(texto);
    int palabras = count_words(texto);

    // Calcule el índice de Coleman-Liau

    // Imprima el nivel de grado
}

int count_letters(string texto)
{
    // Devuelva el número de letras en el texto
}

int count_words(string texto)
{
    // Devuelva el número de palabras en el texto
}
```

Finalmente, escriba una función para contar oraciones. Puede considerar que cualquier secuencia de caracteres que termine con un `.` o un `!` o un `?` es una oración.

```
int count_sentences(string texto)
{
    // Devuelva el número de oraciones en el texto
}
```

Puedes integrar `count_sentences` en tu programa como se muestra a continuación:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);
    int count_sentences(string text);

    int main(void)
    {
        // Solicita al usuario que ingrese un texto
        string text = get_string("Texto: ");

        // Cuenta la cantidad de letras, palabras y oraciones en el texto
        int letters = count_letters(text);
        int words = count_words(text);
        int sentences = count_sentences(text);

        // Calcula el índice de Coleman-Liau

        // Imprime el grado de nivel
    }

    int count_letters(string text)
    {
        // Regresa la cantidad de letras en text
    }

    int count_words(string text)
    {
        // Regresa la cantidad de palabras en text
    }

    int count_sentences(string text)
    {
        // Regresa la cantidad de oraciones en text
    }

Finalmente, calcula el índice de Coleman-Liau e imprime el grado de nivel resultante.

- Recuerda que el índice de Coleman-Liau se calcula utilizando `index = 0.0588 * L - 0.296 * S - 15.8`
- `L` es el promedio de letras por cada 100 palabras en el texto: es decir, el número de letras dividido entre el número de palabras, todo multiplicado por 100.
- `S` es el promedio de oraciones por cada 100 palabras en el texto: es decir, el número de oraciones dividido entre el número de palabras, todo multiplicado por 100.
- Deberás redondear el resultado al número entero más cercano, por lo que recuerda que `round` se declara en `math.h`, según [manual.cs50.io](https://manual.cs50.io/).
- Recuerda que, al dividir valores de tipo `int` en C, el resultado también será un `int`, con cualquier residuo (es decir, dígitos después del punto decimal) descartado. Dicho de otra manera, el resultado será "truncado". ¡Tal vez quieras convertir uno o más de tus valores a `float` antes de realizar la división al calcular `L` y `S`!

Si el número de índice resultante es 16 o mayor (equivalente o mayor que un nivel de lectura de un estudiante universitario de último año), tu programa debe generar "Grado 16+" en lugar de generar un número de índice exacto. Si el número de índice es menor que 1, tu programa debe generar "Antes del grado 1".

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar

Intenta ejecutar tu programa en los siguientes textos para asegurarte de que veas el grado de nivel especificado. Asegúrate de copiar solo el texto, sin espacios adicionales.

- `One fish. Two fish. Red fish. Blue fish.` (Antes del grado 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grado 2)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grado 3)
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (Grado 5)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grado 7)
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (Grado 8)
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (Grado 8)
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (Grado 9)
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (Grado 10)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grado 16+)

### Corrección

En tu terminal, ejecuta lo siguiente para verificar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/readability

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código utilizando `style50`.

    style50 readability.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/readability

