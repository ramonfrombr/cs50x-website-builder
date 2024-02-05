```python
import check50
import check50.c
import os


@check50.check()
def existe():
    """dictionary.c existe"""
    check50.exists("dictionary.c")


@check50.check(existe)
def compila():
    """speller compila"""
    check50.include("speller.c", "Makefile")
    if not os.path.exists("dictionary.h"):
        check50.include("dictionary.h")
    check50.run("make").exit(0)


@check50.check(compila)
def basico():
    """manipula palavras mais básicas corretamente"""
    check50.include("basic")
    check50.run("./speller basic/dict basic/text").stdout(open("basic/out")).exit(0)


@check50.check(compila)
def tamanho_minimo():
    """manipula palavras de tamanho mínimo (1 caractere) corretamente"""
    check50.include("min_length")
    check50.run("./speller min_length/dict min_length/text").stdout(open("min_length/out")).exit(0)


@check50.check(compila)
def tamanho_maximo():
    """manipula palavras de tamanho máximo (45 caracteres) corretamente"""
    check50.include("max_length")
    check50.run("./speller max_length/dict max_length/text").stdout(open("max_length/out")).exit(0)


@check50.check(compila)
def apostrofo():
    """manipula palavras com apóstrofos corretamente"""
    check50.include("apostrophe")
    check50.run("./speller apostrophe/without/dict apostrophe/with/text").stdout(open("apostrophe/outs/without-with")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/without/text").stdout(open("apostrophe/outs/with-without")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/with/text").stdout(open("apostrophe/outs/with-with")).exit(0)


@check50.check(compila)
def maiusculas():
    """verifica ortografia sem diferenciar maiúsculas e minúsculas"""
    check50.include("case")
    check50.run("./speller case/dict case/text").stdout(open("case/out")).exit(0)


@check50.check(compila)
def subcadena():
    """manipula subcadeias corretamente"""
    check50.include("substring")
    check50.run("./speller substring/dict substring/text").stdout(open("substring/out")).exit(0)


@check50.check(subcadena)
def memoria():
    """o programa não tem erros de memória"""
    check50.c.valgrind("./speller substring/dict substring/text").stdout(open("substring/out"), timeout=10).exit(0)
```