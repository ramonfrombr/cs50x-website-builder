import check50
import check50.c
import re


@check50.check()
def existe():
    """half.c existe"""
    check50.exists("half.c")


@check50.check(existe)
def compile():
    """half.c compile"""
    check50.c.compile("half.c", lcs50=True)


@check50.check(compile)
def simple():
    """Facture de 50 $, avec une taxe de 10% et un pourboire de 20%, crée une sortie de 33.00 $"""
    verifier_demi(facture="50", taxe="10", pourboire="20", attendu="33.00")


@check50.check(compile)
def decimale_taxe():
    """Facture de 50 $, avec une taxe de 12.5% et un pourboire de 20%, crée une sortie de 33.75 $"""
    verifier_demi(facture="50", taxe="12.5", pourboire="20", attendu="33.75")


@check50.check(compile)
def arrondi_sup():
    """Facture de 100 $, avec une taxe de 12.5% et un pourboire de 15%, crée une sortie de 64.69 $"""
    verifier_demi(facture="100", taxe="12.5", pourboire="15", attendu="64.69")


@check50.check(compile)
def arrondi_inf():
    """Facture de 96.40 $, avec une taxe de 13% et un pourboire de 14%, crée une sortie de 62.09 $"""
    verifier_demi(facture="96.40", taxe="13", pourboire="14", attendu="62.09")


# Assistants
def regex(entree):
    """Correspondant avec tout caractère non numérique à n'importe quel bout de l'entrée"""
    return rf'^\D*\${re.escape(entree)}\D*$'


def verifier_demi(facture: str, taxe: str, pourboire: str, attendu: str):
    check50.run("./half").stdin(facture).stdin(taxe).stdin(pourboire).stdout(regex(attendu), attendu, regex=True)