## Corrector ortográfico

## Problema a resolver

Para este problema, implementarás un programa que corrija la ortografía de un archivo, como el siguiente, utilizando una tabla hash.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o01nuZNSBSH2khVokTs2GEPtP" src="https://asciinema.org/a/o01nuZNSBSH2khVokTs2GEPtP.js"></script>

## Código de distribución

Para este problema, ampliarás la funcionalidad del código proporcionado por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana del terminal y ejecuta `cd` por sí solo. Deberías encontrar que el indicador de la ventana de tu terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/5/speller.zip

para descargar un ZIP llamado `speller.zip` en tu espacio de códigos.

A continuación, ejecuta

    unzip speller.zip

para crear una carpeta llamada `speller`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm speller.zip

y responde con "y" seguido de Enter en el indicador para eliminar el archivo ZIP descargado.

Ahora escribe

    cd speller

seguido de Enter para moverte (es decir, abrir) ese directorio. Tu indicador ahora debería parecerse al siguiente.

    speller/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos y carpetas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/

Si tienes algún problema, sigue estos mismos pasos de nuevo y ¡observa si puedes determinar dónde te equivocaste!

## Antecedentes

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Dados los numerosos archivos de este programa, es importante leer esta sección en su totalidad antes de comenzar. ¡Entonces sabrás qué hacer y cómo hacerlo!</strong></p></div>

Teóricamente, con una entrada de tamaño _n_, un algoritmo con un tiempo de ejecución de _n_ es "asintóticamente equivalente", en términos de _O_, a un algoritmo con un tiempo de ejecución de _2n_. De hecho, al describir el tiempo de ejecución de un algoritmo, normalmente nos centramos en el término dominante (es decir, el más impactante) (es decir, _n_ en este caso, ya que _n_ podría ser mucho mayor que 2). Sin embargo, en el mundo real, el hecho es que _2n_ se siente el doble de lento que _n_.

El desafío que tienes por delante es implementar el corrector ortográfico más rápido que puedas. Sin embargo, por "más rápido", nos referimos al "muro del reloj" real, no al tiempo asintótico.

En `speller.c`, hemos creado un programa diseñado para corregir la ortografía de un archivo después de cargar un diccionario de palabras del disco a la memoria. Ese diccionario, mientras tanto, se implementa en un archivo llamado `dictionary.c`. (Simplemente podría implementarse en `speller.c`, pero a medida que los programas se vuelven más complejos, a menudo es conveniente dividirlos en varios archivos). Los prototipos para las funciones incluidas, mientras tanto, se definen no en `dictionary.c` sino en `dictionary.h`. De esa manera, tanto `speller.c` como `dictionary.c` pueden `#include` el archivo. Desafortunadamente, no llegamos a implementar la parte de carga. O la parte de verificación. ¡Ambos (y un poco más) te lo dejamos a ti! Pero primero, una visita.

### Entendiendo

#### `dictionary.h`

Abre `dictionary.h` y verás una nueva sintaxis, incluidas algunas líneas que mencionan `DICTIONARY_H`. No hay necesidad de preocuparse por esos, pero, si tienes curiosidad, esas líneas solo aseguran que, aunque `dictionary.c` y `speller.c` (que verás en un momento) `#include` este archivo, `clang` solo lo compilará una vez.

A continuación, observa cómo `#include` un archivo llamado `stdbool.h`. Ese es el archivo en el que se define `bool`. No lo has necesitado antes, ya que la biblioteca CS50 solía `#include` eso por ti.

También observa nuestro uso de `#define`, una "directiva de preprocesador" que define una "constante" llamada `LENGTH` que tiene un valor de `45`. Es una constante en el sentido de que no puedes (accidentalmente) cambiarla en tu propio código. De hecho, `clang` reemplazará cualquier mención de `LENGTH` en tu propio código con, literalmente, `45`. En otras palabras, no es una variable, solo un truco de búsqueda y reemplazo.

Finalmente, observa los prototipos para cinco funciones: `check`, `hash`, `load`, `size` y `unload`. Observa cómo tres de ellos toman un puntero como argumento, según el `*`:

    bool check(const char *word);
    unsigned int hash(const char *word);
    bool load(const char *dictionary);

Recuerda que `char *` es lo que solíamos llamar `string`. Por lo tanto, esos tres prototipos son esencialmente solo:

    bool check(const string word);
    unsigned int hash(const string word);
    bool load(const string dictionary);

Y `const`, mientras tanto, solo dice que esas cadenas, cuando se pasan como argumentos, deben permanecer constantes; ¡no podrás cambiarlas, accidental o de otra manera!

#### `dictionary.c`

Ahora abre `dictionary.c`. Observa cómo, en la parte superior del archivo, hemos definido una `struct` llamada `node` que representa un nodo en una tabla hash. Y hemos declarado una matriz de punteros global, `table`, que (pronto) representará la tabla hash que usarás para llevar un registro de las palabras en el diccionario. La matriz contiene `N` punteros de nodo, y hemos establecido `N` igual a `26` por ahora, para que coincida con la función `hash` predeterminada como se describe a continuación. Es probable que desees aumentar esto según tu propia implementación de `hash`.

A continuación, observa que hemos implementado `load`, `check`, `size` y `unload`, pero apenas lo suficiente para que se compile el código. Observa también que hemos implementado `hash` con un algoritmo de muestra basado en la primera letra de la palabra. Tu trabajo, en última instancia, es reimplementar esas funciones de la manera más inteligente posible para que este corrector ortográfico funcione como se anuncia. ¡Y rápido!

#### `speller.c`

Bien, ahora abre `speller.c` y dedica algo de tiempo a revisar el código y los comentarios contenidos en él. No necesitarás cambiar nada en este archivo y no necesitas entender su totalidad, pero intenta hacerte una idea de su funcionalidad de todos modos. Observa cómo, por medio de una función llamada `getrusage`, usaremos “evaluadores comparativos” (por ejemplo, mediremos la ejecución de) tus implementaciones de `check`, `load`, `size` y `unload`. Observa también cómo pasamos a `check`, palabra por palabra, los contenidos de un archivo para que se revise su ortografía. Finalmente, informamos cada error de ortografía en ese archivo junto con un montón de estadísticas.

Observa, por cierto, que hemos definido el uso de `speller` como:

    Uso: speller [diccionario] texto

donde se asume que `diccionario` es un archivo que contiene una lista de palabras en minúsculas, una por línea, y `texto` es un archivo que se revisará su ortografía. Como sugiere el corchete, la provisión de `diccionario` es opcional; si se omite este argumento, `speller` usará `dictionaries/large` de forma predeterminada. En otras palabras, ejecutar:

    ./speller texto

será equivalente a ejecutar:

    ./speller dictionaries/large texto

donde `texto` es el archivo que deseas revisar su ortografía. Baste decir que el anterior es más fácil de escribir. (Por supuesto, `speller` no podrá cargar ningún diccionario hasta que implementes `load` en `dictionary.c`. Hasta entonces, verás `No se pudo cargar`).

Dentro del diccionario predeterminado, debes tener en cuenta que hay 143,091 palabras, ¡todas las cuales deben cargarse en la memoria! De hecho, echa un vistazo a ese archivo para hacerte una idea de su estructura y tamaño. Observa que cada palabra en ese archivo aparece en minúsculas (incluso, por simplicidad, nombres propios y acrónimos). De arriba hacia abajo, el archivo está ordenado lexicográficamente, con solo una palabra por línea (cada una de las cuales termina con `\n`). Ninguna palabra tiene más de 45 caracteres y ninguna palabra aparece más de una vez. Durante el desarrollo, puedes encontrar útil proporcionar a `speller` un `diccionario` propio que contenga muchas menos palabras, para no tener que esforzarte en depurar una estructura enormemente grande en la memoria. En `dictionaries/small` se encuentra uno de esos diccionarios. Para usarlo, ejecuta:

    ./speller dictionaries/small texto

donde `texto` es el archivo que deseas revisar su ortografía. ¡No sigas adelante hasta que estés seguro de entender cómo funciona `speller`!

Es probable que no hayas dedicado suficiente tiempo a revisar `speller.c`. ¡Retrocede un cuadrado y revísalo de nuevo!

#### `texts/`

Para que puedas probar tu implementación de `speller`, también te hemos proporcionado un montón de textos, entre ellos el guion de _La La Land_, el texto de la Ley de Atención Médica Asequible, tres millones de bytes de Tolstoi, algunos extractos de _The Federalist Papers_ y Shakespeare, y más. Para que sepas qué esperar, abre y hojea cada uno de esos archivos, todos los cuales se encuentran en un directorio llamado `texts` dentro de tu directorio `pset5`.

Ahora, como debes saber por haber leído `speller.c` cuidadosamente, el resultado de `speller`, si se ejecuta con, digamos:

    ./speller texts/lalaland.txt

eventualmente se parecerá a lo siguiente.

A continuación, se muestra parte de la salida que verás. A modo de información, hemos extraído algunos ejemplos de "errores ortográficos". Y para no estropear la diversión, hemos omitido nuestras propias estadísticas por ahora.

    PALABRAS MAL ESCRITAS

    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    fianc
    [...]
    Sebastian's
    [...]

    PALABRAS MAL ESCRITAS:
    PALABRAS EN EL DICCIONARIO:
    PALABRAS EN EL TEXTO:
    TIEMPO EN `load`:
    TIEMPO EN `check`:
    TIEMPO EN `size`:
    TIEMPO EN `unload`:
    TIEMPO TOTAL:

`TIEMPO EN load` representa el número de segundos que `speller` dedica a ejecutar tu implementación de `load`. `TIEMPO EN check` representa el número de segundos que `speller` dedica, en total, a ejecutar tu implementación de `check`. `TIEMPO EN size` representa el número de segundos que `speller` dedica a ejecutar tu implementación de `size`. `TIEMPO EN unload` representa el número de segundos que `speller` dedica a ejecutar tu implementación de `unload`. `TIEMPO TOTAL` es la suma de esas cuatro mediciones.

**Ten en cuenta que estos tiempos pueden variar algo entre las ejecuciones de `speller`, según lo que esté haciendo tu zona de trabajo de códigos, incluso si no cambias tu código.**

Por cierto, para ser claros, con "mal escrito" simplemente queremos decir que alguna palabra no está en el `diccionario` proporcionado.

#### `Makefile`

Y, por último, recuerda que `make` automatiza la compilación de tu código para que no tengas que ejecutar `clang` manualmente junto con un montón de interruptores. Sin embargo, a medida que tus programas crezcan en tamaño, `make` ya no podrá inferir del contexto cómo compilar tu código; tendrás que empezar a indicarle a `make` cómo compilar tu programa, particularmente cuando involucran múltiples fuentes (por ejemplo, archivos `.c`), como en el caso de este problema. Así que utilizaremos un `Makefile`, un archivo de configuración que le dice a `make` exactamente qué hacer. Abre `Makefile` y deberías ver cuatro líneas:

1. La primera línea le dice a `make` que ejecute las siguientes líneas cada vez que tú mismo ejecutes `make speller` (o simplemente `make`).
2. La segunda línea le dice a `make` cómo compilar `speller.c` en código máquina (es decir, `speller.o`).
3. La tercera línea le dice a `make` cómo compilar `dictionary.c` en código máquina (es decir, `dictionary.o`).
4. La cuarta línea le dice a `make` que vincule `speller.o` y `dictionary.o` en un archivo llamado `speller`.

**Asegúrate de compilar `speller` ejecutando `make speller` (o simplemente `make`). ¡Ejecutar `make dictionary` no funcionará!**

## Especificaciones

De acuerdo, el desafío ahora ante ti es implementar, en orden, `load`, `hash`, `size`, `check` y `unload` de la manera más eficiente posible usando una tabla hash de tal manera que `TIME IN load`, `TIME IN check`, `TIME IN size` y `TIME IN unload` sean minimizados. Para estar seguros, no es obvio lo que significa minimizado, ya que estos benchmarks ciertamente variarán a medida que pases a `speller` diferentes valores para `dictionary` y `text`. Pero ahí radica el desafío, si no la diversión, de este problema. Este problema es tu oportunidad de diseñar. Aunque te invitamos a minimizar el espacio, tu enemigo definitivo es el tiempo. Pero antes de sumergirte, algunas especificaciones de nosotros.

- No puedes modificar `speller.c` o `Makefile`.
- Puedes modificar `dictionary.c` (y, de hecho, debes hacerlo para completar las implementaciones de `load`, `hash`, `size`, `check` y `unload`), pero no puedes modificar las declaraciones (es decir, prototipos) de `load`, `hash`, `size`, `check` o `unload`. Sin embargo, puedes añadir nuevas funciones y variables (locales o globales) a `dictionary.c`.
- Puedes cambiar el valor de `N` en `dictionary.c`, para que tu tabla hash pueda tener más cubos.
- Puedes modificar `dictionary.h`, pero no puedes modificar las declaraciones de `load`, `hash`, `size`, `check` o `unload`.
- Tu implementación de `check` debe ser insensible a mayúsculas y minúsculas. En otras palabras, si `foo` está en el diccionario, entonces `check` debe devolver verdadero dado cualquier uso de mayúsculas y minúsculas; ninguno de `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` y `FOO` debe considerarse mal escrito.
- Dejando de lado las mayúsculas y minúsculas, tu implementación de `check` sólo debería devolver `true` para palabras que estén realmente en `dictionary`. Ten cuidado con la codificación de palabras comunes (por ejemplo, `the`), no sea que pasemos tu implementación de un `dictionary` sin esas mismas palabras. Además, los únicos posesivos permitidos son los que están realmente en `dictionary`. En otras palabras, incluso si `foo` está en `dictionary`, `check` debe devolver `false` dado `foo's` si `foo's` no está también en `dictionary`.
- Puedes asumir que cualquier `dictionary` pasado a tu programa estará estructurado exactamente como el nuestro, ordenado alfabéticamente de arriba a abajo con una palabra por línea, cada una de las cuales termina con `\n`. También puedes suponer que `dictionary` contendrá al menos una palabra, que ninguna palabra tendrá más de `LENGTH` (una constante definida en `dictionary.h`) caracteres, que ninguna palabra aparecerá más de una vez, que cada palabra contendrá sólo caracteres alfabéticos en minúsculas y posiblemente apóstrofes, y que ninguna palabra comenzará con un apóstrofe.
- Puedes asumir que `check` sólo recibirá palabras que contengan caracteres alfabéticos (en mayúsculas o minúsculas) y posiblemente apóstrofes.
- Tu corrector ortográfico sólo puede tomar `text` y, opcionalmente, `dictionary` como entrada. Aunque podrías estar inclinado (especialmente si estás entre los más cómodos) a "preprocesar" nuestro diccionario predeterminado para derivar una "función hash ideal" para él, no puedes guardar la salida de dicho preprocesamiento en el disco para volver a cargarlo en la memoria en ejecuciones posteriores de tu corrector ortográfico para obtener una ventaja.
- Tu corrector ortográfico no debe perder memoria. Asegúrate de comprobar las pérdidas con `valgrind`.
- **La función hash que escribas debería ser finalmente tuya, no una que busques en línea.**

Bien, ¿listo para empezar?

- Implementa `load`.
- Implementa `hash`.
- Implementa `size`.
- Implementa `check`.
- Implementa `unload`.

## Sugerencias

### Implementa `load`

Completa la función `load`. `load` debe cargar el diccionario en la memoria (¡en particular, en una tabla hash!). `load` debe devolver `true` si tiene éxito y `false` si no.

Considera que este problema está compuesto sólo por problemas más pequeños:

1.  Abre el archivo del diccionario
2.  Lee cada palabra en el archivo
    1.  Añade cada palabra a la tabla hash
3.  Cierra el archivo del diccionario

Escribe un pseudocódigo para recordarte que hagas precisamente eso:

    bool load(const char *dictionary)
    {
        // Abre el archivo del diccionario

        // Lee cada palabra en el archivo

            // Añade cada palabra a la tabla hash

        // Cierra el archivo del diccionario
    }

Considera primero cómo abrir el archivo del diccionario. [`fopen`](https://manual.cs50.io/3/fopen) es una opción natural. Puedes usar el modo `r`, dado que sólo necesitas _leer_ palabras del archivo del diccionario (no _escribirlas_ o _añadirlas_).

    bool load(const char *dictionary)
    {
        // Abre el archivo del diccionario
        FILE *source = fopen(dictionary, "r");

        // Lee cada palabra en el archivo

            // Añade cada palabra a la tabla hash

        // Cierra el archivo del diccionario
    }

Antes de continuar, debes escribir código para comprobar si el archivo se abrió correctamente. ¡Eso depende de ti! También es mejor asegurarse de cerrar todos los archivos que abras, así que ahora es un buen momento para escribir el código para cerrar el archivo del diccionario:

    bool load(const char *dictionary)
    {
        // Abre el archivo del diccionario
        FILE *source = fopen(dictionary, "r");

        // Lee cada palabra en el archivo

            // Añade cada palabra a la tabla hash

        // Cierra el archivo del diccionario
        fclose(source);
    }

Lo que queda es leer cada palabra del archivo y añadirla a la tabla hash. Devuelve `true` cuando toda la operación sea exitosa y `false` si falla alguna vez. Considera seguir el recorrido de este problema y continúa rompiendo los subproblemas en problemas aún más pequeños. Por ejemplo, añadir cada palabra a la tabla hash podría ser sólo cuestión de implementar unos pocos pasos aún más pequeños:

1.  Crea espacio para un nuevo nodo de tabla hash
2.  Copia la palabra en el nuevo nodo
3.  Convierte la palabra en un hash para obtener su valor de hash
4.  Inserta el nuevo nodo en la tabla hash (usando el índice especificado por su valor de hash)

Por supuesto, hay más de una manera de abordar este problema, cada una con sus propias ventajas y desventajas de diseño. Por esa razón, ¡el resto del código depende de ti!

### Implementa `hash`

Completa la función `hash`. `hash` debe tomar una cadena, `word`, como entrada y devolver un `int` positivo ("sin signo").

La función hash que te damos devuelve un `int` entre 0 y 25, inclusive, basado en el primer carácter de `word`. Sin embargo, hay muchas maneras de implementar una función hash más allá de usar el primer carácter (o _caracteres_) de una palabra. Considera una función hash que usa una suma de valores ASCII o la longitud de una palabra. Una buena función hash reduce las "colisiones" y tiene una (¡casi siempre!) distribución uniforme en los "cubos" de la tabla hash.

### Implementa `size`

Completa la función `size`. `size` debe devolver el número de palabras cargadas en el diccionario. Considera dos enfoques para este problema:

* Cuenta cada palabra cargada en el diccionario. Devuelve ese conteo cuando se llama a `size`.
* Cada vez que se llama a la función `size`, itera mediante las palabras en la tabla hash para contarlas. Devuelve ese conteo.

¿Cuál te parece más eficiente? El que elijas, te dejaremos el código a ti.

### Implementa `check`

Completa la función `check`. `check` debe devolver `true` si una palabra se encuentra en el diccionario; de lo contrario, `false`.

Considera que este problema también se compone de problemas menores. Si has implementado una tabla hash, encontrar una palabra requiere solo unos pasos:

1. Establece un hash para la palabra para obtener su valor hash.
2. Busca en la tabla hash en la ubicación especificada por el valor hash de la palabra.
    1. Devuelve `true` si se encuentra la palabra.
3. Devuelve `false` si no se encuentra ninguna palabra.

Para comparar dos cadenas sin distinción entre mayúsculas y minúsculas, puedes encontrar útil [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (declarada en `strings.h`). También es probable que quieras asegurarte de que tu función hash no distinga entre mayúsculas y minúsculas; de modo que `foo` y `FOO` tengan el mismo valor hash.

### Implementa `unload`

Completa la función `unload`. Asegúrate de `liberar` en `unload` cualquier memoria que hayas asignado en `load`.

Recuerda que `valgrind` es tu mejor amigo de ahora en adelante. Ten en cuenta que `valgrind` observa las fugas mientras tu programa está en ejecución, así que asegúrate de proporcionar argumentos de línea de comandos si quieres que `valgrind` analice `speller` mientras usas un `diccionario` y/o texto en particular, como se muestra a continuación. Sin embargo, es mejor usar un texto pequeño, de lo contrario, valgrind podría tardar bastante en ejecutarse.

    valgrind ./speller texts/cat.txt

Si ejecutas `valgrind` sin especificar un `texto` para `speller`, tus implementaciones de `load` y `unload` no se ejecutarán (y, por lo tanto, no se analizarán).

Si no estás seguro de cómo interpretar el resultado de `valgrind`, pide ayuda a `help50`:

    help50 valgrind ./speller texts/cat.txt

## Guías

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Ten en cuenta que hay 6 videos en esta lista.</strong></p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

## Cómo realizar la prueba

¿Cómo verificar si tu programa está generando las palabras mal escritas correctas? Puedes consultar las "claves de respuesta" que se encuentran en el directorio `keys` dentro de tu directorio `speller`. Por ejemplo, dentro de `keys/lalaland.txt` están todas las palabras que tu programa _debe_ considerar mal escritas.

Por lo tanto, podrías ejecutar tu programa en un texto en una ventana, como se muestra a continuación.

    ./speller texts/lalaland.txt

Y luego podrías ejecutar la solución del personal en el mismo texto en otra ventana, como se muestra a continuación.

    ./speller50 texts/lalaland.txt

Y luego podrías comparar las ventanas visualmente una al lado de la otra. Sin embargo, eso podría volverse tedioso. Por lo tanto, es posible que desees "redirigir" la salida de tu programa a un archivo, como se muestra a continuación.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt

Luego, puedes comparar ambos archivos uno al lado del otro en la misma ventana con un programa como `diff`, como se muestra a continuación.

    diff -y student.txt staff.txt

Alternativamente, para ahorrar tiempo, podrías comparar la salida de tu programa (suponiendo que la redirigiste a, por ejemplo, `student.txt`) con una de las claves de respuesta sin ejecutar la solución del personal, como se muestra a continuación.

    diff -y student.txt keys/lalaland.txt

Si la salida de tu programa coincide con la del personal, `diff` generará dos columnas que deberían ser idénticas, excepto, quizás, por los tiempos de ejecución en la parte inferior. Sin embargo, si las columnas difieren, verás un `>` o `|` donde difieren. Por ejemplo, si ves

    MISSPELLED WORDS                                                MISSPELLED WORDS

    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L

significa que tu programa (cuya salida está a la izquierda) no cree que `Thelonious` o `MIA` estén mal escritas, aunque la salida del personal (a la derecha) sí lo hace, como lo implica la ausencia de, por ejemplo, `Thelonious` en la columna de la izquierda y la presencia de `Thelonious` en la columna de la derecha.

Por último, asegúrate de realizar la prueba con ambos diccionarios, el pequeño y el grande predeterminados. Ten cuidado de no asumir que si tu solución se ejecuta correctamente con el diccionario grande, también se ejecutará correctamente con el pequeño. Aquí tienes cómo probar el diccionario pequeño:

    ./speller dictionaries/small texts/cat.txt

### Corrección

    check50 cs50/problems/2024/x/speller

### Estilo

    style50 dictionary.c

## Solución del personal

¿Cómo evaluar qué tan rápido (y correcto) es tu código? Bueno, como siempre, siéntete libre de jugar con la solución del personal, como se muestra a continuación, y comparar sus números con los tuyos.

    ./speller50 texts/lalaland.txt

## Cómo enviar

    submit50 cs50/problems/2024/x/speller

