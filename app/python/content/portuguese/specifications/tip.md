# Calculadora de Gorjeta

> E agora, para a minha calculadora de gorjeta de bruxo.
>
> — Morty Seinfeld

Nos Estados Unidos, é costume deixar uma gorjeta para o garçom depois de comer em um restaurante, normalmente um valor igual a 15% ou mais do custo da sua refeição. Mas não se preocupe, nós escrevemos uma calculadora de gorjeta para você, logo abaixo!

    def main():
        dolares = dolares_para_float(input("Quanto custou a refeição? "))
        percentual = percentual_para_float(input("Qual porcentagem você gostaria de dar de gorjeta? "))
        gorjeta = dolares * percentual
        print(f"Deixe ${gorjeta:.2f}")


    def dolares_para_float(d):
        # TODO


    def percentual_para_float(p):
        # TODO


    main()

Bem, nós escrevemos _a maior parte_ de uma calculadora de gorjeta para você. Infelizmente, não tivemos tempo de implementar duas funções:

- `dolares_para_float`, que deveria aceitar uma `str` como entrada (formatada como `$##.##`, em que cada `#` é um dígito decimal), remover o `$` inicial, e retornar o valor como `float`. Por exemplo, dado `$50.00` como entrada, deve retornar `50.0`.
- `percentual_para_float`, que deveria aceitar uma `str` como entrada (formatada como `##%`, em que cada `#` é um dígito decimal), remover o `%` final, e retornar a porcentagem como `float`. Por exemplo, dado `15%` como entrada, deve retornar `0.15`.

Assuma que o usuário fornecerá os valores nos formatos esperados.

Dicas

- Lembre-se que `input` retorna uma `str`, conforme [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Lembre-se que `float` pode converter uma `str` em um `float`, conforme [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float).
- Lembre-se que uma `str` possui vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se parecerá com o seguinte:

    $

Em seguida, execute

    mkdir tip

para criar uma pasta chamada `tip` no seu espaço de códigos.

Depois execute

    cd tip

para mudar para dentro dessa pasta. Agora seu prompt de terminal deve ser `tip/ $`. Você pode então executar

    code tip.py

para criar um arquivo chamado `tip.py`. Copie e cole o código acima em um arquivo e complete as implementações de `dolares_para_float` e `percentual_para_float`, substituindo cada `TODO` por uma ou mais linhas do seu próprio código.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python tip.py`. Digite `$50.00` e pressione Enter. Em seguida, digite `15%` e pressione Enter. Seu programa deve exibir:

      Deixe $7.50

- Execute seu programa com `python tip.py`. Digite `$100.00` e pressione Enter. Em seguida, digite `18%` e pressione Enter. Seu programa deve exibir:

      Deixe $18.00

- Execute seu programa com `python tip.py`. Digite `$15.00` e pressione Enter. Em seguida, digite `25%` e pressione Enter. Seu programa deve exibir

      Deixe $3.75

Você pode executar o comando abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código ao enviar. Mas certifique-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/tip

Os smilies verdes significam que seu programa passou em um teste! As carinhas tristes vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` fornece para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava, e qual saída seu programa realmente gerou.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/tip
