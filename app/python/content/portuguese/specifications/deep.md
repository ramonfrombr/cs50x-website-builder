## # Pensamento Profundo

> "Muito bem," disse o computador, e voltou ao silêncio novamente. Os dois homens estavam inquietos. A tensão era insuportável.
> "Você realmente não vai gostar", observou o Pensamento Profundo.
> "Nos diga!"
> "Muito bem", disse o Pensamento Profundo. "A resposta para a Grande Pergunta..."
> "Sim...!"
> "Da Vida, do Universo e de Tudo mais", disse o Pensamento Profundo.
> "Sim...!"
> "É...", disse o Pensamento Profundo, e pausou.
> "Sim...!"
> "É..."
> "Sim...!!!...?"
> "Quarenta e dois", disse o Pensamento Profundo, com majestade infinita e calma".

> - _O Guia do Mochileiro das Galáxias_, Douglas Adams

No arquivo `deep.py`, implemente um programa que solicite ao usuário a resposta para a Grande Pergunta da Vida, do Universo e de Tudo, exibindo `Sim` se o usuário digitar `42` ou (sem diferenciação entre maiúsculas e minúsculas) `quarenta-dois` ou `quarenta dois`. Caso contrário, exiba `Não`.

Dicas

- Não é necessário converter a entrada do usuário para um `int` se você verificar a igualdade com `"42"`, uma `str`, em vez de `42`, um `int`!
- Está tudo bem se sua saída ou a entrada do usuário ocupar várias linhas.

## Demonstração

## Antes de começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você verá que o prompt da sua janela de terminal se parece com o abaixo:

    $

Em seguida, execute

    mkdir deep

para criar uma pasta chamada `deep` no seu ambiente de código.

Então, execute

    cd deep

para acessar esse diretório. Agora você deve ver o prompt do seu terminal como `deep/ $`. Agora você pode executar

    code deep.py

para criar um arquivo chamado `deep.py`, onde você escreverá o seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o seu programa com `python deep.py`. Digite `42` e pressione Enter. Seu programa deve retornar:

      Sim

- Execute o seu programa com `python deep.py`. Digite `Quarenta e Dois` e pressione Enter. Seu programa deve retornar:

      Sim

- Execute o seu programa com `python deep.py`. Digite `quarenta-e-dois` e pressione Enter. Seu programa deve retornar:

      Sim

- Execute o seu programa com `python deep.py`. Digite `50` e pressione Enter. Seu programa deve retornar:

      Não

Certifique-se de variar o uso de maiúsculas e "acidentalmente" adicionar espaços antes e depois da sua entrada antes de pressionar Enter. Seu programa deve se comportar como esperado, independentemente do uso de maiúsculas/minúsculas e espaços.

Você pode executar o código abaixo para verificar o seu código usando o `check50`, um programa que o CS50 usarpara testar o seu código quando você enviar. Mas certifique-se de testá-lo você mesmo também!

    check50 cs50/problems/2022/python/deep

Os smilies verdes significam que o seu programa passou em um teste! Os rostos tristes vermelhos indicarão que o seu programa retornou algo inesperado. Visite a URL que o `check50` retorna para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída o seu programa realmente retornou.

## Como enviar

No terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/deep
