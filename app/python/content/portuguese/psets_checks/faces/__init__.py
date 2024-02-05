```python
import check50

@check50.check()
def existe():
    """faces.py existe"""
    check50.exists("faces.py")

@check50.check(existe)
def testeOla():
    """entrada de \"Hello :)\" gera saída de \"Hello 🙂\""""
    saida = check50.run("python3 faces.py").stdin("Hello :)", prompt=False).stdout("Hello 🙂").exit()

@check50.check(existe)
def testeAdeus():
    """entrada de \"Goodbye :(\" gera saída de \"Goodbye 🙁\""""
    saida = check50.run("python3 faces.py").stdin("Goodbye :(", prompt=False).stdout("Goodbye 🙁").exit()

@check50.check(existe)
def testeMultiplo():
    """entrada de \"Hello :) Goodbye :(\" gera saída de \"Hello 🙂 Goodbye 🙁\""""
    saida = check50.run("python3 faces.py").stdin("Hello :) Goodbye :(", prompt=False).stdout("Hello 🙂 Goodbye 🙁").exit()
```