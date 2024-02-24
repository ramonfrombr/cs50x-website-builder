```python
import check50
import re

@check50.check()
def existe():
    """einstein.py existe"""
    check50.exists("einstein.py")

@check50.check(existe)
def teste1():
    """entrada de 1 resulta na saída de 90000000000000000"""
    output = check50.run("python3 einstein.py").stdin("1", prompt=False).stdout()

    # Extrai o número da saída
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Parece que seu programa não retornou um número!")
    numero = match.group(0)

    # Compara com o número correto
    if not re.match(r"^90(?:,?0{3}){5}(?:\.0+)?$", numero) and not re.match(
        r"^90(?:\.?0{3}){5}(?:,0+)?$", numero
    ):
        raise check50.Mismatch(
            "90000000000000000",
            numero,
            help="Parece que sua saída pode não ser o número correto!"
        )

@check50.check(existe)
def teste14():
    """entrada de 14 resulta na saída de 1260000000000000000"""
    output = check50.run("python3 einstein.py").stdin("14", prompt=False).stdout()

    # Extrai o número da saída
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Parece que seu programa não retornou um número!")
    numero = match.group(0)

    # Compara com o número correto
    if not re.match(r"^1,?260(?:,?0{3}){5}(?:\.0+)?$", numero) and not re.match(
        r"1\.?260(?:\.?0{3}){5}(?:,0+)?$", numero
    ):
        raise check50.Mismatch(
            "1260000000000000000",
            numero,
            help="Parece que sua saída pode não ser o número correto!"
        )

@check50.check(existe)
def teste50():
    """entrada de 50 resulta na saída de 4500000000000000000"""
    output = check50.run("python3 einstein.py").stdin("50", prompt=False).stdout()

    # Extrai o número da saída
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Parece que seu programa não retornou um número!")
    numero = match.group(0)

    # Compara com o número correto
    if not re.match(r"^4,?500(?:,?0{3}){5}(?:\.0+)?$", numero) and not re.match(
        r"^4\.?500(?:\.?0{3}){5}(?:,0+)?$", numero
    ):
        raise check50.Mismatch(
            "4500000000000000000",
            numero,
            help="Parece que sua saída pode não ser o número correto!"
        )
```