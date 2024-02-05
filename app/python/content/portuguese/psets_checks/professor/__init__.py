```python
import check50
from re import escape


@check50.check()
def existe():
    """professor.py existe"""
    check50.exists("professor.py")
    check50.include("testing.py")


@check50.check(existe)
def teste_nivel_baixo():
    """Pequeno Professor rejeita nível 0"""
    check50.run("python3 testing.py get_level").stdin("0", prompt=False).reject()


@check50.check(existe)
def teste_nivel_alto():
    """Pequeno Professor rejeita nível 4"""
    check50.run("python3 testing.py get_level").stdin("4", prompt=False).reject()

    
@check50.check(existe)
def teste_nivel_nao_int():
    """Pequeno Professor rejeita nível de \"um\""""
    check50.run("python3 testing.py get_level").stdin("um", prompt=False).reject()
    
    
@check50.check(existe)
def teste_nivel_valido():
    """Pequeno Professor aceita nível válido"""

    # Testar todos os níveis de 1 a 3
    for nivel in range(1, 4):
        check50.run("python3 testing.py get_level").stdin(str(nivel), prompt=False).exit(0)


@check50.check(teste_nivel_valido)
def teste_intervalo_nivel_1():
    """No Nível 1, o Pequeno Professor gera problemas de adição com 0-9"""
    nivel = "1"

    # Com random.seed(0) em testing.py, 6 + 6 é a saída esperada do randint e randrange com intervalo de 0-9
    saida = "6 + 6 ="
    check50.run("python3 testing.py main").stdin(nivel, prompt=False).stdout(regex(saida), saida, regex=True)


@check50.check(teste_nivel_valido)
def teste_intervalo_nivel_2():
    """No Nível 2, o Pequeno Professor gera problemas de adição com 10-99"""
    nivel = "2"

    # Com random.seed(0) em testing.py, 59 + 63 é a saída esperada do randint e randrange com intervalo de 10-99
    saida = "59 + 63 ="
    check50.run("python3 testing.py main").stdin(nivel, prompt=False).stdout(regex(saida), saida, regex=True)


@check50.check(teste_nivel_valido)
def teste_intervalo_nivel_3():
    """No Nível 3, o Pequeno Professor gera problemas de adição com 100-999"""
    nivel = "3"

    # Com random.seed(0) em testing.py, 964 + 494 é a saída esperada do randint e randrange com intervalo de 100-999
    saida = "964 + 494 ="
    check50.run("python3 testing.py main").stdin(nivel, prompt=False).stdout(regex(saida), saida, regex=True)


@check50.check(teste_intervalo_nivel_1)
def teste_gerar_problemas():
    """O Pequeno Professor gera 10 problemas antes de sair"""
    solucoes = [12, 4, 15, 10, 12, 12, 10, 6, 10, 12]
    programa = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solucao in solucoes:
        programa.stdin(str(solucao), prompt=False)
    programa.exit(0)


@check50.check(teste_gerar_problemas)
def teste_pontuacao():
    """O Pequeno Professor exibe o número de problemas corretos"""
    solucoes = [12, 4, 15, 8, 8, 8, 12, 12, 10, 6, 10, 12]
    programa = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solucao in solucoes:
        programa.stdin(str(solucao), prompt=False)
    programa.stdout(score_regex("9"), "9", regex=True)
    programa.exit(0)


@check50.check(teste_gerar_problemas)
def teste_EEE():
    """O Pequeno Professor exibe EEE quando a resposta está incorreta"""
    check50.run("python3 testing.py main").stdin("1", prompt=False).stdin("0", prompt=False).stdout(regex("EEE"), "EEE", regex=True)


@check50.check(teste_gerar_problemas)
def teste_mostrar_solucao():
    """O Pequeno Professor mostra a solução após 3 tentativas incorretas"""
    programa = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for _ in range(3):
        programa.stdin("0", prompt=False)
    programa.stdout(regex("12"), "12", regex=True)


def regex(texto):
    """faz a correspondência sensível a maiúsculas e minúsculas com qualquer caractere em ambos os lados"""
    return fr'^.*{escape(texto)}.*$'


def score_regex(pontuacao):
    """faz a correspondência insensível a maiúsculas e minúsculas apenas com a impressão final da pontuação"""
    return fr'(?i)[^\d+=]*{pontuacao}[^\d+=]*$'
```