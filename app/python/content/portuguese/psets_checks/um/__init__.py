```python
import check50
from re import escape, sub

"""
Configuração
"""


@check50.check()
def existe():
    """um.py e test_um.py existem"""
    check50.exists("um.py")
    check50.exists("test_um.py")
    check50.include("testing.py")


"""
Verificações em um.py
"""


@check50.check(existe)
def teste_simples():
    """um.py retorna 1 para \"um\""""
    testar_frase(input="um", count="1")


@check50.check(existe)
def teste_virgula():
    """um.py retorna 1 para \"Hello, um, mundo\""""
    testar_frase(input="Hello, um, mundo", count="1")


@check50.check(existe)
def teste_ponto():
    """um.py retorna 1 para \"Isso é, um... CS50.\""""
    testar_frase(input="Isso é, um... CS50.", count="1")


@check50.check(existe)
def teste_maiusculo():
    """um.py retorna 1 para \"Um... o que são expressões regulares?\""""
    testar_frase(input="Um... o que são expressões regulares?", count="1")


@check50.check(existe)
def teste_multiplo():
    """um.py retorna 2 para \"Um, obrigado, um, expressões regulares fazem sentido agora.\""""
    testar_frase(input="Um, obrigado, um, expressões regulares fazem sentido agora.", count="2")


@check50.check(existe)
def teste_parte_da_palavra():
    """um.py retorna 2 para \"Um? Mamãe? É este o álbum onde, um, umm, os ex-alunos desajeitados tocam bateria?\""""
    testar_frase(input="Um? Mamãe? É este o álbum onde, um, umm, os ex-alunos desajeitados tocam bateria?", count="2")


"""
Verificações em test_um.py
"""


@check50.check(existe)
def teste_correto():
    """um.py correto passa em todas as verificações de test_um.py"""
    testar_implementacao("um.py", "correto_test.pyc", "test_um.py", code=0)


@check50.check(teste_correto)
def teste_partes_das_palavras():
    """test_um.py captura um.py combinando \"um\" em palavras"""
    testar_implementacao("um.py", "partes_das_palavras_test.pyc", "test_um.py", code=1)


@check50.check(teste_correto)
def teste_apenas_espacos():
    """test_um.py captura um.py com expressão regular que requer espaços ao redor de \"um\""""
    testar_implementacao("um.py", "apenas_espacos_test.pyc", "test_um.py", code=1)


@check50.check(teste_correto)
def teste_sensivel_ao_caso():
    """test_um.py captura um.py sem correspondência insensível a maiúsculas e minúsculas de \"um\""""
    testar_implementacao("um.py", "sensivel_ao_caso_test.pyc", "test_um.py", code=1)


"""
Auxiliares
"""


def testar_frase(input, count):
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(count).exit(0)


def regex(texto):
    """Corresponder sem distinguir maiúsculas e minúsculas, permitindo caracteres em ambos os lados"""
    return fr'^(?i).*{escape(texto)}.*$'


def testar_implementacao(nome_arquivo_base, nome_implementacao, nome_teste, code=0):
    """Testar o arquivo de implementação, uma implementação do arquivo base, contra as verificações do aluno no arquivo de teste. Espera um determinado status de saída"""

    check50.include("pytest_helper.py")
    check50.include(nome_implementacao)

    # Substituir arquivo base com código para executar arquivo de implementação
    with open(nome_arquivo_base, "w") as base_file, open("pytest_helper.py", "r") as pytest_helper:

        # Ler texto de pytest_helper
        text_pytest_helper = pytest_helper.read()

        # Substituir a declaração open com o arquivo de implementação
        text_pytest_helper = sub("with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{nome_implementacao}\", \"rb\") as test_file:", text_pytest_helper)

        # Escrever o texto do arquivo auxiliar no arquivo base
        base_file.writelines(text_pytest_helper)

    # Esperar que o pytest saia com o código de status dado
    return check50.run(f"pytest {nome_teste}").exit(code=code)
```