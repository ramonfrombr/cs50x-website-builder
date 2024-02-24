```python
import check50
import check50.c

@check50.check()
def existe():
    """hello.c existe"""
    check50.exists("hello.c")

@check50.check(existe)
def compila():
    """hello.c compila"""
    check50.c.compilar("hello.c", lcs50=True)

@check50.check(compila)
def emma():
    """responde ao nome Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compila)
def rodrigo():
    """responde ao nome Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
```  