# Felipe’s Taqueria

Observe que, a partir de [2023-10-25T11:59:00-04:00](https://time.cs50.io/20231025T115900-0400), os preços do Felipe foram atualizados!

![Felipe's Taqueria](felipes-logo.png)

Um dos lugares mais populares para comer no [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) é o [Felipe's Taqueria](https://www.felipesboston.com/), que oferece um [menu](https://www.felipesboston.com/menu) de pratos, conforme o `dicionário` abaixo, em que o valor de cada chave é um preço em dólares:

    {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

Em um arquivo chamado `taqueria.py`, implemente um programa que permita a um usuário fazer um pedido, solicitando itens, um por linha, até que o usuário entre com controle-d (que é uma maneira comum de encerrar a entrada para um programa). Após cada item inserido, exiba o custo total de todos os itens inseridos até o momento, prefixado com um cifrão (`$`) e formatado com duas casas decimais. Trate a entrada do usuário sem diferenciar maiúsculas de minúsculas. Ignore qualquer entrada que não seja um item. Assuma que cada item no menu estará em [titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).

Dicas

- Note que é possível detectar quando o usuário inseriu controle-d capturando um [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) com um código como:

      try:
          item = input()
      except EOFError:
          ...

  Você pode querer imprimir uma nova linha para que o cursor do usuário (e o prompt subsequente) não permaneça na mesma linha que o prompt do seu próprio programa.

- A entrada de controle-d não requer que se pressione Enter também, portanto o cursor do usuário (e o prompt subsequente) podem permanecer na mesma linha que o prompt do seu próprio programa. Você pode mover o cursor do usuário para uma nova linha imprimindo `\n` você mesmo!
- Note que um `dicionário` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), dentre eles `get`, e suporta operações como:

      d[chave]

  e

      if chave in d:
          ...

  onde `d` é um `dicionário` e `chave` é uma `str`.

- Garanta que evite ou capture qualquer [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela do terminal será semelhante ao seguinte:

    $

Depois, execute

    mkdir taqueria

para criar uma pasta chamada `taqueria` em seu espaço de código.

Em seguida, execute

    cd taqueria

para mudar de diretório para essa pasta. Você deverá ver agora o prompt do seu terminal como `taqueria/ $`. Agora, execute

    code taqueria.py

para criar um arquivo chamado `taqueria.py` onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python taqueria.py`. Digite `Taco` e pressione Enter, em seguida digite `Taco` novamente e pressione Enter. Seu programa deve exibir:

      Total: $6.00

  e continuar solicitando ao usuário até que ele insira controle-d.

- Execute seu programa com `python taqueria.py`. Digite `Baja Taco` e pressione Enter, em seguida digite `Tortilla Salad` e pressione Enter. Seu programa deve exibir:

      Total: $12.25

  e continuar solicitando ao usuário até que ele insira controle-d.

- Execute seu programa com `python taqueria.py`. Digite `Burger` e pressione Enter. Seu programa deve solicitar novamente ao usuário.

Certifique-se de tentar outros alimentos e variar o caso da sua entrada. Seu programa deve se comportar conforme esperado, sem fazer diferenciação de maiúsculas e minúsculas.

Você pode rodar o seguinte comando para verificar seu código usando `check50`, um programa que o CS50 utilizará para testar seu código quando você o enviar. Certifique-se de testá-lo também!

    check50 cs50/problems/2022/python/taqueria

Os sorrisos verdes significam que seu programa passou em um teste! Os rostos tristes vermelhos indicarão que seu programa produziu algo inesperado. Acesse a URL que o `check50` fornece para ver a entrada que o `check50` entregou ao seu programa, qual saída era esperada e qual saída seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/taqueria
