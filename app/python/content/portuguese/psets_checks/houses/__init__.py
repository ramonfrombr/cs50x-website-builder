```python
from cs50 import SQL

import check50
import re

@check50.check()
def existe():
    """importar.py, roster.py existem"""
    check50.exists("import.py", "roster.py")
    check50.include("students.db", "students.csv")

@check50.check(existe)
def importar1():
    """importar.py importa corretamente Harry Potter"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Harry'")
    esperado = [{"first": "Harry", "middle": "James", "last": "Potter", "house": "Gryffindor", "birth": 1980}]
    if rows != esperado:
        raise check50.Mismatch(str(esperado), str(rows))

@check50.check(existe)
def importar2():
    """importar.py importa corretamente Luna Lovegood"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Luna'")
    esperado = [{"first": "Luna", "middle": None, "last": "Lovegood", "house": "Ravenclaw", "birth": 1981}]
    if rows != esperado:
        raise check50.Mismatch(str(esperado), str(rows))

@check50.check(existe)
def contar_importacao():
    """importar.py importa o número correto de linhas"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    atual = db.execute("SELECT COUNT(*) as count FROM students")[0]["count"]
    esperado = 40
    if atual != esperado:
        raise check50.Mismatch(str(esperado), str(atual))

@check50.check(contar_importacao)
def lista_hufflepuff():
    """roster.py produz lista de Hufflepuff correta"""
    check50.include("hufflepuff.txt", "hufflepuff_re.txt")
    atual = check50.run("python3 roster.py Hufflepuff").stdout(timeout=10)
    if not re.search(open("hufflepuff_re.txt").read(), atual):
        raise check50.Mismatch(open("hufflepuff.txt").read(), atual)

@check50.check(contar_importacao)
def lista_gryffindor():
    """roster.py produz lista de Gryffindor correta"""
    check50.include("gryffindor.txt", "gryffindor_re.txt")
    atual = check50.run("python3 roster.py Gryffindor").stdout(timeout=10)
    if not re.search(open("gryffindor_re.txt").read(), atual):
        raise check50.Mismatch(open("gryffindor.txt").read(), atual)
```  