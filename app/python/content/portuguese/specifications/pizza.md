# Pizza Py

Possivelmente o lugar mais popular para pizza em [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) é o [Pinocchio's Pizza & Subs](https://www.pinocchiospizza.net/), também conhecido como Noch's, conhecido por sua [pizza siciliana](https://www.pinocchiospizza.net/sicilian_vs_regular.html), que é "uma pizza de borda alta ou de massa grossa".

Os estudantes costumam comprar pizza pela fatia, mas o Pinocchio's também oferece pizzas inteiras em seu [cardápio](https://www.pinocchiospizza.net/menu.html), como demonstrado neste arquivo CSV de pizzas sicilianas, [sicilian.csv](sicilian.csv), abaixo:

    Pizza Siciliana,Pequena,Grande
    Queijo,$25.50,$39.95
    1 ingrediente,$27.50,$41.95
    2 ingredientes,$29.50,$43.95
    3 ingredientes,$31.50,$45.95
    Especial,$33.50,$47.95

Consulte [regular.csv](regular.csv) para um arquivo CSV de pizzas tradicionais também.

Naturalmente, um arquivo CSV não é o formato mais amigável para o cliente visualizar. Uma forma mais agradável pode ser uma tabela, formatada como [arte ASCII](https://en.wikipedia.org/wiki/ASCII_art), como esta:

    +------------------+---------+---------+
    | Pizza Siciliana  | Pequena | Grande  |
    +==================+=========+=========+
    | Queijo           | $25.50  | $39.95  |
    +------------------+---------+---------+
    | 1 ingrediente    | $27.50  | $41.95  |
    +------------------+---------+---------+
    | 2 ingredientes   | $29.50  | $43.95  |
    +------------------+---------+---------+
    | 3 ingredientes   | $31.50  | $45.95  |
    +------------------+---------+---------+
    | Especial         | $33.50  | $47.95  |
    +------------------+---------+---------+

Em um arquivo chamado `pizza.py`, implemente um programa que espera exatamente um argumento de linha de comando, o nome (ou caminho) de um arquivo CSV no formato do Pinocchio's, e gera uma tabela formatada como arte ASCII usando o `tabulate`, um pacote no PyPI em [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Formate a tabela usando o formato `grid` da biblioteca. Se o usuário não especificar exatamente um argumento de linha de comando, ou se o nome do arquivo especificado não terminar com `.csv`, ou se o arquivo especificado não existir, o programa deve sair usando `sys.exit` em vez disso.

Dicas

- Lembre-se de que o módulo `csv` vem com vários métodos, conforme [docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html), incluindo `reader`, conforme [docs.python.org/3/library/csv.html#csv.reader](https://docs.python.org/3/library/csv.html#csv.reader), e `DictReader`, conforme [docs.python.org/3/library/csv.html#csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).
- Observe que o `open` pode `lançar` um `FileNotFoundError`, conforme [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Observe que o pacote `tabulate` vem com apenas uma função, conforme [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Você pode instalar o pacote com:

      pip install tabulate

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir pizza

para criar uma pasta chamada `pizza` no seu espaço de códigos.

Então, execute

    cd pizza

para navegar até essa pasta. Agora, você deverá ver seu prompt de terminal como `pizza/ $`. Você pode então executar

    code pizza.py

para criar um arquivo chamado `pizza.py`, onde você escreverá seu programa. Certifique-se de executar

    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv

para baixar [sicilian.csv](sicilian.csv) na sua pasta. Também execute

    wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

para baixar [regular.csv](regular.csv) na sua pasta.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python pizza.py`. Seu programa deve sair usando `sys.exit` e exibir uma mensagem de erro:

      Argumentos de linha de comando insuficientes

- Certifique-se de baixar os arquivos [regular.csv](regular.csv) e [sicilian.csv](sicilian.csv) e colocá-los na mesma pasta que `pizza.py`. Execute seu programa com `python pizza.py regular.csv sicilian.csv`. Seu programa deve exibir:

      Muitos argumentos de linha de comando

- Execute seu programa com `python pizza.py invalid_file.csv`. Supondo que `invalid_file.csv` não exista, seu programa deve sair usando `sys.exit` e exibir uma mensagem de erro:

      Arquivo não existe

- Crie um arquivo chamado `sicilian.txt`. Execute seu programa com `python pizza.py sicilian.txt`. Seu programa deve sair usando `sys.exit` e exibir uma mensagem de erro:

      Não é um arquivo CSV

- Execute seu programa com `python pizza.py regular.csv`. Supondo que você tenha baixado o arquivo [regular.csv](regular.csv), seu programa deve imprimir uma tabela como a seguinte:

      +-----------------+---------+---------+
      | Pizza Regular   | Pequena | Grande  |
      +=================+=========+=========+
      | Queijo          | $13.50  | $18.95  |
      +-----------------+---------+---------+
      | 1 ingrediente   | $14.75  | $20.95  |
      +-----------------+---------+---------+
      | 2 ingredientes  | $15.95  | $22.95  |
      +-----------------+---------+---------+
      | 3 ingredientes  | $16.95  | $24.95  |
      +-----------------+---------+---------+
      | Especial        | $18.50  | $26.95  |
      +-----------------+---------+---------+

Você pode executar o abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. Mas lembre-se de testá-lo também por conta própria!

    check50 cs50/problems/2022/python/pizza

Os emojis verdes significam que seu programa passou em um teste! Os emojis vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` fornece para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/pizza
