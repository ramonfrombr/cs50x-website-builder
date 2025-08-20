# César

![Criptografia de César](https://cs50.harvard.edu/x/2024/psets/2/caesar/cipher.jpg)

## Problema a resolver

Supostamente, César (sim, aquele César) costumava "criptografar" (ou seja, ocultar de forma reversível) mensagens confidenciais mudando cada letra por alguns lugares. Por exemplo, ele poderia escrever A como B, B como C, C como D, ..., e, voltando ao começo do alfabeto, Z como A. Então, para dizer OLÁ para alguém, César poderia escrever IFMMP. Ao receberem essas mensagens de César, os destinatários precisariam "descriptografá-las" mudando as letras na direção oposta pelo mesmo número de lugares.

A segurança desse "criptossistema" dependia apenas de César e dos destinatários conhecerem um segredo, o número de lugares em que César havia mudado suas letras (por exemplo, 1). Não é particularmente seguro para os padrões modernos, mas, ei, se você é talvez o primeiro no mundo a fazê-lo, é bem seguro!

O texto não criptografado é geralmente chamado de _texto simples_. O texto criptografado é geralmente chamado de _texto cifrado_. E o segredo usado é chamado de _chave_.

Para esclarecer, aqui está como criptografar `OLÁ` com uma chave de \\(1\\) resulta em `IFMMP`:

| texto simples    | `H`     | `E`     | `L`     | `L`     | `O`     |
| ------------ | ------- | ------- | ------- | ------- | ------- |
| \+ chave       | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) |
| = texto cifrado | `I`     | `F`     | `M`     | `M`     | `P`     |

Mais formalmente, o algoritmo de César (ou seja, criptografia) criptografa mensagens "girando" cada letra em \\(k\\) posições. Mais formalmente, se \\(p\\) for um texto claro (ou seja, uma mensagem não criptografada), \\(p_i\\) for o \\(i^{th}\\) caractere em \\(p\\) e \\(k\\) for uma chave secreta (ou seja, um inteiro não negativo), então cada letra, \\(c_i\\), no texto cifrado, \\(c\\), é calculada como

\\\[c_i = (p_i + k)\\space\\%\\space26\\\]

em que \\(\\%\\space26\\) aqui significa "resto da divisão por 26." Essa fórmula talvez faça a criptografia parecer mais complicada do que é, mas é realmente apenas uma maneira concisa de expressar o algoritmo com precisão. Na verdade, para fins de discussão, pense em A (ou a) como \\(0\\), B (ou b) como \\(1\\), ... H (ou h) como \\(7\\), I (ou i) como \\(8\\), ... e Z (ou z) como \\(25\\). Suponha que César queira apenas dizer `Oi` para alguém confidencialmente usando, desta vez, uma chave, \\(k\\), de 3. Então, seu texto simples, \\(p\\), é `Oi`, caso em que o primeiro caractere do seu texto simples, \\(p_0\\), é `H` (também conhecido como 7), e o segundo caractere do seu texto simples, \\(p_1\\), é `i` (também conhecido como 8). O primeiro caractere do seu texto cifrado, \\(c_0\\), é, portanto, `K`, e o segundo caractere do seu texto cifrado, \\(c_1\\), é, portanto, `L`. Faz sentido?

Em um arquivo chamado `caesar.c` em uma pasta chamada `caesar`, escreva um programa que permita criptografar mensagens usando a criptografia de César. No momento em que o usuário executa o programa, ele deve decidir, fornecendo um argumento de linha de comando, qual deve ser a chave na mensagem secreta que ele fornecerá em tempo de execução. Não podemos necessariamente presumir que a chave do usuário será um número; embora você possa supor que, se for um número, será um inteiro positivo.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script>

## Especificação

Projete e implemente um programa, `caesar`, que criptografe mensagens usando a criptografia de César.

- Implemente seu programa em um arquivo chamado `caesar.c` em um diretório chamado `caesar`.
- Seu programa deve aceitar um único argumento de linha de comando, um inteiro não negativo. Vamos chamá-lo de \\(k\\) para fins de discussão.
- Se o seu programa for executado sem nenhum argumento de linha de comando ou com mais de um argumento de linha de comando, o seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor de `1` (que tende a significar um erro) imediatamente.
- Se algum dos caracteres do argumento da linha de comando não for um dígito decimal, seu programa deve imprimir a mensagem `Uso: ./caesar chave` e retornar de `main` um valor de `1`.
- Não presuma que \\(k\\) será menor ou igual a 26. Seu programa deve funcionar para todos os valores inteiros não negativos de \\(k\\) menores que \\(2^{31} - 26\\). Em outras palavras, você não precisa se preocupar se o seu programa eventualmente quebrará se o usuário escolher um valor para \\(k\\) muito grande ou quase muito grande para caber em um `int`. (Lembre-se de que um `int` pode transbordar.) Mas, mesmo que \\(k\\) seja maior que \\(26\\), os caracteres alfabéticos na entrada do seu programa devem permanecer caracteres alfabéticos na saída do seu programa. Por exemplo, se \\(k\\) for \\(27\\), `A` não deve se tornar `\` mesmo que `\` esteja em \\(27\\) posições de distância de `A` em ASCII, de acordo com [asciitable.com](https://www.asciitable.com/); `A` deve se tornar `B`, uma vez que `B` está em \\(27\\) posições de distância de `A`, desde que você alterne de `Z` para `A`.
- Seu programa deve produzir `texto simples:` (com dois espaços mas sem uma nova linha) e, em seguida, solicitar ao usuário uma `string` de texto simples (usando `get_string`).
- Seu programa deve produzir `texto cifrado:` (com um espaço mas sem uma nova linha) seguido pelo texto cifrado correspondente ao texto simples, com cada caractere alfabético no texto simples "girado" em _k_ posições; caracteres não alfabéticos devem ser produzidos inalterados.
- Seu programa deve preservar o caso: letras maiúsculas, embora giradas, devem permanecer letras maiúsculas; letras minúsculas, embora giradas, devem permanecer letras minúsculas.
- Depois de gerar o texto cifrado, você deve imprimir uma nova linha. Seu programa deve então sair retornando `0` de `main`.

## Conselhos

Como começar? Vamos abordar esse problema um passo de cada vez.

### Pseudocódigo

Primeiro escreva, tente escrever uma função `main` em `caesar.c` que implementa o programa usando apenas pseudocódigo, mesmo que (ainda!) não tenha certeza de como escrevê-la no código real.

Há mais de uma maneira de fazer isso, então aqui está apenas uma!

    int main(int argc, string argv[])
    {
        // Verifique se o programa foi executado com apenas um argumento de linha de comando

        // Verifique se cada caractere em argv[1] é um dígito

        // Converta argv[1] de uma `string` para uma `int`

        // Solicite ao usuário o texto simples

        // Para cada caractere no texto simples:

            // Gire o caractere se for uma letra
    }

Tudo bem editar seu próprio pseudocódigo depois de ver o nosso aqui, mas não simplesmente copie/cole o nosso no seu!

### Como contar argumentos da linha de comando

Seja qual for seu pseudocódigo, vamos primeiro escrever somente o código C que verifica se o programa foi executado com um único argumento da linha de comando antes de adicionar funcionalidade adicional.

Especificamente, modifique `main` em `caesar.c` de tal forma que, caso o usuário não forneça nenhum argumento da linha de comando, ou dois ou mais, a função imprima `"Uso: ./caesar key\n"` e retorne `1`, efetivamente saindo do programa. Caso o usuário forneça exatamente um argumento da linha de comando, o programa não deve imprimir nada e simplesmente retornar `0`. O programa deve, portanto, se comportar como abaixo.

    $ ./caesar
    Uso: ./caesar key


    $ ./caesar 1 2 3
    Uso: ./caesar key


    $ ./caesar 1

#### Dicas

- Lembre-se de que você pode imprimir com `printf`.
- Lembre-se de que uma função pode retornar um valor com `return`.
- Lembre-se de que `argc` contém o número de argumentos da linha de comando passados para um programa, além do nome do próprio programa.

### Verificando a chave

Agora que seu programa (esperamos!) está aceitando entrada conforme prescrito, é hora de uma outra etapa.

Adicione em `caesar.c`, abaixo de `main`, uma função chamada, por exemplo, `only_digits` que recebe uma `string` como argumento e retorna `true` se a `string` contiver apenas dígitos, de `0` a `9`, caso contrário, retorna `false`. Lembre-se de adicionar o protótipo da função acima de `main` também.

#### Dicas

- Parece que você vai precisar de um protótipo como:
  bool only_digits(string s);

  E não se esqueça de incluir `cs50.h` no início do arquivo, para que o compilador reconheça `string` (e `bool`).

- Lembre-se de que uma `string` é apenas um array de `char`s.
- Lembre-se de que `strlen`, declarada em `string.h`, calcula o tamanho de uma `string`.
- Você pode considerar útil usar `isdigit`, declarada em `ctype.h`, conforme [manual.cs50.io](https://manual.cs50.io/). Mas observe que ela verifica apenas um `char` por vez!

Em seguida, modifique `main` de tal forma que chame `only_digits` em `argv[1]`. Se a função retornar `false`, então `main` deve imprimir `"Uso: ./caesar key\n"` e retornar `1`. Caso contrário, `main` deve simplesmente retornar `0`. O programa deve, portanto, se comportar como abaixo:

    $ ./caesar 42


    $ ./caesar banana
    Uso: ./caesar key

### Usando a chave

Agora modifique `main` de tal forma que converta `argv[1]` para um `int`. Você pode considerar útil usar `atoi`, declarado em `stdlib.h`, conforme [manual.cs50.io](https://manual.cs50.io/). Em seguida, use `get_string` para solicitar ao usuário algum plaintext com `"plaintext: "`.

Em seguida, implemente uma função chamada, por exemplo, `rotate`, que recebe um `char` como entrada e também um `int`, e roda o `char` por tantas posições quanto o `int`, se for uma letra (ou seja, alfabética), retornando de volta de `Z` para `A` (e de `z` para `a`) conforme necessário. Se o `char` não for uma letra, a função deve retornar o mesmo `char` inalterado.

#### Dicas

- Parece que você vai precisar de um protótipo como:
  char rotate(char c, int n);

  Uma chamada de função como
  rotate('A', 1)

  ou até
  rotate('A', 27)

  deve retornar `'B'`. E uma chamada de função como
  rotate('!', 13)

  deve retornar `'!'`.

- Lembre-se de que você pode converter explicitamente um `char` para um `int` com `(int)` ou um `int` para um `char` com `(char)`. Ou você pode fazer isso implicitamente simplesmente tratando um como o outro.
- Parece que você vai precisar subtrair o valor ASCII de `'A'` de todas as letras maiúsculas, de forma a tratar `'A'` como `0`, `'B'` como `1` e assim por diante, enquanto executa operações aritméticas. E depois adicionar o valor novamente quando terminar.
- Parece que você vai precisar subtrair o valor ASCII de `'a'` de todas as letras minúsculas, de forma a tratar `'a'` como `0`, `'b'` como `1` e assim por diante, enquanto executa operações aritméticas. E depois adicionar o valor novamente quando terminar.
- Você pode considerar útil usar algumas outras funções declaradas em `ctype.h`, conforme [manual.cs50.io](https://manual.cs50.io/).
- Parece que você vai considerar `%` útil ao "retornar a zero" aritmeticamente de um valor como `25` para `0`.

Em seguida, modifique `main` de tal forma que imprima `"ciphertext: "` e então itere sobre cada `char` no plaintext do usuário, chamando `rotate` em cada um e imprimindo o valor de retorno.

#### Dicas

- Lembre-se de que `printf` pode imprimir um `char` usando `%c`.
- Se você não estiver vendo nenhuma saída quando chamar `printf`, provavelmente é porque você está imprimindo caracteres fora do intervalo ASCII válido de 0 a 127. Experimente imprimir caracteres temporariamente como números (usando `%i` em vez de `%c`) para ver quais valores você está imprimindo!

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

### Exatidão

Em seu terminal, execute o comando abaixo para verificar a exatidão do seu trabalho.

    check50 cs50/problems/2024/x/caesar

#### Como usar `debug50`

Quer executar `debug50`? Você pode fazer isso, após compilar seu código com sucesso com `make`, executando o comando:

    debug50 ./caesar KEY

onde `KEY` é a chave que você fornece como um argumento da linha de comando para seu programa. Observe que a execução de

    debug50 ./caesar

irá (idealmente!) encerrar seu programa solicitando uma chave ao usuário.

### Estilo

Execute o comando abaixo para avaliar o estilo do seu código usando `style50`.

    style50 caesar.c

## Como enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2024/x/caesar

