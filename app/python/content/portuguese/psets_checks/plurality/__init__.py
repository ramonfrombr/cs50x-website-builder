```python
import check50
import check50.c
import re

@check50.check()
def existe():
    """plurality.c existe"""
    check50.existe("plurality.c")
    check50.inclui("testing.c")

@check50.check(existe)
def compila():
    """compilação de plurality"""
    check50.c.compila("plurality.c", lcs50=True)
    plurality = re.sub("int\s+main", "int distro_main", open("plurality.c").read())
    testing = open("testing.c").read()
    with open("plurality_test.c", "w") as f:
        f.write(plurality)
        f.write("\n")
        f.write(testing)
    check50.c.compila("plurality_test.c", lcs50=True)

@check50.check(compila)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_primeiro_nome():
    """voto retorna verdadeiro quando é dado o nome do primeiro candidato"""
    check50.run("./plurality_test 0 0").stdout("verdadeiro").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_nome_meio():
    """voto retorna verdadeiro quando é dado o nome do candidato do meio"""
    check50.run("./plurality_test 0 1").stdout("verdadeiro").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto não retornou verdadeiro")
def voto_encontra_ultimo_nome():
    """voto retorna verdadeiro quando é dado o nome do último candidato"""
    check50.run("./plurality_test 0 2").stdout("verdadeiro").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto não retornou falso")
def voto_retorna_falso():
    """voto retorna falso quando é dado o nome de um candidato inválido"""
    check50.run("./plurality_test 0 3").stdout("falso").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto não atualizou corretamente os totais de voto")
def primeiro_totais_votos_corretos():
    """voto produz contagens corretas quando todos os votos são zero"""
    check50.run("./plurality_test 0 4").stdout("1 0 0").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto não atualizou corretamente os totais de voto")
def totais_votos_subsequentes_corretos():
    """voto produz contagens corretas depois que alguns já votaram"""
    check50.run("./plurality_test 0 5").stdout("2 8 0").exit(0)

@check50.check(compila)
@check50.oculto("a função de voto modificou incorretamente os totais de voto")
def voto_invalido_votos_inalterados():
    """voto deixa os totais de voto inalterados ao votar em um candidato inválido"""
    check50.run("./plurality_test 0 6").stdout("2 8 0").exit(0)

@check50.check(compila)
@check50.oculto("a função de print_winner não imprimiu o vencedor da eleição")
def print_winner0():
    """print_winner identifica Alice como vencedora da eleição"""
    check50.run("./plurality_test 0 7").stdout("^Alice\n?$").exit(0)

@check50.check(compila)
@check50.oculto("a função de print_winner não imprimiu o vencedor da eleição")
def print_winner1():
    """print_winner identifica Bob como vencedor da eleição"""
    check50.run("./plurality_test 0 8").stdout("^Bob\n?$").exit(0)

@check50.check(compila)
@check50.oculto("a função de print_winner não imprimiu o vencedor da eleição")
def print_winner2():
    """print_winner identifica Charlie como vencedor da eleição"""
    check50.run("./plurality_test 0 9").stdout("^Charlie\n?$").exit(0)

@check50.check(compila)
@check50.oculto("a função de print_winner não imprimiu ambos os vencedores da eleição")
def print_winner3():
    """print_winner imprime múltiplos vencedores em caso de empate"""
    result = check50.run("./plurality_test 0 10").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:
        raise check50.Diferente("Alice\nBob\nCharlie\n", result)

@check50.check(compila)
@check50.oculto("a função de print_winner não imprimiu todos os três vencedores da eleição")
def print_winner4():
    """print_winner imprime todos os nomes quando todos os candidatos estão empatados"""
    result = check50.run("./plurality_test 0 11").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        raise check50.Diferente("Alice\nBob\nCharlie\n", result)
```  