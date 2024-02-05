```python
import check50
import re

@check50.check()
def existe():
    """jar.py existe"""
    check50.exists("jar.py")
    check50.exists("test_jar.py")
    check50.include("test_file.py")


@check50.check(existe)
def teste_inicializacao():
    """O construtor Jar inicializa um pote de biscoitos com a capacidade fornecida"""
    check50.run("pytest test_file.py -k 'test_init'").exit(0)


@check50.check(existe)
def teste_erro_valor_inicializacao():
    """O construtor Jar levanta ValueError quando chamado com capacidade negativa"""
    check50.run("pytest test_file.py -k 'test_raises_value_error'").exit(0)


@check50.check(existe)
def teste_vazio_str():
    """Pote vazio imprime zero cookies"""
    check50.run("pytest test_file.py -k 'test_empty_str'").exit(0)


@check50.check(existe)
def teste_cheio_str():
    """Pote imprime a quantidade total de cookies depositados"""
    check50.run("pytest test_file.py -k 'test_full_str'").exit(0)


@check50.check(existe)
def teste_muito_cheio():
    """O método de depósito do pote levanta ValueError quando os cookies depositados excedem a capacidade do pote"""
    check50.run("pytest test_file.py -k 'test_too_full'").exit(0)


@check50.check(existe)
def teste_retirada():
    """O método de retirada do pote remove cookies do tamanho do pote"""
    check50.run("pytest test_file.py -k 'test_withdraw'").exit(0)


@check50.check(existe)
def teste_vazio():
    """O método de retirada do pote levanta ValueError quando os cookies retirados excedem o tamanho do pote"""
    check50.run("pytest test_file.py -k 'test_empty'").exit(0)


@check50.check(existe)
def teste_arquivo_aluno_passa():
    """A implementação do Jar passa em todos os testes em test_jar.py"""
    check50.run("pytest test_jar.py").exit(0)


@check50.check(test_arquivo_aluno_passa)
def teste_numero_funcoes():
    """test_jar.py contém pelo menos quatro funções"""
    out = check50.run("pytest test_jar.py").stdout()
    matches = re.search(r'(\d) passed', out)
    if not matches:
        raise check50.Failure("Não foi possível analisar a saída do pytest")
    try:
        funcoes = int(matches.groups(1)[0])
    except ValueError:
        raise check50.Failure("Não foi possível analisar a saída do pytest")
    if funcoes < 4:
        raise check50.Failure("test_jar.py não contém pelo menos quatro funções")
```  