```python
from cs50 import SQL

import check50
import sqlparse

@check50.check()
def existe():
    """Arquivos SQL existem"""
    for i in range(1, 14):
        check50.exists(f"{i}.sql")
    check50.include("movies.db")

@check50.check(existe)
def teste1():
    """1.sql produz o resultado correto"""
    check_single_col(run_query("1.sql"),
        {"Homem de Ferro", "O Cavaleiro das Trevas", "Quem Quer Ser um Milionário", "Kung Fu Panda"},
        ordenado=False)

@check50.check(existe)
def teste2():
    """2.sql produz o resultado correto"""
    check_single_cell(run_query("2.sql"), "1988")

@check50.check(existe)
def teste3():
    """3.sql produz o resultado correto"""
    check_single_col(run_query("3.sql"),
        ["Vingadores: Guerra Infinita", "Pantera Negra", "Oitava Série", "Projeto Gemini",
         "Tempos Felizes", "Os Incríveis 2", "Kirklet", "Roma", "O Professor",
         "Toy Story 4"],
        ordenado=True)

@check50.check(existe)
def teste4():
    """4.sql produz o resultado correto"""
    check_single_cell(run_query("4.sql"), "2")

@check50.check(existe)
def teste5():
    """5.sql produz o resultado correto"""
    check_double_col(run_query("5.sql"),
        [{"Harry Potter e a Pedra Filosofal", "2001"},
         {"Harry Potter e a Câmara Secreta", "2002"},
         {"Harry Potter e o Prisioneiro de Azkaban", "2004"},
         {"Harry Potter e o Cálice de Fogo", "2005"},
         {"Harry Potter e a Ordem da Fênix", "2007"},
         {"Harry Potter e o Enigma do Príncipe", "2009"},
         {"Harry Potter e as Relíquias da Morte: Parte 1", "2010"},
         {"Harry Potter e as Relíquias da Morte: Parte 2", "2011"},
         {"Harry Potter: Uma História de Magia", "2017"}],
        ordenado=True)

@check50.check(existe)
def teste6():
    """6.sql produz o resultado correto"""
    check_single_cell(run_query("6.sql"), "7.74")

@check50.check(existe)
def teste7():
    """7.sql produz o resultado correto"""
    check_double_col(run_query("7.sql"),
        [{"A Origem", "8.8"},
         {"Toy Story 3", "8.3"},
         {"Como Treinar o Seu Dragão", "8.1"},
         {"Ilha do Medo", "8.1"},
         {"O Discurso do Rei", "8.0"},
         {"Harry Potter e as Relíquias da Morte: Parte 1", "7.7"},
         {"Homem de Ferro 2", "7.0"},
         {"Alice no País das Maravilhas", "6.4"}],
        ordenado=True)

@check50.check(existe)
def teste8():
    """8.sql produz o resultado correto"""
    check_single_col(run_query("8.sql"),
        {"Don Rickles", "Jim Varney", "Tom Hanks", "Tim Allen"},
        ordenado=False)

@check50.check(existe)
def teste9():
    """9.sql produz o resultado correto"""
    check_single_col(run_query("9.sql"),
        ["Craig T. Nelson", "Richard Griffifths", "Samuel L. Jackson", "Holly Hunter",
         "Jason Lee", "Rupert Grint", "Daniel Radcliffe", "Emma Watson"],
        ordenado=True)

@check50.check(existe)
def teste10():
    """10.sql produz o resultado correto"""
    check_single_col(run_query("10.sql"),
        {"Christopher Nolan", "Frank Darabont", "Yimou Zhang"},
        ordenado=False)

@check50.check(existe)
def teste11():
    """11.sql produz o resultado correto"""
    check_single_col(run_query("11.sql"),
        ["42", "Pantera Negra", "Marshall", "Get on Up", "Draft Day"],
        ordenado=True)

@check50.check(existe)
def teste12():
    """12.sql produz o resultado correto"""
    check_single_col(run_query("12.sql"),
        {"Noiva Cadáver", "A Fantástica Fábrica de Chocolate",
         "Alice no País das Maravilhas", "Alice Através do Espelho"},
        ordenado=False)

@check50.check(existe)
def teste13():
    """13.sql produz o resultado correto"""
    check_single_col(run_query("13.sql"),
        {"Bill Paxton", "Gary Sinise", "James McAvoy", "Jennifer Lawrence",
         "Tom Cruise", "Michael Fassbender", "Tom Hanks"},
        ordenado=False)

def run_query(nome_arquivo):
    try:
        with open(nome_arquivo) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///movies.db")
        resultado = db.execute(query)
        return resultado
    except Exception as e:
        raise check50.Failure(f"Erro ao executar a consulta: {str(e)}")

def check_single_col(atual, esperado, ordenado=False):
    """
    Verifica consultas que retornam apenas uma coluna, garantindo os resultados corretos.
    """
    
    # Verifica se a consulta retornou resultados
    if atual is None or atual == []:
        raise check50.Failure("A consulta não retornou resultados")
    
    # Verifica se há apenas uma coluna
    contagens_linha = {len(list(row.values())) for row in atual}
    if contagens_linha != {1}:
        raise check50.Failure("A consulta deve retornar apenas uma coluna")
    
    # Obter dados da coluna
    try:
        resultado = [str(list(row.values())[0]) for row in atual]
        resultado = resultado if ordenado else set(resultado)
    except IndexError:
        return None
    
    # Verificar os dados da coluna em relação aos valores esperados
    esperado = [str(valor) for valor in esperado]
    if not ordenado:
        esperado = set(esperado)
    if resultado != esperado:
        raise check50.Mismatch("\n".join(esperado), "\n".join(list(resultado)))

def check_single_cell(atual, esperado):
    return check_single_col(atual, [esperado], ordenado=True)

def check_double_col(atual, esperado, ordenado=False):
    """
    Verifica consultas que retornam apenas uma coluna, garantindo os resultados corretos.
    """

    # Verifica se a consulta retornou resultados
    if atual is None or atual == []:
        raise check50.Failure("A consulta não retornou resultados")

    # Verifica se há apenas duas colunas
    contagens_linha = {len(list(row.values())) for row in atual}
    if contagens_linha != {2}:
        raise check50.Failure("A consulta deve retornar exatamente duas colunas")

    # Obter dados da coluna
    try:
        resultado = []
        for row in atual:
            valores = list(row.values())
            resultado.append({str(valores[0]), str(valores[1])})
        resultado = resultado if ordenado else set(resultado)
    except IndexError:
        return None

    # Verificar os dados da coluna em relação aos valores esperados
    if resultado != esperado:
        raise check50.Mismatch("\n".join([str(entrada) for entrada in list(esperado)]),
                              "\n".join([str(entrada) for entrada in list(resultado)]))
```