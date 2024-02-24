```python
import check50
import check50.c

@check50.check()
def existe():
    """readability.c existe"""
    check50.exists("readability.c")

@check50.check(existe)
def compila():
    """readability.c compila"""
    check50.c.compile("readability.c", lcs50=True)

@check50.check(compila)
def uma_frase():
    """manipula uma única frase com várias palavras"""
    check50.run("./readability").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout("Grau 7\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def uma_frase_outra_pontuacao():
    """manipula pontuação dentro de uma única frase"""
    check50.run("./readability").stdin("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.").stdout("Grau 9\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def uma_frase_complexa():
    """manipula frase única mais complexa"""
    check50.run("./readability").stdin("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"").stdout("Grau 8\n").stdout(check50.EOF).exit(0)

@check50.check(compila)
def multiplas_frases():
    """manipula múltiplas frases"""
    check50.run("./readability").stdin("