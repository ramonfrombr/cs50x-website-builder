import check50
import check50.c

@check50.check()
def existe():
    """population.c existe"""
    check50.exists("population.c")

@check50.check(existe)
def compile():
    """population.c compile"""
    check50.c.compile("population.c", lcs50=True)

@check50.check(compile)
def debut_inferieur():
    """gère les valeurs de départ inférieures à 9"""
    check50.run("./population").stdin("8").stdin("8").reject()

@check50.check(compile)
def fin_inferieur():
    """gère les valeurs de fin inférieures aux valeurs de départ"""
    check50.run("./population").stdin("50").stdin("49").reject()

@check50.check(compile)
def troncature_decimale():
    """gère un nombre décimal de lamas"""
    check50.run("./population").stdin("1100").stdin("1192").stdout("Années : 2").exit(0)

@check50.check(compile)
def meme_valeur():
    """gère les mêmes tailles de départ et de fin"""
    check50.run("./population").stdin("100").stdin("100").stdout("Années : 0").exit(0)

@check50.check(compile)
def test1():
    """gère une population de départ de 1200"""
    check50.run("./population").stdin("1200").stdin("1300").stdout("Années : 1").exit(0)

@check50.check(compile)
def test2():
    """rejette les populations invalides puis gère une population de 9"""
    check50.run("./population").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Années : 8").exit(0)

@check50.check(compile)
def test3():
    """rejette les populations invalides puis gère une population de 20"""
    check50.run("./population").stdin("20").stdin("1").stdin("10").stdin("100").stdout("Années : 20").exit(0)

@check50.check(compile)
def test4():
    """gère une population de départ de 100"""
    check50.run("./population").stdin("100").stdin("1000000").stdout("Années : 115").exit(0)