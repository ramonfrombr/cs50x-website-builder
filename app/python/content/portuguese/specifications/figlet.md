## # Letras de Frank, Ian e Glen

[FIGlet](https://en.wikipedia.org/wiki/FIGlet), nomeado após [as letras de Frank, Ian e Glen](http://www.figlet.org/faq.html), é um programa dos anos 90 para criar letras grandes a partir de texto comum, uma forma de [arte ASCII](https://en.wikipedia.org/wiki/ASCII_art):

     _ _ _          _   _     _
    | (_) | _____  | |_| |__ (_)___
    | | | |/ / _ \ | __| '_ \| / __|
    | | |   <  __/ | |_| | | | \__ \
    |_|_|_|\_\___|  \__|_| |_|_|___/

Entre as fontes suportadas pelo FIGlet estão aquelas em [figlet.org/examples.html](http://www.figlet.org/examples.html).

O FIGlet foi posteriormente portado para Python como um módulo chamado [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

Em um arquivo chamado `figlet.py`, implemente um programa que:

- Espera zero ou dois argumentos de linha de comando:
  - Zero se o usuário deseja mostrar o texto com uma fonte aleatória.
  - Dois se o usuário deseja mostrar o texto com uma fonte específica, em que caso o primeiro dos dois deve ser `-f` ou `--font` e o segundo deve ser o nome da fonte.
- Solicita ao usuário uma `str` de texto.
- Mostra o texto na fonte desejada.

Se o usuário fornecer dois argumentos de linha de comando e o primeiro não for `-f` ou `--font` ou o segundo não for o nome de uma fonte, o programa deve sair via `sys.exit` com uma mensagem de erro.

Dicas

- Você pode instalar o `pyfiglet` com:

      pip install pyfiglet

- A documentação do pyfiglet não é muito clara, mas você pode usar o módulo da seguinte maneira:

      from pyfiglet import Figlet

      figlet = Figlet()

  Em seguida, você pode obter uma `list` de fontes disponíveis com um código como este:

      figlet.getFonts()

  Você pode definir a fonte com um código como este, em que `f` é o nome da fonte como uma `str`:

      figlet.setFont(font=f)

  E você pode mostrar o texto naquela fonte com um código como este, em que `s` é o texto como uma `str`:

      print(figlet.renderText(s))

- Observe que o módulo `random` vem com várias funções, conforme [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demonstração

A saída inicial desta demonstração usou uma fonte aleatória. A sua saída pode variar.

## Antes de começar

Acesse [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` por si só. Você verá que o prompt da janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir figlet

para criar uma pasta chamada `figlet` em seu ambiente de código.

Depois execute

    cd figlet

para navegar até essa pasta. Agora você verá o prompt do seu terminal como `figlet/ $`. Agora você pode executar

    code figlet.py

para criar um arquivo chamado `figlet.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar o seu código manualmente:

- Execute o seu programa com `python figlet.py test`. O seu programa deve sair através de `sys.exit` e imprimir uma mensagem de erro:

      Uso inválido

- Execute o seu programa com `python figlet.py -a slant`. O seu programa deve sair através de `sys.exit` e imprimir uma mensagem de erro:

      Uso inválido

- Execute o seu programa com `python figlet.py -f invalid_font`. O seu programa deve sair através de `sys.exit` e imprimir uma mensagem de erro:

      Uso inválido

- Execute o seu programa com `python figlet.py -f slant`. Digite `CS50`. O seu programa deve imprimir o seguinte:

         ___________ __________
        / ____/ ___// ____/ __ \
       / /    \__ \/___ \/ / / /
      / /___ ___/ /___/ / /_/ /
      \____//____/_____/\____/

- Execute o seu programa com `python figlet.py -f rectangles`. Digite `Hello, world`. O seu programa deve imprimir o seguinte:

       _____     _ _                        _   _
      |  |  |___| | |___      _ _ _ ___ ___| |_| |
      |     | -_| | | . |_   | | | | . |  _| | . |
      |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                        |_|

- Execute o seu programa com `python figlet.py -f alphabet`. Digite `Moo`. O seu programa deve imprimir o seguinte:

      M   M
      MM MM
      M M M ooo ooo
      M   M o o o o
      M   M ooo ooo

Você pode executar o comando abaixo para verificar o seu código usando `check50`, um programa que o CS50 usará para testar o seu código quando você enviar. Mas certifique-se de testá-lo você mesmo também!

    check50 cs50/problems/2022/python/figlet

Os sorrisos verdes significam que o seu programa passou em um teste! As carinhas tristes vermelhas indicarão que o seu programa produziu algo inesperado. Visite a URL que o `check50` imprimir para ver a entrada que o `check50` forneceu para o seu programa, qual saída ele esperava e qual saída o seu programa realmente apresentou.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/figlet
