# Voz Interior

ESCREVER EM LETRAS MAIÚSCULAS É COMO GRITAR.

É melhor usar sua "voz interior" às vezes, escrevendo completamente em minúsculas.

Em um arquivo chamado `indoor.py`, implemente um programa em Python que solicita a entrada do usuário e depois exibe essa mesma entrada em minúsculas. Pontuação e espaços em branco devem ser exibidos inalterados. Você é bem-vindo, mas não é obrigatório, solicitar explicitamente a entrada do usuário, passando uma `str` própria como argumento para `input`.

Dicas

- Lembre-se de que `input` retorna uma `str`, conforme [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Lembre-se de que uma `str` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Antes de Começar

Execute `cd` sozinho na janela do seu terminal. Você deverá ver que o prompt da janela do terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir indoor

para criar uma pasta chamada `indoor` no seu espaço de códigos.

Depois, execute

    cd indoor

para mudar de diretório para essa pasta. Agora, você deverá ver seu prompt do terminal como `indoor/ $`. Agora, execute

    code indoor.py

para criar um arquivo chamado `indoor.py`, onde você escreverá seu programa.

## Demonstração

## Como Testar

Aqui está como testar seu código manualmente. No prompt `indoor/ $` em seu terminal:

- Execute seu programa com `python indoor.py`. Digite `HELLO` e pressione Enter. Seu programa deverá exibir `hello`.
- Execute seu programa com `python indoor.py`. Digite `THIS IS CS50` e pressione Enter. Seu programa deverá exibir `this is cs50`.
- Execute seu programa com `python indoor.py`. Digite `50` e pressione Enter. Seu programa deverá exibir `50`.

Se você encontrar um erro dizendo que seu arquivo não pode ser aberto, refaça seus passos para garantir que você está dentro da sua pasta `indoor` e salvou seu arquivo `indoor.py` lá. Lembra como fazer?

Você pode executar o abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas lembre-se de testá-lo também!

    check50 cs50/problems/2022/python/indoor

Sorrisos verdes significam que seu programa passou em um teste! Tristezas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` gera para ver a entrada que o `check50` forneceu ao seu programa, qual saída esperava e qual saída seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/indoor
