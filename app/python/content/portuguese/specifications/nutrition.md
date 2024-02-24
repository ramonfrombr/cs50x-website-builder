# Informações Nutricionais

A Administração de Alimentos e Medicamentos dos Estados Unidos (FDA) oferece [cartazes para download/impressão](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) que "mostram informações nutricionais para as 20 frutas cruas mais consumidas nos Estados Unidos. As lojas de varejo podem baixar os cartazes, imprimir, exibir e/ou distribuí-los para os consumidores em proximidade com os alimentos relevantes nas lojas".

Em um arquivo chamado `nutrition.py`, implemente um programa que solicita aos usuários consumidores para inserir uma fruta (sem diferenciação de maiúsculas e minúsculas) e, em seguida, mostra o número de calorias em uma porção dessa fruta, de acordo com o [cartaz da FDA para frutas](Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), o qual também está [disponível como texto](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Desconsiderando a capitalização, assuma que os usuários inserirão as frutas exatamente como escritas no cartaz (por exemplo, `morangos`, não `morango`). Ignore qualquer entrada que não seja uma fruta.

Dicas

- Em vez de usar uma condicional com 20 expressões booleanas, uma para cada fruta, é melhor usar um `dict` para associar uma fruta com suas calorias!
- Se `k` é uma `str` e `d` é um `dict`, você pode verificar se `k` é uma chave em `d` com um código como:

      if k in d:
          ...

- Certifique-se de exibir as calorias da fruta, não as calorias provenientes de gordura!

## Demonstração

## Antes de Começar

Acesse o [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir nutrition

para criar uma pasta chamada `nutrition` no seu espaço de código.

Depois execute

    cd nutrition

para mudar para o diretório dessa pasta. Agora você deverá ver o prompt do seu terminal como `nutrition/ $`. Você pode então executar

    code nutrition.py

para criar um arquivo chamado `nutrition.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar manualmente o seu código:

- Execute o seu programa com `python nutrition.py`. Digite `Maçã` e pressione Enter. Seu programa deverá exibir:

      Calorias: 130

- Execute o seu programa com `python nutrition.py`. Digite `Abacate` e pressione Enter. Seu programa deverá exibir:

      Calorias: 50

- Execute o seu programa com `python nutrition.py`. Digite `Cereja Doce` e pressione Enter. Seu programa deverá exibir:

      Calorias: 100

- Execute o seu programa com `python nutrition.py`. Digite `Tomate` e pressione Enter. Seu programa não deverá exibir nada.

Certifique-se de testar com outras frutas e variar a capitalização da sua entrada. Seu programa deve se comportar conforme o esperado, de maneira insensível à caixa.

Você pode executar o comando abaixo para verificar o seu código usando `check50`, um programa que o CS50 usará para testar o seu código quando você enviar. Certifique-se de testar você mesmo também!

    check50 cs50/problems/2022/python/nutrition

Carinhas sorridentes verdes indicam que o seu programa passou no teste! Carinhas tristes vermelhas indicarão que o seu programa exibiu algo inesperado. Visite a URL que o `check50` mostrará para ver a entrada que o `check50` forneceu para o seu programa, qual saída ele esperava e qual saída o seu programa realmente deu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/nutrition
