## Mario

![capitura de tela do Mario pulando uma pirâmide](https://cs50.harvard.edu/x/2024/psets/6/mario/less/pyramid.png)

## Problema a resolver

Em um arquivo chamado `mario.py` em uma pasta chamada `sentimental-mario-less`, escreva um programa que recrie uma semi-pirâmide usando cerquilhas (`#`) como blocos, exatamente como você fez no [Problema 1](../../../1/). Desta vez, o programa deve ser escrito em Python!

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-sUSilCTveD7JTV2lOZ7eIqKbo" src="https://asciinema.org/a/sUSilCTveD7JTV2lOZ7eIqKbo.js"></script>

## Especificação

- Para tornar as coisas mais interessantes, primeiro pergunte ao usuário usando `get_int` pela altura da semi-pirâmide, um número inteiro positivo entre `1` e `8`, inclusive.
- Se o usuário não fornecer um número inteiro positivo menor ou igual a `8`, você deve perguntar novamente.
- Depois, gere (com a ajuda de `print` e um ou mais loops) a semi-pirâmide desejada.
- Tenha o cuidado de alinhar o canto inferior esquerdo da sua semi-pirâmide com a borda esquerda da janela do seu terminal.

## Como testar

Embora o `check50` esteja disponível para este problema, você é encorajado a testar seu código por conta própria primeiro para cada um dos seguintes.

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `-1` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `0` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `1` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

        #

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

         #
        ##

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `8` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

               #
              ##
             ###
            ####
           #####
          ######
         #######
        ########

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `9` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número. Depois, digite `2` e pressione enter. Seu programa deve gerar a saída abaixo. Certifique-se de que a pirâmide esteja alinhada com o canto inferior esquerdo do seu terminal e que não haja espaços extras no final de cada linha.

         #
        ##

- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Digite `foo` e pressione enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python mario.py` e aguarde uma solicitação de entrada. Não digite nada e pressione enter. Seu programa deve rejeitar essa entrada como inválida, solicitando que o usuário digite outro número.

### Correção

    check50 cs50/problems/2024/x/sentimental/mario/less

### Estilo

    style50 mario.py

## Como enviar

    submit50 cs50/problems/2024/x/sentimental/mario/less