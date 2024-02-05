```python
import check50
from re import escape


@check50.verifique()
def existe():
    """camel.py existe"""
    check50.existe("camel.py")


@check50.verifique(existe)
def teste_nome():
    """entrada de \"nome\" resulta na saída de \"nome\""""
    entrada = "nome"
    saida = "nome"
    check50.run("python3 camel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).sair()


@check50.verifique(existe)
def teste_primeiroNome():
    """entrada de \"primeiroNome\" resulta na saída de \"primeiro_nome\""""
    entrada = "primeiroNome"
    saida = "primeiro_nome"
    check50.run("python3 camel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).sair()


@check50.verifique(existe)
def teste_primeiroNomePreferido():
    """entrada de \"primeiroNomePreferido\" resulta na saída de \"primeiro_nome_preferido\""""
    entrada = "primeiroNomePreferido"
    saida = "primeiro_nome_preferido"
    check50.run("python3 camel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).sair()


def regex(texto):
    """faz a correspondência fazendo distinção entre maiúsculas e minúsculas, permitindo caracteres de cada lado."""
    return fr'^.*{escape(texto)}.*$'
```