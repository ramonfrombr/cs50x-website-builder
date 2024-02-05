## # Fazendo Carinhas

Antes dos emojis, existiam os [emoticons](https://en.wikipedia.org/wiki/List_of_emoticons), em que textos como `:)` representavam um rosto feliz e textos como `:(` representavam um rosto triste. Hoje em dia, programas tendem a converter emoticons automaticamente para emojis!

Em um arquivo chamado `faces.py`, implemente uma função chamada `convert` que receba uma `str` como entrada e retorne essa mesma entrada com qualquer ocorrência de `:)` convertida para 🙂 (também conhecido como um [rosto ligeiramente sorridente](https://emojipedia.org/slightly-smiling-face/)) e qualquer ocorrência de `:(` convertida para 🙁 (também conhecido como um [rosto ligeiramente franzido](https://emojipedia.org/slightly-frowning-face/)). Todo o restante do texto deve ser retornado sem alterações.

Em seguida, no mesmo arquivo, implemente uma função chamada `main` que solicite ao usuário uma entrada, chame a função `convert` com essa entrada e imprima o resultado. Você é bem-vindo(a), mas não obrigado(a), a solicitar explicitamente a entrada do usuário, passando uma `str` própria como argumento para `input`. Certifique-se de chamar `main` ao final do seu arquivo.

Dicas

- Lembre-se de que `input` retorna uma `str`, conforme [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Lembre-se de que uma `str` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Um emoji na verdade é apenas um caractere, então você pode citá-lo como qualquer `str`, como por exemplo `"😐"`. E você pode copiar e colar o emoji desta página para o seu próprio código conforme necessário.

## Antes de Começar

Digite `cd` sozinho na janela do seu terminal. Você verá que o prompt da sua janela do terminal se assemelha ao abaixo:

    $

Em seguida, execute o comando

    mkdir faces

para criar uma pasta chamada `faces` no seu espaço de códigos.

Depois, execute

    cd faces

para mudar de diretório para essa pasta. Agora você verá que o prompt do seu terminal é `faces/ $`. Agora, você pode executar o comando

    code faces.py

para criar um arquivo chamado `faces.py`, onde você irá escrever o seu programa.

## Demonstração

## Como Testar

Veja como testar seu código manualmente:

- Execute o programa com `python faces.py`. Digite `Hello :)` e pressione Enter. Seu programa deverá exibir:

      Hello 🙂

- Execute o programa com `python faces.py`. Digite `Goodbye :(` e pressione Enter. Seu programa deverá exibir:

      Goodbye 🙁

- Execute o programa com `python faces.py`. Digite `Hello :) Goodbye :(` e pressione Enter. Seu programa deverá exibir:

      Hello 🙂 Goodbye 🙁

Você também pode executar o abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo também!

    check50 cs50/problems/2022/python/faces

Carinhas sorridentes verdes significam que seu programa passou em um teste! Carinhas tristes vermelhas indicarão que seu programa exibiu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` forneceu para o seu programa, a saída que ele esperava e a saída que o seu programa realmente deu.

## Como enviar

No seu terminal, execute o comando a seguir para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/faces
