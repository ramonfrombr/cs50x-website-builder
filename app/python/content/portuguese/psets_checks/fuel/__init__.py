```python
import check50
from re import escape


@check50.check()
def existe():
    """fuel.py existe"""
    check50.exists("fuel.py")


@check50.check(existe)
def teste_3_sobre_4():
    """entrada de 3/4 resulta em saída de 75%"""
    entrada = "3/4"
    saida = "75%"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_arredondar_para_baixo():
    """entrada de 1/3 resulta em saída de 33%"""
    entrada = "1/3"
    saida = "33%"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_arredondar_para_cima():
    """entrada de 2/3 resulta em saída de 67%"""
    entrada = "2/3"
    saida = "67%"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_vazio():
    """entrada de 0/100 resulta em saída de E"""
    entrada = "0/100"
    saida = "E"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_quase_vazio():
    """entrada de 1/100 resulta em saída de E"""
    entrada = "1/100"
    saida = "E"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_cheio():
    """entrada de 100/100 resulta em saída de F"""
    entrada = "100/100"
    saida = "F"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_quase_cheio():
    """entrada de 99/100 resulta em saída de F"""
    entrada = "99/100"
    saida = "F"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_ZeroDivisionError():
    """entrada de 100/0 resulta em reprompt"""
    entrada = "100/0"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_numerador_maior_que_denominador():
    """entrada de 10/3 resulta em reprompt"""
    entrada = "10/3"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_conversao_str():
    """entrada de three/four resulta em reprompt"""
    entrada = "three/four"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_numerador_float():
    """entrada de 1.5/4 resulta em reprompt"""
    entrada = "1.5/4"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_denominador_float():
    """entrada de 3/5.5 resulta em reprompt"""
    entrada = "3/5.5"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_sem_barra():
    """entrada de 5-10 resulta em reprompt"""
    entrada = "5-10"
    check50.run("python3 fuel.py").stdin(entrada, prompt=True).reject()


def regex(percentual):
    """corresponde de forma case-insensitive com espaço em branco em ambos os lados"""
    return fr'(?i)^\s*{escape(percentual)}\s*$'
```