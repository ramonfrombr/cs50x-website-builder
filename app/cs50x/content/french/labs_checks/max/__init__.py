import check50
import check50.c


@check50.check()
def existe():
    """max.c existe"""
    check50.exists("max.c")


@check50.check(existe)
def compile():
    """max.c compile"""
    check50.c.compile("max.c", lcs50=True)


@check50.check(compile)
def simple():
    """Retourne 3 à partir de 0, 1, 3"""
    check_max(elements=[0, 1, 3])


@check50.check(compile)
def negatif():
    """Retourne 4 à partir de -10, 4, 2"""
    check_max(elements=[-10, 4, 2])


@check50.check(compile)
def negatif_max():
    """Retourne -10 à partir de -10, -50, -100"""
    check_max(elements=[-10, -50, -100])


# Aides
def check_max(elements: list):
    programme = check50.run("./max")
    programme.stdin(str(len(elements)))
    for nombre in elements:
        print(programme.stdin(str(nombre)))
    programme.stdout(str(max(elements)))