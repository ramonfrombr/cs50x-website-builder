# Crédito

![Persona sosteniendo tarjetas de crédito](https://cs50.harvard.edu/x/2024/psets/1/credit/credit_cards.jpeg)

## Problema a resolver

Una tarjeta de crédito (o débito), por supuesto, es una tarjeta de plástico con la que se puede pagar por bienes y servicios. En dicha tarjeta se imprime un número que también se almacena en una base de datos en algún lugar, de modo que cuando se usa su tarjeta para comprar algo, el acreedor sabe a quién facturar. Hay muchas personas con tarjetas de crédito en este mundo, por lo que esos números son bastante largos: American Express usa números de 15 dígitos, MasterCard usa números de 16 dígitos y Visa usa números de 13 y 16 dígitos. Y esos son números decimales (del 0 al 9), no binarios, lo que significa, por ejemplo, ¡que American Express podría imprimir hasta 10^15 = 1,000,000,000,000,000 tarjetas únicas! (Eso es, ejem, un cuatrillón).

En realidad, eso es un poco exagerado, ya que los números de las tarjetas de crédito tienen estructura. Todos los números de American Express empiezan por 34 o 37; la mayoría de los números de MasterCard empiezan por 51, 52, 53, 54 o 55 (también tienen algunos otros números de inicio potenciales que no nos conciernen para este problema); y todos los números de Visa empiezan por 4. Pero los números de las tarjetas de crédito también tienen una "suma de comprobación" incorporada, una relación matemática entre al menos un número y otros. Esa suma de comprobación permite a los ordenadores (o a los humanos a los que les gustan las matemáticas) detectar errores tipográficos (por ejemplo, transposiciones), si no números fraudulentos, sin tener que hacer una consulta a una base de datos, que puede ser lenta. Por supuesto, un matemático deshonesto sin duda podría crear un número falso que, sin embargo, respete la restricción matemática, por lo que sigue siendo necesaria una búsqueda en la base de datos para realizar comprobaciones más rigurosas.

Implementa un programa en C en un archivo llamado `credit.c` en una carpeta llamada `credit` que compruebe la validez de un número de tarjeta de crédito determinado.

## Algoritmo de Luhn

Entonces, ¿cuál es la fórmula secreta? Bueno, la mayoría de las tarjetas usan un algoritmo inventado por Hans Peter Luhn de IBM. Según el algoritmo de Luhn, puedes determinar si el número de una tarjeta de crédito es (sintácticamente) válido de la siguiente manera:

1.  Multiplica cada dos dígitos por 2, empezando por el penúltimo dígito del número, y luego suma los dígitos de esos productos.
2.  Suma el total a la suma de los dígitos que no se han multiplicado por 2.
3.  Si el último dígito del total es 0 (o, dicho de forma más formal, si el total módulo 10 es congruente a 0), ¡el número es válido!

Es un poco confuso, así que probemos con un ejemplo con la Visa de David: 4003600000000014.

1.  Por el bien de la explicación, primero subrayemos cada dos dígitos, empezando por el penúltimo dígito del número:

4003600000000014

Vale, multipliquemos cada uno de los dígitos subrayados por 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

Eso nos da:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Ahora sumamos los dígitos de esos productos (es decir, no los productos en sí):

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2.  Ahora sumemos esa suma (13) a la suma de los dígitos que no se han multiplicado por 2 (empezando por el final):

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

3.  Sí, el último dígito de esa suma (20) es un 0, ¡así que la tarjeta de David es legítima!

Por lo tanto, validar números de tarjetas de crédito no es difícil, pero sí un poco tedioso a mano. Escribamos un programa.

## Detalles de la implementación

En el archivo llamado `credit.c` en el directorio `credit`, escribe un programa que le pide al usuario un número de tarjeta de crédito y luego informa (mediante `printf`) si es un número de tarjeta American Express, MasterCard o Visa válido, según las definiciones del formato de cada uno aquí. Para que podamos automatizar algunas pruebas de tu código, pedimos que la última línea de salida de tu programa sea `AMEX\n` o `MASTERCARD\n` o `VISA\n` o `INVALID\n`, nada más, nada menos. Por simplicidad, puedes suponer que la entrada del usuario será completamente numérica (es decir, sin guiones, como podría aparecer en una tarjeta real) y que no tendrá ceros a la izquierda. Pero no asumas que la entrada del usuario cabrá en un `int`. Es mejor usar `get_long` de la biblioteca de CS50 para obtener la entrada de los usuarios. (¿Por qué?)

Ten en cuenta el siguiente ejemplo representativo de cómo debería comportarse tu propio programa cuando se le proporciona un número de tarjeta de crédito válido (sin guiones).

    $ ./credit
    Number: 4003600000000014
    VISA

Ahora, `get_long` rechazará los guiones (y más) de todos modos:

    $ ./credit
    Number: 4003-6000-0000-0014
    Number: foo
    Number: 4003600000000014
    VISA

Pero depende de ti detectar las entradas que no son números de tarjetas de crédito (por ejemplo, un número de teléfono), aunque sean numéricas:

    $ ./credit
    Number: 6176292929
    INVALID

Prueba tu programa con un montón de entradas, tanto válidas como no válidas. (¡Sin duda lo haremos!) Aquí tienes [algunos números de tarjeta](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) que PayPal recomienda para realizar pruebas.

Si tu programa se comporta incorrectamente con algunas entradas (o no se compila en absoluto), ¡es hora de depurar!

### Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/dF7wNjsRBjI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Cómo probar tu código

También puedes ejecutar lo siguiente para evaluar la exactitud de tu código usando `check50`. ¡Pero asegúrate de compilarlo y probarlo tú mismo también!

### Corrección

En tu terminal, ejecuta lo siguiente para comprobar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/credit

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 credit.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/credit