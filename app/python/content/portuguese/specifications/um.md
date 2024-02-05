# Expressões Regulares

Não é incomum, pelo menos em inglês, dizer "um" ao tentar lembrar de uma palavra. Quanto mais você faz isso, no entanto, mais perceptível tende a ser!

Em um arquivo chamado `um.py`, implemente uma função chamada `count` que espera uma linha de texto como entrada, do tipo `str`, e retorna, como um `int`, o número de vezes que “um” aparece nesse texto, sem diferenciar maiúsculas de minúsculas, como uma palavra isolada, não como uma subcadeia de alguma outra palavra. Por exemplo, dado um texto como `olá, um, mundo`, a função deve retornar `1`. Por outro lado, dado um texto como `delicioso`, a função deve retornar `0`.

Estruture `um.py` da seguinte forma, em que você pode modificar `main` e/ou implementar outras funções conforme achar necessário, mas não pode importar outras bibliotecas. Você pode, mas não é obrigado, a usar `re` e/ou `sys`.

```python
import re
import sys

def main():
    print(contar(input("Texto: ")))

def contar(s):
    ...

...

if __name__ == "__main__":
    main()
```

Antes ou depois de implementar a função `contar` em `um.py`, adicionalmente implemente, em um arquivo chamado `test_um.py`, **três ou mais** funções que testam exaustivamente a sua implementação da função `contar`, sendo que cada uma delas deve começar com `test_`, para que você possa executar seus testes com:

```sh
pytest test_um.py
```

Dicas

- Lembre-se de que o módulo `re` possui várias funções, conforme [docs.python.org/pt-br/3/library/re.html](https://docs.python.org/pt-br/3/library/re.html), incluindo `findall`.
- Lembre-se de que expressões regulares suportam vários caracteres especiais, conforme [docs.python.org/pt-br/3/library/re.html#regular-expression-syntax](https://docs.python.org/pt-br/3/library/re.html#regular-expression-syntax).
- Devido a barras invertidas em expressões regulares, que poderiam ser confundidas com sequências de escape (como `\n`), é melhor usar a [notação de string bruta do Python para padrões de expressão regular](https://docs.python.org/pt-br/3/library/re.html#module-re). Assim como as strings formatadas são prefixadas com `f`, as strings brutas são prefixadas com `r`. Por exemplo, em vez de `"harvard\.edu"`, use `r"harvard\.edu"`.
- Note que `\b` é “definido como a fronteira entre um caractere `\w` e um caractere `\W` (ou vice-versa), ou entre `\w` no início/fim da string,” conforme [docs.python.org/pt-br/3/library/re.html#regular-expression-syntax](https://docs.python.org/pt-br/3/library/re.html#regular-expression-syntax).
- Você pode achar útil [regex101.com](https://regex101.com/) ou [regexr.com](https://regexr.com/) para testar expressões regulares (e visualizar correspondências).
- Consulte [thefreedictionary.com/words-containing-um](https://www.thefreedictionary.com/words-containing-um) para encontrar algumas palavras que contêm “um”.

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deve encontrar um prompt semelhante ao abaixo:

```sh
$
```

Em seguida, execute

```sh
mkdir um
```

para criar uma pasta chamada `um` no seu espaço de códigos.

Depois execute

```sh
cd um
```

para navegar para dentro dessa pasta. Agora, você deve ver o prompt do terminal como `um/ $`. Você pode então executar

```sh
code um.py
```

para criar um arquivo chamado `um.py` onde você escreverá seu programa. Certifique-se também de executar

```sh
code test_um.py
```

para criar um arquivo chamado `test_um.py` onde você, hum, escreverá testes para o seu programa.

## Como Testar

#### Como Testar `um.py`

Veja como testar `um.py` manualmente:

- Execute seu programa com `python um.py`. Certifique-se de que ele solicita uma entrada. Digite `um` e pressione Enter. Sua função `contar` deve retornar `1`.
- Execute seu programa com `python um.py`. Digite `um?`, seguido de Enter. Sua função `contar` deve retornar `1`.
- Execute seu programa com `python um.py`. Digite `Um, obrigado pelo álbum.`, seguido de Enter. Sua função `contar` deve retornar `1`.
- Execute seu programa com `python um.py`. Digite `Um, obrigado, hum...`, seguido de Enter. Sua função `contar` deve retornar `2`.

#### Como Testar `test_um.py`

Para testar seus testes, execute `pytest test_um.py`. Tente usar versões corretas e incorretas de `um.py` para determinar como seus testes identificam erros:

- Certifique-se de ter uma versão correta de `um.py`. Execute seus testes executando `pytest test_um.py`. O `pytest` deve mostrar que todos os testes foram aprovados.
- Modifique a função `contar` na versão correta de `um.py`. `Contar`, por exemplo, pode erroneamente também contar qualquer “um” que faça parte de uma palavra. Execute seus testes executando `pytest test_um.py`. O `pytest` deve mostrar que pelo menos um dos testes falhou.
- Novamente, modifique a função `contar` na versão correta de `um.py`. `Contar`, por exemplo, pode acidentalmente corresponder apenas a um “um” que é cercado em ambos os lados por um espaço. Execute seus testes executando `pytest test_um.py`. O `pytest` deve mostrar que pelo menos um dos testes falhou.

Você pode executar o código a seguir para verificar o seu código usando o `check50`, um programa que o CS50 usará para testar o seu código quando você o enviar. Mas lembre-se de testá-lo também por conta própria!

```sh
check50 cs50/problems/2022/python/um
```

Carinhas sorridentes verdes significam que seu programa passou em um teste! Carinhas tristes vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` mostra para ver a entrada que ele forneceu ao seu programa, qual saída ele esperava e qual saída seu programa realmente forneceu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

```sh
submit50 cs50/problems/2022/python/um
```
