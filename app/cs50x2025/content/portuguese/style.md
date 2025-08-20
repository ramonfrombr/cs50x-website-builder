# Guia de Estilo para C

Não existe uma única maneira correta de estilizar código. Mas há com certeza muitas maneiras erradas (ou, pelo menos, ruins). Mesmo assim, o CS50 pede que você siga as convenções abaixo para que possamos analisar de forma confiável o estilo do seu código. Da mesma forma, as empresas costumam adotar suas próprias convenções de estilo para toda a empresa.

## Comprimento da Linha

Por convenção, o comprimento máximo de uma linha de código é de 80 caracteres em C, que é historicamente baseado em monitores de tamanho padrão em terminais de computador mais antigos, que podiam exibir 24 linhas verticalmente e 80 caracteres horizontalmente. Embora a tecnologia moderna tenha tornado obsoleta a necessidade de manter as linhas com até 80 caracteres, ela ainda é uma orientação que deve ser considerada um "soft stop" e uma linha de 100 caracteres deve realmente ser o máximo que você escreve em C, caso contrário, os leitores geralmente precisarão rolar para baixo. Se você precisar de mais de 100 caracteres, pode ser hora de repensar seus nomes de variáveis ou seu design geral!

    // Estas próximas linhas de código primeiro solicitam ao usuário que forneça dois valores inteiros e então multiplicam esses dois valores inteiros, para que possam ser usados mais tarde no programa
    int primeiro_valor_inteiro_coletado_do_usuario = get_int("Inteiro, por favor: ");
    int segundo_valor_inteiro_coletado_do_usuario = get_int("Outro inteiro, por favor: ");
    int produto_dos_dois_valores_inteiros_do_usuario = primeiro_valor_inteiro_coletado_do_usuario * segundo_valor_inteiro_coletado_do_usuario;

Em outras linguagens, particularmente JavaScript, é significativamente mais difícil restringir linhas a um comprimento máximo; lá, seu objetivo deve ser quebrar linhas (como via `\n`) em locais que maximizem a legibilidade e a clareza.

## Comentários

Os comentários tornam o código mais legível, não apenas para outros (por exemplo, seu TF), mas também para você, especialmente quando horas, dias, semanas, meses ou anos se passam entre escrever e ler seu próprio código. Comentar muito pouco é ruim. Comentar muito é ruim. Onde está o ponto ideal? Comentar cada poucas linhas de código (ou seja, blocos interessantes) é uma orientação decente. Tente escrever comentários que abordem uma ou ambas as seguintes questões:

1. O que este bloco faz?
2. Por que implementei este bloco desta forma?

Dentro das funções, use "comentários embutidos" e mantenha-os curtos (por exemplo, uma linha), caso contrário, torna-se difícil distinguir os comentários do código, mesmo com [realce de sintaxe](http://pt.wikipedia.org/wiki/Realce_de_sintaxe). Coloque o comentário acima da(s) linha(s) à(s) qual(is) ele se aplica. Não há necessidade de escrever frases completas, mas capitalize a primeira palavra do comentário (a menos que seja o nome de uma função, variável ou algo parecido) e deixe um espaço entre `//` e o primeiro caractere do seu comentário, como em:

    // Converte Fahrenheit em Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Em outras palavras, não faça isso:

    //converte Fahrenheit em Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou isso:

    // converte Fahrenheit em Celsius
    float c = 5.0 / 9.0 * (f - 32.0);

Ou isso:

    float c = 5.0 / 9.0 * (f - 32.0); // Converte Fahrenheit em Celsius

Acima de seus arquivos .c e .h deve haver um comentário que resuma o que seu programa (ou aquele arquivo em particular) faz, como em:

    // Diz olá para o mundo

Acima de cada uma de suas funções (exceto, talvez, `main`), por outro lado, deve haver um comentário que resuma o que sua função está fazendo, como em:

    // Retorna o quadrado de n
    int quadrado(int n)
    {
        return n * n;
    }

## Cabeçalhos de Bibliotecas

Todos os cabeçalhos de biblioteca que você incluir devem ser listados em ordem alfabética, como em:

    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

Isso torna mais fácil ver rapidamente, especialmente em uma lista longa, se você incluiu um cabeçalho.

## Condições

As condições devem ser estilizadas da seguinte forma:

    if (x > 0)
    {
        printf("x é positivo\n");
    }
        else if (x < 0)
    {
        printf("x é negativo\n");
    }
    else
    {
        printf("x é zero\n");
    }

Observe como:

- as chaves se alinham bem, cada uma em sua própria linha, deixando perfeitamente claro o que está dentro da ramificação;
- há um único espaço após cada `if`;
- cada chamada para `printf` é recuada com 4 espaços;
- há espaços simples ao redor de `>` e ao redor de `<`; e
- não há nenhum espaço imediatamente após cada `(` ou imediatamente antes de cada `)`.

Para economizar espaço, alguns programadores gostam de manter a primeira chave na mesma linha que a própria condição, mas não recomendamos, pois é mais difícil de ler, então não faça isso:

    if (x < 0) {
        printf("x é negativo\n");
    } else if (x < 0) {
        printf("x é negativo\n");
    }

E definitivamente não faça isso:

    if (x < 0)
        {
        printf("x é negativo\n");
        }
    else
        {
        printf("x é negativo\n");
        }

## Chaves

Declare uma `escolha` do seguinte modo:

    switch (n)
    {
        case -1:
            printf("n é -1\n");
            break;

        case 1:
            printf("n é 1\n");
            break;

        default:
            printf("n não é -1 nem 1\n");
            break;
    }

Observe como:

- cada chave está em uma linha separada;
- há um único espaço após `switch`;
- não há nenhum espaço imediatamente após cada `(` ou imediatamente antes de cada `)`;
- os casos da chave são recuados com 4 espaços;
- os corpos dos casos são recuados ainda mais com 4 espaços; e
- cada `caso` (incluindo `padrão`) termina com um `break`.

## Funções

De acordo com o [C99](http://pt.wikipedia.org/wiki/C99), certifique-se de declarar `main` com:

    int main(void)
    {

    }

ou, se usar a Biblioteca CS50, com:

    #include <cs50.h>

    int main(int argc, string argv[])
    {

    }

ou com:

    int main(int argc, char *argv[])
    {

    }

ou mesmo com:

    int main(int argc, char **argv)
    {

    }

Não declare `main` com:

    int main()
    {

    }

ou com:

    void main()
    {

    }

ou com:

    main()
    {

    }

Quanto às suas próprias funções, certifique-se de defini-las de forma semelhante, com cada chave em sua própria linha e com o tipo de retorno na mesma linha que o nome da função, assim como fizemos com `main`.

## Identar

Identem seu código quatro espaços por vez para deixar claro quais blocos de código estão dentro de outros. Se você usar a tecla Tab do seu teclado para fazer isso, certifique-se de que o editor de texto esteja configurado para converter tabulações (`\t`) em quatro espaços, caso contrário, seu código pode não ser impresso ou exibido corretamente no computador de outra pessoa, pois `\t` é renderizado de forma diferente em diferentes editores. (Se usar o [CS50 IDE](https://ide.cs50.io/), não há problema em usar Tab para identar, em vez de pressionar a barra de espaço do seu teclado repetidamente, pois pré-configuramos para converter `\t` em quatro espaços.)

Aqui está um código bem identado:

    // Imprime argumentos de linha de comando um por linha
    printf("\n");
    for (int i = 0; i < argc; i++)
    {
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            printf("%c\n", argv[i][j]);
        }
        

## Loops

### for

Sempre que você precisar de variáveis temporárias para iteração, use `i`, depois `j`, depois `k`, a menos que nomes mais específicos tornem o seu código mais legível:

    for (int i = 0; i < LIMIT; i++)
    {
        for (int j = 0; j < LIMIT; j++)
        {
            for (int k = 0; k < LIMIT; k++)
            {
                // Faça algo
            }
        }
    }

Se você precisar de mais de três variáveis para iteração, talvez seja hora de repensar seu design!

### while

Declare laços `while` da seguinte forma:

    while (condição)
    {
        // Faça algo
    }

Observe como:

- cada chave está em sua própria linha;
- há um único espaço após `while`;
- não há nenhum espaço imediatamente após o `(` ou imediatamente antes do `)`; e
- o corpo do laço (um comentário neste caso) é recuado com 4 espaços.

### do … while

Declare laços `do ... while` da seguinte forma:

    do
    {
        // Faça algo
    }
    while (condição);

Observe como:

- cada chave está em sua própria linha;
- há um único espaço após `while`;
- não há nenhum espaço imediatamente após o `(` ou imediatamente antes do `)`; e
- o corpo do laço (um comentário neste caso) é recuado com 4 espaços.

## Ponteiros

Ao declarar um ponteiro, escreva o `*` ao lado da variável, como em:

    int *p;

Não escreva ao lado do tipo, como em:

    int* p;

## Variáveis

Como o CS50 usa [C99](http://en.wikipedia.org/wiki/C99), não defina todas as suas variáveis no topo de suas funções, mas sim quando e onde você realmente precisa delas. Além disso, restrinja o escopo de suas variáveis o máximo possível. Por exemplo, se `i` for necessário apenas para um laço, declare `i` dentro do próprio laço:

    for (int i = 0; i < LIMIT; i++)
    {
        printf("%i\n", i);
    }

Embora seja normal usar variáveis como `i`, `j` e `k` para iteração, a maioria de suas variáveis deve ter nomes mais específicos. Se você está somando alguns valores, por exemplo, chame sua variável de `soma`. Se o nome da sua variável justificar duas palavras (por exemplo, `está_pronto`), coloque um sublinhado entre elas, uma convenção popular em C, embora menos em outras linguagens.

Se declarar várias variáveis do mesmo tipo de uma vez, é correto declará-las juntas, como em:

    int quartos, moedas_de_dez_centavos, moedas_de_cinco_centavos, centavos;

Apenas não inicialize algumas, mas não outras, como em:

    int quartos, moedas_de_dez_centavos = 0, moedas_de_cinco_centavos = 0 , centavos;

Também tome cuidado para declarar ponteiros separadamente de não ponteiros, como em:

    int *p;
    int n;

Não declare ponteiros na mesma linha que não ponteiros, como em:

    int *p, n;

## Estruturas

Declare uma `struct` como um tipo da seguinte forma, com cada chave em sua própria linha e membros recuados nela, com o nome do tipo também em sua própria linha:

    typedef struct
    {
        string nome;
        string dormitório;
    }
    aluno;

Se a `struct` contiver como membro um ponteiro para outra `struct`, declare a `struct` como tendo um nome idêntico ao tipo, sem usar sublinhados:

    typedef struct nó
    {
        int n;
        struct nó *próximo;
    }
    nó;

