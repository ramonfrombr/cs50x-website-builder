# Efectivo

![Monedas estadounidenses](https://cs50.harvard.edu/x/2024/psets/1/cash/coins.jpg)

## Problema a resolver

Supongamos que trabajas en una tienda y un cliente te da 1,00 $ (100 centavos) por unas golosinas que cuestan 0,50 $ (50 centavos). Necesitarás darle el "cambio", la cantidad sobrante después de pagar el coste de las golosinas. Al dar el cambio, es probable que quieras minimizar el número de monedas que entregas a cada cliente, ¡para no quedarte sin ellas (o molestar al cliente!). En un archivo llamado `cash.c` en una carpeta llamada `cash`, implementa un programa en C que imprima la cantidad mínima de monedas necesarias para dar el cambio de una cantidad determinada, en centavos, como en el siguiente ejemplo:

    Cambio adeudado: 25
    1

Pero pide al usuario un `int` mayor que 0, para que el programa funcione para cualquier cantidad de cambio:

    Cambio adeudado: 70
    4

Vuelve a pedir al usuario que introduzca un número, tantas veces como sea necesario, si su entrada no es mayor o igual que 0 (¡o si su entrada no es un `int` en absoluto!).

## Demostración

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-p6PlFqQgSWNWn4ggpIIaBOvIq" src="https://asciinema.org/a/p6PlFqQgSWNWn4ggpIIaBOvIq.js"></script>

## Algoritmos voraces

Afortunadamente, la informática ha proporcionado a los cajeros de todo el mundo formas de minimizar el número de monedas adeudadas: algoritmos voraces.

Según el Instituto Nacional de Normas y Tecnología (NIST), un algoritmo voraz es aquel "que siempre toma la mejor solución inmediata o local al encontrar una respuesta". Los algoritmos voraces encuentran la solución general u óptima global para algunos problemas de optimización, pero pueden encontrar soluciones menos que óptimas para algunos casos de otros problemas.

¿Qué significa todo eso? Bueno, supongamos que un cajero debe dar cambio a un cliente y en el cajón de ese cajero hay monedas de 25¢ (cuartos de dólar), 10¢ (monedas de diez centavos), 5¢ (níqueles) y 1¢ (peniques). El problema a resolver es decidir qué monedas y cuántas de cada una entregar al cliente. Piensa en un cajero "voraz" como alguien que quiere dar el bocado más grande posible a este problema con cada moneda que saca del cajón. Por ejemplo, si un cliente tiene que pagar 41¢, el bocado más grande (es decir, la mejor solución inmediata o local) que se puede dar es de 25¢. (Ese bocado es "mejor" en la medida en que nos acerca a 0¢ más rápido que cualquier otra moneda). Ten en cuenta que un bocado de este tamaño reduciría el problema de 41¢ a un problema de 16¢, ya que 41 - 25 = 16. Es decir, el resto es un problema similar pero más pequeño. No hace falta decir que otro bocado de 25¢ sería demasiado grande (asumiendo que el cajero prefiere no perder dinero), por lo que nuestro cajero voraz pasaría a un bocado de 10¢, dejándole un problema de 6¢. En ese momento, la voracidad pide un bocado de 5¢ seguido de un bocado de 1¢, momento en el que el problema está resuelto. El cliente recibe un cuarto de dólar, una moneda de diez centavos, un níquel y un centavo: cuatro monedas en total.

Resulta que este enfoque voraz (es decir, algoritmo) no sólo es óptimo localmente sino también globalmente para la moneda estadounidense (y también para la Unión Europea). Es decir, siempre que un cajero tenga suficientes monedas de cada tipo, este enfoque de mayor a menor proporcionará el menor número de monedas posible. ¿Cuántas? ¡Eso lo decides tú!

## Consejos

### Escribe código que sepas que se compilará

Aunque este programa no haga nada, ¡al menos debería compilarse con `make`!

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

Ten en cuenta que ahora has incluido `cs50.h` y `stdio.h`, dos "archivos de cabecera" que te darán acceso a funciones que podrían ayudarte a resolver este problema.

### Escribe pseudocódigo antes de escribir más código

Si no estás seguro de cómo resolver el problema en sí, divídelo en problemas más pequeños que probablemente puedas resolver primero. Por ejemplo, este problema es en realidad sólo un puñado de problemas:

1.  Pide al usuario el cambio adeudado, en centavos.
2.  Calcula cuántos _cuartos de dólar_ debes dar al cliente. Resta el valor de esos cuartos de dólar de los centavos.
3.  Calcula cuántas _monedas de diez centavos_ debes dar al cliente. Resta el valor de esas monedas de diez centavos de los centavos restantes.
4.  Calcula cuántos _níqueles_ debes dar al cliente. Resta el valor de esos níqueles de los centavos restantes.
5.  Calcula cuántos _peniques_ debes dar al cliente. Resta el valor de esos peniques de los centavos restantes.
6.  Suma el número de cuartos de dólar, monedas de diez centavos, níqueles y peniques utilizados.
7.  Imprime esa suma.

Este es el algoritmo voraz que puedes utilizar para resolver este problema, así que escribamos algo de pseudocódigo como comentarios para recordarte que hagas именно eso:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Pide al usuario el cambio adeudado, en centavos

        // Calcula cuántos cuartos de dólar debes dar al cliente
        // Resta el valor de esos cuartos de dólar de los centavos

        // Calcula cuántas monedas de diez centavos debes dar al cliente
        // Resta el valor de esas monedas de diez centavos de los centavos restantes

        // Calcula cuántos níqueles debes dar al cliente
        // Resta el valor de esos níqueles de los centavos restantes

        // Calcula cuántos peniques debes dar al cliente
        // Resta el valor de esos peniques de los centavos restantes

        // Suma el número de cuartos de dólar, monedas de diez centavos, níqueles y peniques utilizados
        // Imprime esa suma
    }

### Convertir el pseudocódigo a código

Primero, considera cómo podrías solicitar al usuario los centavos que se le deben. Recuerda que un bucle `do while` es útil cuando quieres hacer algo al menos una vez, y posiblemente una y otra vez, como en el siguiente ejemplo:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Solicita al usuario el cambio adeudado, en centavos
        int cents;
        do
        {
            cents = get_int("Cambio adeudado: ");
        }
        while (cents < 0);
    }

Es aconsejable parar aquí y generar tu programa. Prueba para asegurarte de que tu programa se compila y de que te vuelve a solicitar la información si introduces menos de 0 centavos (o si introduces una entrada como "gato").

A continuación, considera cómo calcular cuántas monedas de veinticinco centavos debes darle al cliente. Como estamos utilizando un algoritmo greedy, esta pregunta se convierte en "¿cuál es el _mayor_ número de monedas de veinticinco centavos que podrías darle?". _Podrías_ escribir una solución a este problema en tu función `main`. Pero, podría aclarar tu pensamiento escribir una nueva función: una llamada `calculate_quarters`. De esa manera, puedes centrarte mejor en la lógica para calcular las monedas de veinticinco centavos. Más tarde, puedes integrar esta función en tu solución más amplia.

    int calculate_quarters(int cents)
    {
        // Calcula cuántas monedas de veinticinco centavos debes darle al cliente
    }

Observa que esta función se llama `calculate_quarters`. Por `int cents` entre paréntesis, toma un `int` llamado `cents` como entrada. Y, por el `int` delante de su nombre, también debería "devolver" un `int`. Es decir, la salida de esta función es un entero: el número de monedas de veinticinco centavos que caben en centavos. Si tienes curiosidad sobre esta idea, recuerda que hay varios programas de muestra en el Código fuente de la Semana 1 [Source Code](https://github.com/cs50/lectures/tree/2023/fall/1/src1) que ilustran cómo las funciones pueden devolver un valor.

Ahora considera esta forma de implementar `calculate_quarters` sumando al número de cuartos hasta que nos quedemos sin centavos para convertir en cuartos:

    int calculate_quarters(int cents)
    {
        // Calcula cuántas monedas de veinticinco centavos debes darle al cliente
        int quarters = 0;
        while (cents >= 25)
        {
            quarters++;
            cents = cents - 25;
        }
        return quarters;
    }

Concedido, hay al menos una forma más sencilla de resolver este problema `calculate_quarters`. ¡Pero te dejaremos que lo descubras!

Con `calculate_quarters` funcionando según lo previsto, puedes integrar esta función en tu programa. Ten cuidado de "declarar" la "firma" de la función (es decir, `int calculate_quarters(int cents)`) encima de tu función `main`, para que puedas utilizar `calculate_quarters` allí mientras la defines más tarde, debajo de `main`.

    #include <cs50.h>
    #include <stdio.h>

    int calculate_quarters(int cents);

    int main(void)
    {
        // Solicita al usuario el cambio adeudado, en centavos
        int cents;
        do
        {
            cents = get_int("Cambio adeudado: ");
        }
        while (cents < 0);

        // Calcula cuántas monedas de veinticinco centavos debes darle al cliente
        int quarters = calculate_quarters(cents);

        // Resta el valor de esas monedas de veinticinco centavos de cents
        cents = cents - (quarters * 25);
    }

    int calculate_quarters(int cents)
    {
        // Calcula cuántas monedas de veinticinco centavos debes darle al cliente
        int quarters = 0;
        while (cents >= 25)
        {
            quarters++;
            cents = cents - 25;
        }
        return quarters;
    }

¡Algunos problemas resueltos y algunos más por resolver! ¿Observas un patrón que podrías reutilizar aquí?

## Cómo probar

Para este programa, intenta probar tu código manualmente. Es una buena práctica:

- Si introduces `-1`, ¿tu programa te vuelve a preguntar?
- Si introduces `0`, ¿tu programa muestra `0`?
- Si introduces `1`, ¿tu programa muestra `1` (es decir, un centavo)?
- Si introduces `4`, ¿tu programa muestra `4` (es decir, cuatro centavos)?
- Si introduces `5`, ¿tu programa muestra `1` (es decir, un níquel)?
- Si introduces `24`, ¿tu programa muestra `6` (es decir, dos monedas de diez centavos y cuatro centavos)?
- Si introduces `25`, ¿tu programa muestra `1` (es decir, una moneda de veinticinco centavos)?
- Si introduces `26`, ¿tu programa muestra `2` (es decir, una moneda de veinticinco centavos y un centavo)?
- Si introduces `99`, ¿tu programa muestra `9` (es decir, tres monedas de veinticinco centavos, dos monedas de diez centavos y cuatro centavos)?

### Corrección

En tu terminal, ejecuta el siguiente código para comprobar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/cash

### Estilo

Ejecuta el siguiente código para evaluar el estilo de tu código utilizando `style50`.

    style50 cash.c

## Cómo enviar

En tu terminal, ejecuta el siguiente código para enviar tu trabajo.

    submit50 cs50/problems/2024/x/cash

