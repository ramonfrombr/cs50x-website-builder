```python
import check50
import check50.c
import re

@check50.check()
def existe():
    """runoff.c existe"""
    check50.existe("runoff.c")
    check50.incluir("testing.c")

@check50.check(existe)
def compila():
    """runoff compila"""
    check50.c.compilar("runoff.c", lcs50=True)
    runoff = re.sub("int\s+main", "int distro_main", open("runoff.c").read())
    testing = open("testing.c").read()
    with open("runoff_test.c", "w") as f:
        f.write(runoff)
        f.write("\n")
        f.write(testing)
    check50.c.compilar("runoff_test.c", lcs50=True)

@check50.check(compila)
@check50.oculto("a função vote não retornou true")
def voto_retorna_true():
    """vote retorna true quando é dado o nome de um candidato"""
    check50.run("./runoff_test 0 0").stdout("true").exit(0)

@check50.check(compila)
@check50.oculto("a função vote não retornou false")
def voto_retorna_false():
    """vote retorna false quando é dado o nome de um candidato inválido"""
    check50.run("./runoff_test 0 1").stdout("false").exit(0)

@check50.check(compila)
@check50.oculto("a função vote não configurou corretamente as preferências")
def voto_configura_preferencia1():
    """vote configura corretamente a primeira preferência para o primeiro eleitor"""
    check50.run("./runoff_test 0 2").stdout("2").exit(0)

@check50.check(compila)
@check50.oculto("a função vote não configurou corretamente as preferências")
def voto_configura_preferencia2():
    """vote configura corretamente a terceira preferência para o segundo eleitor"""
    check50.run("./runoff_test 0 3").stdout("0").exit(0)

@check50.check(compila)
@check50.oculto("a função vote não configurou corretamente as preferências")
def voto_configura_todas_preferencias():
    """vote configura corretamente todas as preferências para o eleitor"""
    check50.run("./runoff_test 0 4").stdout("1 0 2").exit(0)

@check50.check(compila)
@check50.oculto("a função tabular não produziu totais de votos corretos")
def tabular1():
    """tabular conta votos quando todos os candidatos permanecem na eleição"""
    check50.run("./runoff_test 1 5").stdout("3 3 1 0 ").exit(0)

@check50.check(compila)
@check50.oculto("a função tabular não produziu totais de votos corretos")
def tabular2():
    """tabular conta votos quando um candidato é eliminado"""
    check50.run("./runoff_test 1 6").stdout("3 3 1 0 ").exit(0)

@check50.check(compila)
@check50.oculto("a função tabular não produziu totais de votos corretos")
def tabular3():
    """tabular conta votos quando vários candidatos são eliminados"""
    check50.run("./runoff_test 1 7").stdout("3 4 0 0 ").exit(0)

@check50.check(compila)
@check50.oculto("a função tabular não produziu totais de votos corretos")
def tabular4():
    """tabular lida com várias rodadas de preferências"""
    check50.run("./runoff_test 1 22").stdout("3 4 0 0 ").exit(0)

@check50.check(compila)
@check50.oculto("a função print_winner não imprimiu o vencedor da eleição")
def imprimir_vencedor1():
    """print_winner imprime o nome quando alguém tem a maioria"""
    check50.run("./runoff_test 2 8").stdout("Bob\n").exit(0)

@check50.check(compila)
@check50.oculto("a função print_winner não imprimiu o vencedor e depois retornou true")
def imprimir_vencedor2():
    """print_winner retorna verdadeiro quando alguém tem a maioria"""
    check50.run("./runoff_test 2 9").stdout("Bob\ntrue").exit(0)

@check50.check(compila)
@check50.oculto("a função print_winner não retornou false")
def imprimir_vencedor3():
    """print_winner retorna false quando ninguém tem a maioria"""
    check50.run("./runoff_test 2 10").stdout("false").exit(0)

@check50.check(compila)
@check50.oculto("a função print_winner não retornou false")
def imprimir_vencedor4():
    """print_winner retorna false quando o líder tem exatamente 50% dos votos"""
    check50.run("./runoff_test 2 11").stdout("false").exit(0)

@check50.check(compila)
@check50.oculto("a função find_min não identificou o mínimo correto")
def encontrar_minimo1():
    """find_min retorna o número mínimo de votos para um candidato"""
    check50.run("./runoff_test 2 12").stdout("1").exit(0)

@check50.check(compila)
@check50.oculto("a função find_min não identificou o mínimo correto")
def encontrar_minimo2():
    """find_min retorna o mínimo quando todos os candidatos estão empatados"""
    check50.run("./runoff_test 2 13").stdout("7").exit(0)

@check50.check(compila)
@check50.oculto("a função find_min não identificou o mínimo correto")
def encontrar_minimo3():
    """find_min ignora candidatos eliminados"""
    check50.run("./runoff_test 2 14").stdout("5").exit(0)

@check50.check(compila)
@check50.oculto("a função is_tie não retornou true")
def empate1():
    """is_tie retorna true quando a eleição está empatada"""
    check50.run("./runoff_test 2 15").stdout("true").exit(0)

@check50.check(compila)
@check50.oculto("a função is_tie não retornou false")
def empate2():
    """is_tie retorna false quando a eleição não está empatada"""
    check50.run("./runoff_test 2 16").stdout("false").exit(0)

@check50.check(compila)
@check50.oculto("a função is_tie não retornou false")
def empate3():
    """is_tie retorna false quando apenas alguns dos candidatos estão empatados"""
    check50.run("./runoff_test 2 17").stdout("false").exit(0)

@check50.check(compila)
@check50.oculto("a função is_tie não retornou true")
def empate4():
    """is_tie detecta empate depois que alguns candidatos foram eliminados"""
    check50.run("./runoff_test 2 18").stdout("true").exit(0)

@check50.check(compila)
@check50.oculto("a função eliminar não eliminou os candidatos corretos")
def eliminar1():
    """Eliminar elimina o candidato em último lugar"""
    check50.run("./runoff_test 2 19").stdout("false false false true ").exit(0)

@check50.check(compila)
@check50.oculto("a função eliminar não eliminou os candidatos corretos")
def eliminar2():
    """Eliminar elimina vários candidatos empatados em último lugar"""
    check50.run("./runoff_test 2 20").stdout("true false true false ").exit(0)

@check50.check(compila)
@check50.oculto("a função eliminar não eliminou os candidatos corretos")
def eliminar3():
    """Eliminar elimina candidatos após alguns já terem sido eliminados"""
    check50.run("./runoff_test 2 21").stdout("true false true false ").exit(0)
```