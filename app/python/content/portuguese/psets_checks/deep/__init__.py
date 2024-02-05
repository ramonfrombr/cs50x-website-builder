```python
import check50

@check50.check()
def existe():
    """deep.py existe"""
    check50.existe("deep.py")

@check50.check(existe)
def teste_42():
    """entrada de 42 resulta na saída de Yes"""
    entrada = "42"
    saida = "Yes"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_quarenta_dois():
    """entrada de quarenta-dois resulta na saída de Yes"""
    entrada = "quarenta-dois"
    saida = "Yes"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_quarenta_dois_espaco():
    """entrada de quarenta dois resulta na saída de Yes"""
    entrada = "quarenta dois"
    saida = "Yes"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_quarenta_dois_malformado():
    """entrada de FoRty TwO resulta na saída de Yes"""
    entrada = "FoRty TwO"
    saida = "Yes"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_42_espacos():
    """entrada de 42, com espaços dos dois lados, resulta na saída de Yes"""
    entrada = " 42  "
    saida = "Yes"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_50():
    """entrada de 50 resulta na saída de No"""
    entrada = "50"
    saida = "No"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

@check50.check(existe)
def teste_cinquenta():
    """entrada de cinquenta resulta na saída de No"""
    entrada = "cinquenta"
    saida = "No"
    check50.run("python3 deep.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

def regex(resposta):
    """corresponde de forma case-insensitive com somente espaços em branco dos lados"""
    return rf'(?i)^\s*{resposta}\s*$'
```  