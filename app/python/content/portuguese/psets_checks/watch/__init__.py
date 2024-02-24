```python
import check50
from re import escape


@check50.check()
def existe():
    """watch.py existe"""
    check50.exists("watch.py")
    check50.include("testing.py")


@check50.check(existe)
def teste_http_simples():
    """watch.py extrai link formatado http:// do iframe com único atributo"""
    link = "http://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_https_simples():
    """watch.py extrai link formatado https:// do iframe com único atributo"""
    link = "https://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_https_www_simples():
    """watch.py extrai link formatado https://www. do iframe com único atributo"""
    link = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_http_completo():
    """watch.py extrai link formatado http:// do iframe com múltiplos atributos"""
    link = "http://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_https_completo():
    """watch.py extrai link formatado https:// do iframe com múltiplos atributos"""
    link = "https://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_https_www_completo():
    """watch.py extrai link formatado https://www. do iframe com múltiplos atributos"""
    link = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_nao_youtube():
    """watch.py retorna None ao receber um iframe sem link do YouTube"""
    link = "https://cs50.harvard.edu/python"
    output = "None"
    teste_iframe_simples(link, output)


@check50.check(existe)
def teste_fora_do_iframe():
    """watch.py retorna None ao receber um link do YouTube fora de um iframe"""
    input = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "None"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


"""
Auxiliares
"""


def teste_iframe_simples(link, output):
    input = f"<iframe src=\"{link}\"></iframe>"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


def teste_iframe_completo(link, output):
    input = f"<iframe width=\"560\" height=\"315\" src=\"{link}\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


def regex(text):
    """Corresponde considerando maiúsculas e minúsculas, permitindo apenas espaços em branco de cada lado"""
    return fr'^\s*{escape(text)}\s*$'
```