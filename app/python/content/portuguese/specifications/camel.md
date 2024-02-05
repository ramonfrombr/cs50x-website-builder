## CamelCase

![camel](1024px-CamelCase_new.svg.png)

Fonte: [en.wikipedia.org/wiki/Camel_case](https://en.wikipedia.org/wiki/Camel_case)

Em alguns idiomas, é comum usar [camel case](https://en.wikipedia.org/wiki/Camel_case) (também conhecido como "mixed case") para os nomes das variáveis quando esses nomes consistem em várias palavras, onde a primeira letra da primeira palavra é minúscula, mas a primeira letra de cada palavra subsequente é maiúscula. Por exemplo, enquanto uma variável para o nome de um usuário pode ser chamada de `nome`, uma variável para o primeiro nome de um usuário pode ser chamada de `primeiroNome`, e uma variável para o primeiro nome preferido de um usuário (por exemplo, apelido) pode ser chamada de `primeiroNomePreferido`.

Por outro lado, o Python [recomenda](https://peps.python.org/pep-0008/#function-and-variable-names) o [snake case](https://en.wikipedia.org/wiki/Snake_case), onde as palavras são separadas por underscores (`_`), com todas as letras em minúsculas. Por exemplo, as mesmas variáveis seriam chamadas de `nome`, `primeiro_nome` e `primeiro_nome_preferido`, respectivamente, em Python.

Em um arquivo chamado `camel.py`, implemente um programa que solicita ao usuário o nome de uma variável em camel case e imprime o nome correspondente em snake case. Assuma que a entrada do usuário estará em camel case.

Dicas

- Lembre-se de que uma `str` possui diversos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Assim como uma `list`, uma `str` é "iterável", o que significa que você pode iterar sobre cada um de seus caracteres em um loop. Por exemplo, se `s` é uma `str`, você pode imprimir cada um de seus caracteres, um de cada vez, com código como este:

      for c in s:
          print(c, end="")

## Demonstração

## Antes de começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você verá que o prompt da janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir camel

para criar uma pasta chamada `camel` em seu espaço de códigos.

Depois, execute

    cd camel

para entrar nessa pasta. Agora você verá o prompt do seu terminal como `camel/ $`. Agora você pode executar

    code camel.py

para criar um arquivo chamado `camel.py`, onde você escreverá o seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute o programa com `python camel.py`. Digite `name` e pressione Enter. Seu programa deve imprimir:

      name

- Execute o programa com `python camel.py`. Digite `firstName` e pressione Enter. Seu programa deve imprimir:

      first_name

- Execute o programa com `python camel.py`. Digite `preferredFirstName` e pressione Enter. Seu programa deve imprimir:

      preferred_first_name

Você também pode executar o código abaixo para verificar o seu programa usando o `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. Mas lembre-se de testá-lo também por conta própria!

    check50 cs50/problems/2022/python/camel

Emojis verdes significam que seu programa passou em um teste! Emojis vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` passou para o seu programa, a saída esperada e a saída real do seu programa.

## Como enviar

No seu terminal, execute o seguinte para enviar o seu trabalho.

    submit50 cs50/problemas/2022/python/camel
