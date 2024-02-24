## # Emojize

Como os emojis não são tão fáceis de digitar como textos, pelo menos em laptops e desktops, alguns programas suportam "códigos", nos quais você pode digitar, por exemplo, `:thumbs_up:`, que será automaticamente convertido para 👍. Alguns programas também suportam aliases, nos quais você pode digitar de forma mais sucinta, por exemplo, `:thumbsup:`, que também será automaticamente convertido para 👍.

Veja [carpedm20.github.io/emoji/all.html?enableList=enable_list_alias](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias) para obter uma lista de códigos com aliases.

Em um arquivo chamado `emojize.py`, implemente um programa que solicite ao usuário uma `str` em inglês e, em seguida, imprima a versão "emojizada" dessa `str`, convertendo quaisquer códigos (ou aliases) contidos nela para seus respectivos emojis correspondentes.

Dicas

- Observe que o módulo `emoji` vem com duas funções, de acordo com [pypi.org/project/emoji](https://pypi.org/project/emoji/), sendo uma delas `emojize`, que possui um parâmetro opcional chamado `language`. Você pode instalá-lo com:

      pip install emoji

## Demonstração

## Antes de começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir emojize

para criar uma pasta chamada `emojize` no seu codespace.

Depois execute

    cd emojize

para mudar para o diretório dessa pasta. Agora você deverá ver o prompt do seu terminal como `emojize/ $`. Agora você pode executar

    code emojize.py

para criar um arquivo chamado `emojize.py`, onde você escreverá seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o seu programa com `python emojize.py`. Digite `:1st_place_medal:` e pressione Enter. Seu programa deve exibir:

      Saída: 🥇

- Execute o seu programa com `python emojize.py`. Digite `:money_bag:` e pressione Enter. Seu programa deve exibir:

      Saída: 💰

- Execute o seu programa com `python emojize.py`. Digite `:smile_cat:` e pressione Enter. Seu programa deve exibir:

      Saída: 😸

Você também pode executar o código abaixo para verificar o seu código usando `check50`, um programa que o CS50 utilizará para testar o seu código quando você enviar. Certifique-se também de testá-lo você mesmo!

    check50 cs50/problems/2022/python/emojize

Smiles verdes significam que o seu programa passou no teste! Carinhas vermelhas indicarão que o seu programa exibiu algo inesperado. Visite a URL que `check50` exibe para ver a entrada que `check50` forneceu para o seu programa, qual saída ele esperava e qual saída o seu programa realmente deu.

## Como enviar

No seu terminal, execute o seguinte para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/emojize
