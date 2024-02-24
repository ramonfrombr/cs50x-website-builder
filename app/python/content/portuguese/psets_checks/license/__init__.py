```python
import check50

@check50.check()
def existe():
    """license.py existe"""
    check50.existe("license.py")

@check50.check(existe)
def testePython():
    """entrada de PYTHON gera PYTHN"""
    check50.run("python3 license.py").stdin("PYTHON", prompt=False).stdout("PYTHN").exit()

@check50.check(existe)
def testeProgramador():
    """entrada de PROGRAMMER gera PRGRMMR"""
    check50.run("python3 license.py").stdin("PROGRAMMER", prompt=False).stdout("PRGRMMR").exit()

@check50.check(existe)
def testeCS50():
    """entrada de CS50 gera CS50"""
    check50.run("python3 license.py").stdin("CS50", prompt=False).stdout("CS50").exit()
```  