```python
import check50
de re import escape


@check50.check()
def existe():
    """coke.py existe"""
    check50.exists("coke.py")


@check50.check(exists)
def teste_25():
    """coke aceita 25 centavos"""
    entrada = "25"
    saida = "Quantia Devida: 25\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdout(saida, regex=True).kill()


@check50.check(exists)
def teste_10():
    """coke aceita 10 centavos"""
    entrada = "10"
    saida = "Quantia Devida: 40\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdout(saida, regex=True).kill()


@check50.check(exists)
def teste_1():
    """coke aceita 5 centavos"""
    entrada = "5"
    saida = "Quantia Devida: 45\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdout(saida, regex=True).kill()


@check50.check(exists)
def teste_invalido():
    """coke rejeita quantia inválida de centavos"""
    entrada = "30"
    saida = "Quantia Devida: 50\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdout(saida, regex=True).kill()


@check50.check(exists)
def teste_multiplo():
    """coke aceita entrada contínua"""
    entrada = "10"
    saida = "Quantia Devida: 30\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdin(entrada, prompt=True).stdout(saida, regex=True).kill()


@check50.check(exists)
def teste_terminar():
    """coke termina em 50 centavos"""
    entrada = "10"
    saida = "Troco Devido: 0\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdin(entrada, prompt=True).stdin(entrada, prompt=True).stdin(entrada, prompt=True).stdin(entrada, prompt=True).stdout(saida, regex=True).exit()


@check50.check(exists)
def teste_troco():
    """coke fornece troco correto"""
    entrada = "25"
    saida = "Troco Devido: 10\n"
    check50.run("python3 coke.py").stdin(entrada, prompt=True).stdin("10", prompt=True).stdin(entrada, prompt=True).stdout(saida, regex=True).exit()
```