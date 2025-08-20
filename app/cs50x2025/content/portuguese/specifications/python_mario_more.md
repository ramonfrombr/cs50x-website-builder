# Mario

![captura de tela do Mario pulando na pirâmide](https://cs50.harvard.edu/x/2024/psets/6/mario/more/pyramids.png)

## Problema a ser resolvido

Em um arquivo chamado `mario.py` em uma pasta chamada `sentimental-mario-more`, escreva um programa que recrie uma meia-pirâmide usando cerquilhas (`#`) para blocos, exatamente como você fez no [Conjunto de problemas 1](../../../1/). Desta vez, seu programa deve ser escrito em Python!

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-B0CE4bjPGR19PoRKUe5ZF9VoM" src="https://asciinema.org/a/B0CE4bjPGR19PoRKUe5ZF9VoM.js"></script>

## Especificação

- Para deixar as coisas mais interessantes, primeiro solicite ao usuário com `get_int` a altura da meia-pirâmide, um número inteiro positivo entre `1` e `8`, inclusive. (A altura das meias-pirâmides ilustradas acima é `4`, a largura de cada meia-pirâmide é `4`, com uma lacuna de tamanho `2` separando-as).
- Se o usuário não fornecer um número inteiro positivo maior que `8`, você deve solicitar o mesmo novamente.
- Em seguida, gere (com a ajuda de `print` e um ou mais loops) as meias-pirâmides desejadas.
- Tome cuidado para alinhar o canto inferior esquerdo da sua pirâmide com a borda esquerda da janela do terminal e certifique-se de que haja dois espaços entre as duas pirâmides e que não haja espaços adicionais após o último conjunto de cerquilhas em cada linha.

## Como testar

Embora `check50` esteja disponível para este problema, você é encorajado a testar seu código por conta própria para cada um dos seguintes.

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `-1` e pressione Enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `0` e pressione Enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `1` e pressione Enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

        #  #

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `2` e pressione Enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

         #  #
        ##  ##

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `8` e pressione Enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

               #  #
              ##  ##
             ###  ###
            ####  ####
           #####  #####
          ######  ######
         #######  #######
        ########  ########

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `9` e pressione Enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número. Em seguida, digite `2` e pressione Enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

         #  #
        ##  ##

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `foo` e pressione Enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Não digite nada e pressione Enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.

### Correção

    check50 cs50/problems/2024/x/sentimental/mario/more

### Estilo

    style50 mario.py

## Como enviar

    submit50 cs50/problems/2024/x/sentimental/mario/more