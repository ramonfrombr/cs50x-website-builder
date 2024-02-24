# Interpretador de Matemática

O Python já suporta operações matemáticas, onde _você_ pode escrever código para somar, subtrair, multiplicar ou dividir valores e até mesmo variáveis. Mas vamos escrever um programa que permite aos _usuários_ fazer cálculos matemáticos, mesmo sem conhecer Python.

Em um arquivo chamado `interpreter.py`, implemente um programa que solicita ao usuário uma expressão aritmética e, em seguida, calcula e exibe o resultado como um valor de ponto flutuante formatado para uma casa decimal. Assuma que a entrada do usuário será formatada como `x y z`, com um espaço entre `x` e `y` e um espaço entre `y` e `z, em que:

- `x` é um número inteiro
- `y` é `+`, `-`, `*` ou `/`
- `z` é um número inteiro

Por exemplo, se o usuário inserir `1 + 1`, seu programa deve exibir `2.0`. Assuma que, se `y` for `/`, então `z` não será `0`.

Observe que, assim como o `python` é um interpretador para Python, seu `interpreter.py` será um interpretador matemático!

Dicas

Lembre-se de que uma `str` possui vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluindo `split`, que separa uma `str` em uma sequência de valores, todos os quais podem ser atribuídos a variáveis de uma vez. Por exemplo, se `expressão` for uma `str` como `1 + 1`, então

    x, y, z = expression.split(" ")

vai atribuir `1` a `x`, `+` a `y` e `1` a `z`.

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd`. Você deverá ver que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir interpreter

para criar uma pasta chamada `interpreter` no seu espaço de códigos.

Depois, execute

    cd interpreter

para entrar nessa pasta. Agora, o prompt do seu terminal deve aparecer como `interpreter/ $`. Em seguida, você pode executar

    code interpreter.py

para criar um arquivo chamado `interpreter.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python interpreter.py`. Digite `1 + 1` e pressione Enter. Seu programa deve exibir:

      2.0

- Execute seu programa com `python interpreter.py`. Digite `2 - 3` e pressione Enter. Seu programa deve exibir:

      -1.0

- Execute seu programa com `python interpreter.py`. Digite `2 * 2` e pressione Enter. Seu programa deve exibir:

      4.0

- Execute seu programa com `python interpreter.py`. Digite `50 / 5` e pressione Enter. Seu programa deve exibir:

      10.0

Você pode executar o seguinte para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas não se esqueça de testar também por conta própria!

    check50 cs50/problems/2022/python/interpreter

Smileys verdes significam que seu programa passou no teste! Frownies vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` gera para ver a entrada que o `check50` forneceu ao seu programa, qual saída era esperada e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/interpreter
