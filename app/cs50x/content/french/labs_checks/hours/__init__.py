import check50
import check50.c


@check50.check()
def existe():
    """hours.c existe"""
    check50.exists("hours.c")


@check50.check(existe)
def compile():
    """hours.c compile"""
    check50.c.compile("hours.c", lcs50=True)


@check50.check(compile)
def somme_3_semaines():
    """hours additionne les heures sur 3 semaines."""
    verifier_heures(type="T", données=[8, 8, 10], attendu="26")


@check50.check(compile)
def somme_5_semaines():
    """hours additionne les heures sur 5 semaines."""
    verifier_heures(type="T", données=[5, 5, 6, 7, 8], attendu="31")


@check50.check(compile)
def moyenne_3_semaines():
    """hours calcule la moyenne des heures sur 3 semaines."""
    verifier_heures(type="A", données=[8, 9, 10], attendu="9")


@check50.check(compile)
def moyenne_5_semaines():
    """hours calcule la moyenne des heures sur 4 semaines."""
    verifier_heures(type="A", données=[8, 8, 8, 6], attendu="7.5")


# Helpers
def verifier_heures(type: str, données: list, attendu: str):
    programme = check50.run("./hours").stdin(str(len(données)))
    for heures in données:
        programme.stdin(str(heures))
    programme.stdin(type).stdout(attendu)