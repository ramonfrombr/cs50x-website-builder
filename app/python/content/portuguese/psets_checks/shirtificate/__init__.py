```python
import check50


@check50.check()
def existe():
    """shirtificate.py existe"""
    check50.exists("shirtificate.py")
    check50.include("shirtificate.png")


@check50.check(existe)
def test_criar_pdf():
    """shirtificate.py cria um arquivo PDF chamado shirtificate.pdf"""
    check50.run("python3 shirtificate.py").stdin("John Harvard", prompt=True).exit(0)
    check50.exists("shirtificate.pdf")
```