# Pluralidade

## Problema a Resolver

As eleições variam muito em forma e tamanho. No Reino Unido, o [Primeiro Ministro](https://www.parliament.uk/education/about-your-parliament/general-elections/) é oficialmente nomeado pelo monarca, que geralmente escolhe o líder do partido político que conquistou mais cadeiras na Câmara dos Comuns. Os Estados Unidos usam um processo de [Colégio Eleitoral](https://www.archives.gov/federal-register/electoral-college/about.html) com várias etapas, no qual os cidadãos votam em como cada estado deve alocar eleitores, que então elegem o Presidente.

Porém, talvez a maneira mais simples de realizar uma eleição seja por meio de um método comumente conhecido como "voto por pluralidade" (também conhecido como "primeiro a ultrapassar o posto" ou "vencedor leva tudo"). No voto por pluralidade, cada eleitor vota em um candidato. Ao final da eleição, o candidato que tiver o maior número de votos é declarado vencedor da eleição.

Neste problema, você implementará um programa que realiza uma eleição por pluralidade, conforme abaixo.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o2EXEqiz7iqfDB31wYxBOWjs8" src="https://asciinema.org/a/o2EXEqiz7iqfDB31wYxBOWjs8.js"></script>

## Código de Distribuição

Para este problema, você estenderá a funcionalidade do "código de distribuição" fornecido a você pela equipe do CS50.

### Baixe o código de distribuição

Entre no [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você verá que o prompt da janela do terminal ficará parecido com o abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/3/plurality.zip

para baixar um ZIP chamado `plurality.zip` no seu codespace.

Em seguida, execute

    unzip plurality.zip

para criar uma pasta chamada `pluralidade`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm plurality.zip

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd plurality

seguido de Enter para ir (ou seja, abrir) aquele diretório. Seu prompt agora deve ser parecido com o abaixo.

    plurality/ $

Se tudo der certo, você deve executar

    ls

e ver um arquivo chamado `plurality.c`. Executar `code plurality.c` deve abrir o arquivo no qual você digitará seu código para esta série de problemas. Se não, refaça os passos e veja se consegue determinar onde errou!

### Entenda o código em `plurality.c`

Sempre que você estende a funcionalidade do código existente, é melhor ter certeza de entendê-lo primeiro no seu estado atual.

Olhe primeiro no topo do arquivo. A linha `#define MAX 9` é uma sintaxe usada aqui para significar que `MAX` é uma constante (igual a `9`) que pode ser usada em todo o programa. Aqui, representa o número máximo de candidatos que uma eleição pode ter.

    // Número máximo de candidatos
    #define MAX 9

Observe que `plurality.c` usa essa constante para definir uma matriz global, ou seja, uma matriz que qualquer função pode acessar.

    // Matriz de candidatos
    candidate candidates[MAX];

Mas o que, nesse caso, é um `candidate`? Em `plurality.c`, um `candidate` é uma `struct`. Cada `candidate` tem dois campos: uma `string` chamada `name` que representa o nome do candidato, e um `int` chamado `votes` que representa a quantidade de votos que o candidato tem.

    // Os candidatos têm nome e contagem de votos
    typedef struct
    {
        string name;
        int votes;
    }
    candidate;

Agora, dê uma olhada na própria função `main`. Veja se consegue encontrar onde o programa define uma variável global `candidate_count` que representa o número de candidatos na eleição.

    // Número de candidatos
    int candidate_count;

E quanto a onde copia argumentos da linha de comando para a matriz `candidates`?

    // Popule a matriz de candidatos
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("O número máximo de candidatos é %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

E onde pede ao usuário que digite o número de eleitores?

    int voter_count = get_int("Número de eleitores: ");

Então, o programa deixa cada eleitor digitar um voto, chamando a função `vote` para cada candidato votado. Finalmente, `main` faz uma chamada para a função `print_winner` para imprimir o vencedor (ou vencedores) da eleição. Deixaremos para você identificar o código que implementa essa funcionalidade.

Se você olhar mais para baixo no arquivo, no entanto, notará que as funções `vote` e `print_winner` foram deixadas em branco.

    // Atualize os totais de votos com base em um novo voto
    bool vote(string name)
    {
        // TODO
        return false;
    }

    // Imprima o vencedor (ou vencedores) da eleição
    void print_winner(void)
    {
        // TODO
        return;
    }

Esta parte é sua para concluir! **Você não deve modificar mais nada em `plurality.c` além das implementações das funções `vote` e `print_winner` (e a inclusão de arquivos de cabeçalho adicionais, se desejar).**

## Dicas

### Complete a função `vote`

Agora, complete a função `vote`.

- Considere que a assinatura da `vote`, `bool vote(string name)`, mostra que ela recebe um único argumento, uma `string` chamada `name`, representando o nome do candidato para quem o voto foi dado.
- `vote` deve retornar um `bool`, em que `true` indica que o voto foi computado com sucesso e `false` indica que não foi.

Uma maneira de solucionar este problema é fazer o seguinte:

1.  Iterar por cada candidato
    1.  Verificar se o nome do candidato corresponde à entrada `name`
        1.  Se sim, incrementar os votos do candidato e retornar `true`
        2.  Se não, continuar verificando
2.  Se não houver correspondências após verificar cada candidato, retornar `false`

Vamos escrever um pseudocódigo para lembrar você de fazer exatamente isso:

    // Atualizar o total de votos para um novo voto
    bool vote(string name)
    {
        // Iterar por cada candidato
            // Verificar se o nome do candidato corresponde ao nome fornecido
                // Se sim, incrementar os votos do candidato e retornar true

        // Se não houver correspondência, retornar false
    }

Nós deixaremos a implementação em código por sua conta!

### Complete a função `print_winner`

Finalmente, complete a função `print_winner`.

- A função deve imprimir o nome do candidato que recebeu o maior número de votos na eleição e, em seguida, imprimir uma nova linha.
- A eleição pode terminar em empate se vários candidatos tiverem o número máximo de votos. Nesse caso, você deve imprimir os nomes de cada um dos candidatos vencedores, cada um em uma linha separada.

Você pode pensar que um algoritmo de classificação seria a melhor solução para este problema: imagine classificar os candidatos por seus totais de votos e imprimir o principal candidato (ou candidatos). Lembre-se, no entanto, que a classificação pode ser cara: mesmo o Merge Sort, um dos algoritmos de classificação mais rápidos, roda em \\(O(N \\space log(N))\\).

Considere que você precisa apenas de duas informações para resolver este problema:

1.  O número máximo de votos
2.  O candidato (ou candidatos) com esse número de votos

Dessa forma, uma boa solução pode exigir apenas duas pesquisas. Escreva um pseudocódigo para se lembrar de fazer exatamente isso:

    // Imprimir o vencedor (ou vencedores) da eleição
    void print_winner(void)
    {
        // Encontrar o número máximo de votos

        // Imprimir o candidato (ou candidatos) com o máximo de votos

    }

Mas deixaremos o código para você!

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

Certifique-se de testar seu código para garantir que ele lida com…

- Uma eleição com qualquer número de candidatos (até o `MAX` de `9`)
- Votação para um candidato pelo nome
- Votos inválidos para candidatos que não estão na cédula
- Impressão do vencedor da eleição se houver apenas um
- Impressão do vencedor da eleição se houver vários vencedores

### Correção

    check50 cs50/problems/2024/x/plurality

### Estilo

    style50 plurality.c

## Como enviar

    submit50 cs50/problems/2024/x/plurality

