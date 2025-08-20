# Crédito

## Problema a resolver

Em um arquivo chamado `credit.py` em uma pasta chamada `sentimental-credit`, escreva um programa que solicite ao usuário um número de cartão de crédito e, em seguida, informe (via `print`) se é um número de cartão American Express, MasterCard ou Visa válido, exatamente como você fez no [Conjunto de problemas 1](../../1/). Desta vez, seu programa deve ser escrito em Python!

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QYLr1R1RDLO9QkPF2XFODLkq4" src="https://asciinema.org/a/QYLr1R1RDLO9QkPF2XFODLkq4.js"></script>

## Especificação

- Para que possamos automatizar alguns testes do seu código, pedimos que a última linha de saída do seu programa seja `AMEX\n` ou `MASTERCARD\n` ou `VISA\n` ou `INVALID\n`, nada mais, nada menos.
- Para simplificar, você pode assumir que a entrada do usuário será totalmente numérica (ou seja, desprovida de hífens, como pode ser impresso em um cartão real).
- É melhor usar `get_int` ou `get_string` da biblioteca do CS50 para obter a entrada dos usuários, dependendo de como você decidir implementar este.

## Dicas

- É possível usar expressões regulares para validar a entrada do usuário. Você pode usar o módulo [`re`](https://docs.python.org/3/library/re.html) do Python, por exemplo, para verificar se a entrada do usuário é realmente uma sequência de dígitos com o comprimento correto.

## Como testar

Embora o `check50` esteja disponível para este problema, você é encorajado a testar seu código por conta própria para cada um dos seguintes.

- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `378282246310005` e pressione enter. Seu programa deve gerar `AMEX`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `371449635398431` e pressione enter. Seu programa deve gerar `AMEX`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `5555555555554444` e pressione enter. Seu programa deve gerar `MASTERCARD`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `5105105105105100` e pressione enter. Seu programa deve gerar `MASTERCARD`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `4111111111111111` e pressione enter. Seu programa deve gerar `VISA`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `4012888888881881` e pressione enter. Seu programa deve gerar `VISA`.
- Execute seu programa como `python credit.py` e aguarde um prompt de entrada. Digite `1234567890` e pressione enter. Seu programa deve gerar `INVALID`.

### Correção

    check50 cs50/problems/2024/x/sentimental/credit

### Estilo

    style50 credit.py

## Como enviar

    submit50 cs50/problems/2024/x/sentimental/credit