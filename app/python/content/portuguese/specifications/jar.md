# Pote de Biscoitos

![Monstro das Bolachas](giphy1.gif)

Fonte: Sesame Street

Suponha que você deseje implementar um [pote de biscoitos](https://en.wikipedia.org/wiki/Cookie_jar) no qual armazenar biscoitos. Em um arquivo chamado `jar.py`, implemente uma `classe` chamada `Jar` com os seguintes métodos:

- `__init__` deve inicializar um pote de biscoitos com a `capacidade` fornecida, que representa o número máximo de biscoitos que cabem no pote. Se `capacidade` não for um `int` não negativo, no entanto, `__init__` deve em vez disso gerar um `ValueError`.
- `__str__` deve retornar um `str` com \\(n\\) `🍪`, onde \\(n\\) é o número de biscoitos no pote. Por exemplo, se houver 3 biscoitos no pote, então `str` deve retornar `"🍪🍪🍪"`.
- `deposit` deve adicionar `n` biscoitos ao pote. Se adicionar tantos biscoitos excederia a capacidade do pote, no entanto, `deposit` deve em vez disso gerar um `ValueError`.
- `withdraw` deve remover `n` biscoitos do pote. Nom nom nom. Se não houver tantos biscoitos no pote, no entanto, `withdraw` deve em vez disso gerar um `ValueError`.
- `capacidade` deve retornar a capacidade do pote de biscoitos.
- `tamanho` deve retornar o número de biscoitos realmente no pote, inicialmente `0`.

Estruture sua `classe` conforme abaixo. Você não pode alterar os parâmetros destes métodos, mas pode adicionar seus próprios métodos.

```python
class Jar:
    def __init__(self, capacidade=12):
        ...

    def __str__(self):
        ...

    def depositar(self, n):
        ...

    def sacar(self, n):
        ...

    @property
    def capacidade(self):
        ...

    @property
    def tamanho(self):
        ...
```

Antes ou depois de implementar `jar.py`, adicionalmente implemente, em um arquivo chamado `test_jar.py`, **quatro ou mais** funções que testem coletivamente sua implementação de `Jar` minuciosamente, cujos nomes devem começar com `test_` para que você possa executar seus testes com:

```bash
pytest test_jar.py
```

Note que não é tão fácil testar métodos de instância quanto testar funções isoladamente, já que os métodos de instância às vezes manipulam o mesmo “estado” (ou seja, variáveis de instância). Para testar um método (por exemplo, `sacar`), então, você pode precisar chamar outro método primeiro (por exemplo, `depositar`). Mas o método que você chama primeiro pode não estar correto!

Portanto, programadores às vezes [simulam](https://en.wikipedia.org/wiki/Mock_object) (ou seja, criam versões simuladas) o estado ao testar métodos, como com a própria [biblioteca de objetos simulados](https://docs.python.org/3/library/unittest.mock.html) do Python, para que você possa chamar apenas o método desejado, mas modificar o estado subjacente primeiro, sem chamar o outro método para fazer isso.

No entanto, por simplicidade, não há necessidade de simular nenhum estado. Implemente seus testes como normalmente faria!

Dicas

```python
from jar import Jar

def test_init():
    ...

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.depositar(1)
    assert str(jar) == "🍪"
    jar.depositar(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_depositar():
    ...

def test_sacar():
    ...
```

## Demonstração

Você é bem-vindo, mas não obrigado, a implementar uma função `principal`, para que seja tudo o que podemos demonstrar!

![Monstro das Bolachas](giphy2.gif)

Fonte: Sesame Street

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se assemelha ao assim:

```bash
$
```

Em seguida, execute

```bash
mkdir jar
```

para criar uma pasta chamada `jar` no seu espaço de códigos.

Depois, execute

```bash
cd jar
```

para mudar para o diretório dessa pasta. Agora seu prompt do terminal deve ser `jar/ $`. Você pode agora executar

```bash
code jar.py
```

para criar um arquivo chamado `jar.py` no qual você escreverá o seu programa. Você também pode executar

```bash
code test_jar.py
```

para criar um arquivo chamado `test_jar.py` onde poderá escrever os testes para o seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Abra seu arquivo `test_jar.py` e importe sua classe `Jar` com `from jar import Jar`. Crie uma função chamada `test_init`, na qual você cria uma nova instância de `Jar` com `jar = Jar()`. `assert` que este pote tem a capacidade que deveria ter, em seguida, execute seus testes com `pytest test_jar.py`.
- Adicione outra função ao seu arquivo `test_jar.py` chamada `test_str`. Em `test_str`, crie uma nova instância da sua classe `Jar` e `deposite` alguns biscoitos. `assert` que `str(jar)` imprime tantos biscoitos quanto foram `depositados`, em seguida, execute seus testes com `pytest test_jar.py`.
- Adicione outra função ao seu arquivo `test_jar.py` chamada `test_depositar`. Em `test_depositar`, crie uma nova instância da sua classe `Jar` e `deposite` alguns biscoitos. `assert` que o atributo `tamanho` do pote é tão grande quanto o número de biscoitos que foram `depositados`. Também `assert` que, se depositar mais que a `capacidade` do pote, `deposite` deve gerar um `ValueError`. Execute seus testes com `pytest test_jar.py`.
- Adicione outra função ao seu arquivo `test_jar.py` chamada `test_sacar`. Em `test_sacar`, crie uma nova instância da sua classe `Jar` e primeiro `deposite` alguns biscoitos. `assert` que ao `sacar` do pote, o número apropriado de biscoitos é deixado no atributo `tamanho` do pote. Também `assert` que, se você retirar mais do que o `tamanho` do pote, `sacar` deve gerar um `ValueError`. Execute seus testes com `pytest test_jar.py`.

Você pode executar o comando abaixo para verificar seu código usando `check50`, um programa que o CS50 utilizará para testar seu código quando você o enviar. Mas certifique-se de testá-lo também por conta própria!

```bash
check50 cs50/problems/2022/python/jar
```

Rostinhos verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` produz para ver a entrada que `check50` forneceu ao seu programa, qual saída era esperada e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

```bash
submit50 cs50/problems/2022/python/jar
```
