# Indicador de Combustível

![indicador de combustível](51-hsJaA+SL._SL1000_.jpg)  
Fonte: [amazon.com/dp/B09C4FL56G](https://www.amazon.com/dp/B09C4FL56G)

Os indicadores de combustível indicam, frequentemente com frações, quanto combustível há no tanque. Por exemplo, 1/4 indica que o tanque está 25% cheio, 1/2 indica que o tanque está 50% cheio e 3/4 indica que o tanque está 75% cheio.

Em um arquivo chamado `fuel.py`, implemente um programa que solicita ao usuário uma fração formatada como `X/Y`, em que cada `X` e `Y` é um inteiro, e então exibe, como um percentual arredondado para o inteiro mais próximo, quanto combustível há no tanque. Se, no entanto, restar 1% ou menos, exiba `E` para indicar que o tanque está essencialmente vazio. E se restar 99% ou mais, exiba `F` para indicar que o tanque está essencialmente cheio.

Se, no entanto, `X` ou `Y` não for um inteiro, `X` for maior que `Y`, ou `Y` for `0`, solicite novamente ao usuário. (Não é necessário que `Y` seja `4`.) Certifique-se de capturar exceções como [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) ou [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

Dicas

- Lembre-se de que uma `str` possui muitos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluindo `split`.
- Observe que você pode lidar com duas exceções separadamente com um código como:

      try:
          ...
      except ValueError:
          ...
      except ZeroDivisionError:
          ...

  Ou você pode lidar com duas exceções juntas com um código como:

      try:
          ...
      except (ValueError, ZeroDivisionError):
          ...

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique em sua janela de terminal e execute `cd` sozinho. Você deve ver um prompt na sua janela de terminal como abaixo:

    $

Em seguida, execute

    mkdir fuel

para criar uma pasta chamada `fuel` em seu espaço de códigos.

Depois execute

    cd fuel

para mudar para esse diretório. Agora você deve ver o prompt do terminal como `fuel/ $`. Agora você pode executar

    code fuel.py

para criar um arquivo chamado `fuel.py` onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python fuel.py`. Digite `3/4` e pressione Enter. Seu programa deve exibir:

      75%

- Execute seu programa com `python fuel.py`. Digite `1/4` e pressione Enter. Seu programa deve exibir:

      25%

- Execute seu programa com `python fuel.py`. Digite `4/4` e pressione Enter. Seu programa deve exibir:

      F

- Execute seu programa com `python fuel.py`. Digite `0/4` e pressione Enter. Seu programa deve exibir:

      E

- Execute seu programa com `python fuel.py`. Digite `4/0` e pressione Enter. Seu programa deve lidar com um [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) e solicitar novamente ao usuário.
- Execute seu programa com `python fuel.py`. Digite `three/four` e pressione Enter. Seu programa deve lidar com um [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) e solicitar novamente ao usuário.
- Execute seu programa com `python fuel.py`. Digite `1.5/3` e pressione Enter. Seu programa deve lidar com um [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) e solicitar novamente ao usuário.
- Execute seu programa com `python fuel.py`. Digite `5/4` e pressione Enter. Seu programa deve solicitar novamente ao usuário.

Você pode executar o código abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas certifique-se de testar também por conta própria!

    check50 cs50/problems/2022/python/fuel

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicam que seu programa apresentou algo inesperado. Visite a URL que o `check50` imprime para ver a entrada que o `check50` forneceu ao seu programa, a saída esperada e a saída real do seu programa.

## Como Enviar

Em seu terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/fuel
