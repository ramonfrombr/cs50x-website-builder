```python
import check50
from re import escape

@check50.check()
def existe():
    """game.py existe"""
    check50.exists("game.py")
    check50.include("testing.py")

@check50.check(existe)
def teste_nivel_string():
    """game.py rejeita nível não numérico"""
    check50.run("python3 game.py").stdin("gato", prompt=True).reject()

@check50.check(existe)
def teste_nivel_inteiro():
    """game.py rejeita nível fora do alcance"""
    check50.run("python3 game.py").stdin("0", prompt=True).reject()

@check50.check(existe)
def teste_nivel_valido():
    """game.py aceita nível válido"""
    check50.run("python3 game.py").stdin("10", prompt=True).stdout(regex("Adivinhe"), "Adivinhe:", regex=True).kill()

@check50.check(teste_nivel_valido)
def teste_palpite_string():
    """game.py rejeita palpite não numérico"""
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("gato", prompt=True).reject()

@check50.check(teste_nivel_valido)
def teste_fora_de_alcance_pequeno():
    """game.py rejeita palpite abaixo do intervalo especificado com \"Muito pequeno!\""""
    output = "Muito pequeno!"
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("0", prompt=True).stdout(regex(output), output, regex=True).reject()

@check50.check(teste_nivel_valido)
def teste_fora_de_alcance_grande():
    """game.py rejeita palpite acima do intervalo especificado com \"Muito grande!\""""
    output = "Muito grande!"
    check50.run("python3 testing.py").stdin("4", prompt=True).stdin("8", prompt=True).stdout(regex(output), output, regex=True).reject()

@check50.check(teste_nivel_valido)
def teste_muito_grande():
    """game.py exibe \"Muito grande!\" quando o palpite é muito grande"""
    output = "Muito grande!"
    check50.run("python3 testing.py").stdin("22", prompt=True).stdin("18", prompt=True).stdout(regex(output), output, regex=True).reject()

@check50.check(teste_nivel_valido)
def teste_justo():
    """game.py exibe \"Na mosca!\" quando o palpite está correto"""
    output = "Na mosca!"
    check50.run("python3 testing.py").stdin("6", prompt=True).stdin("4", prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(teste_nivel_valido)
def teste_muito_pequeno():
    """game.py exibe \"Muito pequeno!\" quando o palpite é muito pequeno"""
    output = "Muito pequeno!"
    check50.run("python3 testing.py").stdin("5", prompt=True).stdin("2", prompt=True).stdout(regex(output), output, regex=True).reject()

def regex(texto):
    """corresponde sem diferenciar maiúsculas e minúsculas com qualquer caractere dos dois lados"""
    return fr'(?i)^.*{escape(texto)}.*$'
```