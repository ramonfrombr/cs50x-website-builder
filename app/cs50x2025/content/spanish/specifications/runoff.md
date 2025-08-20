**# Sistema de votación por mayoría relativa**

## Problema a resolver

Ya conoces las elecciones por mayoría relativa, que siguen un algoritmo muy sencillo para determinar el ganador de una elección: cada votante obtiene un voto y el candidato con más votos gana.

Pero el voto por mayoría relativa tiene algunas desventajas. ¿Qué sucede, por ejemplo, en una elección con tres candidatos y se emiten las siguientes papeletas?

[!Cinco papeletas para votar con empate entre Alice y Bob](https://cs50.harvard.edu/x/2024/psets/3/fptp_ballot_1.png)

El voto por mayoría relativa declararía un empate entre Alice y Bob, ya que cada uno tiene dos votos. Pero, ¿es ese el resultado correcto?

Existe otro tipo de sistema de votación conocido como sistema de votación por orden de preferencia. En un sistema de orden de preferencia, los votantes pueden votar por más de un candidato. En lugar de votar solo por su primera opción, pueden clasificar a los candidatos en orden de preferencia. Por lo tanto, las papeletas resultantes podrían verse como las siguientes.

[!Cinco papeletas para votar con preferencias ordenadas](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_1.png)

Aquí, cada votante, además de especificar su candidato de primera preferencia, también ha indicado sus segunda y tercera opciones. Y ahora, lo que antes era una elección empatada podría tener un ganador. La carrera originalmente estaba empatada entre Alice y Bob, por lo que Charlie estaba fuera de la contienda. Pero el votante que eligió a Charlie prefirió a Alice sobre Bob, por lo que Alice podría ser declarada ganadora aquí.

También el voto por orden de preferencia puede resolver otro posible inconveniente del voto por mayoría relativa. Echa un vistazo a las siguientes papeletas.

[!Nueve papeletas para votar con preferencias ordenadas](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_3.png)

¿Quién debería ganar esta elección? En una votación por mayoría en la que cada votante elige solo su primera preferencia, Charlie gana esta elección con cuatro votos en comparación con solo tres para Bob y dos para Alice. Pero la mayoría de los votantes (5 de los 9) estarían más contentos con Alice o Bob en lugar de Charlie. Al considerar las preferencias ordenadas, un sistema de votación puede elegir un ganador que refleje mejor las preferencias de los votantes.

Uno de esos sistemas de votación por orden de preferencia es el sistema de segunda vuelta instantánea. En una elección de segunda vuelta instantánea, los votantes pueden calificar a tantos candidatos como deseen. Si algún candidato tiene la mayoría (más del 50%) de los votos de primera preferencia, ese candidato es declarado ganador de la elección.

Si ningún candidato obtiene más del 50% de los votos, se produce una "segunda vuelta instantánea". El candidato que recibió el menor número de votos es eliminado de la elección, y cualquiera que originalmente eligiera a ese candidato como su primera preferencia ahora tiene su segunda preferencia considerada. ¿Por qué hacerlo de esta manera? Efectivamente, esto simula lo que habría sucedido si el candidato menos popular no hubiera estado en la elección para empezar.

El proceso se repite: si ningún candidato tiene mayoría de los votos, se elimina el candidato del último lugar y cualquiera que haya votado por él votará en su lugar por su próxima preferencia (que no haya sido eliminada). Una vez que un candidato obtiene la mayoría, ese candidato es declarado ganador.

Suena un poco más complicado que un voto por mayoría relativa, ¿no es así? Pero podría decirse que tiene la ventaja de ser un sistema electoral en el que el ganador de la elección representa con mayor precisión las preferencias de los votantes. En un archivo llamado `runoff.c` en una carpeta llamada `runoff`, crea un programa para simular una elección de segunda vuelta.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-4rhSKgaZQsY93RLj0xgu7nwKB" src="https://asciinema.org/a/4rhSKgaZQsY93RLj0xgu7nwKB.js"></script>

## Código de distribución

### Descarga el código de distribución

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en la ventana del terminal y ejecuta `cd` solo. Deberías encontrar que el mensaje de la ventana de tu terminal se asemeja al siguiente:

    $

A continuación, ejecuta

    wget https://cdn.cs50.net/2023/fall/psets/3/runoff.zip

para descargar un ZIP llamado `runoff.zip` en tu espacio de códigos.

Luego ejecuta

    unzip runoff.zip

para crear una carpeta llamada `runoff`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm runoff.zip

y responder con "y" seguido de Entrar en el mensaje para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd runoff

seguido de Enter para moverte a ese directorio (es decir, abrirlo). Tu mensaje ahora debería parecerse al siguiente.

    runoff/ $

Si todo salió bien, debes ejecutar

    ls

y ver un archivo llamado `runoff.c`. Al ejecutar `code runoff.c` debería abrirse el archivo donde escribirás tu código para este conjunto de problemas. Si no, vuelve sobre tus pasos y mira si puedes determinar en qué te equivocaste.

### Comprenda el código en `runoff.c`

Siempre que extienda la funcionalidad del código existente, es mejor asegurarse de comprenderlo primero en su estado actual.

Mire primero la parte superior de `runoff.c`. Se definen dos constantes: `MAX_CANDIDATES` para el número máximo de candidatos en las elecciones y `MAX_VOTERS` para el número máximo de votantes en las elecciones.

    // Máximo de votantes y candidatos
    #define MAX_VOTERS 100
    #define MAX_CANDIDATES 9

Tenga en cuenta que` MAX_CANDIDATES `se utiliza para dimensionar una matriz,` candidatos `.

    // Matriz de candidatos
    candidate candidates[MAX_CANDIDATES];

`candidates` es un array de `candidate`s. En `runoff.c` un `candidate` es un `struct`. Cada `candidato` tiene un campo `string` para su `name`, un `int` que representa el número de `votes` que tienen actualmente y un valor `bool` llamado `eliminated` que indica si el candidato ha sido eliminado de las elecciones. El array `candidates` hará un seguimiento de todos los candidatos en las elecciones.

    // Los candidatos tienen nombre, recuento de votos, estado eliminado
    typedef struct
    {
        string name;
        int votes;
        bool eliminated;
    }
    candidate;

Ahora puede comprender mejor `preferences`, la matriz bidimensional. La matriz `preferences[i]` representará todas las preferencias para el votante número `i`. El entero, `preferences[i][j]`, almacenará el índice del candidato, de la matriz `candidates`, que es la preferencia `j` del votante `i`.

    // preferences[i][j] es la j-ésima preferencia para el votante i
    int preferences[MAX_VOTERS][MAX_CANDIDATES];

El programa también tiene dos variables globales: `voter_count` y `candidate_count`.

    // Número de votantes y candidatos
    int voter_count;
    int candidate_count;

Ahora en `main`. Tenga en cuenta que después de determinar la cantidad de candidatos y la cantidad de votantes, comienza el ciclo de votación principal, dando a cada votante la oportunidad de votar. A medida que el votante ingresa sus preferencias, se llama a la función `vote` para realizar un seguimiento de todas las preferencias. Si en algún momento la boleta se considera inválida, el programa finaliza.

Una vez que se han emitido todos los votos, comienza otro ciclo: este seguirá repitiéndose a través del proceso de segunda vuelta de verificación de un ganador y eliminación del candidato del último lugar hasta que haya un ganador.

La primera llamada aquí es a una función llamada `tabulate`, que debería observar todas las preferencias de los votantes y calcular los totales de votos actuales, mirando al candidato de primera opción de cada votante que aún no ha sido eliminado. A continuación, la función `print_winner` debe imprimir al ganador si lo hay; si lo hay, el programa ha terminado. Pero de lo contrario, el programa debe determinar la menor cantidad de votos que recibió cualquier persona aún en las elecciones (mediante una llamada a `find_min`). Si resulta que todos en las elecciones están empatados con el mismo número de votos (como lo determina la función `is_tie`), las elecciones se declaran empatadas; de lo contrario, el candidato o candidatos del último lugar son eliminados de las elecciones mediante una llamada a la función `eliminate`.

Si observa un poco más abajo en el archivo, verá que el resto de las funciones (`vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` y `eliminate`) quedan a su criterio para completar. **No debe modificar nada más en `runoff.c` (y la inclusión de archivos de encabezado adicionales, si lo desea).**

## Consejos

### Complete la función `vote`

- La función toma tres argumentos: `voter`, `rank` y `name`.
- Si `name` coincide con el nombre de un candidato válido, entonces debe actualizar la matriz de preferencias global para indicar que el votante `voter` tiene ese candidato como su preferencia `rank`. Tenga en cuenta que `0` es la primera preferencia, `1` es la segunda preferencia, etc. Puede suponer que no hay dos candidatos con el mismo nombre.
- Si la preferencia se registra correctamente, la función debe devolver `true`. De lo contrario, la función debería devolver `false`. Considere, por ejemplo, cuando` name `no es el nombre de uno de los candidatos.

Mientras escribe su código, considere estas sugerencias:

- Recuerde que` candidate_count` almacena el número de candidatos en las elecciones.
- Recuerde que puede usar [`strcmp`](https://man.cs50.io/3/strcmp) para comparar dos cadenas.
- Recuerde que` preferences[i][j] `almacena el índice del candidato que es la preferencia clasificada `j` para el `i`º votante.

### Completa la función `tabulate`

- La función debe actualizar el número de `votos` que cada candidato tiene en esta etapa de la segunda vuelta.
- Recuerda que en cada etapa de la segunda vuelta, cada votante vota efectivamente por su candidato favorito que aún no ha sido eliminado.

Mientras escribes tu código, considera estas pistas:

- Recuerda que `voter_count` almacena el número de votantes en la elección y que, para cada votante en nuestra elección, queremos contar una boleta.
- Recuerda que para un votante `i`, su candidato preferido es representado por `preferences[i][0]`, su candidato de segunda preferencia por `preferences[i][1]`, etc.
- Recuerda que la `struct` `candidate` tiene un campo llamado `eliminated`, que será `true` si el candidato ha sido eliminado de la elección.
- Recuerda que la `struct` `candidate` tiene un campo llamado `votes`, que probablemente querrás actualizar para el candidato preferido de cada votante.
- Recuerda que una vez que has emitido un voto para el primer candidato no eliminado de un votante, querrás parar ahí, no continuar con su boleta. Puedes salir de un ciclo antes de tiempo usando `break` dentro de un condicional.

### Completa la función `print_winner`

- Si algún candidato tiene más de la mitad de los votos, su nombre debe imprimirse y la función debe devolver `true`.
- Si nadie ha ganado la elección todavía, la función debe devolver `false`.

Mientras escribes tu código, considera esta pista:

- Recuerda que `voter_count` almacena el número de votantes en la elección. Dado esto, ¿cómo expresarías el número de votos necesarios para ganar la elección?

### Completa la función `find_min`

- La función debe devolver el total de votos mínimo para cualquier candidato que aún esté en la elección.

Mientras escribes tu código, considera esta pista:

- Probablemente querrás recorrer los candidatos para encontrar el que todavía está en la elección y tiene el menor número de votos. ¿Qué información debes llevar un registro mientras recorres los candidatos?

### Completa la función `is_tie`

- La función toma un argumento `min`, que será el número mínimo de votos que cualquiera en la elección tiene actualmente.
- La función debe devolver `true` si todos los candidatos que quedan en la elección tienen el mismo número de votos, y debe devolver `false` de lo contrario.

Mientras escribes tu código, considera esta pista:

- Recuerda que un empate ocurre si todos los candidatos aún en la elección tienen el mismo número de votos. Ten en cuenta también que la función `is_tie` toma un argumento `min`, que es el menor número de votos que cualquier candidato tiene actualmente. ¿Cómo podrías usar `min` para determinar si la elección es un empate (o, por el contrario, no un empate)?

### Completa la función `eliminate`

- La función toma un argumento `min`, que será el número mínimo de votos que cualquiera en la elección tiene actualmente.
- La función debe eliminar al candidato (o candidatos) que tienen `min` número de votos.

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar

Asegúrate de probar tu código para asegurarte de que maneja…

- Una elección con cualquier número de candidatos (hasta el `MAX` de `9`)
- Votar por un candidato por su nombre
- Votos inválidos para candidatos que no están en la boleta
- Imprimir el ganador de la elección si solo hay uno
- No eliminar a nadie en el caso de un empate entre todos los candidatos restantes

### Corrección

    check50 cs50/problems/2024/x/runoff

### Estilo

    style50 runoff.c

## Cómo enviar

    submit50 cs50/problems/2024/x/runoff

