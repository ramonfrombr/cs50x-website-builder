```python
import check50
from pexpect import EOF
from re import escape


@check50.check()
def existe():
    """taqueria.py existe"""
    check50.exists("taqueria.py")


@check50.check(existe)
def teste_EOF():
    """entrada de EOF interrompe o programa"""
    check50.run("python3 taqueria.py").stdin(EOF, prompt=False).exit(0)


@check50.check(teste_EOF)
def teste_pedido_basico():
    """entrada de \"taco\", \"taco\" e \"salada de tortilla\" resulta em $14.00"""
    itens = ["taco", "taco", "salada de tortilla"]
    output = 14.0
    check50.run("python3 taqueria.py").stdin(itens[0], prompt=True).stdin(itens[1], prompt=True).stdin(itens[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(teste_EOF)
def teste_pedido_basico_2():
    """entrada de \"burrito\", \"bowl\" e \"nachos\" resulta em $27.00"""
    itens = ["burrito", "bowl", "nachos"]
    output = 27.0
    check50.run("python3 taqueria.py").stdin(itens[0], prompt=True).stdin(itens[1], prompt=True).stdin(itens[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(teste_EOF)
def teste_pedido_basico_3():
    """entrada de \"Baja Taco\", \"Quesadilla\" e \"Super Burrito\" resulta em $21.25"""
    itens = ["Baja Taco", "Quesadilla", "Super Burrito"]
    output = 21.25
    check50.run("python3 taqueria.py").stdin(itens[0], prompt=True).stdin(itens[1], prompt=True).stdin(itens[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(teste_EOF)
def teste_capitalizacao():
    """entrada de \"Super quesadilla\" resulta em $9.50"""
    entrada = "Super quesadilla"
    output = 9.50
    check50.run("python3 taqueria.py").stdin(entrada, prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(teste_EOF)
def teste_pedido_invalido():
    """entrada de \"burger\" resulta em nova solicitação"""
    entrada = "burger"
    check50.run("python3 taqueria.py").stdin(entrada, prompt=True).reject()


def regex(custo):
    """corresponde sem diferenciar maiúsculas e minúsculas com sinal de dólar obrigatório e somente caracteres de cada lado"""
    return fr'(?i)^[\D]*\${escape(custo)}[\D]*$'
```