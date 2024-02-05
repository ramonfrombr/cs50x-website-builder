# Apenas configurando meu twttr

> apenas configurando meu twttr
>
> — jack⚡️ (@jack) [21 de março de 2006](https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw)

Quando enviamos mensagens de texto ou tweets, é comum abreviar palavras para economizar tempo ou espaço, como omitindo vogais, assim como o Twitter era originalmente chamado de _twttr_. Em um arquivo chamado `twttr.py`, implemente um programa que solicita ao usuário uma `str` de texto e depois exibe o mesmo texto, mas com todas as vogais (A, E, I, O e U) omitidas, independentemente de serem inseridas em maiúsculas ou minúsculas.

Dicas

- Lembre-se de que uma `str` vem com muitos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Assim como uma `list`, uma `str` é "iterável", o que significa que você pode iterar sobre cada um de seus caracteres em um loop. Por exemplo, se `s` é uma `str`, você pode imprimir cada um de seus caracteres, um por vez, com o seguinte código:

      for c in s:
          print(c, end="")

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver um prompt de terminal semelhante ao abaixo:

    $

Em seguida, execute

    mkdir twttr

para criar uma pasta chamada `twttr` em seu espaço de códigos.

Depois execute

    cd twttr

para entrar nessa pasta. Agora você deve ver seu prompt de terminal como `twttr/ $`. Você pode então executar

    code twttr.py

para criar um arquivo chamado `twttr.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python twttr.py`. Digite `Twitter` e pressione Enter. Seu programa deve exibir:

      Twttr

- Execute seu programa com `python twttr.py`. Digite `Qual é o seu nome?` e pressione Enter. Seu programa deve exibir:

      Ql é s sr nm?

- Execute seu programa com `python twttr.py`. Digite `CS50` e pressione Enter. Seu programa deve exibir

      CS50

Você pode executar o código abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Certifique-se de testá-lo também!

    check50 cs50/problems/2022/python/twttr

Smiles verdes significam que seu programa passou em um teste! Frownies vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` passou para seu programa, qual saída era esperada e qual saída seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/twttr
