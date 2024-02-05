# Testando meu twttr

Em um arquivo chamado `twttr.py`, reimplemente [Configurando meu twttr](../../2/twttr/) do [Problema 2](../../2/), reestruturando seu código conforme abaixo, onde `shorten` espera uma entrada do tipo `str` e retorna a mesma `str` sem todas as vogais (A, E, I, O, e U), independentemente de estarem em maiúsculas ou minúsculas.

```python
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
```

Em seguida, em um arquivo chamado `test_twttr.py`, implemente **uma ou mais** funções que testem de forma abrangente sua implementação de `shorten`, cujos nomes devem começar com `test_` para que você possa executar seus testes com:

```bash
pytest test_twttr.py
```

Dicas

- Certifique-se de incluir

  ```python
  import twttr
  ```

  ou

  ```python
  from twttr import shorten
  ```

  no início do arquivo `test_twttr.py` para poder chamar `shorten` em seus testes.

- Tome cuidado para `return`, não `print`, um `str` em `shorten`. Somente `main` deve chamar `print`.

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você deverá ver o seguinte prompt na janela do terminal:

```bash
$
```

Em seguida, execute

```bash
mkdir test_twttr
```

para criar uma pasta chamada `test_twttr` em sua área de códigos.

Depois, execute

```bash
cd test_twttr
```

para entrar nessa pasta. Agora você deverá ver o prompt do terminal como `test_twttr/ $`. Você pode então executar

```bash
code test_twttr.py
```

para criar um arquivo chamado `test_twttr.py`, onde você escreverá seus testes.

## Como Testar

Para testar seus testes, execute `pytest test_twttr.py`. Certifique-se de ter uma cópia do arquivo `twttr.py` na mesma pasta. Tente usar versões corretas e incorretas de `twttr.py` para determinar o quão bem seus testes identificam erros:

- Garanta que tenha uma versão correta de `twttr.py`. Execute seus testes executando `pytest test_twttr.py`. O `pytest` deve mostrar que todos os seus testes passaram.
- Modifique a versão correta de `twttr.py` de forma a causar um bug. Seu programa pode, por exemplo, omitir acidentalmente apenas as vogais minúsculas! Execute seus testes executando `pytest test_twttr.py`. O `pytest` deve mostrar que pelo menos um dos seus testes falhou.

Você pode executar o seguinte para verificar seus testes usando `check50`, um programa que a CS50 usará para testar seu código quando você submeter. (Agora existem testes para testar seus testes!). Certifique-se de testar seus testes por conta própria e determinar quais testes são necessários para garantir que `twttr.py` seja verificado de forma abrangente.

```bash
check50 cs50/problems/2022/python/tests/twttr
```

Carinhas verdes significam que seu programa passou no teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` gera para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

Em seu terminal, execute o seguinte para enviar seu trabalho.

```bash
submit50 cs50/problems/2022/python/tests/twttr
```
