```python
import check50

@check50.verifique()
def existe():
    """indoor.py existe"""
    check50.existe("indoor.py")

@check50.verifique(existe)
def testehello():
    """entrada de HELLO resulta na saída hello"""
    check50.run("python3 indoor.py").stdin("HELLO", prompt=False).stdout("hello").sair()

@check50.verifique(existe)
def testecs50():
    """entrada de THIS IS CS50 resulta na saída this is cs50"""
    check50.run("python3 indoor.py").stdin("THIS IS CS50", prompt=False).stdout("this is cs50").sair()

@check50.verifique(existe)
def testenumero():
    """entrada de 50 resulta na saída 50"""
    check50.run("python3 indoor.py").stdin("50", prompt=False).stdout("50").sair()
```  