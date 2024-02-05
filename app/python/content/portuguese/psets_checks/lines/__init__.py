```python
import check50
from re import escape


@check50.verifique()
def existe():
    """lines.py existe"""
    check50.existe("lines.py")


@check50.verifique(existe)
def teste_argumentos_insuficientes():
    """lines.py sai dado zero argumentos de linha de comando"""
    exit = check50.run("python3 lines.py").sair()
    if exit == 0:
        raise check50.Falha(f"Código de saída não-zero esperado.")


@check50.verifique(existe)
def teste_arquivo_invalido():
    """lines.py sai dado um arquivo sem extensão .py"""
    check50.incluir("invalid_extension.txt")
    exit = check50.run("python3 lines.py invalid_extension.txt").sair()
    if exit == 0:
        raise check50.Falha(f"Código de saída não-zero esperado.")


@check50.verifique(teste_arquivo_invalido)
def teste_mais_argumentos():
    """lines.py sai dado mais de um argumento de linha de comando"""
    check50.incluir("four.py")
    check50.incluir("two-thousand-fifty-eight.py")
    exit = check50.run("python3 lines.py four.py two-thousand-fifty-eight.py").sair()
    if exit == 0:
        raise check50.Falha(f"Código de saída não-zero esperado.")


@check50.verifique(existe)
def teste_simples():
    """lines.py gera 3 dado um arquivo com 3 linhas de código"""
    check50.incluir(f"three.py")
    check50.run(f"python3 lines.py three.py").stdout(regex(3), "3", regex=True).sair(0)


@check50.verifique(teste_simples)
def teste_espacos_em_branco():
    """lines.py gera 4 dado um arquivo com 4 linhas e espaços em branco"""
    check50.incluir(f"four.py")
    check50.run(f"python3 lines.py four.py").stdout(regex(4), "4", regex=True).sair(0)


@check50.verifique(teste_espacos_em_branco)
def teste_comentario():
    """lines.py gera 5 dado um arquivo com 5 linhas, espaços em branco e comentários"""
    check50.incluir(f"five.py")
    check50.run(f"python3 lines.py five.py").stdout(regex(5), "5", regex=True).sair(0)


@check50.verifique(teste_comentario)
def teste_docstring():
    """lines.py gera 9 dado um arquivo com 9 linhas, espaços em branco, comentários e docstrings"""
    check50.incluir(f"nine.py")
    check50.run(f"python3 lines.py nine.py").stdout(regex(9), "9", regex=True).sair(0)


@check50.verifique(teste_docstring)
def teste_open_source():
    """lines.py gera 2058 dado 2058 linhas de código em um arquivo de biblioteca de código aberto"""
    check50.incluir(f"two-thousand-fifty-eight.py")
    check50.run(f"python3 lines.py two-thousand-fifty-eight.py").stdout(regex(2058), "2058", regex=True).sair(0)


def regex(linhas):
    """aceitar número da linha sem dígitos antes ou depois"""
    return fr'^\D*{escape(str(linhas))}\D*$'
```  