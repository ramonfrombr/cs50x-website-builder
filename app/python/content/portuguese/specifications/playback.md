# Velocidade de Reprodução

Algumas pessoas têm o hábito de falar durante uma aula muito rapidamente, e seria bom diminuir a velocidade, como a velocidade de reprodução de 0.75 do YouTube, ou até mesmo pedir para que façam pausas entre as palavras.

Em um arquivo chamado `playback.py`, implemente um programa em Python que solicita a entrada do usuário e depois exibe essa mesma entrada, substituindo cada espaço por `...` (ou seja, três pontos).

Dicas

- Lembre-se de que `input` retorna uma `str`, conforme [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Lembre-se de que uma `str` possui diversos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deve ver que o seu prompt na janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir playback

para criar uma pasta chamada `playback` no seu ambiente de codificação.

Depois execute

    cd playback

para navegar até essa pasta. Agora o seu prompt de terminal deve aparecer como `playback/ $`. Você pode agora executar

    code playback.py

para criar um arquivo chamado `playback.py`, onde você irá escrever o seu programa.

## Como Testar

Veja como testar o seu código manualmente:

- Execute o seu programa com `python playback.py`. Digite `This is CS50` e pressione Enter. Seu programa deve exibir:

      This...is...CS50

- Execute o seu programa com `python playback.py`. Digite `This is our week on functions` e pressione Enter. Seu programa deve exibir:

      This...is...our...week...on...functions

- Execute o seu programa com `python playback.py`. Digite `Let's implement a function called hello` e pressione Enter. Seu programa deve exibir:

      Let's...implement...a...function...called...hello

Você pode executar o código abaixo para verificar o seu código usando o `check50`, um programa que o CS50 usará para testar o seu código quando você o enviar. Mas certifique-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/playback

Carinhas verdes indicam que o seu programa passou em um teste! Carinhas vermelhas indicarão que o seu programa produziu algo inesperado. Visite a URL que o `check50` mostrar para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída o seu programa realmente deu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/playback
