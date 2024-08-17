# Dinheiro

![Moedas dos EUA](https://cs50.harvard.edu/x/2024/psets/1/cash/coins.jpg)

## Problema a Resolver

Suponha que você trabalhe em uma loja e um cliente lhe dê US$1,00 (100 centavos) por um doce que custa US$0,50 (50 centavos). Você precisará pagar o "troco" a ele, a quantia que sobrar após pagar pelo custo do doce. Ao calcular o troco, é provável que você queira minimizar o número de moedas que está entregando para cada cliente, para não ficar sem (ou irritar o cliente!). Em um arquivo chamado `cash.c` em uma pasta chamada `cash`, implemente um programa em C que imprima o mínimo de moedas necessárias para fazer a determinada quantia do troco, em centavos, como abaixo:

    Troco devido: 25
    1

Mas peça ao usuário um número inteiro maior que 0, para que o programa funcione para qualquer valor de troco:

    Troco devido: 70
    4

Pergunte novamente ao usuário, quantas vezes for necessário, se a entrada não for maior ou igual a 0 (ou se a entrada não for um número inteiro!).

## Demonstração

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-p6PlFqQgSWNWn4ggpIIaBOvIq" src="https://asciinema.org/a/p6PlFqQgSWNWn4ggpIIaBOvIq.js"></script>

## Algoritmos Gulosos

Felizmente, a ciência da computação deu aos caixas de todo lugar maneiras de minimizar o número de moedas devidas: algoritmos gulosos.

De acordo com o National Institute of Standards and Technology (NIST), um algoritmo guloso é aquele "que sempre pega a melhor solução imediata ou local ao encontrar uma resposta. Algoritmos gulosos encontram a solução geral ou globalmente ideal para alguns problemas de otimização, mas podem encontrar soluções abaixo do ideal para alguns casos de outros problemas".

O que isso significa? Bem, suponha que um caixa deva dar algum troco a um cliente e que na gaveta desse caixa haja moedas de 25 centavos, 10 centavos, 5 centavos e 1 centavo. O problema a ser resolvido é decidir quais moedas e quantas de cada uma entregar ao cliente. Pense em um caixa "guloso" como aquele que deseja tirar o maior pedaço possível desse problema a cada moeda que tira da gaveta. Por exemplo, se algum cliente receber 41 centavos, o maior pedaço inicial (ou seja, a melhor solução imediata ou local) que pode ser tirado é de 25 centavos. (Esse pedaço é "melhor" na medida em que nos aproxima de 0 centavos mais rápido do que qualquer outra moeda faria.) Observe que um pedaço desse tamanho reduziria o que era um problema de 41 centavos para um problema de 16 centavos, já que 41 - 25 = 16. Ou seja, o restante é um problema semelhante, mas menor. Nem é preciso dizer que outro pedaço de 25 centavos seria muito grande (assumindo que o caixa prefira não perder dinheiro) e, portanto, nosso caixa guloso passaria para um pedaço de 10 centavos, deixando-o com um problema de 6 centavos. Nesse ponto, a ganância pede uma mordida de 5 centavos seguida de uma mordida de 1 centavo, e o problema é resolvido. O cliente recebe uma moeda de 25 centavos, uma de 10 centavos, uma de 5 centavos e uma de 1 centavo: quatro moedas no total.

Acontece que essa abordagem gulosa (ou seja, algoritmo) não é apenas localmente ideal, mas também globalmente para a moeda dos Estados Unidos (e também da União Europeia). Ou seja, contanto que um caixa tenha moedas suficientes de cada tipo, essa abordagem da maior para a menor gerará o menor número possível de moedas. Quão pouco? Bem, você nos diga!

## Conselhos

### Escreva algum código que você sabe que será compilado

Mesmo que este programa não faça nada, ele deve pelo menos ser compilado com `make`!

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

Observe que você agora incluiu `cs50.h` e `stdio.h`, dois "arquivos de cabeçalho" que lhe darão acesso a funções que podem ajudá-lo a resolver este problema.

### Escreva algum pseudocódigo antes de escrever mais código

Se não tiver certeza de como resolver o problema em si, divida-o em problemas menores que você provavelmente pode resolver primeiro. Por exemplo, este problema é realmente apenas um punhado de problemas:

1.  Peça ao usuário o troco devido, em centavos.
2.  Calcule quantas moedas de _vinte e cinco centavos_ você deve dar ao cliente. Subtraia o valor dessas moedas de vinte e cinco centavos dos centavos.
3.  Calcule quantas moedas de _dez centavos_ você deve dar ao cliente. Subtraia o valor dessas moedas de dez centavos dos centavos restantes.
4.  Calcule quantas moedas de _cinco centavos_ você deve dar ao cliente. Subtraia o valor dessas moedas de cinco centavos dos centavos restantes.
5.  Calcule quantas moedas de _um centavo_ você deve dar ao cliente. Subtraia o valor dessas moedas de um centavo dos centavos restantes.
6.   some o número de moedas de vinte e cinco centavos, dez centavos, cinco centavos e um centavo usadas.
7.  Imprima essa soma.

Este é o algoritmo guloso que você pode usar para resolver este problema, então vamos escrever alguns pseudocódigos como comentários para lembrá-lo de fazer exatamente isso:

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Peça ao usuário o troco devido, em centavos

        // Calcule quantas moedas de vinte e cinco centavos você deve dar ao cliente
        // Subtraia o valor dessas moedas de vinte e cinco centavos dos centavos

        // Calcule quantas moedas de dez centavos você deve dar ao cliente
        // Subtraia o valor dessas moedas de dez centavos dos centavos restantes

        // Calcule quantas moedas de cinco centavos você deve dar ao cliente
        // Subtraia o valor dessas moedas de cinco centavos dos centavos restantes

        // Calcule quantas moedas de um centavo você deve dar ao cliente
        // Subtraia o valor dessas moedas de um centavo dos centavos restantes

        // Some o número de moedas de vinte e cinco centavos, dez centavos, cinco centavos e um centavo usadas
        // Imprima essa soma
    }

### Converta o pseudocódigo em código

Primeiro, considere como você pode perguntar ao usuário os centavos que lhe devem. Lembre-se de que um loop `do while` é útil quando você quer fazer algo pelo menos uma vez e possivelmente de novo e de novo, como abaixo:

```C
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Pergunta ao usuário o troco devido em centavos
    int cents;
    do
    {
        cents = get_int("Troco devido: ");
    }
    while (cents < 0);
}
```

É aconselhável parar aqui e `make` o seu programa. Teste para ter certeza que o seu programa compila e que ele pergunta novamente se você digitar menos de 0 centavos (ou se você digitar uma entrada como “cat”).

Em seguida, considere como calcular quantos quarters você deve dar ao cliente. Como estamos usando um algoritmo ganancioso, esta questão se torna “qual é o _maior_ número de quarters que você poderia dar a eles?”. Você _poderia_ escrever uma solução para este problema na sua função `main`. Mas poderia clarear o seu pensamento escrever uma nova função: uma chamada `calculate_quarters`. Assim você pode se concentrar melhor na lógica para calcular quarters. Mais tarde, você pode integrar esta função em sua solução maior.

```C
int calculate_quarters(int cents)
{
    // Calcula quantos quarters você deve dar ao cliente
}
```

Perceba que esta função é realmente chamada de `calculate_quarters`. Por `int cents` em parênteses, ela pega um `int` chamado `cents` como entrada. E, por `int` na frente do seu nome, ela também deve “retornar” um `int`. Ou seja, a saída desta função é um número inteiro: o número de quarters que cabem em cents. Se estiver curioso sobre esta ideia, lembre-se de que há vários programas de amostra no [Código Fonte](https://github.com/cs50/lectures/tree/2023/fall/1/src1) da Semana 1 que ilustram como funções podem retornar um valor.

Agora considere esta forma de implementar `calculate_quarters` adicionando ao número de quarters até acabarmos os centavos para converter em quarters:

```C
int calculate_quarters(int cents)
{
    // Calcula quantos quarters você deve dar ao cliente
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Claro, há pelo menos uma maneira mais simples de resolver este problema `calculate_quarters`. Mas vamos deixar você descobrir isso!

Com `calculate_quarters` funcionando como pretendido, você pode integrar esta função em seu programa. Declare a “assinatura” da função (ou seja, `int calculate_quarters(int cents)`) acima da sua função `main`, para que você possa realmente usar `calculate_quarters` lá enquanto define depois, abaixo de `main`.

```C
#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);

int main(void)
{
    // Pergunta ao usuário o troco devido em centavos
    int cents;
    do
    {
        cents = get_int("Troco devido: ");
    }
    while (cents < 0);

    // Calcula quantos quarters você deve dar ao cliente
    int quarters = calculate_quarters(cents);

    // Subtrai o valor desses quarters de cents
    cents = cents - (quarters * 25);
}

int calculate_quarters(int cents)
{
    // Calcula quantos quarters você deve dar ao cliente
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Poucos problemas resolvidos e mais alguns para resolver! Percebeu um padrão que você poderia reutilizar aqui?

## Como testar

Para este programa, tente testar seu código manualmente. É uma boa prática:

- Se você digitar `-1`, o seu programa pergunta novamente?
- Se você digitar `0`, o seu programa imprime `0`?
- Se você digitar `1`, o seu programa imprime `1` (ou seja, um centavo)?
- Se você digitar `4`, o seu programa imprime `4` (ou seja, quatro centavos)?
- Se você digitar `5`, o seu programa imprime `1` (ou seja, um níquel)?
- Se você digitar `24`, o seu programa imprime `6` (ou seja, duas moedas de dez centavos e quatro centavos)?
- Se você digitar `25`, o seu programa imprime `1` (ou seja, um quarter)?
- Se você digitar `26`, o seu programa imprime `2` (ou seja, um quarter e um centavo)?
- Se você digitar `99`, o seu programa imprime `9` (ou seja, três quarters, duas moedas de dez centavos e quatro centavos)?

### Correção

No seu terminal, execute o comando abaixo para verificar a correção do seu trabalho.

```
check50 cs50/problems/2024/x/cash
```

### Estilo

Execute o comando abaixo para avaliar o estilo do seu código usando o `style50`.

```
style50 cash.c
```

## Como enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

```
submit50 cs50/problems/2024/x/cash
```

