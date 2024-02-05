```python
import check50

@check50.verificar()
def existe():
    """dna.py existe"""
    check50.existe("dna.py")
    check50.incluir("sequências", "bancos de dados")

@check50.verificar(existe)
def teste1():
    """identifica corretamente sequências/1.txt"""
    check50.executar("python3 dna.py bancos de dados/small.csv sequências/1.txt").stdout("^Bob", "Bob\n", timeout=5).sair()

@check50.verificar(existe)
def teste2():
    """identifica corretamente sequências/2.txt"""
    check50.executar("python3 dna.py bancos de dados/small.csv sequências/2.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()

@check50.verificar(existe)
def teste3():
    """identifica corretamente sequências/3.txt"""
    check50.executar("python3 dna.py bancos de dados/small.csv sequências/3.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()

@check50.verificar(existe)
def teste4():
    """identifica corretamente sequências/4.txt"""
    check50.executar("python3 dna.py bancos de dados/small.csv sequências/4.txt").stdout("^Alice", "Alice\n", timeout=5).sair()

@check50.verificar(existe)
def teste5():
    """identifica corretamente sequências/5.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).sair()

@check50.verificar(existe)
def teste6():
    """identifica corretamente sequências/6.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/6.txt").stdout("^Luna", "Luna\n", timeout=5).sair()

@check50.verificar(existe)
def teste7():
    """identifica corretamente sequências/7.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/7.txt").stdout("^Ron", "Ron\n", timeout=5).sair()

@check50.verificar(existe)
def teste8():
    """identifica corretamente sequências/8.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).sair()

@check50.verificar(existe)
def teste9():
    """identifica corretamente sequências/9.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/9.txt").stdout("^Draco", "Draco\n", timeout=5).sair()

@check50.verificar(existe)
def teste10():
    """identifica corretamente sequências/10.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/10.txt").stdout("^Albus", "Albus\n", timeout=5).sair()

@check50.verificar(existe)
def teste11():
    """identifica corretamente sequências/11.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).sair()

@check50.verificar(existe)
def teste12():
    """identifica corretamente sequências/12.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/12.txt").stdout("^Lily", "Lily\n", timeout=5).sair()

@check50.verificar(existe)
def teste13():
    """identifica corretamente sequências/13.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/13.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()

@check50.verificar(existe)
def teste14():
    """identifica corretamente sequências/14.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/14.txt").stdout("^Severus", "Severus\n", timeout=5).sair()

@check50.verificar(existe)
def teste15():
    """identifica corretamente sequências/15.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).sair()

@check50.verificar(existe)
def teste16():
    """identifica corretamente sequências/16.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/16.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()

@check50.verificar(existe)
def teste17():
    """identifica corretamente sequências/17.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/17.txt").stdout("^Harry", "Harry\n", timeout=5).sair()

@check50.verificar(existe)
def teste18():
    """identifica corretamente sequências/18.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/18.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()

@check50.verificar(existe)
def teste19():
    """identifica corretamente sequências/19.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/19.txt").stdout("^Fred", "Fred\n", timeout=5).sair()

@check50.verificar(existe)
def teste20():
    """identifica corretamente sequências/20.txt"""
    check50.executar("python3 dna.py bancos de dados/large.csv sequências/20.txt").stdout("^[Nn]o [Mm]atch\.?\n", "Sem correspondência\n", timeout=5).sair()
```