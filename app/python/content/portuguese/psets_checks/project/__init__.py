```python
import re
import check50

@check50.check()
def existe_readme():
    """README.md existe"""
    check50.exists("README.md")

@check50.check(existe_readme)
def readme_final():
    """detalhes do projeto final"""
    texto = open("README.md").read().lower()
    if len(texto) < 1500:
        raise check50.Failure(f"A descrição não é longa o suficiente.")

    urls = re.findall("https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+", texto)
    if not urls:
        raise check50.Failure(f"Falta o URL do vídeo.")

@check50.check(readme_final)
def existe_projeto():
    """project.py existe"""
    check50.exists("project.py")

@check50.check(existe_projeto)
def funcao_principal():
    """função principal existe"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py funcao_principal").exit(0)

@check50.check(existe_projeto)
def funcoes_personalizadas():
    """implementado pelo menos 3 funções de nível superior além da principal"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py funcoes_personalizadas").exit(0)

@check50.check(funcoes_personalizadas)
def teste_unitario():
    """cada função além da principal acompanhada de um teste unitário"""
    check50.include("custom_checks.py")
    codigo = check50.run("python3 custom_checks.py teste_unitario").exit()
    if codigo == 2:
        raise check50.Failure("test_project.py não encontrado")
    elif codigo != 0:
        raise check50.Failure("falha ao executar testes unitários")
```  