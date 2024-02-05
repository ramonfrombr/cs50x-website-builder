```python
import check50
from re import escape, sub

"""
configuração
"""

@check50.check()
def existe():
    """numb3rs.py existe"""
    check50.exists("numb3rs.py")
    check50.include("testing.py")

"""
Verificações numb3rs.py
"""

@check50.check(existe)
def teste_ipv4_localhost_correto():
    """numb3rs.py imprime True para 127.0.0.1"""
    entrada = "127.0.0.1"
    saida = "True"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_ipv4_broadcast_correto():
    """numb3rs.py imprime True para 255.255.255.255"""
    entrada = "255.255.255.255"
    saida = "True"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_ipv4_harvard_correto():
    """numb3rs.py imprime True para 140.247.235.144"""
    entrada = "140.247.235.144"
    saida = "True"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_fora_de_faixa_incorreto():
    """numb3rs.py imprime False para 256.255.255.255"""
    entrada = "256.255.255.255"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_fora_de_faixa_incorreto2():
    """numb3rs.py imprime False para 64.128.256.512"""
    entrada = "64.128.256.512"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_numero_bytes_incorreto():
    """numb3rs.py imprime False para 8.8.8"""
    entrada = "8.8.8"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_numero_bytes_incorreto2():
    """numb3rs.py imprime False para 10.10.10.10.10"""
    entrada = "10.10.10.10.10"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_ipv6_incorreto():
    """numb3rs.py imprime False para 2001:0db8:85a3:0000:0000:8a2e:0370:7334"""
    entrada = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

@check50.check(existe)
def teste_nao_ip():
    """numb3rs.py imprime False para cat"""
    entrada = "cat"
    saida = "False"
    check50.run("python3 testing.py").stdin(entrada, prompt=True).stdout(saida).exit(0)

"""
Verificações test_numb3rs.py
"""

@check50.check(existe)
def teste_correto():
    """numb3rs.py correto passa em todas as verificações de test_numb3rs.py"""
    testar_implementacao("numb3rs.py", "correct_test.pyc", "test_numb3rs.py", code=0)

@check50.check(teste_correto)
def teste_primeiro_byte():
    """test_numb3rs.py pega numb3rs.py verificando apenas se o primeiro byte do endereço IPv4 está no alcance"""
    testar_implementacao("numb3rs.py", "first_byte_test.pyc", "test_numb3rs.py", code=1)

@check50.check(teste_correto)
def teste_formato_invalido():
    """test_numb3rs.py pega numb3rs.py aceitando um endereço IPv4 de cinco bytes"""
    testar_implementacao("numb3rs.py", "invalid_format_test.pyc", "test_numb3rs.py", code=1)

"""
Auxiliares
"""

def regex(texto):
    """faz a correspondência sem diferenciar maiúsculas e minúsculas, permitindo apenas espaços em branco de cada lado"""
    return fr'^(?i)\s*{escape(texto)}\s*$'

def testar_implementacao(nome_arquivo_base, nome_implementacao, nome_teste, code=0):
    """Testa o arquivo implementacao, uma implementação do arquivo base, contra as verificações do estudante no arquivo de teste. Espera um determinado status de saída"""

    check50.include("pytest_helper.py")
    check50.include(nome_implementacao)

    # Sobrescrever arquivo base com o código para executar o arquivo de implementação
    with open(nome_arquivo_base, "w") as arquivo_base, open("pytest_helper.py", "r") as pytest_helper:

        texto_pytest_helper = pytest_helper.read()

        # Substituindo a declaração open com nome do arquivo de implementação
        texto_pytest_helper = sub("with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{nome_implementacao}\", \"rb\") as test_file:", texto_pytest_helper)

        # Escrever o texto do arquivo helper para o arquivo base
        arquivo_base.writelines(texto_pytest_helper)

    # Esperar que pytest saia com o código de status dado
    return check50.run(f"pytest {nome_teste}").exit(code=code)
```