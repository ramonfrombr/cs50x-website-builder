# De Volta ao Banco

Em um arquivo chamado `bank.py`, reimplemente o [Home Federal Savings Bank](../../1/bank/) do [Conjunto de Problemas 1](../../1/), reestruturando seu código conforme abaixo, em que `value` espera uma entrada do tipo `str` e retorna um `int`, a saber `0` se aquela `str` começa com "hello", `20` se aquela `str` começa com "h" (mas não "hello"), ou `100` caso contrário, tratando a `str` de forma insensível a maiúsculas e minúsculas. Você pode assumir que a string passada para a função `value` não conterá espaços iniciais. Apenas a função `main` deve chamar `print`.

    def main():
        ...


    def value(saudacao):
        ...


    if __name__ == "__main__":
        main()

Então, em um arquivo chamado `test_bank.py`, implemente **três ou mais** funções que testem de forma abrangente a sua implementação de `value`, sendo que cada uma deve ter seu nome iniciando com `test_` para que você possa executar seus testes com:

    pytest test_bank.py

Dicas

- Certifique-se de incluir

      import bank

  ou

      from bank import value

  no topo de `test_bank.py` para poder chamar `value` em seus testes.

- Tenha cuidado para `return`, não `print`, um `int` em `value. Apenas a função `main`deve chamar`print`.

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela do terminal e execute `cd` sozinho. Você deve ver que o prompt da sua janela do terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir test_bank

para criar uma pasta chamada `test_bank` no seu espaço de códigos.

Então execute

    cd test_bank

para mudar para o diretório dentro dessa pasta. Agora você deverá ver o prompt do terminal como `test_bank/ $`. Você pode agora executar

    code test_bank.py

para criar um arquivo chamado `test_bank.py` onde você escreverá seus testes.

## Como Testar

Para testar seus testes, execute `pytest test_bank.py`. Certifique-se de ter uma cópia do arquivo `bank.py` na mesma pasta. Tente usar versões corretas e incorretas de `bank.py` para determinar quão bem seus testes identificam erros:

- Garanta que você tenha uma versão correta de `bank.py`. Execute seus testes executando `pytest test_bank.py`. `pytest` deverá mostrar que todos os seus testes passaram.
- Modifique a versão correta de `bank.py`, alterando os valores fornecidos para cada saudação. Seu programa pode, por exemplo, fornecer erroneamente $100 para um cliente saudado com "Hello" e $0 para um cliente saudado com "What’s up"! Agora, execute seus testes executando `pytest test_bank.py`. `pytest` deverá mostrar que pelo menos um dos seus testes falhou.

Você pode executar o seguinte para verificar seus testes usando `check50`, um programa que a CS50 usará para testar seu código quando você o enviar. (Agora há testes para testar seus testes!). Certifique-se de testar seus testes você mesmo e determinar quais testes são necessários para garantir que `bank.py` seja verificado minuciosamente.

    check50 cs50/problems/2022/python/tests/bank

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` fornece para ver a entrada que o `check50` passou para o seu programa, a saída esperada e a saída que seu programa realmente deu.

## Como Enviar

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/tests/bank
