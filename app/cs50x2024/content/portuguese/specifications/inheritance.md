# Herança

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/xfZhb6lmxjk?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Problema a ser resolvido

O tipo sanguíneo de uma pessoa é determinado por dois alelos (ou seja, formas diferentes de um gene). Os três alelos possíveis são A, B e O, dos quais cada pessoa possui dois (possivelmente iguais, possivelmente diferentes). Cada um dos pais de uma criança passa aleatoriamente um de seus dois alelos de tipo sanguíneo para seu filho. As possíveis combinações de tipos sanguíneos, portanto, são: OO, OA, OB, AO, AA, AB, BO, BA e BB.

Por exemplo, se um dos pais tem tipo sanguíneo AO e o outro pai tem tipo sanguíneo BB, então os possíveis tipos sanguíneos da criança seriam AB e OB, dependendo de qual alelo é recebido de cada pai. Da mesma forma, se um pai tem tipo sanguíneo AO e o outro OB, então os possíveis tipos sanguíneos da criança seriam AO, OB, AB e OO.

Em um arquivo chamado `inheritance.c` em uma pasta chamada `inheritance`, simule a herança de tipos sanguíneos para cada membro de uma família.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-J9DnbdokgIAjWUbzC2CBqP22N" src="https://asciinema.org/a/J9DnbdokgIAjWUbzC2CBqP22N.js"></script>

## Código de distribuição

Para esse problema, você estenderá a funcionalidade do código fornecido pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você verá que o prompt da janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/5/inheritance.zip

para baixar um ZIP chamado `inheritance.zip` em seu código-espaço.

Em seguida, execute

    unzip inheritance.zip

para criar uma pasta chamada `inheritance`. Você não precisa mais do arquivo ZIP; portanto, você pode executar

    rm inheritance.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd inheritance

seguido de Enter para mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o seguinte:

    inheritance/ $

Execute `ls` sozinho e você deverá ver um arquivo chamado `inheritance.c`.

Se você tiver algum problema, siga esses mesmos passos novamente e veja se consegue descobrir onde errou!

## Detalhes de implementação

Conclua a implementação de `inheritance.c`, de modo que crie uma família com um tamanho de geração especificado e atribua alelos de tipo sanguíneo a cada membro da família. A geração mais antiga terá alelos atribuídos aleatoriamente a eles.

- A função `create_family` recebe um número inteiro (`gerações`) como entrada e deve alocar (via `malloc`) uma `pessoa` para cada membro da família com esse número de gerações, retornando um ponteiro para a `pessoa` na geração mais jovem.
  - Por exemplo, `create_family(3)` deve retornar um ponteiro para uma pessoa com dois pais, onde cada pai também tem dois pais.
  - Cada `pessoa` deve ter `alelos` atribuídos a ela. A geração mais antiga deve ter alelos escolhidos aleatoriamente (como chamando a função `random_allele`), e as gerações mais jovens devem herdar um alelo (escolhido aleatoriamente) de cada pai.
  - Cada `pessoa` deve ter `pais` atribuídos a ela. A geração mais antiga deve ter ambos os `pais` definidos como `NULL`, e as gerações mais jovens devem ter `pais` como um array de dois ponteiros, cada um apontando para uma estrutura `pessoa` diferente.

## Dicas

### Entenda o código em `inheritance.c`

Dê uma olhada no código de distribuição em `inheritance.c`.

Observe a definição de um tipo chamado `pessoa`. Cada pessoa tem uma matriz de dois `pais`, cada um dos quais é um ponteiro para outra estrutura `pessoa`. Cada pessoa também tem uma matriz de dois `alelos`, cada um dos quais é um `char` (ou seja, `'A'`, `'B'` ou `'O'`).

    // Cada pessoa tem dois pais e dois alelos
    typedef struct person
    {
        struct person *parents[2];
        char alleles[2];
    }
    person;

Agora, dê uma olhada na função `main`. A função começa "semeando" (ou seja, fornecendo alguma entrada inicial para) um gerador de números aleatórios que usaremos posteriormente para gerar alelos aleatórios.

    // Inicializa o gerador de números aleatórios
    srand(time(0));

A função `main` chama então a função `create_family` para simular a criação de estruturas `pessoa` para uma família de 3 gerações (ou seja, uma pessoa, seus pais e seus avós).

    // Cria uma nova família com três gerações
    person *p = create_family(GENERATIONS);

Chamamos então `print_family` para imprimir cada um desses membros da família e seus tipos sanguíneos.

    // Imprime a árvore genealógica de tipos sanguíneos
    print_family(p, 0);

Finalmente, a função chama `free_family` para `liberar` qualquer memória que foi alocada anteriormente com `malloc`.

    // Libera a memória
    free_family(p);

As funções `create_family` e `free_family` estão a seu cargo para escrever!

### Conclua a função `create_family`

A função `create_family` deve retornar um ponteiro para uma `pessoa` que herdou seu tipo sanguíneo da quantidade de `gerações` fornecida como entrada.

- Primeiro, observe que este problema é uma boa oportunidade para recursão.
  - Para determinar o tipo sanguíneo da pessoa atual, você primeiro precisa determinar os tipos sanguíneos de seus pais.
  - Para determinar esses tipos sanguíneos dos pais, você primeiro deve determinar _os tipos sanguíneos de seus_ pais. E assim por diante até chegar à última geração que deseja simular.

Para resolver este problema, você encontrará vários TODOs no código de distribuição.

Primeiro, você deve alocar memória para uma nova pessoa. Lembre-se de que você pode usar `malloc` para alocar memória e `sizeof(pessoa)` para obter o número de bytes a serem alocados.

    // Aloque memória para uma nova pessoa
    person *new_person = malloc(sizeof(person));

Em seguida, você deve verificar se ainda há gerações para criar, ou seja, se `gerações > 1`.

Se `gerações > 1`, então há mais gerações que ainda precisam ser alocadas. Já criamos dois novos pais, `parent0` e `parent1`, chamando recursivamente `create_family`. Sua função `create_family` deve então definir os ponteiros dos pais da nova pessoa que você criou. Finalmente, atribua os dois `alelos` para a nova pessoa escolhendo aleatoriamente um alelo de cada pai.

- Lembre-se, para acessar uma variável por meio de um ponteiro, você pode usar a notação de seta. Por exemplo, se `p` é um ponteiro para uma pessoa, então um ponteiro para o primeiro pai dessa pessoa pode ser acessado por `p->parents[0]`.
- Você pode achar a função `rand()` útil para atribuir aleatoriamente alelos. Esta função retorna um número inteiro entre `0` e `RAND_MAX` ou `32767`. Em particular, para gerar um número pseudoaleatório que seja `0` ou `1`, você pode usar a expressão `rand() % 2`.

  // Crie dois novos pais para a pessoa atual chamando create_family recursivamente
  person *parent0 = create_family(generations - 1);
  person *parent1 = create_family(generations - 1);

  // Defina ponteiros dos pais para a pessoa atual
  new_person->parents[0] = parent0;
  new_person->parents[1] = parent1;

  // Atribua aleatoriamente os alelos da pessoa atual com base nos alelos de seus pais
  new_person->alleles[0] = parent0->alleles[rand() % 2];
  new_person->alleles[1] = parent1->alleles[rand() % 2];

Digamos que não haja mais gerações para simular. Isto é, `gerações == 1`. Nesse caso, não haverá dados dos pais para esta pessoa. Ambos os pais de sua nova pessoa devem ser definidos como `NULL` e cada `alelo` deve ser gerado aleatoriamente.

    // Defina ponteiros dos pais como NULL
    new_person->parents[0] = NULL;
    new_person->parents[1] = NULL;

    // Atribua alelos aleatoriamente
    new_person->alleles[0] = random_allele();
    new_person->alleles[1] = random_allele();

Finalmente, sua função deve retornar um ponteiro para a `pessoa` que foi alocada.

    // Retorne a pessoa recém-criada
    return new_person;

### Conclua a função `free_family`

A função `free_family` deve aceitar como entrada um ponteiro para uma `pessoa`, liberar memória para essa pessoa e, em seguida, liberar recursivamente memória para todos os seus ancestrais.

- Como esta é uma função recursiva, você deve primeiro lidar com o caso base. Se a entrada para a função for `NULL`, então não há nada para liberar, então sua função pode retornar imediatamente.
- Caso contrário, você deve `free` recursivamente os dois pais da pessoa antes de `free` a criança.

O que está abaixo é uma dica, mas é como fazer isso!

    // Liberte `p` e todos os ancestrais de `p`.
    void free_family(person *p)
    {
        // Trate do caso base
        if (p == NULL)
        {
            return;
        }

        // Liberte pais recursivamente
        free_family(p->parents[0]);
        free_family(p->parents[1]);

        // Liberte filho
        free(p);
    }

### Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9p7ddI3ozTY?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Não sabe como resolver?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/H7LULatPwcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Como testar

Ao executar `./inheritance`, seu programa deve aderir às regras descritas no contexto. A criança deve ter dois alelos, um de cada pai. Cada um dos pais deve ter dois alelos, um de cada um de seus pais.

Por exemplo, no exemplo abaixo, a criança na Geração 0 recebeu um alelo O de ambos os pais da Geração 1. O primeiro pai recebeu um A do primeiro avô e um O do segundo avô. Da mesma forma, o segundo pai recebeu um O e um B de seus avós.

    $ ./inheritance
    Filho (Geração 0): tipo sanguíneo OO
        Pai (Geração 1): tipo sanguíneo AO
            Avô (Geração 2): tipo sanguíneo OA
            Avó (Geração 2): tipo sanguíneo BO
        Mãe (Geração 1): tipo sanguíneo OB
            Avô (Geração 2): tipo sanguíneo AO
            Avó (Geração 2): tipo sanguíneo BO

### Correção

    check50 cs50/problems/2024/x/inheritance

### Estilo

    style50 inheritance.c

## Como enviar

    submit50 cs50/problems/2024/x/inheritance

