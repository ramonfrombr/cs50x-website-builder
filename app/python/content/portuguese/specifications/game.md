# Jogo de Adivinhação

Estou pensando em um número entre 1 e 100...

O que será?

É 50! Mas e se fosse mais aleatório?

Em um arquivo chamado `game.py`, implemente um programa que:

- Solicita ao usuário um nível, \\(n\\). Se o usuário não inserir um número inteiro positivo, o programa deve solicitar novamente.
- Gera aleatoriamente um número inteiro entre 1 e \\(n\\), inclusive, usando o módulo `random`.
- Solicita ao usuário para adivinhar esse inteiro. Se a suposição não for um número inteiro positivo, o programa deve solicitar ao usuário novamente.
  - Se a suposição for menor do que o inteiro, o programa deve exibir `Muito pequeno!` e solicitar ao usuário novamente.
  - Se a suposição for maior do que o inteiro, o programa deve exibir `Muito grande!` e solicitar ao usuário novamente.
  - Se a suposição for a mesma que o inteiro, o programa deve exibir `Acertou!` e sair.

Dicas

- Note que o módulo `random` possui várias funções, de acordo com [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir game

para criar uma pasta chamada `game` no seu espaço de códigos.

Depois execute

    cd game

para mudar para esse diretório. Agora você deve ver o prompt do terminal como `game/ $`. Você pode então executar

    code game.py

para criar um arquivo chamado `game.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python game.py`. Digite `cat` em um prompt que diz `Nível:` e pressione Enter. Seu programa deve solicitar novamente:

      Nível:

- Execute seu programa com `python game.py`. Digite `-1` em um prompt que diz `Nível:` e pressione Enter. Seu programa deve solicitar novamente:

      Nível:

- Execute seu programa com `python game.py`. Digite `10` em um prompt que diz `Nível:` e pressione Enter. Seu programa agora deve estar pronto para aceitar palpites:

      Palpite:

- Execute seu programa com `python game.py`. Digite `10` em um prompt que diz `Nível:` e pressione Enter. Em seguida, digite `cat`. Seu programa deve solicitar novamente:

      Palpite:

- Execute seu programa com `python game.py`. Digite `10` em um prompt que diz `Nível:` e pressione Enter. Em seguida, digite `-1`. Seu programa deve solicitar novamente:

      Palpite:

- Execute seu programa com `python game.py`. Digite `1` em um prompt que diz `Nível:` e pressione Enter. Em seguida, digite `1`. Seu programa deve exibir:

      Acertou!

  A resposta só pode ser um número!

- Execute seu programa com `python game.py`. Digite `10` em um prompt que diz `Nível:` e pressione Enter. Em seguida, digite `100`. Seu programa deve exibir:

      Muito grande!

  Parece que você está fazendo palpites fora da faixa que você especificou.

- Execute o seu programa com `python game.py`. Digite `10000` em um prompt que diz `Nível:` e pressione Enter. Em seguida, digite `1`. Seu programa deve exibir:

      Muito pequeno!

  Na maioria das vezes, no entanto, é mais provável: você pode ser sortudo e ver `Acertou!`. Mas certamente seria estranho ver `Acertou!` o tempo todo. E certamente você não deveria ver `Muito grande!`.

Você pode executar o código abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas lembre-se de testar também por conta própria!

    check50 cs50/problems/2022/python/game

Carinhas verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` mostra para ver a entrada que `check50` passou para o seu programa, qual saída era esperada e qual saída seu programa realmente forneceu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/game
