```python
import check50
from re import escape, search


@check50.check()
def existe():
    """response.py existe"""
    check50.exists("response.py")


@check50.check(existe)
def bibliotecas():
    """response.py não utiliza re e utiliza validators ou validator-collection"""
    with open("response.py", "r") as arquivo:
        conteudo = arquivo.read()
        if not search(r'(?<!#)(?<! )((import[ \t]*(validators|validator_collection))|(from[ \t]*(validators|validator_collection)[ \t]*import[ \t]*[\w\*]+))', conteudo):
            raise check50.Failure("response.py não importa a biblioteca validators ou validator-collection", help="Você esqueceu de incluir \"import validators\" ou \"import validator_collection\"?")
        if search(r'(?<!#)(?<! )((import[ \t]*re)|(from[ \t]*re[ \t]*import[ \t]*[\w\*]+))', conteudo):
            raise check50.Failure("response.py utiliza a biblioteca re", help="Certifique-se de não importar funções da biblioteca re, seja através de \"import re\" ou \"from re import ...\"")


@check50.check(bibliotecas)
def teste_email_valido():
    """response.py exibe Válido quando o endereço de email é \"malan@harvard.edu\""""
    entrada = "malan@harvard.edu"
    saida = "Válido"
    check50.run("python3 response.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(bibliotecas)
def teste_email_valido_2():
    """response.py exibe Válido quando o endereço de email é \"sysadmins@cs50.harvard.edu\""""
    entrada = "sysadmins@cs50.harvard.edu"
    saida = "Válido"
    check50.run("python3 response.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(bibliotecas)
def teste_email_invalido_escrito_por_extenso():
    """response.py exibe Inválido quando o endereço de email é \"malan at harvard dot edu\""""
    entrada = "malan at harvard dot edu"
    saida = "Inválido"
    check50.run("python3 response.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit(0)


@check50.check(bibliotecas)
def teste_email_invalido_símbolos_arroba():
    """response.py exibe Inválido quando o endereço de email é \"malan@@@harvard.edu\""""
    entrada = "malan@@@harvard.edu"
    saida = "Inválido"
    check50.run("python3 response.py").stdin(entrada, prompt=True).stdout(regex(saida), saida, regex=True).exit(0)


"""
Helpers
"""


def regex(texto):
    """faz a correspondência sem diferenciar maiúsculas e minúsculas, permitindo apenas espaços em branco em ambos os lados"""
    return fr'(?i)^\s*{escape(texto)}\s*$'
```