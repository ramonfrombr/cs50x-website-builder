# Banco de Poupança Doméstica

No [episódio 24 da temporada 7](https://pt.wikipedia.org/wiki/The_Invitations) de [Seinfeld](https://pt.wikipedia.org/wiki/Seinfeld), [Kramer](https://pt.wikipedia.org/wiki/Cosmo_Kramer) visita um banco que promete dar $100 a qualquer pessoa que não seja cumprimentada com um "olá". Kramer é cumprimentado com um "ei", ao invés de um "olá", e então ele pede $100. O gerente do banco propõe um acordo: "Você recebeu um cumprimento que começa com a letra "h", o que acha de $20?" Kramer aceita.

Em um arquivo chamado `bank.py`, implemente um programa que solicite ao usuário um cumprimento. Se o cumprimento começar com "olá", exiba `$0`. Se o cumprimento começar com a letra "h" (mas não for "olá"), exiba `$20`. Caso contrário, exiba `$100`. Ignore os espaços em branco no início do cumprimento do usuário e trate o cumprimento do usuário sem diferenciar maiúsculas e minúsculas.

Dicas:

- Lembre-se que uma `str` oferece vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Certifique-se de dar $0 não apenas para "olá", mas também para "olá, tudo bem?", "olá, Newman" e similares.

## Demonstração

## Antes de começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você verá que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir bank

para criar uma pasta chamada `bank` no seu ambiente de código.

Depois, execute

    cd bank

para entrar nessa pasta. Agora você verá o seu prompt do terminal como `bank/ $`. Agora você pode executar

    code bank.py

para criar um arquivo chamado `bank.py`, onde você escreverá seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o programa com `python bank.py`. Digite `Hello` e pressione Enter. Seu programa deve fornecer a seguinte saída:

      $0

- Execute o programa com `python bank.py`. Digite `Hello, Newman` e pressione Enter. Seu programa deve fornecer a seguinte saída:

      $0

- Execute o programa com `python bank.py`. Digite `How you doing?` e pressione Enter. Seu programa deve fornecer a seguinte saída:

      $20

- Execute o programa com `python bank.py`. Digite `What's happening?` e pressione Enter. Seu programa deve fornecer a seguinte saída:

      $100

Você pode executar o código abaixo para verificar o seu programa usando `check50`, um programa que a CS50 utilizará para testar o seu código quando você enviar. Mas certifique-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/bank

Smiles verdes significam que o seu programa passou em um teste! Carinhas tristes vermelhas indicarão que o seu programa produziu algo inesperado. Acesse a URL que o `check50` fornece para ver a entrada que o `check50` forneceu ao seu programa, qual saída ele esperava e qual saída o seu programa realmente deu.

## Como enviar

No seu terminal, execute o seguinte para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/bank
