# Desatualizado

Nos Estados Unidos, as datas são tipicamente formatadas na ordem [mês-dia-ano](https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States) (MM/DD/YYYY), também conhecida como ordem [middle-endian](https://en.wikipedia.org/wiki/Endianness#Middle-endian), o que é considerado como um design ruim. Datas nesse formato não podem ser facilmente ordenadas, pois o ano da data vem por último ao invés de vir primeiro. Tente ordenar, por exemplo, `2/2/1800`, `3/3/1900` e `1/1/2000` em ordem cronológica em qualquer programa (por exemplo, uma planilha). As datas nesse formato também são ambíguas. Harvard foi [fundada](https://www.harvard.edu/about/history/) em 8 de setembro de 1636, mas 9/8/1636 também poderia ser interpretado como 9 de agosto de 1636!

Felizmente, os computadores tendem a utilizar o formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), um padrão internacional que prescreve que as datas devem ser formatadas na ordem ano-mês-dia (YYYY-MM-DD), independentemente do país, formatando os anos com quatro dígitos, os meses com dois dígitos e os dias com dois dígitos, "preenchendo" cada um com zeros à esquerda conforme necessário.

Em um arquivo chamado `outdated.py`, implemente um programa que solicita ao usuário uma data, [anno Domini](https://en.wikipedia.org/wiki/Anno_Domini), no formato mês-dia-ano, formatada como `9/8/1636` ou `8 de setembro de 1636`, onde o mês neste último formato pode ser qualquer um dos valores da `lista` abaixo:

    [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
    ]

Em seguida, exiba a mesma data no formato `YYYY-MM-DD`. Se a entrada do usuário não for uma data válida em nenhum dos formatos, solicite novamente. Assuma que cada mês tem no máximo 31 dias; não é necessário validar se um mês tem 28, 29, 30 ou 31 dias.

Dicas

- Lembre-se de que uma `str` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluindo `split`.
- Lembre-se de que uma `lista` vem com vários métodos, conforme [docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), entre os quais está o `index`.
- Observe que você pode formatar um `int` com zeros à esquerda com código como

      print(f"{n:02}")

  onde, se `n` for um único dígito, ele será prefixado com um `0`, conforme [docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` isoladamente. Você deverá ver que o prompt de sua janela de terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir outdated

para criar uma pasta chamada `outdated` em seu espaço de códigos.

Depois, execute

    cd outdated

para mudar para o diretório dessa pasta. Agora você deve ver o prompt do seu terminal como `outdated/ $`. Agora, você pode executar

    code outdated.py

para criar um arquivo chamado `outdated.py` onde você escreverá seu programa.

## Como Testar

Aqui estão instruções para testar seu código manualmente:

- Execute seu programa com `python outdated.py`. Digite `9/8/1636` e pressione Enter. Seu programa deve exibir:

      1636-09-08

- Execute seu programa com `python outdated.py`. Digite `8 de setembro de 1636` e pressione Enter. Seu programa deve exibir:

      1636-09-08

- Execute seu programa com `python outdated.py`. Digite `23/6/1912` e pressione Enter. Seu programa deve solicitar novamente a entrada do usuário.
- Execute seu programa com `python outdated.py`. Digite `Dezembro 80, 1980` e pressione Enter. Seu programa deve solicitar novamente a entrada do usuário.

Você pode executar o comando abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. Mas não se esqueça de também testar por conta própria!

    check50 cs50/problems/2022/python/outdated

Emojis verdes significam que seu programa passou em um teste! Emojis vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` imprimir para ver a entrada que o `check50` forneceu para o seu programa, a saída esperada e a saída real do seu programa.

## Como Enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/outdated
