```python
import check50
from pexpect import EOF
from re import escape


@check50.check()
def existe():
    """grocery.py existe"""
    check50.exists("grocery.py")


@check50.check(existe)
def teste_EOF():
    """entrada de EOF interrompe o programa"""
    check50.run("python3 grocery.py").stdin(EOF, prompt=False).exit(0)


@check50.check(teste_EOF)
def teste_itens_simples():
    """entrada de \"maçã\" e \"banana\" resulta em \"1 MAÇÃ 1 BANANA\""""
    items = ["maçã", "banana"]
    output = "1 MAÇÃ\n1 BANANA"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(teste_EOF)
def teste_itens_multiplos():
    """entrada de \"morango\" e \"morango\" resulta em \"2 MORANGO\""""
    items = ["morango", "morango"]
    output = "2 MORANGO"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(teste_EOF)
def teste_itens_simples_e_multiplos():
    """entrada de \"manga\", \"açúcar\" e \"manga\" resulta em \"2 MANGA 1 AÇÚCAR\""""
    items = ["manga", "açúcar", "manga"]
    output = "2 MANGA\n1 AÇÚCAR"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(items[2], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(teste_EOF)
def teste_alfabetico():
    """entrada de \"tortilla\" e \"batata doce\" resulta em \"1 BATATA DOCE 1 TORTILLA\""""
    items = ["tortilla", "batata doce"]
    output = "1 BATATA DOCE\n1 TORTILLA"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


def regex(items):
    """corresponde de forma sensível a maiúsculas e minúsculas somente com espaços em branco de cada lado"""
    return fr'^\s*{escape(items)}\s*$'
```  