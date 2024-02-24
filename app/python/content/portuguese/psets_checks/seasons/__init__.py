```python
import check50
from re import escape, search, sub


@check50.check()
def existe():
    """seasons.py e test_seasons.py existem"""
    check50.exists("seasons.py")
    check50.exists("test_seasons.py")
    check50.include("testing.py")


@check50.check(existe)
def test_um_ano():
    """Entrada de \"1999-01-01\" resulta em "Quinhentos e vinte e cinco mil, seiscentos minutos" quando hoje é 2000-01-01"""
    test_datas_validas(data="1999-01-01", hoje="2000-01-01", saida="Quinhentos e vinte e cinco mil, seiscentos minutos")


@check50.check(existe)
def test_dois_anos():
    """Entrada de \"2001-01-01\" resulta em "Um milhão, cinquenta e um mil, duzentos minutos" quando hoje é 2003-01-01"""
    test_datas_validas(data="2001-01-01", hoje="2003-01-01", saida="Um milhão, cinquenta e um mil, duzentos minutos")


@check50.check(existe)
def test_ano_bissexto():
    """Entrada de \"1995-01-01\" resulta em "Dois milhões, seiscentos vinte e nove mil, quatrocentos e quarenta minutos" quando hoje é 2000-01-1"""
    test_datas_validas(data="1995-01-01", hoje="2000-01-01", saida="Dois milhões, seiscentos vinte e nove mil, quatrocentos e quarenta minutos")


@check50.check(existe)
def test_meses():
    """Entrada de \"2020-06-01\" resulta em "Seis milhões, noventa e dois mil, seiscentos e quarenta minutos" quando hoje é 2032-01-01"""
    test_datas_validas(data="2020-06-01", hoje="2032-01-01", saida="Seis milhões, noventa e dois mil, seiscentos e quarenta minutos")


@check50.check(existe)
def test_dia():
    """Entrada de \"1998-06-20\" resulta em "Oitocentos e seis mil, quatrocentos minutos" quando hoje é 2000-01-01"""
    test_datas_validas(data="1998-06-20", hoje="2000-01-01", saida="Oitocentos e seis mil, quatrocentos minutos")


@check50.check(existe)
def test_entrada_invalida():
    """Entrada de \"6 de fevereiro de 1998\" leva o programa a sair com sys.exit"""
    test_datas_invalidas(data="6 de fevereiro de 1998")


"""
test_seasons verifica
"""


@check50.check(existe)
def teste_arquivo_aluno_passa():
    """seasons.py passa em todos os testes em test_seasons.py"""
    check50.run("pytest test_seasons.py").exit(0)


"""
Auxiliares
"""


def regex(texto):
    """corresponde com distinção entre maiúsculas e minúsculas, permitindo apenas espaço em branco de cada lado"""
    return fr'^\s*{escape(texto)}\s*$'


def definir_hoje(data):

    # Analisar data
    ano, mes, dia = data.split(sep="-", maxsplit=2)
    mes = mes.lstrip("0")
    dia = dia.lstrip("0")

    # Substituir objeto de data de teste pela nova data de teste
    with open("testing.py", "r") as arquivo_teste:
        novo_conteudo_teste = sub(r"return date\(\d{4}, *\d{1,2}, *\d{1,2}\)", fr"return date({ano}, {mes}, {dia})", arquivo_teste.read())

    # Escrever o novo objeto de data de teste no arquivo de teste
    with open("testing.py", "w") as arquivo_teste:
        arquivo_teste.write(novo_conteudo_teste)


def test_datas_validas(data, hoje, saida):
    definir_hoje(hoje)
    check50.run("python3 testing.py").stdin(data, prompt=True).stdout(regex(saida), saida, regex=True).exit(0)


def test_datas_invalidas(data):
    codigo = check50.run("python3 testing.py").stdin(data, prompt=True).exit()
    if codigo == 0:
        raise check50.Failure("Era esperado um código de saída não nulo.")
    saida = check50.run("python3 testing.py").stdin(data, prompt=True).stdout()
    if search(r'(Traceback)', saida):
        raise check50.Failure("O programa saiu com um traceback")
```