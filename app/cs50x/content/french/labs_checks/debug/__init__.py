import check50
import check50.c


@check50.check()
def existe():
    """debug.c existe"""
    check50.exists("debug.c")


@check50.check(existe)
def compile():
    """debug.c compile"""
    check50.c.compile("debug.c", lcs50=True)


@check50.check(compile)
def harry():
    """L'entrée de \"Harry\" et \"Godrick's Hollow\" produit la sortie \"Bonjour, Harry, de Godrick's Hollow!\""""
    verifier_debug(nom="Harry", lieu="Godrick's Hollow")


@check50.check(compile)
def dumbledore():
    """L'entrée de \"Dumbledore\" et \"Mould-on-the-Wold\" produit la sortie \"Bonjour, Dumbledore, de Mould-on-the-Wold!\""""
    verifier_debug(nom="Dumbledore", lieu="Mould-on-the-Wold")


# Aides
def verifier_debug(nom: str, lieu: str):
    check50.run("./debug").stdin(nom).stdin(lieu).stdout(f"Bonjour, {nom}, de {lieu}!")