```python
import check50
from re import escape


@check50.verifique()
def existe():
    """interpreter.py existe"""
    check50.existe("interpreter.py")


@check50.verifique(existe)
def teste_um_mais_um():
    """entrada de \"1 + 1\" resulta na saída de 2.0"""
    entrada = "1 + 1"
    saida = "2.0"
    check50.run("python3 interpreter.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def teste_dois_menos_tres():
    """entrada de \"2 - 3\" resulta na saída de -1.0"""
    entrada = "2 - 3"
    saida = "-1.0"
    check50.run("python3 interpreter.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def teste_dois_vezes_dois():
    """entrada de \"2 * 2\" resulta na saída de 4.0"""
    entrada = "2 * 2"
    saida = "4.0"
    check50.run("python3 interpreter.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def teste_cinquenta_dividido_por_cinco():
    """entrada de \"50 / 5\" resulta na saída de 10.0"""
    entrada = "50 / 5"
    saida = "10.0"
    check50.run("python3 interpreter.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.verifique(existe)
def teste_3_dividido_por_2():
    """entrada de \"3 / 2\" resulta na saída de 1.5"""
    entrada = "3 / 2"
    saida = "1.5"
    check50.run("python3 interpreter.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


def regex(num):
    """combina o número fornecido com um decimal flutuante único; permite apenas texto ou espaço em branco de ambos os lados do número"""
    return fr'^[^\d]*{escape(num)}[^\d]*$'
```