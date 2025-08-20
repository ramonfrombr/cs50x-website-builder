# Dinheiro

## Problema a Ser Solucionado

Em um arquivo chamado `cash.py` em uma pasta chamada `sentimental-cash`, escreva um programa que pergunta ao usuário quanto troco é devido e então divide o valor no menor número de moedas possível que pode ser usado para efetuar o pagamento. Você pode fazer isso exatamente como foi feito no [Conjunto de Problemas 1](../../1/), exceto que desta vez seu programa deve ser escrito em Python, e você deve presumir que o usuário informará o troco em dólares (por exemplo, 0,50 dólares em vez de 50 centavos).

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-eoFGGVR2gwl2jvyj7sHchxUmW" src="https://asciinema.org/a/eoFGGVR2gwl2jvyj7sHchxUmW.js"></script>

## Especificação

- Use `get_float` da CS50 Library para obter a entrada do usuário e `print` para exibir sua resposta. Presuma que as únicas moedas disponíveis são moedas de 25 centavos, 10 centavos, 5 centavos e 1 centavo.
  - Pedimos que você use `get_float` para conseguir lidar com dólares e centavos, embora sem o símbolo de cifrão. Em outras palavras, se algum cliente deve receber $ 9,75 (como no caso de um jornal custar 25 centavos, mas o cliente pagar com uma nota de $ 10), presuma que a entrada do seu programa será `9,75` e não `$ 9,75` ou `975`. No entanto, se algum cliente deve receber $ 9 exatamente, presuma que a entrada do seu programa será `9,00` ou apenas `9`, mas, novamente, não `$ 9` ou `900`. Claro que, devido à natureza dos valores de ponto flutuante, seu programa provavelmente funcionará também com entradas como `9,0` e `9,000`; você não precisa se preocupar em verificar se a entrada do usuário está "formatada" como o dinheiro deveria ser.
- Se o usuário não fornecer um valor não negativo, seu programa deve pedir ao usuário um valor válido novamente e novamente até que o usuário obedeça.
- A propósito, para que possamos automatizar alguns testes de seu código, pedimos que a última linha de saída de seu programa seja apenas o menor número possível de moedas: um número inteiro seguido por uma nova linha.

## Como Testar

Apesar de `check50` estar disponível para este problema, encorajamos você a testar seu código primeiro por conta própria para cada um dos seguintes.

- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `0,41` e pressione enter. Seu programa deve produzir `4`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `0,01` e pressione enter. Seu programa deve produzir `1`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `0,15` e pressione enter. Seu programa deve produzir `2`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `1,60` e pressione enter. Seu programa deve produzir `7`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `23` e pressione enter. Seu programa deve produzir `92`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `4,2` e pressione enter. Seu programa deve produzir `18`.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `-1` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Digite `foo` e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando que o usuário digite outro número.
- Execute seu programa como `python cash.py` e aguarde por uma solicitação de entrada. Não digite nada e pressione enter. Seu programa deve rejeitar esta entrada como inválida, solicitando que o usuário digite outro número.

### Exatidão

    check50 cs50/problems/2024/x/sentimental/cash

### Estilo

    style50 cash.py

## Como Enviar

    submit50 cs50/problems/2024/x/sentimental/cash