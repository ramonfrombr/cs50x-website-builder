# Segundo turno

## Problema a resolver

Você já conhece as eleições por pluralidade, que seguem um algoritmo muito simples para determinar o vencedor de uma eleição: cada eleitor ganha um voto e vence o candidato com maior número de votos.

Mas o voto plural tem algumas desvantagens. O que acontece, por exemplo, em uma eleição com três candidatos e as cédulas abaixo são lançadas?

![Cinco cédulas, empate entre Alice e Bob](https://cs50.harvard.edu/x/2024/psets/3/fptp_ballot_1.png)

Um voto plural declararia aqui um empate entre Alice e Bob, pois cada um tem dois votos. Mas esse é o resultado certo?

Existe outro tipo de sistema de votação conhecido como sistema de votação por ordem de preferência. Em um sistema de votação por ordem de preferência, os eleitores podem votar em mais de um candidato. Em vez de apenas votar em sua primeira escolha, eles podem classificar os candidatos em ordem de preferência. As cédulas resultantes podem, portanto, se parecer com o abaixo.

![Cinco cédulas com preferências classificadas](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_1.png)

Aqui, cada eleitor, além de especificar seu candidato de primeira preferência, também indicou sua segunda e terceira escolhas. E agora, o que antes era uma eleição empatada poderia ter um vencedor. A corrida estava originalmente empatada entre Alice e Bob, então Charlie estava fora da disputa. Mas o eleitor que escolheu Charlie preferia Alice a Bob, então Alice poderia ser declarada vencedora aqui.

A votação por ordem de preferência também pode resolver outra desvantagem potencial da votação por pluralidade. Dê uma olhada nas seguintes cédulas.

![Nove cédulas, com preferências classificadas](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_3.png)

Quem deveria vencer esta eleição? Em uma votação de pluralidade onde cada eleitor escolhe apenas sua primeira preferência, Charlie vence esta eleição com quatro votos contra apenas três para Bob e dois para Alice. Mas a maioria dos eleitores (5 do 9) ficaria mais feliz com Alice ou Bob do que com Charlie. Ao considerar as preferências classificadas, um sistema de votação pode escolher um vencedor que reflita melhor as preferências dos eleitores.

Um desses sistemas de votação por ordem de preferência é o sistema de segundo turno instantâneo. Em uma eleição de segundo turno instantâneo, os eleitores podem classificar quantos candidatos desejarem. Se algum candidato tiver maioria (mais de 50%) dos votos de primeira preferência, esse candidato é declarado vencedor da eleição.

Se nenhum candidato tiver mais de 50% dos votos, então ocorre um "segundo turno instantâneo". O candidato que recebeu o menor número de votos é eliminado da eleição, e qualquer pessoa que originalmente escolheu aquele candidato como sua primeira preferência tem agora sua segunda preferência considerada. Por que fazer isso desta maneira? Efetivamente, isso simula o que teria acontecido se o candidato menos popular não tivesse participado da eleição para começar.

O processo se repete: se nenhum candidato tiver maioria dos votos, o candidato do último lugar é eliminado e quem votou nele votará na sua próxima preferência (que ainda não foi eliminado). Uma vez que um candidato tenha maioria, esse candidato é declarado vencedor.

Parece um pouco mais complicado do que uma votação por pluralidade, não é? Mas sem dúvida tem o benefício de ser um sistema eleitoral em que o vencedor da eleição representa com mais precisão as preferências dos eleitores. Em um arquivo chamado `runoff.c` em uma pasta chamada `runoff`, crie um programa para simular uma eleição de segundo turno.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-4rhSKgaZQsY93RLj0xgu7nwKB" src="https://asciinema.org/a/4rhSKgaZQsY93RLj0xgu7nwKB.js"></script>

## Código de distribuição

### Baixe o código de distribuição

Faça login em [cs50.dev](https://cs50.dev/), clique em sua janela de terminal e execute `cd` sozinho. Você deve descobrir que o prompt de sua janela de terminal se assemelha ao seguinte:

    $

Execute a seguir

    wget https://cdn.cs50.net/2023/fall/psets/3/runoff.zip

para baixar um ZIP chamado `runoff.zip` no seu código-fonte.

Então execute

    unzip runoff.zip

para criar uma pasta chamada `runoff`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm runoff.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd runoff

seguido por Enter para se mover (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    runoff/ $

Se tudo deu certo, você deve executar

    ls

e veja um arquivo chamado `runoff.c`. A execução de `code runoff.c` deve abrir o arquivo onde você digitará seu código para este conjunto de problemas. Caso contrário, refaça seus passos e veja se consegue determinar onde errou!

### Entenda o código em `runoff.c`

Sempre que você for estender a funcionalidade do código existente, é melhor ter certeza de que primeiro o entendeu no seu estado atual.

Veja o topo de `runoff.c` primeiro. Duas constantes são definidas: `MAX_CANDIDATES` para o número máximo de candidatos na eleição, and `MAX_VOTERS` para o número máximo de eleitores na eleição.

    // Máximo de eleitores e candidatos
    #define MAX_VOTERS 100
    #define MAX_CANDIDATES 9

Observe que `MAX_CANDIDATES` é usado para dimensionar um array, `candidates`.

    // Array de candidatos
    candidate candidates[MAX_CANDIDATES];

`candidates` é um array de `candidate`. Em `runoff.c` um `candidate` é uma `struct`. Cada `candidate` tem um campo `string` para seu `name`, um `int` representando o número de `votes` eles tem atualmente, e um valor `bool` chamado `eliminated` que indica se o candidato foi eliminado da eleição. O array `candidates` acompanhará todos os candidatos na eleição.

    // Os candidatos tem nome, contagem de votos e status de eliminação
    typedef struct
    {
        string name;
        int votes;
        bool eliminated;
    }
    candidate;

Agora você pode entender melhor as `preferences`, o array bidimensional. O array `preferences[i]` representará todas as preferências para o eleitor número `i`. O inteiro, `preferences[i][j]`, armazenará o índice do candidato, do array `candidates`, que é a `j`-ésima preferência do eleitor `i`.

    // preferences[i][j] é a j-ésima preferência para o eleitor i
    int preferences[MAX_VOTERS][MAX_CANDIDATES];

O programa também tem duas variáveis globais: `voter_count` e `candidate_count`.

    // Número de eleitores e candidatos
    int voter_count;
    int candidate_count;

Agora para `main`. Observe que após determinar o número de candidatos e o número de eleitores, o loop de votação principal começa, dando a cada eleitor uma chance de votar. Quando o eleitor entra em suas preferências, a função `vote` é chamada para manter o controle de todas as preferências. Se em algum momento, a cédula for considerada inválida, o programa é encerrado.

Assim que todos os votos são contados, outro loop começa: este continuará passando pelo processo de segundo turno para verificar um vencedor e eliminar o último candidato até que haja um vencedor.

A primeira chamada aqui é para uma função chamada `tabulate`, que deve observar todas as preferências dos eleitores e calcular o total atual de votos, olhando para o candidato de primeira escolha de cada eleitor que ainda não foi eliminado. Em seguida, a função `print_winner` deve imprimir o vencedor se houver um; se houver o programa acabou. Mas, caso contrário, o programa precisa determinar o menor número de votos que qualquer pessoa ainda na eleição recebeu (por meio de uma chamada para `find_min`). Se acontecer de todos na eleição estarem empatados com o mesmo número de votos (conforme determinado pela função `is_tie`), a eleição é declarada empatada; caso contrário, o candidato (ou candidatos) do último lugar é eliminado da eleição por meio de uma chamada para a função `eliminate`.

Se você olhar um pouco mais abaixo no arquivo, verá que o resto das funções—`vote`, `tabulate`, `print_winner`, `find_min`, `is_tie`, e `eliminate`—restam para você completar! **Você não deve modificar nada em `runoff.c` além disso (e a inclusão de cabeçalhos adicionais, se você quiser).**

## Dicas

### Complete a função `vote`

- A função leva três argumentos: `voter`, `rank` e `name`.
- Se `name` corresponder ao nome de um candidato válido, você deve atualizar o array de preferências global para indicar que o eleitor `voter` tem aquele candidato como sua preferência de `rank`. Lembre-se de que `0` é a primeira preferência, `1` é a segunda preferência, etc. Você pode presumir que nenhum dois candidatos terão o mesmo nome.
- Se a preferência for registrada com sucesso, a função deve retornar `true`. Caso contrário, a função deve retornar `false`. Considere, por exemplo, quando `name` não é o nome de um dos candidatos.

Ao escrever seu código, considere estas dicas:

- Lembre-se que `candidate_count` armazena o número de candidatos na eleição.
- Lembre-se que você pode usar [`strcmp`](https://man.cs50.io/3/strcmp) para comparar duas strings.
- Lembre-se que `preferences[i][j]` armazena o índice do candidato que é a `j`-ésima preferência para o `i`-ésimo eleitor.

### Complete a função `tabulate`

- A função deve atualizar o número de ` votos` que cada candidato tem neste estágio do segundo turno.
- Lembre-se de que em cada estágio do segundo turno, cada eleitor efetivamente vota no seu candidato de maior preferência que ainda não foi eliminado.

Ao escrever o código, considere essas dicas:

- Lembre-se de que `voter_count` armazena o número de eleitores na eleição e que, para cada eleitor em nossa eleição, queremos contar um boletim de voto.
- Lembre-se de que para um eleitor 'i', o candidato de sua primeira escolha é representado por  `preferences[i][0]`, o candidato de sua segunda escolha por `preferences[i][1]`, etc.
- Lembre-se de que a ` candidate` `struct` tem um campo chamado `eliminated`, que será 'true' se o candidato foi eliminado da eleição.
- Lembre-se de que a ` candidato` `struct` tem um campo chamado `votos`, que você provavelmente desejará atualizar para o candidato preferido de cada eleitor.
- Lembre-se de que depois de dar um voto para o primeiro candidato não eliminado de um eleitor, você deve parar por aí, não continuar sua votação. Você pode sair de um loop mais cedo usando 'break' dentro de um condicional.

### Complete a função `print_winner`

- Se algum candidato tiver mais da metade dos votos, seu nome deve ser impresso e a função deve retornar 'true'.
- Se ninguém ganhou a eleição ainda, a função deve retornar `false`.

Ao escrever o código, considere esta dica:

- Lembre-se de que `voter_count` armazena o número de eleitores na eleição. Diante disso, como você expressaria o número de votos necessários para vencer a eleição?

### Complete a função `find_min`

- A função deve retornar o total mínimo de votos para qualquer candidato que ainda esteja na eleição.

Ao escrever o código, considere esta dica:

- Você provavelmente desejará percorrer os candidatos para encontrar aquele que ainda está na eleição e tem o menor número de votos. Quais informações você deve acompanhar ao percorrer os candidatos?

### Complete a função `is_tie`

- A função recebe um argumento `min`, que será o número mínimo de votos que qualquer pessoa na eleição atualmente tem.
- A função deve retornar `true` se cada candidato restante na eleição tiver o mesmo número de votos e deve retornar `false` caso contrário.

Ao escrever o código, considere esta dica:

- Lembre-se de que há um empate se cada candidato ainda na eleição tiver o mesmo número de votos. Observe também que a função `is_tie` recebe um argumento `min`, que é o menor número de votos que qualquer candidato tem atualmente. Como você pode usar `min` para determinar se a eleição está empatada (ou, inversamente, não empatada)?

### Complete a função `eliminate`

- A função recebe um argumento `min`, que será o número mínimo de votos que qualquer pessoa na eleição atualmente tem.
- A função deve eliminar o candidato (ou candidatos) que tiver `min` número de votos.

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar.

Certifique-se de testar seu código para garantir que ele lida com...

- Uma eleição com qualquer número de candidatos (até o 'MAX' de '9')
- Votação em um candidato pelo nome
- Votos inválidos para candidatos que não estão na cédula
- Imprimir o vencedor da eleição se houver apenas um
- Não eliminar ninguém no caso de empate entre todos os candidatos restantes

### Correção

    check50 cs50/problems/2024/x/runoff

### Estilo

    style50 runoff.c

## Como enviar

    submit50 cs50/problems/2024/x/runoff

