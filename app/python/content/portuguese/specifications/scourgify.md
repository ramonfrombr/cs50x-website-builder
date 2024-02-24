# Scourgify

> "Ah, bem," disse Tonks, fechando a tampa da mala com força, "pelo menos está tudo dentro. Isso precisa de uma limpeza também." Ela apontou sua varinha para a gaiola de Hedwig. "[Scourgify](https://harrypotter.fandom.com/wiki/Scouring_Charm)." Algumas penas e excrementos desapareceram.
>
> — _Harry Potter e a Ordem da Fênix_

Os dados, muitas vezes, também precisam ser "limpos", como reformatando-os, para que os valores estejam em um formato consistente, se não mais conveniente. Considere, por exemplo, este arquivo CSV de estudantes, [before.csv](before.csv), abaixo:

    name,house
    "Abbott, Hannah",Hufflepuff
    "Bell, Katie",Gryffindor
    "Bones, Susan",Hufflepuff
    "Boot, Terry",Ravenclaw
    "Brown, Lavender",Gryffindor
    "Bulstrode, Millicent",Slytherin
    "Chang, Cho",Ravenclaw
    "Clearwater, Penelope",Ravenclaw
    "Crabbe, Vincent",Slytherin
    "Creevey, Colin",Gryffindor
    ...

Fonte: [en.wikipedia.org/wiki/List_of_Harry_Potter_characters](https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters)

Embora cada "linha" no arquivo tenha três valores (sobrenome, nome e casa), os dois primeiros são combinados em uma "coluna" (nome), escapados com aspas duplas, com sobrenome e nome separados por vírgula e espaço. Não é ideal se [Hogwarts](https://en.wikipedia.org/wiki/Hogwarts) quiser enviar uma [carta modelo](https://en.wikipedia.org/wiki/Form_letter) para cada estudante, como via [mesclagem de correspondências](https://en.wikipedia.org/wiki/Mail_merge), já que seria estranho começar uma carta com:

> Querido Potter, Harry,

Em um arquivo chamado `scourgify.py`, implemente um programa que:

- Espera que o usuário forneça dois argumentos na linha de comando:
    - o nome de um arquivo CSV existente para ler como entrada, cujas colunas são assumidas, na ordem, `name` e `house`, e
    - o nome de um novo CSV para escrever como saída, cujas colunas devem ser, na ordem, `first`, `last`, e `house`.
- Converte a entrada para a saída, dividindo cada `name` em um nome `first` e sobrenome `last`. Presuma que cada aluno terá tanto um primeiro nome quanto um sobrenome.

Se o usuário não fornecer exatamente dois argumentos na linha de comando, ou se o primeiro não puder ser lido, o programa deve encerrar via `sys.exit` com uma mensagem de erro.

Dicas

- Observe que o módulo `csv` possui muitos métodos, conforme [docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html), entre os quais estão `DictReader`, conforme [docs.python.org/3/library/csv.html#csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader), e `DictWriter`, conforme [docs.python.org/3/library/csv.html#csv.DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter).
- Observe que você pode instruir um `DictWriter` a escrever seus `fieldnames` em um arquivo usando `writeheader` sem argumentos, conforme [docs.python.org/3/library/csv.html#csv.DictWriter.writeheader](https://docs.python.org/3/library/csv.html#csv.DictWriter.writeheader).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da janela do terminal se assemelha a este:

    $

Em seguida, execute

    mkdir scourgify

para criar uma pasta chamada `scourgify` em seu espaço de códigos.

Então, execute

    cd scourgify

para mudar para esse diretório. Você deve ver agora o seu prompt de terminal como `scourgify/ $`. Você pode então executar

    code scourgify.py

para criar um arquivo chamado `scourgify.py`, onde você escreverá seu programa. Certifique-se de executar

    wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

para baixar [before.csv](before.csv) para a sua pasta.

## Como Testar

Aqui está como testar seu código manualmente:

- Execute seu programa com `python scourgify.py`. Seu programa deve encerrar usando `sys.exit` e fornecer uma mensagem de erro:

      Poucos argumentos na linha de comando

- Crie arquivos vazios `1.csv`, `2.csv` e `3.csv`. Execute seu programa com `python scourgify.py 1.csv 2.csv 3.csv`. Seu programa deve exibir:

      Muitos argumentos na linha de comando

- Execute seu programa com `python scourgify.py invalid_file.csv output.csv`. Supondo que `invalid_file.csv` não exista, seu programa deve encerrar usando `sys.exit` e fornecer uma mensagem de erro:

      Não foi possível ler invalid_file.csv

- Execute seu programa com `python scourgify.py before.csv after.csv`. Supondo que `before.csv` exista, seu programa deve criar um novo arquivo, `after.csv`, cujas colunas devem ser, na ordem, `first`, `last` e `house`.

Você pode executar o seguinte para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas não deixe de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/scourgify

Os sorrisos verdes significam que seu programa passou em um teste! Os rostos tristes vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` forneceu ao seu programa, qual saída ele esperava e qual saída seu programa realmente forneceu.

## Como Enviar

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/scourgify
