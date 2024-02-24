```python
import check50

@check50.check()
def existe():
    """scourgify.py existe"""
    check50.exists("scourgify.py")
    check50.include("before.csv")
    check50.include("after_correct.csv")
    check50.include("before_long.csv")
    check50.include("after_long_correct.csv")

@check50.check(exists)
def teste_sem_argumentos():
    """scourgify.py sai se nenhum argumento de linha de comando for fornecido"""
    exit = check50.run("python3 scourgify.py").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado diferente de zero.")

@check50.check(exists)
def teste_argumentos_insuficientes():
    """scourgify.py sai se poucos argumentos de linha de comando forem fornecidos"""
    exit = check50.run("python3 scourgify.py before.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado diferente de zero.")

@check50.check(exists)
def teste_argumentos_excedentes():
    """scourgify.py sai se muitos argumentos de linha de comando forem fornecidos"""
    exit = check50.run("python3 scourgify.py before.csv after.csv before_long.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado diferente de zero.")

@check50.check(exists)
def teste_arquivo_invalido():
    """scourgify.py sai se o arquivo de entrada fornecido for inválido"""
    exit = check50.run("python3 scourgify.py invalid_name.csv after.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Código de saída esperado diferente de zero.")

@check50.check(exists)
def teste_criar_arquivo():
    """scourgify.py cria novo arquivo CSV"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    check50.exists("after.csv")

@check50.check(test_create_file)
def teste_limpar_arquivo():
    """scourgify.py limpa arquivo CSV curto"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    check50.exists("after.csv")

    with open("after.csv", "r") as student_file, open("after_correct.csv") as check_file:
        compare_csv_files(student_file, check_file)

@check50.check(test_clean_file)
def teste_limpar_arquivo_longo():
    """scourgify.py limpa arquivo CSV longo"""
    check50.run("python3 scourgify.py before_long.csv after_long.csv").exit(0)
    check50.exists("after_long.csv")

    with open("after_long.csv", "r") as student_file, open("after_long_correct.csv") as check_file:
        compare_csv_files(student_file, check_file)

def compare_csv_files(student_file, check_file):
    """compara dois arquivos CSV, padronizando CRLF e CR em LF (quebra de linha)"""

    student_output = student_file.read().replace("\r\n", "\n").replace("\r", "\n")
    correct_output = check_file.read().replace("\r\n", "\n").replace("\r", "\n")
    
    if student_output == correct_output + correct_output:
        raise check50.Failure("scourgify.py não produz CSV com o formato especificado", help="Você abriu o arquivo por engano no modo de anexar (append)?")
    elif student_output != correct_output:
        raise check50.Failure("scourgify.py não produz CSV com o formato especificado")
```