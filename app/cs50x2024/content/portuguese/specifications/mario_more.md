# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problema a ser resolvido

No início do Mundo 1-1 em Super Mario Brothers da Nintendo, Mario deve saltar sobre pirâmides adjacentes de blocos, conforme abaixo.

![Captura de tela do Mario pulando sobre pirâmides adjacentes](https://cs50.harvard.edu/x/2024/psets/1/mario/more/pyramids.png)

Em um arquivo chamado `mario.c` em uma pasta chamada `mario-more`, implemente um programa em C que recria essa pirâmide, usando cerquilhas (`#`) para tijolos, como abaixo:

       #  #
      ##  ##
     ###  ###
    ####  ####

E vamos permitir que o usuário decida qual a altura das pirâmides ao primeiro perguntá-lo um `int` positivo entre, digamos, 1 e 8, inclusive.

#### Exemplos

Veja como o programa pode funcionar se o usuário digitar `8` quando perguntado:

    $ ./mario
    Altura: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Veja como o programa pode funcionar se o usuário digitar `4` quando perguntado:

    $ ./mario
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Veja como o programa pode funcionar se o usuário digitar `2` quando perguntado:

    $ ./mario
    Altura: 2
     #  #
    ##  ##

E veja como o programa pode funcionar se o usuário digitar `1` quando perguntado:

    $ ./mario
    Altura: 1
    #  #

Se o usuário não digitar, de fato, um inteiro positivo entre 1 e 8, inclusive, quando perguntado, o programa deve perguntar novamente ao usuário até que ele colabore:

    $ ./mario
    Altura: -1
    Altura: 0
    Altura: 42
    Altura: 50
    Altura: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Observe que a largura do "espaço" entre as pirâmides adjacentes é igual à largura de duas cerquilhas, independentemente das alturas das pirâmides.

### Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Como testar seu código

Seu código funciona conforme prescrito quando você digita

- `-1` (ou outros números negativos)?
- `0`?
- `1` a `8`?
- `9` ou outros números positivos?
- letras ou palavras?
- nenhuma entrada, quando você apenas pressiona Enter?

Você também pode executar o seguinte para avaliar a correção do seu código usando `check50`. Mas certifique-se de compilá-lo e testá-lo você mesmo também!

### Correção

Em seu terminal, execute o seguinte para verificar a correção do seu trabalho.

    check50 cs50/problems/2024/x/mario/more

### Estilo

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 mario.c

## Como enviar

Em seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2024/x/mario/more