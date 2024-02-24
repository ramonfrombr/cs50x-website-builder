```python
import check50
from re import escape


@check50.check()
def existe():
    """bank.py existe"""
    check50.exists("bank.py")


@check50.check(existe)
def testeOla():
    """input \"Hello\" gera output de $0"""
    input = "Hello"
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(existe)
def testeOla_espacos():
    """input de \" Hello \" gera output de $0"""
    input = " Hello "
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(existe)
def testeOla_Newman():
    """input de \"Hello, Newman\" gera output de $0"""
    input = "Hello, Newman"
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(existe)
def testeComo_vai_voce():
    """input de \"How you doing?\" gera output de $20"""
    input = "How you doing?"
    output = "$20"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(existe)
def testeOQue_esta_acontecendo():
    """input de \"What's happening?\" gera output de $100"""
    input = "What's happening?"
    output = "$100"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(existe)
def testeOQue_ta_rolando():
    """input de \"What's up?\" gera output de $100"""
    input = "What's up?"
    output = "$100"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(quantia):
    """corresponde à quantia, permitindo caracteres (não números) em ambos os lados"""
    return fr'^[^\d]*{escape(quantia)}[^\d]*$'
```