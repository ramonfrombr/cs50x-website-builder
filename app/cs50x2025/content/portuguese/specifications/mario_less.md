# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problema a resolver

Por perto do final do World 1-1 no jogo [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.) da Nintendo, Mario deve subir uma pirâmide alinhada à direita, como abaixo.

![imagem do Mario pulando em uma pirâmide alinhada à direita](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

No arquivo chamado `mario.c` dentro de uma pasta chamada `mario-less`, implemente um programa em C que recrie a pirâmide, usando cerquilhas (`#`) para os tijolos, como abaixo:

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Mas peça ao usuário por um número inteiro para a altura real da pirâmide, de modo que o programa possa também exibir pirâmides mais curtas como abaixo:

      #
     ##
    ###

Pergunte novamente ao usuário, várias vezes conforme for necessário, caso a entrada não seja superior a 0 ou não seja um número inteiro.

#### Dicas

- Lembre-se de que você consegue um número inteiro de um usuário com `get_int`, que é declarado no `cs50.h`.
- Lembre-se de que você consegue imprimir uma `string` com `printf`, que é declarado no `stdio.h`.

## Demonstração

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-WPrv7PFVLaLkJ2BU96uTEQKuA" src="https://asc
iinema.org/a/WPrv7PFVLaLkJ2BU96uTEQKuA.js"></script>

## Conselho

### Escreva um código que você sabe que vai compilar

Ainda que este programa não faça nada, pelo menos ele deve compilar no `make`!

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

### Escreva um pseudo código antes de escrever mais códigos

Caso você não tenha certeza de como resolver o problema, divida-o em problemas menores que você provavelmente consiga resolver primeiro. Por exemplo, este programa é na verdade dois problemas:

1.  Pedir ao usuário a altura da pirâmide
2.  Imprimir uma pirâmide com essa altura

Então, escreva um pseudo código como comentário, que irá lembrá-lo de fazer exatamente isso:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide

        // Imprimir uma pirâmide com essa altura
    }

### Converta o pseudo código em código

Primeiramente, considere como você pode pedir ao usuário pela altura da pirâmide. Lembre-se de que um laço `do while` é útil quando você quer fazer algo pelo menos uma vez, e provavelmente várias vezes, como abaixo:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
    }

Em segundo lugar, considere como você pode imprimir uma pirâmide com essa altura, de cima para baixo. Perceba como a primeira linha deve ter um tijolo, a segunda linha deve ter dois tijolos e assim por diante. As chances são de que você desejará um laço, como abaixo, ainda que não tenha certeza (por enquanto!) do que colocar dentro desse laço, então adicione um pouco mais de pseudo código como um comentário por enquanto:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
        for (int i = 0; i < n; i++)
        {
            // Imprimir uma linha de tijolos
        }
    }

Como imprimir essa linha de tijolos? Bem, não seria bom se houvesse uma função chamada `print_row` que fizesse exatamente isso? Vamos supor que haja:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
        for (int i = 0; i < n; i++)
        {
            // Imprimir uma linha de tijolos
        }
    }

    void print_row(int bricks)
    {
        // Imprimir uma linha de tijolos
    }

Podemos, então, chamar essa função de `main`, como abaixo:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
        for (int i = 0; i < n; i++)
        {
            // Imprimir uma linha de tijolos
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        // Imprimir uma linha de tijolos
    }

Por que `i + 1`?

Vamos implementar `print_row` agora:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
        for (int i = 0; i < n; i++)
        {
            // Imprimir uma linha de tijolos
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        for (int i = 0; i < bricks; i++)
        {
            printf("#");
        }
        printf("\n");
    }

Por que o `\n` no final?

Infelizmente, este código imprime uma pirâmide alinhada à esquerda, mas você precisa de uma alinhada à direita! Talvez devêssemos imprimir alguns espaços em branco antes de alguns dos tijolos, para movê-los para a direita? Vamos mudar `print_row` da seguinte forma para que ela consiga imprimir as duas coisas:

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int spaces, int bricks);

    int main(void)
    {
        // Perguntar ao usuário a altura da pirâmide
        int n;
        do
        {
            n = get_int("Altura: ");
        }
        while (n < 1);

        // Imprimir uma pirâmide com essa altura
        for (int i = 0; i < n; i++)
        {
            // Imprimir uma linha de tijolos
        }
    }

    void print_row(int spaces, int bricks)
    {
        // Imprimir espaços

        // Imprimir tijolos
    }

Um pouco mais de pseudo código permanece em `main` e `print_row`, então deixamos isso para você!

E pense se você consegue refatorar parte do código em `main` para uma função `get_height` também, que retorna o número inteiro que você precisa!

## Passo a passo

<div class="alert alert-info" data-alert="info" role="alert"><p>Observa que este passo a passo especifica que seu programa deve pedir ao usuário a altura da pirâmide e <em>pedir novamente</em> se o usuário inserir um valor menor que 1 ou maior que 8. A especificação requer apenas pedir novamente ao usuário se ele inserir um valor menor que 1.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

Seu código funciona como esperado quando você insere:

- `-1` ou outros números negativos?
- `0`?
- `1` ou outros números positivos?
- letras ou palavras?
- nenhuma entrada, quando você apenas pressiona Enter?

### Correção

No seu terminal, execute o seguinte para verificar se seu trabalho está correto.

    check50 cs50/problems/2024/x/mario/less

### Estilo

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 mario.c

## Como enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2024/x/mario/less

