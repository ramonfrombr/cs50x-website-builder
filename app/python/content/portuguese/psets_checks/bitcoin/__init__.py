```python
import check50
from re import escape

preço = 37817.3283

@check50.check()
def existe():
    """bitcoin.py existe"""
    check50.exists("bitcoin.py")
    check50.include("testing.py")

@check50.check(existe)
def teste_sem_argumentos():
    """bitcoin.py sai sem argumentos de linha de comando"""
    check50.run("python3 bitcoin.py").exit(1)

@check50.check(existe)
def teste_argumento_não_numérico():
    """bitcoin.py sai dado argumento não numérico de linha de comando"""
    check50.run("python3 bitcoin.py cat").exit(1)

@check50.check(existe)
def teste_única_moeda():
    """bitcoin.py fornece preço de 1 Bitcoin com 4 casas decimais"""
    moedas = 1
    montante = moedas * preço
    check50.run(f"python3 testing.py {moedas}").stdout(regex(montante), f'${montante:,.4f}', regex=True).exit(0)

@check50.check(existe)
def teste_duas_moedas():
    """bitcoin.py fornece preço de 2 Bitcoins com 4 casas decimais"""
    moedas = 2
    montante = moedas * preço
    check50.run(f"python3 testing.py {moedas}").stdout(regex(montante), f'${montante:,.4f}', regex=True).exit(0)

@check50.check(existe)
def teste_moedas_decimais():
    """bitcoin.py fornece preço de 2.5 Bitcoins com 4 casas decimais"""
    moedas = 2.5
    montante = moedas * preço
    check50.run(f"python3 testing.py {moedas}").stdout(regex(montante), f'${montante:,.4f}', regex=True).exit(0)

def regex(montante):
    """corresponde de forma sensível a maiúsculas e minúsculas com qualquer caractere antes ou depois"""
    montante = f'${montante:,.4f}'
    return fr'^.*{escape(montante)}.*$'
```