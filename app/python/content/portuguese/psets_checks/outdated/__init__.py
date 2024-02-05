```python
import check50
from re import escape


@check50.check()
def existe():
    """outdated.py existe"""
    check50.exists("outdated.py")


@check50.check(existe)
def teste_digitos_harvard():
    """entrada 9/8/1636 produz 1636-09-08"""
    entrada = "9/8/1636"
    saida = "1636-09-08"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_caracteres_harvard():
    """entrada September 8, 1636 produz 1636-09-08"""
    entrada = "September 8, 1636"
    saida = "1636-09-08"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_digitos_yale():
    """entrada 10/9/1701 produz 1701-10-09"""
    entrada = "10/9/1701"
    saida = "1701-10-09"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_caracteres_yale():
    """entrada October 9, 1701 produz 1701-10-09"""
    entrada = "October 9, 1701"
    saida = "1701-10-09"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_espacos_extra():
    """entrada \" 9/8/1636 \" produz 1636-09-08"""
    entrada = " 9/8/1636 "
    saida = "1636-09-08"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def teste_mes_fora_de_range():
    """entrada 23/6/1912 resulta em reprompt"""
    entrada = "23/6/1912"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_char_fora_de_ordem():
    """entrada 10 December, 1815 resulta em reprompt"""
    entrada = "10 December, 1815"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()

    
@check50.check(existe)
def teste_formato_incorreto():
    """entrada October/9/1701 resulta em reprompt"""
    entrada = "October/9/1701"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()
    
    
@check50.check(existe)
def teste_dia_fora_de_range():
    """entrada 1/50/2000 resulta em reprompt"""
    entrada = "1/50/2000"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_dia_char_fora_de_range():
    """entrada December 80, 1980 resulta em reprompt"""
    entrada = "December 80, 1980"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()


@check50.check(existe)
def teste_sem_virgula():
    """entrada September 8 1636 resulta em reprompt"""
    entrada = "September 8 1636"
    check50.run("python3 outdated.py").stdin(entrada, prompt=True).reject()


def regex(itens):
    """corresponde de forma sensível a maiúsculas/minúsculas com espaços em branco apenas dos lados"""
    return fr'^\s*{escape(itens)}\s*$'
```