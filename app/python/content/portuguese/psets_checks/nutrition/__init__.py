```python
import check50
from re import escape


@check50.check()
def existe():
    """nutrition.py existe"""
    check50.exists("nutrition.py")


@check50.check(existe)
def teste_maca():
    """entrada de maçã gera saída de 130"""
    entrada = "apple"
    saida = "130"
    check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_abacate():
    """entrada de Abacate gera saída de 50"""
    entrada = "Avocado"
    saida = "50"
    check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_kiwi():
    """entrada de Kiwi gera saída de 90"""
    entrada = "Kiwifruit"
    saida = "90"
    check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_pera():
    """entrada de pera gera saída de 100"""
    entrada = "pear"
    saida = "100"
    check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_cerejas_dulces():
    """entrada de Cerejas Dulces gera saída de 100"""
    entrada = "Sweet Cherries"
    saida = "100"
    check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_nenhum():
    """nutrition.py ignora entradas inválidas"""
    entrada = "Tomato"
    saida = ""
    saida = str(check50.run("python3 nutrition.py").stdin(entrada, prompt=True).stdout())
    if saida != "":
        raise check50.Mismatch("", saida)


def regex(texto):
    """faz uma correspondência sensível a maiúsculas, permitindo caracteres (mas não números) em ambos os lados"""
    return fr'^[^\d]*{escape(texto)}[^\d]*$'
```