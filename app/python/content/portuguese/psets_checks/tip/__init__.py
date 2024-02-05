```python
import check50

@check50.check()
def existe():
    """tip.py existe"""
    check50.exists("tip.py")

@check50.check(existe)
def teste50():
    """entrada de $50.00 e 15% resulta em $7.50"""
    check50.run("python3 tip.py").stdin("$50.00", prompt=True).stdin("15%", prompt=True).stdout(r'\$?7.50', 'Deixe $7.50\n').exit()

@check50.check(existe)
def teste100():
    """entrada de $100.00 e 18% resulta em $18.00"""
    check50.run("python3 tip.py").stdin("$100.00", prompt=True).stdin("18%", prompt=True).stdout(r'\$?18.00', 'Deixe $18.00\n').exit()

@check50.check(existe)
def teste15():
    """entrada de $15.00 e 25% resulta em $3.75"""
    check50.run("python3 tip.py").stdin("$15.00", prompt=True).stdin("25%", prompt=True).stdout(r'\$?3.75', 'Deixe $3.75\n').exit()
```