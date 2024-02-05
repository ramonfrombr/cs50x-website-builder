## # Einstein

Mesmo que você não tenha estudado física (recentemente ou nunca!), você pode ter ouvido falar que \\(E = mc^2\\), em que \\(E\\) representa energia (medida em joules), \\(m\\) representa massa (medida em quilogramas) e \\(c\\) representa a velocidade da luz (medida aproximadamente como 300000000 metros por segundo), de acordo com [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein) e outros. Essencialmente, a fórmula significa que massa e energia são equivalentes.

Em um arquivo chamado `einstein.py`, implemente um programa em Python que solicite ao usuário uma massa como um número inteiro (em quilogramas) e, em seguida, exiba o número equivalente de joules como um número inteiro. Assuma que o usuário informará um número inteiro.

Dicas

- Lembre-se de que `input` retorna uma `str`, conforme [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Lembre-se de que `int` pode converter uma `str` em um `int`, conforme [docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int).
- Lembre-se de que o Python vem com várias funções internas, conforme [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

## Demonstração

## Antes de começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deverá ver que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir einstein

para criar uma pasta chamada `einstein` em seu espaço de códigos.

Depois, execute

    cd einstein

para mudar para o diretório dessa pasta. Agora você deverá ver seu prompt de terminal como `einstein/ $`. Agora você pode executar

    code einstein.py

para criar um arquivo chamado `einstein.py` onde você escreverá seu programa.

## Como Testar

Aqui está como testar seu código manualmente:

- Execute seu programa com `python einstein.py`. Digite `1` e pressione Enter. Seu programa deve exibir:

      90000000000000000

- Execute seu programa com `python einstein.py`. Digite `14` e pressione Enter. Seu programa deve exibir:

      1260000000000000000

- Execute seu programa com `python einstein.py`. Digite `50` e pressione Enter. Seu programa deve exibir:

      4500000000000000000

Você pode executar o seguinte comando para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo você mesmo também!

    check50 cs50/problems/2022/python/einstein

Carinhas verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite o URL que o `check50` exibe para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o código abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/einstein
