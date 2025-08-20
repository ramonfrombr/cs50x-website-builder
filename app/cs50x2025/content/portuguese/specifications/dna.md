## DNA

## Problema a resolver

O DNA, o transportador de informações genéticas em seres vivos, tem sido usado na justiça criminal por décadas. Mas como exatamente funciona o perfil genético? Dada uma sequência de DNA, como os investigadores forenses podem identificar a quem ela pertence?

Em um arquivo chamado `dna.py` em uma pasta chamada `dna`, implemente um programa que identifica a quem pertence uma sequência de DNA.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-5onE9BNq1zhL2D72gfu9IbdsD" src="https://asciinema.org/a/5onE9BNq1zhL2D72gfu9IbdsD.js"></script>

## Código de distribuição

Para este problema, você estenderá a funcionalidade do código fornecido a você pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` por si só. Você deve descobrir que o prompt da janela do seu terminal se assemelha ao abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/6/dna.zip

para baixar um ZIP chamado `dna.zip` em seu espaço de códigos.

Em seguida, execute

    unzip dna.zip

para criar uma pasta chamada `dna`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm dna.zip

e responder com "s" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd dna

seguido de Enter para entrar (ou seja, abrir) aquele diretório. Seu prompt agora deve se parecer com o abaixo.

    dna/ $

Execute `ls` por si só e você deverá ver alguns arquivos e pastas:

    databases/ dna.py sequences/

Se você encontrar algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou!

## Contexto

O DNA é na verdade apenas uma sequência de moléculas chamadas nucleotídeos, organizadas em uma forma particular (uma dupla hélice). Cada célula humana tem bilhões de nucleotídeos organizados em sequência. Cada nucleotídeo de DNA contém uma das quatro bases diferentes: adenina (A), citosina (C), guanina (G) ou timina (T). Algumas partes dessa sequência (ou seja, genoma) são as mesmas, ou pelo menos muito semelhantes, em quase todos os seres humanos, mas outras partes da sequência têm uma maior diversidade genética e, portanto, variam mais na população.

Um lugar onde o DNA tende a ter alta diversidade genética é nas repetições curtas em tandem (STRs). Um STR é uma sequência curta de bases de DNA que tende a se repetir consecutivamente várias vezes em locais específicos dentro do DNA de uma pessoa. O número de vezes que qualquer STR específico se repete varia muito entre os indivíduos. Nas amostras de DNA abaixo, por exemplo, Alice tem o STR `AGAT` repetido quatro vezes em seu DNA, enquanto Bob tem o mesmo STR repetido cinco vezes.

![STRs de exemplo](https://cs50.harvard.edu/x/2024/psets/6/dna/strs.png)

Usar vários STRs, em vez de apenas um, pode melhorar a precisão do perfil de DNA. Se a probabilidade de que duas pessoas tenham o mesmo número de repetições para um único STR for de 5%, e o analista observar 10 STRs diferentes, então a probabilidade de que duas amostras de DNA correspondam puramente por acaso é de cerca de 1 em 1 quatrilhão (assumindo que todos os STRs sejam independentes entre si). Portanto, se duas amostras de DNA corresponderem no número de repetições para cada um dos STRs, o analista pode estar bastante confiante de que elas vieram da mesma pessoa. CODIS, o [banco de dados de DNA](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet) do FBI, usa 20 STRs diferentes como parte de seu processo de criação de perfil de DNA.

Como seria esse banco de dados de DNA? Bem, em sua forma mais simples, você poderia imaginar formatar um banco de dados de DNA como um arquivo CSV, em que cada linha corresponde a um indivíduo e cada coluna corresponde a um STR específico.

    nome, AGAT, AATG, TATC
    Alice, 28, 42, 14
    Bob, 17, 22, 19
    Charlie, 36, 18, 25

Os dados no arquivo acima sugerem que Alice tem a sequência `AGAT` repetida 28 vezes consecutivas em algum lugar em seu DNA, a sequência `AATG` repetida 42 vezes e `TATC` repetida 14 vezes. Bob, por sua vez, tem esses mesmos três STRs repetidos 17 vezes, 22 vezes e 19 vezes, respectivamente. E Charlie tem esses mesmos três STRs repetidos 36, 18 e 25 vezes, respectivamente.

Então, dada uma sequência de DNA, como você pode identificar a quem ela pertence? Bem, imagine que você olhou através da sequência de DNA para a sequência consecutiva mais longa de `AGAT`s repetidos e descobriu que a sequência mais longa tinha 17 repetições. Se você então descobrisse que a sequência mais longa de `AATG` tem 22 repetições e a sequência mais longa de `TATC` tem 19 repetições, isso forneceria uma boa evidência de que o DNA era de Bob. Claro, também é possível que, depois de fazer as contagens para cada um dos STRs, elas não correspondam a ninguém no seu banco de dados de DNA, caso em que você não tenha correspondência.

Na prática, como os analistas sabem em qual cromossomo e em qual local no DNA um STR será encontrado, eles podem localizar sua pesquisa em apenas uma seção estreita do DNA. Mas vamos ignorar esse detalhe para este problema.

Sua tarefa é escrever um programa que receberá uma sequência de DNA e um arquivo CSV contendo contagens de STR para uma lista de indivíduos e, em seguida, produzirá a quem o DNA (provavelmente) pertence.

## Especificação

- O programa deve exigir como seu primeiro argumento de linha de comando o nome de um arquivo CSV contendo as contagens de STR para uma lista de indivíduos e deve exigir como seu segundo argumento de linha de comando o nome de um arquivo de texto contendo a sequência de DNA a ser identificada.
  - Se o seu programa for executado com o número incorreto de argumentos de linha de comando, o programa deverá imprimir uma mensagem de erro de sua escolha (com `print`). Se o número correto de argumentos for fornecido, você pode presumir que o primeiro argumento é realmente o nome de arquivo de um arquivo CSV válido e que o segundo argumento é o nome de arquivo de um arquivo de texto válido.
- Seu programa deve abrir o arquivo CSV e ler seu conteúdo na memória.
  - Você pode assumir que a primeira linha do arquivo CSV serão os nomes das colunas. A primeira coluna será a palavra `nome` e as demais colunas serão as próprias sequências STR.
- Seu programa deve abrir a sequência de DNA e ler seu conteúdo na memória.
- Para cada um dos STRs (da primeira linha do arquivo CSV), seu programa deve calcular a execução mais longa de repetições consecutivas do STR na sequência de DNA a ser identificada. Observe que definimos uma função auxiliar para você, `longest_match`, que fará exatamente isso!
- Se as contagens de STR corresponderem exatamente a qualquer um dos indivíduos no arquivo CSV, seu programa deve imprimir o nome do indivíduo correspondente.
  - Você pode assumir que as contagens de STR não corresponderão a mais de um indivíduo.
  - Se as contagens de STR não corresponderem exatamente a qualquer um dos indivíduos no arquivo CSV, seu programa deve imprimir `Nenhuma correspondência`.

## Dicas

- Você pode achar o módulo [`csv`](https://docs.python.org/3/library/csv.html) do Python útil para ler arquivos CSV e salvá-los na memória. O particularmente útil pode ser [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).

  - Por exemplo, se um arquivo como `foo.csv` tiver uma linha de cabeçalho, em que cada string é o nome de algum campo, veja como você pode imprimir esses `fieldnames` como uma `lista`:
    import csv

          with open("foo.csv") as file:
              reader = csv.DictReader(file)
              print(reader.fieldnames)

  - E veja como você lê todas as (outras) linhas de um CSV em uma `lista`, em que cada elemento é um `dict` que representa essa linha:
    import csv

          rows = []
          with open("foo.csv") as file:
              reader = csv.DictReader(file)
              for row in reader:
                  rows.append(row)

- As funções [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) e [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) também podem ser úteis para ler arquivos de texto em sua memória.
- Considere quais estruturas de dados podem ser úteis para manter o rastreamento de informações em seu programa. Uma [`lista`](https://docs.python.org/3/tutorial/introduction.html#lists) ou um [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) podem ser úteis.
- Lembre-se de que definimos uma função (`longest_match`) que, quando recebe uma sequência de DNA e um STR como entradas, retorna o número máximo de vezes que o STR é repetido. Você pode usar essa função em outras partes do seu programa!

## Passo a Passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como Testar

Embora o `check50` esteja disponível para este problema, é recomendável que você teste seu código em primeiro lugar em cada um dos seguintes.

- Execute seu programa como `python dna.py databases/small.csv sequences/1.txt`. Seu programa deve exibir `Bob`.
- Execute seu programa como `python dna.py databases/small.csv sequences/2.txt`. Seu programa deve exibir `Nenhuma correspondência`.
- Execute seu programa como `python dna.py databases/small.csv sequences/3.txt`. Seu programa deve exibir `Nenhuma correspondência`.
- Execute seu programa como `python dna.py databases/small.csv sequences/4.txt`. Seu programa deve exibir `Alice`.
- Execute seu programa como `python dna.py databases/large.csv sequences/5.txt`. Seu programa deve exibir `Lavender`.
- Execute seu programa como `python dna.py databases/large.csv sequences/6.txt`. Seu programa deve exibir `Luna`.
- Execute seu programa como `python dna.py databases/large.csv sequences/7.txt`. Seu programa deve exibir `Ron`.
- Execute seu programa como `python dna.py databases/large.csv sequences/8.txt`. Seu programa deve exibir `Ginny`.
- Execute seu programa como `python dna.py databases/large.csv sequences/9.txt`. Seu programa deve exibir `Draco`.
- Execute seu programa como `python dna.py databases/large.csv sequences/10.txt`. Seu programa deve exibir `Albus`.
- Execute seu programa como `python dna.py databases/large.csv sequences/11.txt`. Seu programa deve exibir `Hermione`.
- Execute seu programa como `python dna.py databases/large.csv sequences/12.txt`. Seu programa deve exibir `Lily`.
- Execute seu programa como `python dna.py databases/large.csv sequences/13.txt`. Seu programa deve exibir `Nenhuma correspondência`.
- Execute seu programa como `python dna.py databases/large.csv sequences/14.txt`. Seu programa deve exibir `Severus`.
- Execute seu programa como `python dna.py databases/large.csv sequences/15.txt`. Seu programa deve exibir `Sirius`.
- Execute seu programa como `python dna.py databases/large.csv sequences/16.txt`. Seu programa deve exibir `Nenhuma correspondência`.
- Execute seu programa como `python dna.py databases/large.csv sequences/17.txt`. Seu programa deve exibir `Harry`.
- Execute seu programa como `python dna.py databases/large.csv sequences/18.txt`. Seu programa deve exibir `Nenhuma correspondência`.
- Execute seu programa como `python dna.py databases/large.csv sequences/19.txt`. Seu programa deve exibir `Fred`.
- Execute seu programa como `python dna.py databases/large.csv sequences/20.txt`. Seu programa deve exibir `Nenhuma correspondência`.

### Exatidão

    check50 cs50/problems/2024/x/dna

### Estilo

    style50 dna.py

## Como Enviar

    submit50 cs50/problems/2024/x/dna

