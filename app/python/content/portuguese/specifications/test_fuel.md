# Abastecimento

Em um arquivo chamado `fuel.py`, reimplemente [Indicador de Combustível](../../3/fuel/) do [Conjunto de Problemas 3](../../3/), reestruturando seu código conforme abaixo, onde:

- `convert` espera uma `str` no formato `X/Y` como entrada, em que cada `X` e `Y` é um número inteiro, e retorna essa fração como uma porcentagem arredondada para o inteiro mais próximo entre `0` e `100`, inclusive. Se `X` e/ou `Y` não forem inteiros, ou se `X` for maior que `Y`, então `convert` deve gerar um `ValueError`. Se `Y` for `0`, então `convert` deve gerar um `ZeroDivisionError`.
- `gauge` espera um `int` e retorna uma `str` que é:

  - `"E"` se esse `int` for menor ou igual a `1`,
  - `"F"` se esse `int` for maior ou igual a `99`,
  - e `"Z%"` caso contrário, onde `Z` é o mesmo `int`.

  def main():
  ...

  def convert(fraction):
  ...

  def gauge(percentage):
  ...

  if **name** == "**main**":
  main()

Em seguida, em um arquivo chamado `test_fuel.py`, implemente **duas ou mais** funções que testam de forma abrangente suas implementações de `convert` e `gauge`, cujos nomes devem começar com `test_` para que você possa executar seus testes com:

    pytest test_fuel.py

Dicas

- Certifique-se de incluir

      import fuel

  ou

      from fuel import convert, gauge

  no topo do arquivo `test_fuel.py` para que você possa chamar `convert` e `gauge` em seus testes.

- Tome cuidado para `return`, não `print`, um `int` em `convert` e uma `str` em `gauge. Somente `main`deve chamar`print`.
- Note que você pode verificar com `pytest` se uma função gerou uma exceção, conforme [docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions](https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions).

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deve ver que o prompt da sua janela do terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir test_fuel

para criar uma pasta chamada `test_fuel` em seu espaço de códigos.

Depois execute

    cd test_fuel

para mudar para o diretório dessa pasta. Agora seu prompt do terminal deve ser `test_fuel/ $`. Agora você pode executar

    code test_fuel.py

para criar um arquivo chamado `test_fuel.py` onde você escreverá seus testes.

## Como Testar

Para testar seus testes, execute `pytest test_fuel.py`. Certifique-se de ter uma cópia de um arquivo `fuel.py` na mesma pasta. Tente usar versões corretas e incorretas de `fuel.py` para determinar quão bem seus testes identificam erros:

- Garanta que você tenha uma versão correta de `fuel.py`. Execute seus testes executando `pytest test_fuel.py`. `pytest` deve mostrar que todos os seus testes passaram.
- Modifique a versão correta de `fuel.py`, alterando os valores de retorno de `convert`. Seu programa pode, por exemplo, retornar acidentalmente uma `str` em vez de um `int`. Execute seus testes executando `pytest test_fuel.py`. `pytest` deve mostrar que pelo menos um dos seus testes falhou.
- Da mesma forma, modifique a versão correta de `fuel.py`, alterando os valores de retorno de `gauge`. Seu programa pode, por exemplo, omitir um `%` na `str` resultante. Execute seus testes executando `pytest test_fuel.py`. `pytest` deve mostrar que pelo menos um dos seus testes falhou.

Você pode executar o comando abaixo para verificar seus testes usando o `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. (Agora existem testes para testar seus testes!). Certifique-se de testar seus testes e determinar quais testes são necessários para garantir que `fuel.py` seja verificado adequadamente.

    check50 cs50/problems/2022/python/tests/fuel

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa gerou algo inesperado. Visite o URL que o `check50` gera para ver a entrada que o `check50` forneceu ao seu programa, o que a saída esperava e o que seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/tests/fuel
