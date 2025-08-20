## Guía de estilo para C

No existe una única forma correcta de diseñar códigos. Pero definitivamente hay muchas formas incorrectas (o al menos malas). Aun así, CS50 te pide que respetes las siguientes convenciones para que podamos analizar de forma confiable el estilo de tu código. De manera similar, las empresas suelen adoptar sus propias convenciones de estilo en toda la empresa.

## Longitud de línea

Por convención, la longitud máxima de una línea de código en C es de 80 caracteres, lo que históricamente se basa en monitores de tamaño estándar en terminales de computadora antiguos, que podían mostrar 24 líneas verticalmente y 80 caracteres horizontalmente. Aunque la tecnología moderna ha dejado obsoleta la necesidad de mantener las líneas con un máximo de 80 caracteres, sigue siendo una pauta que debe considerarse una "detención suave", y una línea de 100 caracteres realmente debería ser la más larga que escribas en C, de lo contrario, los lectores generalmente deberán desplazarse. Si necesitas más de 100 caracteres, ¡quizás sea hora de repensar tus nombres de variables o tu diseño general!

    // Estas siguientes líneas de código primero le piden al usuario que dé dos valores enteros y luego multiplica esos dos valores enteros para que puedan usarse más adelante en el programa
    int first_collected_integer_value_from_user = get_int("Integer please: ");
    int second_collected_integer_value_from_user = get_int("Another integer please: ");
    int product_of_the_two_integer_values_from_user = first_collected_integer_value_from_user * second_collected_integer_value_from_user;

En otros idiomas, particularmente JavaScript, es significativamente más difícil restringir las líneas a una longitud máxima; en cambio, tu objetivo debería ser dividir líneas (como mediante `\n`) en lugares que maximicen la legibilidad y claridad.

## Comentarios

Los comentarios hacen que el código sea más legible, no solo para otros (por ejemplo, tu TF) sino también para ti, especialmente cuando pasan horas, días, semanas, meses o años entre escribir y leer tu propio código. Comentar muy poco es malo. Comentar demasiado es malo. ¿Dónde está el punto óptimo? Comentar cada pocas líneas de código (es decir, bloques interesantes) es una pauta decente. Intenta escribir comentarios que aborden una o ambas de estas preguntas:

1. ¿Qué hace este bloque?
2. ¿Por qué implementé este bloque de esta manera?

Dentro de las funciones, usa "comentarios en línea" y mantenlos cortos (por ejemplo, una línea), de lo contrario, se vuelve difícil distinguir los comentarios del código, incluso con [resaltado de sintaxis](http://en.wikipedia.org/wiki/Syntax_highlighting). Coloca el comentario encima de las líneas a las que se aplica. No es necesario escribir oraciones completas, pero sí poner en mayúscula la primera palabra del comentario (a menos que sea el nombre de una función, variable o similar), y deja un espacio entre el `//` y el primer carácter de tu comentario, como en:

    // Convertir Fahrenheit a Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

En otras palabras, no hagas esto:

    //Convertir Fahrenheit a Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

O esto:

    // convertir Fahrenheit a Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

O esto:

    float c = 5.0 / 9.0 * (f - 32.0); // Convertir Fahrenheit a Celsius

En la parte superior de tus archivos .c y .h debe haber un comentario que resuma lo que hace tu programa (o ese archivo en particular), como:

    // Saluda al mundo

En la parte superior de cada una de tus funciones (excepto, quizás, `main`), mientras tanto, debe haber un comentario que resuma lo que está haciendo tu función, como:

    // Devuelve el cuadrado de n
    int square(int n)
    {
        return n * n;
    }

## Encabezados de biblioteca

Cualquier encabezado de biblioteca que incluyas debe aparecer en orden alfabético, como en:

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

Esto hace que sea más fácil ver de un vistazo, particularmente en una lista larga, si has incluido un encabezado.

## Condiciones

Las condiciones deben tener el siguiente estilo:

    if (x > 0)
    {
        printf("x es positivo\n");
    }
        else if (x < 0)
    {
        printf("x es negativo\n");
    }
    else
    {
        printf("x es cero\n");
    }

Observa cómo:

- las llaves se alinean muy bien, cada una en su propia línea, dejando muy claro lo que hay dentro de la rama;
- hay un solo espacio después de cada `if`;
- cada llamada a `printf` está sangrada con 4 espacios;
- hay espacios sencillos alrededor de `>` y alrededor de `<`; y
- no hay ningún espacio inmediatamente después de cada `(` o inmediatamente antes de cada `)`.

Para ahorrar espacio, a algunos programadores les gusta mantener las primeras llaves en la misma línea que la condición misma, pero no lo recomendamos, ya que es más difícil de leer, así que no hagas esto:

    if (x < 0) {
        printf("x es negativo\n");
    } else if (x < 0) {
        printf("x es negativo\n");
    }

Y definitivamente no hagas esto:

    if (x < 0)
        {
        printf("x es negativo\n");
        }
    else
        {
        printf("x es negativo\n");
        }

## Interruptores

Declara un `switch` de la siguiente manera:

    switch (n)
    {
        case -1:
            printf("n es -1\n");
            break;

        case 1:
            printf("n es 1\n");
            break;

        default:
            printf("n no es -1 ni 1\n");
            break;
    }

Observa cómo:

- cada llave está en su propia línea;
- hay un solo espacio después de `switch`;
- no hay ningún espacio inmediatamente después de cada `(` o inmediatamente antes de cada `)`;
- los casos del switch están sangrados con 4 espacios;
- los cuerpos de los casos están sangrados aún más con 4 espacios; y
- cada `case` (incluido `default`) termina con un `break`.

## Funciones

De acuerdo con [C99](http://en.wikipedia.org/wiki/C99), asegúrate de declarar `main` con:

    int main(void)
    {

    }

o, si utilizas la biblioteca CS50, con:

    #include <cs50.h>

    int main(int argc, string argv[])
    {

    }

o con:

    int main(int argc, char *argv[])
    {

    }

o incluso con:

    int main(int argc, char **argv)
    {

    }

No declares `main` con:

    int main()
    {

    }

o con:

    void main()
    {

    }

o con:

    main()
    {

    }

En cuanto a tus propias funciones, asegúrate de definirlas de manera similar, con cada llave en su propia línea y con el tipo de retorno en la misma línea que el nombre de la función, tal como lo hemos hecho con `main`.

## Sangría

Sangra tu código cuatro espacios a la vez para dejar en claro qué bloques de código están dentro de otros. Si usas la tecla Tab de tu teclado para hacerlo, asegúrate de que tu editor de texto esté configurado para convertir tabulaciones (`\t`) en cuatro espacios; de lo contrario, es posible que tu código no se imprima o muestre correctamente en la computadora de otra persona, ya que `\t` se representa de manera diferente en diferentes editores. (Si utilizas [CS50 IDE](https://ide.cs50.io/), puedes usar la tecla Tab para sangrar, en lugar de presionar la barra espaciadora de tu teclado repetidamente, ya que lo hemos preconfigurado para convertir `\t` en cuatro espacios.)

Aquí tienes un código bien sangrado:

    // Imprimir argumentos de línea de comandos uno por línea
    printf("\n");
    for (int i = 0; i < argc; i++)
    {
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            printf("%c\n", argv[i][j]);
        }
        printf("\n");
    }
## Bucles

### for

Cuando necesites variables temporales para iteraciones, utiliza `i`, luego `j`, después `k`, a menos que nombres más específicos hagan que el código sea legible:

    for (int i = 0; i < LIMIT; i++)
    {
        for (int j = 0; j < LIMIT; j++)
        {
            for (int k = 0; k < LIMIT; k++)
            {
                // Hacer algo
            }
        }
    }

¡Si necesitas más de tres variables para iteración, quizás sea hora de repensar el diseño!

### while

Declara a los bucles `while` como se hace a continuación:

    while (condition)
    {
        // Hacer algo
    }

Observa cómo:
- cada llave está en su propia línea;
- hay un único espacio después de `while`;
- no hay ningún espacio inmediatamente después del `(` o inmediatamente antes del `)`;
- el cuerpo del bucle (un comentario en este caso) tiene una sangría de 4 espacios.

### do … while

Declara a los bucles `do...while` como se hace a continuación:

    do
    {
        // Hacer algo
    }
    while (condition);

Observa cómo:

- cada llave está en su propia línea;
- hay un único espacio después de `while`;
- no hay ningún espacio inmediatamente después del `(` o inmediatamente antes del `)`;
- el cuerpo del bucle (un comentario en este caso) tiene una sangría de 4 espacios.

## Punteros

Cuando declares un puntero, escribe el `*` junto a la variable, como en:

    int *p;

No lo escribas junto al tipo, como en:

    int* p;

## Variables

Como CS50 utiliza [C99](http://en.wikipedia.org/wiki/C99), no definas todas las variables en la primera parte de las funciones, más bien hazlo cuando las necesites. Más aún, limita el alcance de las variables lo más posible. Por ejemplo, si `i` sólo es necesaria para un bucle, declara a `i` dentro del propio bucle:

    for (int i = 0; i < LIMIT; i++)
    {
        printf("%i\n", i);
    }

Aunque está bien utilizar variables como `i`, `j` y `k` para iteración, la mayoría de tus variables deberían tener nombres más específicos. Si estás sumando algunos valores, por ejemplo, llama a tu variable `sum` (suma). Si el nombre de tu variable requiere más de una palabra (p. ej., `is_ready`), coloca un guión bajo entre ellas, una convención popular en C aunque menos en otros lenguajes.

Si quieres declarar múltiples variables del mismo tipo a la vez, está bien si las declaras juntas, como en:

    int quarters, dimes, nickels, pennies;

Sólo no inicialices algunas y no otras, como en:

    int quarters, dimes = 0, nickels = 0 , pennies;

También ten cuidado de declarar punteros separándolos de los no punteros, como en:

    int *p;
    int n;

No declares punteros en la misma línea que los no punteros, como en:

    int *p, n;

## Estructuras

Declara un `struct` como tipo como se hace a continuación, con cada llave en su propia línea y los miembros en sangría, con el nombre del tipo también en su propia línea:

    typedef struct
    {
        string name;
        string dorm;
    }
    student;

Si el `struct` contiene como miembro un puntero a otro de dicho `struct`, declara al `struct` con un nombre idéntico al tipo, sin utilizar guiones bajos:

    typedef struct node
    {
        int n;
        struct node *next;
    }
    node;
