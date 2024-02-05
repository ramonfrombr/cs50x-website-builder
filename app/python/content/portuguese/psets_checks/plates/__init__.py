```python
import check50
from re import escape


@check50.check()
def existe():
    """plates.py existe"""
    check50.exists("plates.py")


@check50.check(existe)
def teste_cs50():
    """entrada de CS50 gera saída de Válido"""
    entrada = "CS50"
    saida = "Valid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Jogador Pronto Um
@check50.check(existe)
def teste_ECTO88():
    """entrada de ECTO88 gera saída de Válido"""
    entrada = "ECTO88"
    saida = "Valid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# O dia da folga de Ferris Bueller
@check50.check(existe)
def teste_NRVOUS():
    """entrada de NRVOUS gera saída de Válido"""
    entrada = "NRVOUS"
    saida = "Valid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Testes para Zero como primeiro número
@check50.check(existe)
def teste_CS05():
    """entrada de CS05 gera saída de Inválido"""
    entrada = "CS05"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Primeiros dois caracteres não são letras
@check50.check(existe)
def teste_50():
    """entrada de 50 gera saída de Inválido"""
    entrada = "50"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Números antes de letras (após as duas primeiras letras)
@check50.check(existe)
def teste_CS50P2():
    """entrada de CS50P2 gera saída de Inválido"""
    entrada = "CS50P2"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Caracteres não alfanuméricos (após as duas primeiras letras)
@check50.check(existe)
def teste_PI3_14():
    """entrada de PI3.14 gera saída de Inválido"""
    entrada = "PI3.14"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Comprimento (muito curto)
@check50.check(existe)
def teste_445108():
    """entrada de H gera saída de Inválido"""
    entrada = "H"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


# Comprimento (muito longo) (De Volta para o Futuro)
@check50.check(existe)
def teste_OUTATIME():
    """entrada de OUTATIME gera saída de Inválido"""
    entrada = "OUTATIME"
    saida = "Invalid"
    check50.run("python3 plates.py").stdin(entrada, prompt=True).stdout(
        regex(saida), saida, regex=True
    ).exit()


def regex(texto):
    """corresponde insensitivamente a maiúsculas e minúsculas, permitindo apenas espaços de cada lado"""
    return rf"(?i)^\s*{escape(texto)}\s*$"
```  