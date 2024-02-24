```python
import check50
from re import escape


@check50.check()
def existe():
    """figlet.py existe"""
    check50.exists("figlet.py")


@check50.check(existe)
def teste_um_argumento():
    """figlet.py sai dado um argumento de linha de comando"""
    saida = check50.run("python3 figlet.py test").exit()
    if saida == 0:
        raise check50.Failure(f"Código de saída não nulo esperado.")


@check50.check(existe)
def teste_primeiro_argumento_invalido():
    """figlet.py sai dado primeiro argumento inválido de linha de comando"""
    saida = check50.run("python3 figlet.py --front slant").exit()
    if saida == 0:
        raise check50.Failure(f"Código de saída não nulo esperado.")


@check50.check(existe)
def teste_segundo_argumento_invalido():
    """figlet.py sai dado segundo argumento inválido de linha de comando"""
    saida = check50.run("python3 figlet.py --font slnt").exit()
    if saida == 0:
        raise check50.Failure(f"Código de saída não nulo esperado.")


@check50.check(existe)
def teste_texto_inclinado():
    """figlet.py renderiza texto inclinado"""
    verificar_renderizacao_fonte(fonte="slant", texto="CS50")


@check50.check(existe)
def teste_texto_retangular():
    """figlet.py renderiza texto retangular"""
    verificar_renderizacao_fonte(fonte="rectangles", texto="Hello, world")


@check50.check(existe)
def teste_texto_alfabeto():
    """figlet.py renderiza texto de alfabeto"""
    verificar_renderizacao_fonte(fonte="alphabet", texto="Moo")


def expressao_regular(texto):
    """corresponde com sensibilidade a maiúsculas e minúsculas com quaisquer caracteres precedentes e somente espaços em branco após"""
    return fr'^.*{escape(texto)}\s*$'


def verificar_renderizacao_fonte(fonte, texto):
    check50.include(f"{fonte}.txt")
    with open(f"{fonte}.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        saida = ""
        for linha in linhas:
            saida += linha
        check50.run(f"python3 figlet.py -f {fonte}").stdin(texto, prompt=False).stdout(expressao_regular(saida), saida, regex=True).exit(0)
```  