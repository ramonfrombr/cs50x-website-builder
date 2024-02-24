# Requisitando novamente uma placa de identificação personalizada

Em um arquivo chamado `plates.py`, reimplemente [Vanity Plates](../../2/plates/) do [Conjunto de Problemas 2](../../2/), reestruturando seu código conforme abaixo, no qual `is_valid` ainda espera uma entrada do tipo `str` e retorna `True` se essa `str` atende a todos os requisitos e `False` caso contrário, mas `main` é chamado apenas se o valor de `__name__` for `"__main__"`:

    def main():
        ...


    def is_valid(s):
        ...


    if __name__ == "__main__":
        main()

Em seguida, em um arquivo chamado `test_plates.py`, implemente **quatro ou mais** funções que testem minuciosamente sua implementação de `is_valid`, cujos nomes devem começar com `test_` para que você possa executar seus testes com:

    pytest test_plates.py

Dicas

- Certifique-se de incluir

      import plates

  ou

      from plates import is_valid

  no topo do arquivo `test_plates.py` para que você possa chamar `is_valid` nos seus testes.

- Tenha cuidado para `return`, não `print`, um `bool` em `is_valid`. Apenas o `main` deve chamar `print`.

## Antes de Começar

Acesse o [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você verá que o prompt da sua janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir test_plates

para criar uma pasta chamada `test_plates` no seu espaço de códigos.

Depois execute

    cd test_plates

para mudar para o diretório dessa pasta. Agora, você deverá ver o prompt do terminal como `test_plates/ $`. Agora você pode executar

    code test_plates.py

para criar um arquivo chamado `test_plates.py`, onde você escreverá seus testes.

## Como Testar

Para testar seus testes, execute `pytest test_plates.py`. Certifique-se de ter uma cópia do arquivo `plates.py` na mesma pasta. Tente usar versões corretas e incorretas de `plates.py` para determinar o quão bem seus testes identificam erros:

- Garanta que você tenha uma versão correta do arquivo `plates.py`. Execute seus testes executando `pytest test_plates.py`. O `pytest` deverá mostrar que todos os seus testes passaram.
- Modifique a versão correta do arquivo `plates.py`, talvez eliminando algumas de suas restrições. Seu programa pode, por exemplo, erroneamente imprimir "Válido" para uma placa de identificação de qualquer comprimento! Execute seus testes executando `pytest test_plates.py`. O `pytest` deverá mostrar que pelo menos um dos seus testes falhou.

Você pode executar o seguinte para verificar seus testes usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. (Agora existem testes para testar seus testes!). Certifique-se de testar seus testes por conta própria e determinar quais testes são necessários para garantir que `plates.py` seja verificado minuciosamente.

    check50 cs50/problems/2022/python/tests/plates

Smiles verdes significam que seu programa passou em um teste! Frownies vermelhos indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` forneceu ao seu programa, qual saída ele esperava, e qual saída seu programa de fato deu.

## Como Enviar

No seu terminal, execute o seguinte para submeter seu trabalho.

    submit50 cs50/problems/2022/python/tests/plates
