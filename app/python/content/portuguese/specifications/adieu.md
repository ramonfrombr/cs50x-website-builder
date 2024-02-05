# Adeus, Adeus

Em [A Noviça Rebelde](https://pt.wikipedia.org/wiki/A_Noviça_Rebelde), existe uma música cantada principalmente em inglês, [So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU), com essas [letras](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell), onde "adeus" significa "goodbye" em francês:

> Adeus, adeus, para ti e ti e ti

Claro, a frase não está gramaticalmente correta, já que normalmente seria escrita (com uma [vírgula de Oxford](https://pt.wikipedia.org/wiki/V%C3%ADrgula_de_Oxford)) como:

> Adeus, adeus, para ti, ti e ti

Para ser justo, "ti" nem é uma palavra, só rima com "you"!

Em um arquivo chamado `adieu.py`, implemente um programa que solicita ao usuário os nomes, um por linha, até que o usuário digite controle-d. Suponha que o usuário fornecerá pelo menos um nome. Em seguida, se despeça desses nomes, separando dois nomes com um `and`, três nomes com duas vírgulas e um `and`, e \\(n\\) nomes com \\(n-1\\) vírgulas e um `and`, como no exemplo abaixo:

> Adeus, adeus, para Liesl  
> Adeus, adeus, para Liesl e Friedrich  
> Adeus, adeus, para Liesl, Friedrich e Louisa  
> Adeus, adeus, para Liesl, Friedrich, Louisa e Kurt  
> Adeus, adeus, para Liesl, Friedrich, Louisa, Kurt e Brigitta  
> Adeus, adeus, para Liesl, Friedrich, Louisa, Kurt, Brigitta e Marta  
> Adeus, adeus, para Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta e Gretl

Dicas

- Observe que o módulo `inflect` possui vários métodos, conforme [pypi.org/project/inflect](https://pypi.org/project/inflect/). Você pode instalá-lo com:

      pip install inflect

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você verá que o prompt da janela do terminal será semelhante ao seguinte:

    $

Em seguida, execute

    mkdir adieu

para criar uma pasta chamada `adieu` em seu espaço de códigos.

Depois, execute

    cd adieu

para entrar nessa pasta. Agora, você verá seu prompt do terminal como `adieu/ $`. Agora você pode executar

    code adieu.py

para criar um arquivo chamado `adieu.py`, onde você escreverá o seu programa.

## Como Testar

Aqui está como testar seu código manualmente:

- Execute o programa com `python adieu.py`. Digite `Liesl` e pressione Enter, seguido de control-d. Seu programa deve exibir:

      Adieu, adieu, para Liesl

- Execute o programa com `python adieu.py`. Digite `Liesl` e pressione Enter, em seguida, digite `Friedrich` e pressione Enter, seguido de control-d. Seu programa deve exibir:

      Adieu, adieu, para Liesl e Friedrich

- Execute o programa com `python adieu.py`. Digite `Liesl` e pressione Enter, em seguida, digite `Friedrich` e pressione Enter. Agora digite `Louisa` e pressione Enter, seguido de control-d. Seu programa deve exibir:

      Adieu, adieu, para Liesl, Friedrich e Louisa

Você pode executar o código abaixo para verificar seu código usando o `check50`, um programa que a equipe do CS50 usará para testar seu código quando você enviar. Mas lembre-se de testá-lo também!

    check50 cs50/problems/2022/python/adieu

Carinhas verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa exibiu algo inesperado. Visite a URL que o `check50` imprime para ver a entrada que o `check50` forneceu ao seu programa, qual saída era esperada e qual saída seu programa realmente deu.

## Como enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/adieu

<\_io.TextIOWrapper name='app/python/content/portuguese/specifications/adieu.md' mode='r' encoding='UTF-8'>
