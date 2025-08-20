**# Pluralidad**

**## Problema a resolver**

Las elecciones pueden ser de todo tipo y tamaño. En el Reino Unido, el [Primer Ministro](https://www.parliament.uk/education/about-your-parliament/general-elections/) es designado oficialmente por el monarca, quien generalmente elige al líder del partido político que obtenga la mayor cantidad de escaños en la Cámara de los Comunes. Estados Unidos utiliza un proceso de [Colegio Electoral](https://www.archives.gov/federal-register/electoral-college/about.html) multietapa en el que los ciudadanos votan sobre cómo debe asignar cada estado a los electores que luego eligen al Presidente.

Quizás la forma más sencilla de celebrar una elección es mediante un método comúnmente conocido como "voto mayoritario" (también conocido como "el primero que pasa o el ganador se lo lleva todo"). En la votación por mayoría, cada votante puede votar por un candidato. Al final de la elección, el candidato que tenga la mayor cantidad de votos es declarado ganador de la elección.

Para este problema, implementarás un programa que ejecuta una elección por mayoría, según lo establecido a continuación.

**## Demostración**

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o2EXEqiz7iqfDB31wYxBOWjs8" src="https://asciinema.org/a/o2EXEqiz7iqfDB31wYxBOWjs8.js"></script>

**## Código de distribución**

Para este problema, ampliarás la funcionalidad del "código de distribución" que te proporcionó el personal de CS50.

**### Descarga el código de distribución**

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana de tu terminal y ejecuta `cd` por sí mismo. Deberías encontrar que el símbolo del sistema de tu ventana de terminal se asemeja al siguiente:

    $

Luego ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/3/plurality.zip

para descargar un ZIP llamado `plurality.zip` en tu espacio de códigos.

Luego ejecuta

    unzip plurality.zip

para crear una carpeta llamada `plurality`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm plurality.zip

y responde con "y" seguido de Enter en el símbolo del sistema para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd plurality

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu símbolo del sistema ahora debería parecerse al siguiente.

    plurality/ $

Si todo fue exitoso, deberías ejecutar

    ls

y ver un archivo llamado `plurality.c`. Al ejecutar `code plurality.c` deberías abrir el archivo donde escribirás tu código para este conjunto de problemas. De lo contrario, ¡regresa sobre tus pasos e intenta determinar dónde te equivocaste!

**### Comprende el código en `plurality.c`**

Siempre que amplíes la funcionalidad del código existente, es mejor asegurarte de que primero lo comprendas en su estado actual.

Mira primero la parte superior del archivo. La línea `#define MAX 9` es una sintaxis que se usa aquí para indicar que `MAX` es una constante (igual a `9`) que se puede usar en todo el programa. Aquí, representa el número máximo de candidatos que puede tener una elección.

    // Número máximo de candidatos
    #define MAX 9

Ten en cuenta que `plurality.c` luego usa esta constante para definir un arreglo global, es decir, un arreglo al que cualquier función puede acceder.

    // Arreglo de candidatos
    candidate candidates[MAX];

Pero ¿qué es, en este caso, un `candidate`? En `plurality.c`, un `candidate` es una `struct`. Cada `candidate` tiene dos campos: una `string` llamada `name` que representa el nombre del candidato y un `int` llamado `votes` que representa el número de votos que tiene el candidato.

    // Los candidatos tienen nombre y recuento de votos
    typedef struct
    {
        string name;
        int votes;
    }
    candidate;

Ahora, observa la propia función `main`. Mira si puedes encontrar dónde el programa establece una variable global `candidate_count` que representa el número de candidatos en la elección.

    // Número de candidatos
    int candidate_count;

¿Qué pasa con el lugar donde copia los argumentos de la línea de comandos en el arreglo `candidates`?

    // Llenar el arreglo de candidatos
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("El número máximo de candidatos es %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

¿Y dónde le pide al usuario que escriba el número de votantes?

    int voter_count = get_int("Número de votantes: ");

Luego, el programa permite que cada votante escriba un voto, llamando a la función `vote` para cada candidato votado. Finalmente, `main` realiza una llamada a la función `print_winner` para imprimir el ganador (o ganadores) de la elección. Te dejaremos identificar el código que implementa esta funcionalidad.

Sin embargo, si miras más abajo en el archivo, notarás que las funciones `vote` y `print_winner` se han dejado en blanco.

    // Actualizar los totales de votos dado un nuevo voto
    bool vote(string name)
    {
        // TODO
        return false;
    }

    // Imprimir el ganador (o ganadores) de la elección
    void print_winner(void)
    {
        // TODO
        return;
    }

¡Esta parte depende de ti completarla! **No debes modificar nada más en `plurality.c` aparte de las implementaciones de las funciones `vote` y `print_winner` (y la inclusión de archivos de encabezado adicionales, si lo deseas).**

## Sugerencias

### Completa la función `vote`

A continuación, completa la función `vote`.

- Considera que la firma de `vote`, `bool vote(string nombre)`, muestra que toma un único argumento, un `string` llamado `nombre`, que representa el nombre del candidato por el que se votó.
- `vote` debe devolver un `bool`, donde `true` indica que se emitió un voto correctamente y `false` indica que no.

Una forma de abordar este problema es hacer lo siguiente:

1. Iterar sobre cada candidato
    1. Comprobar si el nombre del candidato coincide con la entrada, `name`
        1. Si es así, incrementar los votos de ese candidato y devolver `true`
        2. Si no, seguir comprobando
2. Si no hay coincidencias después de comprobar cada candidato, devolver `false`

Vamos a escribir un pseudo código para recordarte que hagas justo eso:

    // Actualizar los totales de votos dado un nuevo voto
    bool vote(string nombre)
    {
        // Iterar sobre cada candidato
            // Comprobar si el nombre del candidato coincide con el nombre dado
                // Si es así, incrementar los votos del candidato y devolver true

        // Si no hay coincidencia, devolver false
    }

¡Sin embargo, dejaremos la implementación en código para ti!

### Completa la función `print_winner`

Finalmente, completa la función `print_winner`.

- La función debe imprimir el nombre del candidato que recibió más votos en las elecciones y, a continuación, imprimir una nueva línea.
- Las elecciones podrían terminar en empate si varios candidatos tienen el número máximo de votos. En ese caso, debes mostrar los nombres de cada uno de los candidatos ganadores, cada uno en una línea separada.

Podrías pensar que un algoritmo de ordenación sería la mejor solución para este problema: imagina ordenar a los candidatos por sus totales de votos e imprimir el candidato (o candidatos) principal. Sin embargo, recuerda que ordenar puede ser costoso: incluso Merge Sort, uno de los algoritmos de ordenación más rápidos, se ejecuta en \\(O(N \\space log(N))\\).

Considera que solo necesitas dos fragmentos de información para resolver este problema:

1. El número máximo de votos
2. El candidato (o candidatos) con ese número de votos

Como tal, una buena solución podría requerir solo dos búsquedas. Escribe un pseudo código para recordarte que hagas justo eso:

    // Imprimir el ganador (o ganadores) de las elecciones
    void print_winner(void)
    {
        // Encontrar el número máximo de votos

        // Imprimir el candidato (o candidatos) con el máximo de votos

    }

¡Sin embargo, dejaremos el código para ti!

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo realizar pruebas

Asegúrate de probar tu código para comprobar que gestiona...

- Unas elecciones con cualquier número de candidatos (hasta el `MAX` de `9`)
- Votar por un candidato por su nombre
- Votos no válidos para candidatos que no están en la papeleta
- Imprimir el ganador de las elecciones si solo hay uno
- Imprimir al ganador de las elecciones si hay varios ganadores

### Corrección

    check50 cs50/problems/2024/x/plurality

### Estilo

    style50 plurality.c

## Cómo enviar

    submit50 cs50/problems/2024/x/plurality

