```python
import check50
from re import escape


@check50.check()
def existe():
    """emojize.py existe"""
    check50.existe("emojize.py")


@check50.check(existe)
def teste_primeiro_lugar():
    """entrada de \":1st_place_medal:\" gera a saída 🥇"""
    entrada = ":1st_place_medal:"
    saida = "🥇"
    check50.run("python3 emojize.py").stdin(entrada, prompt=False).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(existe)
def teste_polegar_para_cima():
    """entrada de \":thumbsup:\" gera a saída de 👍"""
    entrada = ":thumbsup:"
    saida = "👍"
    check50.run("python3 emojize.py").stdin(entrada, prompt=False).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(existe)
def teste_alias_na_frase():
    """entrada de \"olá, :earth_asia:\" gera a saída olá, 🌏"""
    entrada = "olá, :earth_asia:"
    saida = "olá, 🌏"
    check50.run("python3 emojize.py").stdin(entrada, prompt=False).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(existe)
def teste_multiplo():
    """entrada de \":candy: ou :ice_cream:\" gera a saída 🍬 ou 🍨?"""
    entrada = ":candy: ou :ice_cream:?"
    saida = "🍬 ou 🍨?"
    check50.run("python3 emojize.py").stdin(entrada, prompt=False).stdout(regex(saida), saida, regex=True).exit(0)


def regex(texto):
    """faz a correspondência de forma sensível a maiúsculas com quaisquer caracteres anteriores e somente espaço em branco depois"""
    return fr'^.*{escape(texto)}\s*$'
```  