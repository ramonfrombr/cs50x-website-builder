# Lista de Compras

Suponha que você tem o hábito de fazer uma lista de itens que precisa do supermercado.

Em um arquivo chamado `grocery.py`, implemente um programa que solicita ao usuário os itens, um por linha, até que o usuário insira control-d (que é uma maneira comum de encerrar a entrada em um programa). Em seguida, exiba a lista de compras do usuário em maiúsculas, ordenada alfabeticamente por item, prefixando cada linha com o número de vezes que o usuário inseriu esse item. Não é necessário pluralizar os itens. Trate a entrada do usuário de forma que não seja sensível a maiúsculas e minúsculas.

Dicas

- Note que você pode detectar quando o usuário inseriu control-d capturando um [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) com um código como:

      try:
          item = input()
      except EOFError:
          ...

- É provável que você queira armazenar sua lista de compras como um `dict`.
- Observe que um `dict` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), entre eles `get`, e suporta operações como:

      d[chave]

  e

      if chave in d:
          ...

  onde `d` é um `dict` e `chave` é uma `str`.

- Certifique-se de evitar ou capturar qualquer [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela do terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir grocery

para criar uma pasta chamada `grocery` no seu espaço de códigos.

Depois, execute

    cd grocery

para mudar de diretório para essa pasta. Você deverá ver seu prompt do terminal agora como `grocery/ $`. Agora você pode executar

    code grocery.py

para criar um arquivo chamado `grocery.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar manualmente o seu código:

- Execute seu programa com `python grocery.py`. Digite `manga` e pressione Enter, depois digite `morango` e pressione Enter e, em seguida, pressione control-d. Seu programa deve exibir:

      1 MANGA
      1 MORANGO

- Execute seu programa com `python grocery.py`. Digite `leite` e pressione Enter, depois digite `leite` novamente e pressione Enter e, em seguida, pressione control-d. Seu programa deve exibir:

      2 LEITE

- Execute seu programa com `python grocery.py`. Digite `tortilha` e pressione Enter, depois digite `batata doce` e pressione Enter e, em seguida, pressione control-d. Seu programa deve exibir:

      1 BATATA DOCE
      1 TORTILHA

Você pode executar o seguinte comando para verificar seu código usando o `check50`, um programa que a CS50 usará para testar seu código quando você o enviar. Mas não se esqueça de testá-lo você mesmo também!

    check50 cs50/problems/2022/python/grocery

Os sorrisos verdes significam que seu programa passou em um teste! As carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite o URL que o `check50` imprime para ver a entrada que o `check50` forneceu ao seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/grocery
