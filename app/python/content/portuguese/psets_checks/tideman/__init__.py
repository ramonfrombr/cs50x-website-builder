```python
import check50
import check50.c
import re

@check50.check()
def existe():
    """tideman.c existe"""
    check50.exists("tideman.c")
    check50.include("testing.c")

@check50.check(existe)
def compila():
    """tideman compila"""
    check50.c.compile("tideman.c", lcs50=True)
    tideman = re.sub("int\s+main", "int distro_main", open("tideman.c").read())
    testing = open("testing.c").read()
    with open("tideman_test.c", "w") as f:
        f.write(tideman)
        f.write("\n")
        f.write(testing)
    check50.c.compile("tideman_test.c", lcs50=True)

@check50.check(compila)
@check50.hidden("função vote não retornou verdadeiro")
def voto_retorna_true():
    """vote retorna verdadeiro ao receber o nome de um candidato"""
    check50.run("./tideman_test 0 0").stdout("true").exit(0)

@check50.check(compila)
@check50.hidden("função vote não retornou falso")
def voto_retorna_false():
    """vote retorna falso ao receber o nome de um candidato inválido"""
    check50.run("./tideman_test 0 1").stdout("false").exit(0)

@check50.check(compila)
@check50.hidden("função vote não configurou corretamente os rankings")
def voto_configura_rank():
    """vote configura corretamente o ranking para a primeira preferência"""
    check50.run("./tideman_test 0 2").stdout("1").exit(0)

@check50.check(compila)
@check50.hidden("função vote não configurou corretamente os rankings")
def voto_configura_todos_ranks():
    """vote configura corretamente o ranking para todas as preferências"""
    check50.run("./tideman_test 0 2").stdout("1 2 0").exit(0)

@check50.check(compila)
@check50.hidden("função record_preferences não configurou corretamente as preferências")
def registra_preferencias_primeiro():
    """record_preferences configura corretamente as preferências para o primeiro eleitor"""
    check50.run("./tideman_test 0 3").stdout("0 0 0 1 0 1 1 0 0 ").exit(0)

@check50.check(compila)
@check50.hidden("função record_preferences não configurou corretamente as preferências")
def registra_preferencias_todos():
    """record_preferences configura corretamente as preferências para todos os eleitores"""
    check50.run("./tideman_test 0 4").stdout("0 2 2 4 0 5 3 5 0").exit(0)

@check50.check(compila)
@check50.hidden("função add_pairs não gerou 3 pares corretos")
def adiciona_pares1():
    """add_pairs gera a contagem correta de pares quando não há empates"""
    check50.run("./tideman_test 1 5").stdout("3").exit(0)

@check50.check(compila)
@check50.hidden("função add_pairs não gerou 2 pares corretos")
def adiciona_pares2():
    """add_pairs gera a contagem correta de pares quando há empates"""
    check50.run("./tideman_test 2 5").stdout("2").exit(0)

@check50.check(compila)
@check50.hidden("função add_pairs não gerou os pares corretos")
def adiciona_pares3():
    """add_pairs preenche o array de pares vencedores corretamente"""
    check50.run("./tideman_test 1 6").stdout("true true true ").exit(0)

@check50.check(compila)
@check50.hidden("função add_pairs não gerou os pares corretos")
def adiciona_pares4():
    """add_pairs não preenche o array de pares perdedores"""
    check50.run("./tideman_test 1 7").stdout("0").exit(0)

@check50.check(compila)
@check50.hidden("função sort_pairs não ordenou corretamente os pares")
def ordena_pares1():
    """sort_pairs ordena pares de candidatos pela margem de vitória"""
    check50.run("./tideman_test 3 8").stdout("0 2 0 1 2 1 ").exit(0)

@check50.check(compila)
@check50.hidden("função lock_pairs não travou todos os pares")
def trava_pares1():
    """lock_pairs trava todos os pares quando não há ciclos"""
    check50.run("./tideman_test 5 16").stdout("false false false true false true false false false false false false false false false false false false false true false false true false false ").exit(0)

@check50.check(compila)
@check50.hidden("função lock_pairs não travou corretamente todos os pares não cíclicos")
def trava_pares2():
    """lock_pairs pula o par final se isso cria um ciclo"""
    check50.run("./tideman_test 6 14").stdout("false true false false false false false false false false true false false false false false false false false false false false false true false false true true false false false false false false false false ").exit(0)

@check50.check(compila)
@check50.hidden("função lock_pairs não travou corretamente todos os pares não cíclicos")
def trava_pares3():
    """lock_pairs pula o par do meio se isso cria um ciclo"""
    check50.run("./tideman_test 5 15").stdout("false false false false false false false false true false true false false false false false false false false false false true true false false ").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não imprimiu o vencedor da eleição")
def imprime_vencedor1():
    """print_winner imprime o vencedor da eleição quando um candidato vence sobre todos os outros"""
    check50.run("./tideman_test 4 12").stdout("^Alice\n?$").exit(0)

@check50.check(compila)
@check50.hidden("função print_winner não imprimiu o vencedor da eleição")
def imprime_vencedor2():
    """print_winner imprime o vencedor da eleição quando alguns pares estão empatados"""
    check50.run("./tideman_test 4 13").stdout("^Charlie\n?$").exit(0)
```