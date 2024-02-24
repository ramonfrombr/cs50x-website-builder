## # Índice de Preços do Bitcoin

![Logotipo do Bitcoin](Bitcoin.svg.png)

[Bitcoin](https://en.wikipedia.org/wiki/Bitcoin) é uma forma de moeda digital, também conhecida como [criptomoeda](https://en.wikipedia.org/wiki/Cryptocurrency). Em vez de depender de uma autoridade central como um banco, o Bitcoin depende de uma rede distribuída, também conhecida como [blockchain](https://en.wikipedia.org/wiki/Blockchain), para registrar transações.

Devido à demanda pelo Bitcoin (ou seja, os usuários o querem), os usuários estão dispostos a comprá-lo, trocando uma moeda (por exemplo, USD) pelo Bitcoin.

Em um arquivo chamado `bitcoin.py`, implemente um programa que:

- Espera que o usuário especifique, como argumento de linha de comando, o número de Bitcoins, \\(n\\), que eles gostariam de comprar. Se esse argumento não puder ser convertido em um `float`, o programa deve ser encerrado via `sys.exit` com uma mensagem de erro.
- Consulta a API do Índice de Preços do Bitcoin da CoinDesk em [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json), que retorna um objeto [JSON](https://en.wikipedia.org/wiki/JSON), no qual uma das chaves aninhadas é o preço atual do Bitcoin como um `float`. Certifique-se de capturar quaisquer [exceções](https://requests.readthedocs.io/en/latest/api/#exceptions), como com o código a seguir:

      import requests

      try:
          ...
      except requests.RequestException:
          ...

- Exibe o custo atual de \\(n\\) Bitcoins em USD com quatro casas decimais, usando `,` como separador de milhares.

Dicas

- Lembre-se de que o módulo `sys` vem com `argv`, conforme [docs.python.org/3/library/sys.html#sys.argv](https://docs.python.org/3/library/sys.html#sys.argv).
- Observe que o módulo `requests` possui vários métodos, conforme [requests.readthedocs.io/en/latest](https://requests.readthedocs.io/en/latest/), incluindo `get`, conforme [requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request](https://requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request), e `json`, conforme [requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content](https://requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content). Você pode instalá-lo com:

      pip install requests

- Observe que a API da CoinDesk retorna uma resposta JSON como:

      {
         "time":{
            "updated":"May 2, 2022 15:27:00 UTC",
            "updatedISO":"2022-05-02T15:27:00+00:00",
            "updateduk":"May 2, 2022 at 16:27 BST"
         },
         "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
         "chartName":"Bitcoin",
         "bpi":{
            "USD":{
               "code":"USD",
               "symbol":"&#36;",
               "rate":"38,761.0833",
               "description":"United States Dollar",
               "rate_float":38761.0833
            },
            "GBP":{
               "code":"GBP",
               "symbol":"&pound;",
               "rate":"30,827.6198",
               "description":"British Pound Sterling",
               "rate_float":30827.6198
            },
            "EUR":{
               "code":"EUR",
               "symbol":"&euro;",
               "rate":"36,800.2764",
               "description":"Euro",
               "rate_float":36800.2764
            }
         }
      }

- Lembre-se de que você pode formatar USD com quatro casas decimais e um [separador de milhares](https://docs.python.org/3/library/string.html#formatspec) com o seguinte código:

      print(f"${amount:,.4f}")

## Demonstração

Esta demonstração foi gravada quando o preço do Bitcoin era de $38,761.0833. Seu próprio resultado pode variar.

## Antes de Começar

Acesse [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute o comando `cd` isoladamente. Você deve verificar que o prompt da janela do seu terminal se parece com o seguinte:

    $

Em seguida, execute o comando

    mkdir bitcoin

para criar uma pasta chamada `bitcoin` em seu ambiente de códigos.

Depois, execute o comando

    cd bitcoin

para mudar para o diretório dessa pasta. Agora, você deverá ver o prompt do seu terminal como `bitcoin/ $`. Agora, você pode executar o comando

    code bitcoin.py

para criar um arquivo chamado `bitcoin.py`, onde você escreverá seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o seu programa com `python bitcoin.py`. O seu programa deve usar `sys.exit` para sair com uma mensagem de erro:

      Argumento de linha de comando ausente

- Execute o seu programa com `python bitcoin.py cat`. O seu programa deve usar `sys.exit` para sair com uma mensagem de erro:

      O argumento de linha de comando não é um número

- Execute o seu programa com `python bitcoin.py 1`. O seu programa deve imprimir o preço de um único Bitcoin com quatro casas decimais, usando `,` como [separador de milhares](https://docs.python.org/3/library/string.html#formatspec).
- Execute o seu programa com `python bitcoin.py 2`. O seu programa deve imprimir o preço de dois Bitcoin com quatro casas decimais, usando `,` como [separador de milhares](https://docs.python.org/3/library/string.html#formatspec).
- Execute o seu programa com `python bitcoin.py 2.5`. O seu programa deve imprimir o preço de 2.5 Bitcoin com quatro casas decimais, usando `,` como [separador de milhares](https://docs.python.org/3/library/string.html#formatspec).

Você pode executar o código abaixo para verificar o seu código usando `check50`, um programa que a CS50 usará para testar o seu código quando você submeter. Mas certifique-se de testar também por conta própria!

    check50 cs50/problems/2022/python/bitcoin

Os sorrisos verdes significam que o seu programa passou em um teste! As carinhas tristes vermelhas indicarão que o seu programa produziu algo inesperado. Visite a URL que o `check50` imprime para ver a entrada que o `check50` forneceu ao seu programa, qual saída ele esperava e qual saída o seu programa realmente deu.

## Como enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/bitcoin
