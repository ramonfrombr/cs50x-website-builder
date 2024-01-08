import check50
import check50.c
import re

@check50.check()
def existe():
    """Le fichier inheritance.c existe"""
    check50.exists("inheritance.c")
    check50.include("testing.c")

@check50.check(existe)
def compile():
    """Le fichier inheritance.c compile"""
    check50.c.compile("inheritance.c", lcs50=True)

@check50.check(existe)
def compile():
    """Le fichier inheritance compile"""
    check50.c.compile("inheritance.c", lcs50=True)
    inheritance = re.sub("int\s+main", "int distro_main", open("inheritance.c").read())
    testing = open("testing.c").read()
    with open("inheritance_test.c", "w") as f:
        f.write(inheritance)
        f.write("\n")
        f.write(testing)
    check50.c.compile("inheritance_test.c", lcs50=True)

@check50.check(compile)
def taille_correcte():
    """La fonction create_family crée la bonne taille de famille"""
    check50.run("./inheritance_test").stdout("size_true.*").exit(0)


@check50.check(compile)
def regles_heritage_1():
    """La fonction create_family suit la première règle d'héritage"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compile)
def regles_heritage_2():
    """La fonction create_family suit la deuxième règle d'héritage"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compile)
def regles_heritage_3():
    """La fonction create_family suit la troisième règle d'héritage"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compile)
def libere_memoire():
    """La fonction free_family ne provoque pas de fuites de mémoire"""
    check50.c.valgrind("./inheritance").exit(0)