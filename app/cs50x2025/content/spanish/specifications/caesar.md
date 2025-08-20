# César

![Cifrado César](https://cs50.harvard.edu/x/2024/psets/2/caesar/cipher.jpg)

## Problema a Resolver

Supuestamente, César (sí, ese César) solía "cifrar" (es decir, ocultar de forma reversible) mensajes confidenciales desplazando cada letra dentro del mensaje un cierto número de posiciones. Por ejemplo, podría escribir la A como B, la B como C, la C como D, ..., y regresando alfabéticamente, la Z como A. Por tanto, para decirle HOLAb a alguien, César podría escribir en su lugar IFMMP. Al recibir este tipo de mensajes de César, los destinatarios deberían "descifrarlos" desplazando las letras en la dirección opuesta el mismo número de posiciones.

La confidencialidad de este "criptosistema" dependía de que sólo César y los destinatarios conocieran un secreto, el número de posiciones que César había desplazado sus letras (por ejemplo, 1). No es particularmente seguro para los estándares modernos, pero, ¡oye!, si eres quizás el primero en el mundo en hacerlo, ¡bastante seguro!

El texto sin cifrar se llama generalmente _texto plano_. El texto cifrado se llama generalmente _texto cifrado_. Y el secreto utilizado se llama _clave_.

Para ser claros, a continuación, te mostramos cómo al cifrar `HOLAb` con una clave de \\(1\\) produce `IFMMP`:

| texto plano    | `H`     | `O`     | `L`     | `A`     | `b`     |
| ------------ | ------- | ------- | ------- | ------- | ------- |
| + clave       | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) |
| = texto cifrado | `I`     | `F`     | `M`     | `M`     | `P`     |

Más formalmente, el algoritmo (es decir, cifrado) de César cifra mensajes "rotando" cada letra \\(k\\) posiciones. Más formalmente, si \\(p\\) es un texto plano (es decir, un mensaje sin cifrar), \\(p_i\\) es el \\(i^{ésimo}\\) carácter en \\(p\\), y \\(k\\) es una clave secreta (es decir, un entero no negativo), entonces cada letra, \\(c_i\\), en el texto cifrado, \\(c\\), se calcula como

\\\[c_i = (p_i + k)\\space\\%\\space26\\\]

donde \\(\\%\\space26\\) aquí significa "resto al dividir entre 26." Esta fórmula quizás hace que el cifrado parezca más complicado de lo que es, pero es realmente sólo una forma concisa de expresar el algoritmo con precisión. De hecho, para fines de discusión, piensa en la A (o a) como \\(0\\), la B (o b) como \\(1\\), ... la H (o h) como \\(7\\), la I (o i) como \\(8\\), ... y la Z (o z) como \\(25\\). Supongamos que César sólo quiere decirle `Hola` a alguien confidencialmente usando, esta vez, una clave, \\(k\\), de 3. Por tanto, su texto plano, \\(p\\), es `Hola`, en cuyo caso el primer carácter de su texto plano, \\(p_0\\), es `H` (también conocida como 7), y el segundo carácter de su texto plano, \\(p_1\\), es `o` (también conocida como 14). El primer carácter de su texto cifrado, \\(c_0\\), es por tanto `K`, y el segundo carácter de su texto cifrado, \\(c_1\\), es por tanto `r`. ¿Tiene sentido?

En un archivo llamado `caesar.c` en una carpeta llamada `caesar`, escribe un programa que te permita cifrar mensajes utilizando el cifrado de César. En el momento en que el usuario ejecute el programa, debe decidir, proporcionando un argumento de línea de comandos, cuál debe ser la clave en el mensaje secreto que proporcionará en tiempo de ejecución. No debemos asumir necesariamente que la clave del usuario será un número; aunque puedes asumir que, si es un número, será un entero positivo.

## Demostración

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script>

## Especificación

Diseña e implementa un programa, `caesar`, que cifra mensajes utilizando el cifrado de César.

- Implementa tu programa en un archivo llamado `caesar.c` en un directorio llamado `caesar`.
- Tu programa debe aceptar un solo argumento de línea de comandos, un entero no negativo. Llamémoslo \\(k\\) para fines de discusión.
- Si tu programa se ejecuta sin ningún argumento de línea de comandos o con más de un argumento de línea de comandos, tu programa debe imprimir un mensaje de error de tu elección (con `printf`) y devolver desde `main` un valor de `1` (que tiende a significar un error) inmediatamente.
- Si alguno de los caracteres del argumento de la línea de comandos no es un dígito decimal, tu programa debe imprimir el mensaje `Uso: ./caesar clave` y devolver desde `main` un valor de `1`.
- No asumas que \\(k\\) será menor o igual que 26. Tu programa debe funcionar para todos los valores enteros integrales no negativos de \\(k\\) menores que \\(2^{31} - 26\\). En otras palabras, no necesitas preocuparte si tu programa eventualmente se rompe si el usuario elige un valor para \\(k\\) que sea demasiado grande o casi demasiado grande para caber en un `int`. (Recuerda que un `int` puede desbordarse.) Pero, incluso si \\(k\\) es mayor que \\(26\\), los caracteres alfabéticos en la entrada de tu programa deben seguir siendo caracteres alfabéticos en la salida de tu programa. Por ejemplo, si \\(k\\) es \\(27\\), `A` no debe convertirse en `\` incluso si `\` está a \\(27\\) posiciones de `A` en ASCII, según [asciitable.com](https://www.asciitable.com/); `A` debe convertirse en `B`, ya que `B` está a \\(27\\) posiciones de `A`, siempre que regreses de la `Z` a la `A`.
- Tu programa debe generar `plaintext:` (con dos espacios pero sin una nueva línea) y luego solicitar al usuario una `cadena` de texto plano (usando `get_string`).
- Tu programa debe generar `ciphertext:` (con un espacio pero sin una nueva línea) seguido del texto cifrado correspondiente del texto plano, con cada carácter alfabético en el texto plano "rotado" \\(k\\) posiciones; Los caracteres no alfabéticos deben emitirse sin cambios.
- Tu programa debe conservar las mayúsculas y minúsculas: las letras mayúsculas, aunque rotadas, deben seguir siendo mayúsculas; Las letras minúsculas, aunque rotadas, deben seguir siendo minúsculas.
- Después de generar texto cifrado, debes imprimir una nueva línea. Tu programa debe salir devolviendo `0` desde `main`.

## Consejo

¿Cómo empezar? Abordemos este problema paso a paso.

### Pseudocódigo

Primero escribe, intenta escribir una función `main` en `caesar.c` que implemente el programa usando sólo pseudocódigo, incluso si no estás (¡aún!) seguro de cómo escribirlo en el código real.

¡Hay más de una forma de hacer esto, así que aquí tienes sólo una!

    int main(int argc, string argv[])
    {
        // Asegúrate de que el programa se ejecutó con un solo argumento de línea de comandos

        // Asegúrate de que cada carácter en argv[1] sea un dígito

        // Convierte argv[1] de una `cadena` a un `int`

        // Pídele al usuario el texto plano

        // Para cada carácter en el texto plano:

            // Rota el carácter si es una letra
    }

¡Está bien editar tu propio pseudocódigo después de ver el nuestro aquí, pero no simplemente copies/pegues el nuestro en el tuyo!

### Conteo de argumentos de línea de comandos

Independientemente de tu pseudocódigo, primero escribamos solo el código C que verifica si el programa se ejecutó con un único argumento de línea de comandos antes de agregar funcionalidad adicional.

Específicamente, modifica `main` en `caesar.c` de tal manera que, si el usuario no proporciona ningún argumento de línea de comandos, o dos o más, la función imprima `"Uso: ./caesar clave\n"` y luego devuelva `1`, saliendo efectivamente del programa. Si el usuario proporciona exactamente un argumento de línea de comandos, el programa no debe imprimir nada y simplemente devolver `0`. Por lo tanto, el programa debe comportarse según lo siguiente.

    $ ./caesar
    Uso: ./caesar clave


    $ ./caesar 1 2 3
    Uso: ./caesar clave


    $ ./caesar 1

#### Sugerencias

- Recuerda que puedes imprimir con `printf`.
- Recuerda que una función puede devolver un valor con `return`.
- Recuerda que `argc` contiene el número de argumentos de línea de comandos pasados a un programa, más el propio nombre del programa.

### Verificación de la clave

Ahora que tu programa (¡con suerte!) está aceptando la entrada como se prescribe, es hora de dar otro paso.

Agrega a `caesar.c`, debajo de `main`, una función llamada, por ejemplo, `only_digits` que tome una `cadena` como argumento y devuelva `true` si esa `cadena` contiene solo dígitos, del `0` al `9`, de lo contrario devuelve `false`. Asegúrate de agregar también el prototipo de la función sobre `main`.

#### Sugerencias

- Lo más probable es que quieras un prototipo como:
  bool only_digits(string s);

  Y asegúrate de incluir `cs50.h` en la parte superior de tu archivo, para que el compilador reconozca `string` (y `bool`).

- Recuerda que una `cadena` es solo una matriz de `char`.
- Recuerda que `strlen`, declarado en `string.h`, calcula la longitud de una `cadena`.
- Es posible que encuentres útil `isdigit`, declarado en `ctype.h`, según [manual.cs50.io](https://manual.cs50.io/). ¡Pero ten en cuenta que solo verifica un `char` a la vez!

Luego modifica `main` de tal manera que llame a `only_digits` en `argv[1]`. Si esa función devuelve `false`, entonces `main` debe imprimir `"Uso: ./caesar clave\n"` y devolver `1`. De lo contrario, `main` simplemente debe devolver `0`. Por lo tanto, el programa debe comportarse según lo siguiente:

    $ ./caesar 42


    $ ./caesar plátano
    Uso: ./caesar clave

### Uso de la clave

Ahora modifica `main` de tal manera que convierta `argv[1]` a un `int`. Es posible que encuentres útil `atoi`, declarado en `stdlib.h`, según [manual.cs50.io](https://manual.cs50.io/). Y luego usa `get_string` para solicitar al usuario un texto sin formato con `"texto sin formato: "`.

Luego, implementa una función llamada, por ejemplo, `rotate`, que tome un `char` como entrada y también un `int`, y gire ese `char` en esa cantidad de posiciones si es una letra (es decir, alfabético), envolviendo desde `Z` a `A` (y desde `z` a `a`) según sea necesario. Si el `char` no es una letra, la función debería devolver el mismo `char` sin cambios.

#### Sugerencias

- Lo más probable es que quieras un prototipo como:
  char rotate(char c, int n);

  Una llamada a función como
  rotate('A', 1)

  o incluso
  rotate('A', 27)

  debe devolver `'B'`. Y una llamada a función como
  rotate('!', 13)

  debe devolver `'!'`.

- Recuerda que puedes "convertir" explícitamente un `char` a un `int` con `(int)` y un `int` a un `char` con `(char)`. O puedes hacerlo implícitamente simplemente tratando uno como el otro.
- Lo más probable es que quieras restar el valor ASCII de `'A'` de todas las letras mayúsculas, para tratar `'A'` como `0`, `'B'` como `1`, etc., mientras realizas operaciones aritméticas. Y luego agrégalo de nuevo cuando termines con el mismo.
- Lo más probable es que quieras restar el valor ASCII de `'a'` de todas las letras minúsculas, para tratar `'a'` como `0`, `'b'` como `1`, etc., mientras realizas operaciones aritméticas. Y luego agrégalo de nuevo cuando termines con el mismo.
- Es posible que encuentres útiles algunas otras funciones declaradas en `ctype.h`, según [manual.cs50.io](https://manual.cs50.io/).
- Lo más probable es que encuentres `%` útil cuando "envuelvas" aritméticamente de un valor como `25` a `0`.

Luego modifica `main` de tal manera que imprima `"texto cifrado: "` y luego itere sobre cada `char` en el texto sin formato del usuario, llamando a `rotate` en cada uno e imprimiendo el valor de retorno del mismo.

#### Sugerencias

- Recuerda que `printf` puede imprimir un `char` usando `%c`.
- Si no ves ninguna salida cuando llamas a `printf`, lo más probable es que se deba a que estás imprimiendo caracteres fuera del rango ASCII válido de 0 a 127. ¡Intenta imprimir caracteres temporalmente como números (usando `%i` en lugar de `%c`) para ver qué valores estás imprimiendo!

## Tutorial

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Cómo probar

### Corrección

En tu terminal, ejecuta lo siguiente para verificar la corrección de tu trabajo.

    check50 cs50/problems/2024/x/caesar

#### Cómo usar `debug50`

¿Buscas ejecutar `debug50`? Puedes hacerlo de la siguiente manera, después de compilar tu código correctamente con `make`,

    debug50 ./caesar KEY

donde `KEY` es la clave que proporcionas como argumento de línea de comandos para tu programa. Tenga en cuenta que ejecutar

    debug50 ./caesar

(idealmente) hará que tu programa se cierre al solicitarle al usuario una clave.

### Estilo

Ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

    style50 caesar.c

## Cómo enviar

En tu terminal, ejecuta lo siguiente para enviar tu trabajo.

    submit50 cs50/problems/2024/x/caesar

