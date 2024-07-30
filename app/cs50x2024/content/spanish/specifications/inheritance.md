## Herencia

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/xfZhb6lmxjk?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Problema a resolver

El tipo de sangre de una persona está determinado por dos alelos (es decir, diferentes formas de un gen). Los tres posibles alelos son A, B y O, de los cuales cada persona tiene dos (posiblemente el mismo, posiblemente diferente). Cada uno de los padres de un niño transmite aleatoriamente uno de sus dos alelos de tipo sanguíneo a su hijo. Las posibles combinaciones de tipos sanguíneos, entonces, son: OO, OA, OB, AO, AA, AB, BO, BA y BB.

Por ejemplo, si un padre tiene el tipo de sangre AO y el otro padre tiene el tipo de sangre BB, entonces los posibles tipos de sangre del hijo serían AB y OB, dependiendo de qué alelo se reciba de cada padre. De manera similar, si un padre tiene el tipo de sangre AO y el otro OB, entonces los posibles tipos de sangre del hijo serían AO, OB, AB y OO.

En un archivo llamado `inheritance.c` en una carpeta llamada `inheritance`, simule la herencia de los tipos sanguíneos para cada miembro de una familia.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-J9DnbdokgIAjWUbzC2CBqP22N" src="https://asciinema.org/a/J9DnbdokgIAjWUbzC2CBqP22N.js"></script>

## Código de distribución

Para este problema, ampliarás la funcionalidad del código proporcionado por el personal de CS50.

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí solo. Deberías encontrar que el mensaje de tu ventana de terminal se asemeja a lo siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/5/inheritance.zip

para descargar un ZIP llamado `inheritance.zip` en tu espacio de códigos.

Luego ejecuta

    unzip inheritance.zip

para crear una carpeta llamada `inheritance`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm inheritance.zip

y responder con "y" seguido de Enter en el mensaje para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd inheritance

seguido de Enter para moverte a (es decir, abrir) ese directorio. Tu mensaje ahora debería parecerse al siguiente.

    inheritance/ $

Ejecuta `ls` por sí solo, y deberías ver un archivo llamado `inheritance.c`.

Si tienes algún problema, sigue estos mismos pasos de nuevo y mira si puedes determinar dónde te equivocaste.

## Detalles de implementación

Completa la implementación de `inheritance.c`, de manera que cree una familia de un tamaño de generación especificado y asigne alelos de tipo sanguíneo a cada miembro de la familia. La generación más antigua tendrá alelos asignados aleatoriamente.

- La función `create_family` toma un entero (`generations`) como entrada y debe asignar (como mediante `malloc`) una `persona` para cada miembro de la familia de ese número de generaciones, devolviendo un puntero a la `persona` en la generación más joven.
  - Por ejemplo, `create_family(3)` debe devolver un puntero a una persona con dos padres, donde cada padre también tiene dos padres.
  - A cada `persona` se le deben asignar `alelos`. A la generación más antigua se le deben asignar alelos elegidos aleatoriamente (como llamando a la función `random_allele`), y las generaciones más jóvenes deben heredar un alelo (elegido aleatoriamente) de cada padre.
  - A cada `persona` se le deben asignar `padres`. La generación más antigua debe tener ambos `padres` establecidos en `NULL`, y las generaciones más jóvenes deben tener `padres` como una matriz de dos punteros, cada uno apuntando a una estructura `persona` diferente.

## Sugerencias

### Comprende el código en `inheritance.c`

Echa un vistazo al código de distribución en `inheritance.c`.

Observa la definición de un tipo llamado `persona`. Cada persona tiene una matriz de dos `padres`, cada uno de los cuales es un puntero a otra estructura `persona`. Cada persona también tiene una matriz de dos `alelos`, cada uno de los cuales es un `char` (ya sea `'A'`, `'B'` o `'O'`).

    // Cada persona tiene dos padres y dos alelos
    typedef struct person
    {
        struct person *parents[2];
        char alleles[2];
    }
    person;

Ahora, echa un vistazo a la función `main`. La función comienza "sembrando" (es decir, proporcionando alguna entrada inicial a) un generador de números aleatorios, que usaremos más adelante para generar alelos aleatorios.

    // Sembrar generador de números aleatorios
    srand(time(0));

La función `main` luego llama a la función `create_family` para simular la creación de estructuras `persona` para una familia de 3 generaciones (es decir, una persona, sus padres y sus abuelos).

    // Crear una nueva familia con tres generaciones
    person *p = create_family(GENERATIONS);

Luego llamamos a `print_family` para imprimir cada uno de esos miembros de la familia y sus tipos de sangre.

    // Imprimir árbol genealógico de tipos sanguíneos
    print_family(p, 0);

Finalmente, la función llama a `free_family` para `liberar` cualquier memoria que se haya asignado previamente con `malloc`.

    // Liberar memoria
    free_family(p);

¡Las funciones `create_family` y `free_family` quedan para que las escribas!

### Completa la función `create_family`

La función `create_family` debería devolver un puntero a una `persona` que haya heredado su tipo de sangre del número de `generaciones` dado como entrada.

- Primero, nota que este problema plantea una buena oportunidad para la recursividad.
  - Para determinar el tipo de sangre de la persona presente, primero necesitas determinar los tipos de sangre de sus padres.
  - Para determinar los tipos de sangre de esos padres, primero debes determinar los tipos de sangre de sus padres. Y así sucesivamente hasta llegar a la última generación que deseas simular.

Para resolver este problema, encontrarás varios TODOs en el código de distribución.

Primero, deberías asignar memoria para una nueva persona. Recuerda que puedes usar `malloc` para asignar memoria y `sizeof(person)` para obtener el número de bytes a asignar.

    // Asigna memoria para una nueva persona
    person *new_person = malloc(sizeof(person));

Luego, deberías verificar si todavía quedan generaciones por crear: es decir, si `generaciones > 1`.

Si `generaciones > 1`, entonces hay más generaciones que aún necesitan ser asignadas. Ya hemos creado dos nuevos padres, `padre0` y `padre1`, llamando recursivamente a `create_family`. Entonces, tu función `create_family` debería establecer los punteros de los padres de la nueva persona que creaste. Finalmente, asigna ambos `alelos` para la nueva persona eligiendo aleatoriamente un alelo de cada padre.

- Recuerda, para acceder a una variable a través de un puntero, puedes utilizar la notación de flecha. Por ejemplo, si `p` es un puntero a una persona, entonces se puede acceder a un puntero al primer padre de esta persona mediante `p->parents[0]`.
- Puede que encuentres útil la función `rand()` para asignar alelos aleatoriamente. Esta función devuelve un entero entre `0` y `RAND_MAX`, o `32767`. En particular, para generar un número pseudoaleatorio que sea `0` o `1`, puedes utilizar la expresión `rand() % 2`.

  // Crea dos nuevos padres para la persona actual llamando recursivamente a create_family
  person *parent0 = create_family(generations - 1);
  person *parent1 = create_family(generations - 1);

  // Establece los punteros de los padres para la persona actual
  new_person->parents[0] = parent0;
  new_person->parents[1] = parent1;

  // Asigna aleatoriamente los alelos de la persona actual en función de los alelos de sus padres
  new_person->alleles[0] = parent0->alleles[rand() % 2];
  new_person->alleles[1] = parent1->alleles[rand() % 2];

Digamos que no quedan más generaciones para simular. Es decir, `generaciones == 1`. Si es así, no habrá datos de padres para esta persona. Ambos padres de tu nueva persona deben configurarse en `NULL` y cada `alelo` debe generarse aleatoriamente.

    // Establece los punteros de los padres en NULL
    new_person->parents[0] = NULL;
    new_person->parents[1] = NULL;

    // Asigna alelos aleatoriamente
    new_person->alleles[0] = random_allele();
    new_person->alleles[1] = random_allele();

Finalmente, tu función debería devolver un puntero para la `persona` que fue asignada.

    // Devuelve la persona recién creada
    return new_person;

### Completa la función `free_family`

La función `free_family` debería aceptar como entrada un puntero a una `persona`, liberar la memoria para esa persona y luego liberar recursivamente la memoria para todos sus antepasados.

- Como esta es una función recursiva, primero debes manejar el caso base. Si la entrada a la función es `NULL`, entonces no hay nada que liberar, por lo que tu función puede regresar inmediatamente.
- De lo contrario, deberías `liberar` recursivamente a los dos padres de la persona antes de `liberar` al niño.

La siguiente es una gran pista, ¡pero aquí tienes cómo hacerlo!

    // Libera `p` y todos los antepasados de `p`.
    void free_family(person *p)
    {
        // Maneja el caso base
        if (p == NULL)
        {
            return;
        }

        // Libera a los padres recursivamente
        free_family(p->parents[0]);
        free_family(p->parents[1]);

        // Libera al niño
        free(p);
    }

### Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9p7ddI3ozTY?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>¿No estás seguro de cómo resolverlo?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/H7LULatPwcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Cómo probar

Al ejecutar `./inheritance`, tu programa debería cumplir con las reglas descritas en los antecedentes. El niño debería tener dos alelos, uno de cada padre. Los padres deberían tener cada uno dos alelos, uno de cada uno de sus padres.

Por ejemplo, en el siguiente ejemplo, el niño en la generación 0 recibió un alelo O de ambos padres de la generación 1. El primer padre recibió una A del primer abuelo y una O del segundo abuelo. De manera similar, el segundo padre recibió una O y una B de sus abuelos.

    $ ./inheritance
    Niño (Generación 0): tipo de sangre OO
        Padre (Generación 1): tipo de sangre AO
            Abuelo (Generación 2): tipo de sangre OA
            Abuela (Generación 2): tipo de sangre BO
        Padre (Generación 1): tipo de sangre OB
            Abuelo (Generación 2): tipo de sangre AO
            Abuela (Generación 2): tipo de sangre BO

### Corrección

    check50 cs50/problems/2024/x/inheritance

### Estilo

    style50 inheritance.c

## Enviar

    submit50 cs50/problems/2024/x/inheritance

