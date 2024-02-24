```python
import check50
from pexpect import EOF
from re import escape


@check50.verifique()
def existe():
    """adieu.py existe"""
    check50.existe("adieu.py")


@check50.verifique(existe)
def teste_EOF():
    """entrada EOF interrompe o programa"""
    entrada = "Liesl"

    # Executar o programa
    programa = check50.executar("python3 adieu.py")
    
    # Enviar nome e EOF
    programa.stdin(entrada, prompt=False).stdin(EOF, prompt=False)
    
    # O programa fecha corretamente
    programa.exit(0)


@check50.verifique(teste_EOF)
def teste_nome_simples():
    """entrada \"Liesl\" resulta em \"Adieu, adieu, para Liesl\""""
    entrada = "Liesl"
    saida = "Adieu, adieu, para Liesl"
    
    # Executar o programa
    programa = check50.executar("python3 adieu.py")
    
    # Enviar nome e EOF
    programa.stdin(entrada, prompt=False).stdin(EOF, prompt=False)

    # Verificar a saída esperada
    programa.stdout(regex(saida), saida, regex=True)

    # O programa fecha corretamente
    programa.exit(0)


@check50.verifique(teste_EOF)
def teste_dois_nomes():
    """entrada \"Liesl\" e \"Friedrich\" resulta em \"Adieu, adieu, para Liesl e Friedrich\""""
    entrada = ["Liesl", "Friedrich"]
    saida = "Adieu, adieu, para Liesl e Friedrich"
    teste_varios_nomes(entrada, saida)


@check50.verifique(teste_EOF)
def teste_tres_nomes():
    """entrada \"Liesl\", \"Friedrich\", e \"Louisa\" resulta em \"Adieu, adieu, para Liesl, Friedrich, e Louisa\""""
    entrada = ["Liesl", "Friedrich", "Louisa"]
    saida = "Adieu, adieu, para Liesl, Friedrich, e Louisa"
    teste_varios_nomes(entrada, saida)


@check50.verifique(teste_EOF)
def teste_quatro_nomes():
    """entrada \"Liesl\", \"Friedrich\", \"Louisa\", e \"Kurt\" resulta em \"Adieu, adieu, para Liesl, Friedrich, Louisa, e Kurt\""""
    entrada = ["Liesl", "Friedrich", "Louisa", "Kurt"]
    saida = "Adieu, adieu, para Liesl, Friedrich, Louisa, e Kurt"
    teste_varios_nomes(entrada, saida)


@check50.verifique(teste_EOF)
def teste_cinco_nomes():
    """entrada \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", e \"Brigitta\" resulta em \"Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, e Brigitta\""""
    entrada = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta"]
    saida = "Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, e Brigitta"
    teste_varios_nomes(entrada, saida)


@check50.verifique(teste_EOF)
def teste_seis_nomes():
    """entrada \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", \"Brigitta\", e \"Marta\" resulta em \"Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, Brigitta, e Marta\""""
    entrada = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta"]
    saida = "Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, Brigitta, e Marta"
    teste_varios_nomes(entrada, saida)


@check50.verifique(teste_EOF)
def teste_sete_nomes():
    """entrada \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", \"Brigitta\", \"Marta\", e \"Gretl\" resulta em \"Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, e Gretl\""""
    entrada = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl"]
    saida = "Adieu, adieu, para Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, e Gretl"
    teste_varios_nomes(entrada, saida)


def regex(texto):
    """corresponde de forma sensível a maiúsculas e minúsculas com quaisquer caracteres que precedem e apenas 1 ponto e espaço em branco depois"""
    return fr'^.*{escape(texto)}\.?\s*$'


def teste_varios_nomes(entrada, saida):
    """testa se os nomes na lista criam a saída esperada"""

    # Executar o programa e fornecer os nomes de entrada via stdin
    programa = check50.executar("python3 adieu.py")
    for nome in entrada:
        programa.stdin(nome, prompt=False)

    # EOF interrompe o programa, a saída é a esperada
    programa.stdin(EOF, prompt=False)
    programa.stdout(regex(saida), saida, regex=True)

    # O programa fecha corretamente
    programa.exit(0)
```