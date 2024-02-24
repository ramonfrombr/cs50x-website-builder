import check50
from re import escape


@check50.check()
def existe():
    """pizza.py existe"""
    check50.exists("pizza.py")


@check50.check(exists)
def teste_sem_argumentos():
    """pizza.py sai sem argumentos na linha de comando"""
    exit = check50.run("python3 pizza.py").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado não nulo.")


@check50.check(exists)
def teste_nao_existente():
    """pizza.py sai com arquivo inexistente"""
    exit = check50.run("python3 pizza.py non_existent.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado não nulo.")


@check50.check(exists)
def teste_nao_csv():
    """pizza.py sai com arquivo não csv"""
    check50.include("sicilian.txt")
    exit = check50.run("python3 pizza.py sicilian.txt").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado não nulo.")


@check50.check(exists)
def teste_demasiados_argumentos():
    """pizza.py sai com demasiados argumentos na linha de comando"""
    check50.include("regular.csv")
    check50.include("sicilian.csv")
    check50.run("python3 pizza.py regular.csv sicilian.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado não nulo.")


@check50.check(exists)
def teste_siciliano():
    """pizza.py renderiza preços de sicilian.csv"""
    check_table_rendering("sicilian")


@check50.check(exists)
def teste_regular():
    """pizza.py renderiza preços de regular.csv"""
    check_table_rendering("regular")


def regex(texto):
    """combinar com distinção entre maiúsculas e minúsculas com quaisquer caracteres precedentes e somente espaços em branco após"""
    return fr'^.*{escape(texto)}\s*$'


def check_table_rendering(pizza):
    check50.include(f"{pizza}.txt")
    check50.include(f"{pizza}.csv")
    with open(f"{pizza}.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        output = ""
        for linha in linhas:
            output += linha
        check50.run(f"python3 pizza.py {pizza}.csv").stdout(regex(output), output, regex=True).exit(0)