# Corretor ortográfico

## Problema a resolver

Para este problema, você implementará um programa que verifica a ortografia de um arquivo, como o abaixo, usando uma tabela hash.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o01nuZNSBSH2khVokTs2GEPtP" src="https://asciinema.org/a/o01nuZNSBSH2khVokTs2GEPtP.js"></script>

## Código de distribuição

Para este problema, você estenderá a funcionalidade do código fornecido a você pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` por conta própria. Você verá que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/5/speller.zip

para baixar um ZIP chamado `speller.zip` em seu espaço de código.

Em seguida, execute

    unzip speller.zip

para criar uma pasta chamada `speller`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm speller.zip

e responder com "s" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd speller

seguido de Enter para se mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o seguinte.

    speller/ $

Execute `ls` por conta própria e você deverá ver alguns arquivos e pastas:

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/

Se você tiver algum problema, siga estas mesmas etapas novamente e veja se consegue determinar onde errou!

## Histórico

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Dados os muitos arquivos neste programa, é importante ler esta seção na íntegra antes de começar. Assim, você saberá o que fazer e como fazer!</strong></p></div>

Teoricamente, na entrada de tamanho _n_, um algoritmo com um tempo de execução de _n_ é "assintoticamente equivalente", em termos de _O_, a um algoritmo com um tempo de execução de _2n_. Na verdade, ao descrever o tempo de execução de um algoritmo, normalmente nos concentramos no termo dominante (ou seja, mais impactante) (ou seja, _n_ neste caso, uma vez que _n_ pode ser muito maior que 2). No mundo real, porém, o fato é que _2n_ parece duas vezes mais lento que _n_.

O desafio que você tem pela frente é implementar a verificação ortográfica mais rápida que puder! Por "mais rápido", no entanto, estamos falando de "tempo real", não de tempo assintótico.

Em `speller.c`, criamos um programa projetado para verificar a ortografia de um arquivo depois de carregar um dicionário de palavras do disco para a memória. Esse dicionário, entretanto, é implementado em um arquivo chamado `dictionary.c`. (Ele poderia ser implementado em `speller.c`, mas à medida que os programas ficam mais complexos, geralmente é conveniente dividi-los em vários arquivos.) Os protótipos para as funções nele contidas, entretanto, não são definidos no próprio `dictionary.c`, mas em `dictionary.h`. Dessa forma, tanto `speller.c` quanto `dictionary.c` podem `#include` o arquivo. Infelizmente, não conseguimos implementar a parte de carregamento. Ou a parte de verificação. Deixamos ambos (e um pouco mais) para você! Mas primeiro, um passeio.

### Compreendendo

#### `dictionary.h`

Abra o `dictionary.h` e você verá uma nova sintaxe, incluindo algumas linhas que mencionam `DICTIONARY_H`. Não precisa se preocupar com isso, mas, se estiver curioso, essas linhas apenas garantem que, embora `dictionary.c` e `speller.c` (que você verá em um momento) `#include` este arquivo, `clang` o compilará apenas uma vez.

Em seguida, observe como `#include` um arquivo chamado `stdbool.h`. Esse é o arquivo no qual o próprio `bool` é definido. Você não precisava disso antes, pois a Biblioteca CS50 costumava `#include` isso para você.

Observe também nosso uso de `#define`, uma "diretiva de pré-processador" que define uma "constante" chamada `LENGTH` que tem um valor de `45`. É uma constante no sentido de que você não pode (acidentalmente) alterá-la em seu próprio código. Na verdade, `clang` substituirá qualquer menção a `LENGTH` em seu próprio código por, literalmente, `45`. Em outras palavras, não é uma variável, apenas um truque de localizar e substituir.

Finalmente, observe os protótipos para cinco funções: `check`, `hash`, `load`, `size` e `unload`. Observe como três deles recebem um ponteiro como argumento, de acordo com `*`:

    bool check(const char *word);
    unsigned int hash(const char *word);
    bool load(const char *dictionary);

Lembre-se de que `char *` é o que costumávamos chamar de `string`. Portanto, esses três protótipos são essencialmente apenas:

    bool check(const string word);
    unsigned int hash(const string word);
    bool load(const string dictionary);

E `const`, entretanto, apenas diz que essas strings, quando passadas como argumentos, devem permanecer constantes; você não poderá alterá-las, acidentalmente ou não!

#### `dictionary.c`

Agora abra `dictionary.c`. Observe como, no topo do arquivo, definimos um `struct` chamado `node` que representa um nó em uma tabela hash. E declaramos uma matriz de ponteiros globais, `table`, que (em breve) representará a tabela hash que você usará para controlar as palavras no dicionário. A matriz contém `N` ponteiros de nó, e definimos `N` igual a `26` por enquanto, para corresponder à função `hash` padrão conforme descrito abaixo. Você provavelmente desejará aumentar isso dependendo de sua própria implementação de `hash`.

Em seguida, observe que implementamos `load`, `check`, `size` e `unload`, mas apenas o suficiente para o código compilar. Observe também que implementamos `hash` com um algoritmo de amostra baseado na primeira letra da palavra. Seu trabalho, em última análise, é reimplementar essas funções da forma mais inteligente possível para que este verificador ortográfico funcione conforme anunciado. E rápido!

#### `speller.c`

Certo, agora abra `speller.c` e passe um tempo examinando o código e os comentários incluídos. Você não precisará alterar nada neste arquivo e não é preciso entender a sua totalidade, no entanto, tente entender a sua funcionalidade. Observe como, através de uma função chamada `getrusage`, nós estaremos "benchmarkando" (ou seja, cronometrando a execução de) as suas implementações de `check`, `load`, `size` e `unload`. Observe também como passamos `check`, palavra por palavra, o conteúdo de alguns arquivo a ser verificado. Finalmente, relatamos cada palavra mal escrita naquele arquivo juntamente com um monte de estatísticas.

Observe, incidentalmente, que definimos o uso de `speller` como:

    Uso: speller [dicionário] texto

onde `dicionário` é assumido como um arquivo contendo uma lista de palavras em minúsculas, uma por linha, e `texto` é um arquivo a ser verificado. Como as chaves sugerem, fornecer `dicionário` é opcional; se este argumento for omitido, `speller` usará `diccionários/grande` por padrão. Em outras palavras, executar

    ./speller texto

será equivalente a executar

    ./speller dicionários/grande texto

onde `texto` é o arquivo que você deseja verificar. Basta dizer que o primeiro é mais fácil de digitar! (Claro, `speller` não será capaz de carregar nenhum dicionário até que você implemente `load` em `dictionary.c`! Até então, você verá `Não foi possível carregar`.)

Dentro do dicionário padrão, lembre-se, existem 143.091 palavras, todas as quais devem ser carregadas na memória! Na verdade, dê uma olhada nesse arquivo para ter uma noção de sua estrutura e tamanho. Observe que todas as palavras naquele arquivo aparecem em minúsculas (mesmo, para simplificar, nomes próprios e acrônimos). De cima para baixo, o arquivo é classificado lexicograficamente, com apenas uma palavra por linha (cada uma terminando com `\n`). Nenhuma palavra tem mais de 45 caracteres e nenhuma palavra aparece mais de uma vez. Durante o desenvolvimento, você pode achar útil fornecer `speller` com um `dicionário` seu próprio que contenha muito menos palavras, para que você não tenha dificuldade em depurar uma estrutura enorme na memória. Em `dicionários/pequeno` existe um dicionário assim. Para usá-lo, execute:

    ./speller dicionários/pequeno texto

onde `texto` é o arquivo que você deseja verificar. Não prossiga até ter certeza de que entendeu como o próprio `speller` funciona!

Provavelmente, você não passou tempo suficiente examinando `speller.c`. Volte uma casa e examine-o novamente!

#### `textos/`

Para que você possa testar sua implementação do `speller`, também fornecemos vários textos, entre eles o roteiro de _La La Land_, o texto do Affordable Care Act, três milhões de bytes de Tolstói, alguns trechos de _The Federalist Papers_ e Shakespeare e muito mais. Para que você saiba o que esperar, abra e examine cada um desses arquivos, todos os quais estão em um diretório chamado `textos` no diretório `pset5`.

Agora, como você deve saber por ter lido cuidadosamente `speller.c`, a saída de `speller`, se executado com, digamos,

    ./speller textos/lalaland.txt

eventualmente se parecerá com o abaixo.

Veja a seguir parte da saída que você verá. Para fins informativos, extraímos alguns exemplos de “erros ortográficos”. E para não estragar a diversão, omitimos nossas próprias estatísticas por enquanto.

    PALAVRAS COM ERROS DE ORTOGRAFIA

    [...]
    AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
    [...]
    Shangri
    [...]
    noivo
    [...]
    Sebastian
    [...]

    PALAVRAS COM ERROS DE ORTOGRAFIA:
    PALAVRAS NO DICIONÁRIO:
    PALAVRAS NO TEXTO:
    TEMPO EM load:
    TEMPO EM check:
    TEMPO EM size:
    TEMPO EM unload:
    TEMPO TOTAL:

`TEMPO EM load` representa o número de segundos que `speller` gasta executando sua implementação de `load`. `TEMPO EM check` representa o número de segundos que `speller` gasta, no total, executando sua implementação de `check`. `TEMPO EM size` representa o número de segundos que `speller` gasta executando sua implementação de `size`. `TEMPO EM unload` representa o número de segundos que `speller` gasta executando sua implementação de `unload`. `TEMPO TOTAL` é a soma dessas quatro medições.

**Observe que esses tempos podem variar um pouco entre as execuções do `speller`, dependendo do que mais o seu codespace está fazendo, mesmo que você não altere o seu código.**

Incidentalmente, para deixar claro, por “erro de ortografia” queremos dizer simplesmente que alguma palavra não está no `dicionário` fornecido.

#### `Makefile`

E, por último, lembre-se de que `make` automatiza a compilação do seu código para que você não precise executar `clang` manualmente junto com um monte de chaves. No entanto, conforme seus programas crescem em tamanho, `make` não será mais capaz de inferir do contexto como compilar seu código; você precisará começar a dizer ao `make` como compilar seu programa, principalmente quando envolvem vários arquivos de origem (ou seja, `.c`), como no caso deste problema. Assim, utilizaremos um `Makefile`, um arquivo de configuração que diz ao `make` exatamente o que fazer. Abra `Makefile` e você verá quatro linhas:

1. A primeira linha diz ao `make` para executar as linhas subsequentes sempre que você executar `make speller` (ou apenas `make`).
2. A segunda linha diz ao `make` como compilar `speller.c` para código de máquina (ou seja, `speller.o`).
3. A terceira linha diz ao `make` como compilar `dictionary.c` para código de máquina (ou seja, `dictionary.o`).
4. A quarta linha diz ao `make` para vincular `speller.o` e `dictionary.o` em um arquivo chamado `speller`.

**Certifique-se de compilar `speller` executando `make speller` (ou apenas `make`). Executar `make dictionary` não funcionará!**

## Especificação

Muito bem, o desafio que você tem agora é implementar, em ordem, `load`, `hash`, `size`, `check` e `unload` o mais eficientemente possível usando uma tabela hash de tal forma que `TIME IN load`, `TIME IN check`, `TIME IN size` e `TIME IN unload` sejam todos minimizados. Para ter certeza, não é óbvio o que significa minimizar, uma vez que estes valores de referência certamente variarão conforme você alimenta `speller` com valores diferentes para `dictionary` e para `text`. Mas aí reside o desafio, senão a diversão, deste problema. Este problema é a sua chance para projetar. Embora o convidemos a minimizar espaço, seu maior inimigo é o tempo. Mas antes que você mergulhe, algumas especificações nossas.

- Você não pode alterar `speller.c` ou `Makefile`.
- Você pode alterar `dictionary.c` (e, de fato, deve a fim de completar as implementações de `load`, `hash`, `size`, `check` e `unload`), mas você não pode alterar as declarações (ou seja, protótipos) de `load`, `hash`, `size`, `check` ou `unload`. Você pode, no entanto, adicionar novas funções e variáveis (locais ou globais) para `dictionary.c`.
- Você pode alterar o valor de `N` em `dictionary.c`, assim sua tabela hash pode ter mais baldes.
- Você pode alterar `dictionary.h`, mas não pode alterar as declarações de `load`, `hash`, `size`, `check` ou `unload`.
- Sua implementação de `check` deve ignorar o caso. Em outras palavras, se `foo` está no dicionário, então `check` deve retornar verdadeiro dado qualquer capitalização dela; nenhuma de `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` e `FOO` deve ser considerada mal escrita.
- Tirando a capitalização, sua implementação de `check` deve retornar `true` apenas para palavras que estejam realmente no `dicionário`. Cuidado com palavras comuns codificadas com força (p. ex., `the`), para que não passemos para sua implementação um `dicionário` sem essas mesmas palavras. Além disso, os únicos possessivos permitidos são aqueles realmente no `dicionário`. Em outras palavras, mesmo que `foo` esteja no `dicionário`, `check` deve retornar `false` dado `foo's` se `foo's` também não estiver no `dicionário`.
- Você pode assumir que qualquer `dicionário` passado ao seu programa será estruturado exatamente como o nosso, ordenado alfabeticamente de cima para baixo com uma palavra por linha, cada uma das quais termina com `\n`. Você também pode assumir que `dictionary` conterá pelo menos uma palavra, que nenhuma palavra terá mais de caracteres `LENGTH` (uma constante definida em `dictionary.h`), que nenhuma palavra aparecerá mais de uma vez, que cada palavra conterá apenas caracteres alfabéticos minúsculos e, possivelmente, apóstrofos, e que nenhuma palavra começará com apóstrofo.
- Você pode assumir que `check` só receberá palavras que contenham caracteres alfabéticos (maiúsculos ou minúsculos) e, possivelmente, apóstrofos.
- Seu corretor ortográfico pode receber apenas `text` e `dictionary` como entrada. Embora você possa estar inclinado (particularmente se for mais confortável) a “pré-processar” nosso dicionário padrão a fim de derivar uma “função hash ideal” para ele, você não pode salvar a saída de nenhum desses pré-processamento em disco para carregá-la de volta na memória em execuções subsequentes do seu corretor ortográfico para obter vantagem.
- Seu corretor ortográfico não deve vazar nenhuma memória. Certifique-se de verificar vazamentos com `valgrind`.
- **A função hash que você escreve deve ser sua, não uma que você procure online.**

Muito bem, pronto para começar?

- Implemente o `load`.
- Implemente o `hash`.
- Implemente o `size`.
- Implemente o `check`.
- Implemente o `unload`.

## Dicas

### Implemente o `load`

Complete a função `load`. `load` deve carregar o dicionário na memória (em particular, em uma tabela hash!). `load` deve retornar `true` se for bem-sucedido e `false` em caso contrário.

Considere que este problema é composto apenas de problemas menores:

1. Abra o arquivo do dicionário
2. Leia cada palavra no arquivo
    1. Adicione cada palavra na tabela hash
3. Feche o arquivo do dicionário

Escreva algum pseudocódigo para se lembrar de fazer exatamente isso:

    bool load(const char *dictionary)
    {
        // Abra o arquivo do dicionário

        // Leia cada palavra no arquivo

            // Adicione cada palavra na tabela hash

        // Feche o arquivo do dicionário
    }

Considere primeiro como abrir o arquivo do dicionário. [`fopen`](https://manual.cs50.io/3/fopen) é uma escolha natural. Você pode usar o modo `r`, dado que precisa apenas _ler_ palavras no arquivo do dicionário (não _escrever_ ou _acrescentar_ elas).

    bool load(const char *dictionary)
    {
        // Abra o arquivo do dicionário
        FILE *source = fopen(dictionary, "r");

        // Leia cada palavra no arquivo

            // Adicione cada palavra na tabela hash

        // Feche o arquivo do dicionário
    }

Antes de continuar, você deve escrever o código para verificar se o arquivo foi aberto corretamente. Isso depende de você! Também é melhor garantir que você feche todos os arquivos que abrir, então agora é um bom momento para escrever o código para fechar o arquivo do dicionário:

    bool load(const char *dictionary)
    {
        // Abra o arquivo do dicionário
        FILE *source = fopen(dictionary, "r");

        // Leia cada palavra no arquivo

            // Adicione cada palavra na tabela hash

        // Feche o arquivo do dicionário
        fclose(source);
    }

O que resta é ler cada palavra no arquivo e adicionar cada palavra na tabela hash. Retorne `true` quando toda a operação for bem-sucedida e `false` se falhar. Considere seguir o passo a passo deste problema e continuar a dividir os subproblemas em problemas menores ainda. Por exemplo, adicionar cada palavra na tabela hash pode ser apenas uma questão de implementar alguns passos menores ainda:

1. Crie espaço para um novo nó da tabela hash
2. Copie a palavra no novo nó
3. Hash a palavra para obter seu valor hash
4. Insira o novo nó na tabela hash (usando o índice especificado pelo seu valor hash)

Claro, há mais de uma maneira de abordar este problema, com suas próprias compensações de design. Por esse motivo, o restante do código fica a seu critério!

### Implemente o `hash`

Complete a função `hash`. `hash` deve pegar uma string, `word`, como entrada e retornar um `int` “não assinado” positivo.

A função hash fornecida a você retorna um `int` entre 0 e 25, inclusive, com base no primeiro caractere de `word`. No entanto, há muitas maneiras de implementar uma função hash além de usar o primeiro caractere (ou _caracteres_) de uma palavra. Considere uma função hash que use uma soma de valores ASCII ou o tamanho de uma palavra. Uma boa função hash reduz “colisões” e tem uma distribuição (na maior parte!) uniforme entre os “baldes” da tabela hash.

### Implementando `size`

Complete a função `size`. `size` deve retornar o número de palavras carregadas no dicionário. Considere duas abordagens para este problema:

- Conte cada palavra na medida em que ela for carregada no dicionário. Retorne essa contagem quando `size` for chamada.
- A cada vez que `size` for chamada, itere pelas palavras na tabela hash para contá-las. Retorne essa contagem.

Qual parece mais eficiente para você? Independente do que você escolher, deixaremos o código por sua conta.

### Implementando `check`

Complete a função `check`. `check` deve retornar `true` se uma palavra for localizada no dicionário, caso contrário `false`.

Considere que este problema também é composto por problemas menores. Se você implementou uma tabela hash, encontrar uma palavra leva apenas alguns passos:

1. Faça o hash da palavra para obter o seu valor de hash
2. Pesquise a tabela hash na localização especificada pelo valor de hash da palavra
    1. Retorne `true` se a palavra for encontrada
3. Retorne `false` se nenhuma palavra for encontrada

Para comparar duas strings sem distinção de maiúsculas e minúsculas, você pode achar útil [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (declarado em `strings.h`)! Você provavelmente também desejará garantir que sua função hash não faça distinção entre maiúsculas e minúsculas, de modo que `foo` e `FOO` tenham o mesmo valor de hash.

### Implementando `unload`

Complete a função `unload`. Certifique-se de `free` em `unload` qualquer memória que tenha sido alocada em `load`!

Lembre-se de que o `valgrind` é o seu melhor amigo de agora em diante. Saiba que o `valgrind` observa se há vazamentos enquanto o seu programa está realmente em execução, portanto certifique-se de fornecer argumentos de linha de comando se quiser que o `valgrind` analise o `speller` enquanto você usa um `dicionário` e/ou texto específico, como o abaixo. É melhor usar um texto pequeno, entretanto, senão o `valgrind` pode levar um bom tempo para rodar.

    valgrind ./speller texts/cat.txt

Se você executar o `valgrind` sem especificar um `texto` para o `speller`, suas implementações de `load` e `unload` não serão realmente chamadas (e, portanto, analisadas).

Se não tiver certeza de como interpretar o output do `valgrind`, basta pedir ajuda ao `help50`:

    help50 valgrind ./speller texts/cat.txt

## Guia

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Observe que há 6 vídeos nesta lista de reprodução.</strong></p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

## Como testar

Como verificar se o seu programa está exibindo as palavras erradas? Bem, você pode consultar as "chaves de respostas" que estão dentro do diretório `keys` que está dentro do seu diretório `speller`. Por exemplo, dentro de `keys/lalaland.txt` estão todas as palavras que o seu programa _deveria_ considerar erradas.

Portanto, você pode executar o seu programa em algum texto em uma janela, como abaixo:

    ./speller texts/lalaland.txt

E você pode então executar a solução da equipe no mesmo texto em outra janela, como abaixo:

    ./speller50 texts/lalaland.txt

E então você pode comparar as janelas visualmente lado a lado. Isso pode se tornar tedioso rapidamente. Então, você pode querer "redirecionar" o output do seu programa para um arquivo, como abaixo:

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt

Você pode então comparar os dois arquivos lado a lado na mesma janela com um programa como `diff`, como abaixo:

    diff -y student.txt staff.txt

Alternativamente, para economizar tempo, você pode simplesmente comparar o output do seu programa (assumindo que você redirecionou para, por exemplo, `student.txt`) com uma das chaves de resposta sem executar a solução da equipe, como abaixo:

    diff -y student.txt keys/lalaland.txt

Se o output do seu programa corresponder ao da equipe, o `diff` exibirá duas colunas que devem ser idênticas, exceto, talvez, pelos tempos de execução na parte inferior. Se as colunas forem diferentes, você verá um `>` ou `|` onde elas diferem. Por exemplo, se você vir

    MISSPELLED WORDS                                                MISSPELLED WORDS

    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L

isso significa que o seu programa (cujo output está à esquerda) não considera `Thelonious` ou `MIA` com erros, embora o output da equipe (à direita) considere, como é implícito pela ausência de, digamos, `Thelonious` na coluna da esquerda e pela presença de `Thelonious` na coluna da direita.

Por fim, certifique-se de testar com os dicionários padrão grande e pequeno. Tenha cuidado para não presumir que se a sua solução for executada com sucesso com o dicionário grande, ela também será executada com sucesso com o pequeno. Veja como tentar o dicionário pequeno:

    ./speller dictionaries/small texts/cat.txt

### Correção

    check50 cs50/problems/2024/x/speller

### Estilo

    style50 dictionary.c

## Solução da equipe

Como avaliar quão rápido (e correto) o seu código é? Bem, como sempre, sinta-se à vontade para mexer com a solução da equipe, como abaixo, e comparar os seus números com os seus.

    ./speller50 texts/lalaland.txt

## Como enviar

    submit50 cs50/problems/2024/x/speller

