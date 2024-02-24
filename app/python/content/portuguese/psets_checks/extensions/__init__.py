```python
import check50
from re import escape


@check50.check()
def existe():
    """extensions.py existe"""
    check50.exists("extensions.py")


@check50.check(existe)
def testgif():
    """entrada de cs50.gif produz saída de image/gif"""
    entrada = "cs50.gif"
    saida = "image/gif"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testjpg():
    """entrada de happy.jpg produz saída de image/jpeg"""
    entrada = "happy.jpg"
    saida = "image/jpeg"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testjpeg():
    """entrada de happy.jpeg produz saída de image/jpeg"""
    entrada = "happy.jpeg"
    saida = "image/jpeg"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testpng():
    """entrada de check.png produz saída de image/png"""
    entrada = "check.png"
    saida = "image/png"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testpdf():
    """entrada de document.pdf produz saída de application/pdf"""
    entrada = "document.pdf"
    saida = "application/pdf"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testtxt():
    """entrada de plain.txt produz saída de text/plain"""
    entrada = "plain.txt"
    saida = "text/plain"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testzip():
    """entrada de files.zip produz saída de application/zip"""
    entrada = "files.zip"
    saida = "application/zip"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testbin():
    """entrada de application.bin produz saída de application/octet-stream"""
    entrada = "application.bin"
    saida = "application/octet-stream"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testpdf_capital():
    """entrada de document.PDF produz saída de application/pdf"""
    entrada = "document.PDF"
    saida = "application/pdf"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()


@check50.check(existe)
def testpdf_spaces():
    """entrada de document.PDF, com espaços dos lados, produz saída de application/pdf"""
    entrada = " document.PDF   "
    saida = "application/pdf"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

    
@check50.check(existe)
def test_two():
    """entrada de test.txt.pdf, com uma extensão extra, produz saída de application/pdf"""
    entrada = "test.txt.pdf"
    saida = "application/pdf"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()

    
@check50.check(existe)
def testjpg_substring():
    """entrada de zipper.jpg, com um nome de extensão diferente, produz saída de image/jpeg"""
    entrada = "zipper.jpg"
    saida = "image/jpeg"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()
    

@check50.check(existe)
def test_noextension():
    """entrada de myfile, sem extensão, produz saída de application/octet-stream"""
    entrada = "myfile"
    saida = "application/octet-stream"
    check50.run("python3 extensions.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit()
    
    
def regex(texto):
    """combina maiúsculas/minúsculas, permitindo espaços nos lados"""
    return fr'^\s*{escape(texto)}\s*$'
```  