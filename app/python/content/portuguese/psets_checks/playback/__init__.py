```python
import check50

@check50.check()
def existe():
    """playback.py existe"""
    check50.exists("playback.py")

@check50.check(existe)
def testcs50():
    """a entrada de \"This is CS50\" resulta na saída de \"This...is...CS50\""""
    check50.run("python3 playback.py").stdin("This is CS50", prompt=False).stdout(r"This\.\.\.is\.\.\.CS50|This…is…CS50", "This...is...CS50").exit()

@check50.check(existe)
def testfuncoes():
    """a entrada de \"This is our week on functions\" resulta na saída de \"This...is...our...week...on...functions\""""
    check50.run("python3 playback.py").stdin("This is our week on functions", prompt=False).stdout(r"This\.\.\.is\.\.\.our\.\.\.week\.\.\.on\.\.\.functions|This…is…our…week…on…functions", "This...is...our...week...on...functions").exit()

@check50.check(existe)
def testimplementado():
    """a entrada de \"Let's implement a function called hello\" resulta na saída de \"Let's...implement...a...function...called...hello\""""
    check50.run("python3 playback.py").stdin("Let's implement a function called hello", prompt=False).stdout(r"Let's\.\.\.implement\.\.\.a\.\.\.function\.\.\.called\.\.\.hello|Let's…implement…a…function…called…hello", "Let's...implement...a...function...called...hello").exit()
```