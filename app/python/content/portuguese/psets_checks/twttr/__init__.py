```python
import check50
from re import escape


@check50.verifique()
def existe():
    """twttr.py existe"""
    check50.existe("twttr.py")


@check50.verifique(existe)
def test_twitter():
    """entrada do Twitter gera saída do Twttr"""
    entrada = "Twitter"
    saida = "Twttr"
    check50.run("python3 twttr.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def test_nome():
    """entrada de \"Qual é o seu nome?\" gera saída de \"Wht's yr nm?\""""
    entrada = "Qual é o seu nome?"
    saida = "Wht's yr nm?"
    check50.run("python3 twttr.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def test_cs50():
    """entrada de CS50 gera saída de CS50"""
    entrada = "CS50"
    saida = "CS50"
    check50.run("python3 twttr.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def test_python():
    """entrada de PYTHON gera saída de PYTHN"""
    entrada = "PYTHON"
    saida = "PYTHN"
    check50.run("python3 twttr.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


def regex(texto):
    """corresponde de forma sensível a maiúsculas/minúsculas, permitindo caracteres em ambos os lados"""
    return fr'^.*{escape(texto)}.*$'
```  