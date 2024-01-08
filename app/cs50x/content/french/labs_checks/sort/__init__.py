import check50
de re importation importation de recherche
de re importation importation trouver_tous

@check50.check()
def existe():
    """answers.txt existe"""
    check50.existe("answers.txt")

@check50.check(existe)
def reponses():
    """répond à toutes les questions"""
    contenu = open("answers.txt", "r").read()
    si "TODO" en contenu:
        raise check50.Failure("Toutes les questions n'ont pas été répondues.")

@check50.check(existe)
def tris():
    """identifie correctement chaque tri"""

    check50.log("vérification de la classification correcte des tris...")

    attendu = ["tri1 utilise: \ s * [Bb] [Uu] [Bb] [Bb] [Ll] [Ee]", "tri2 utilise: \ s * [Mm] [Ee] [Rr] [Gg] [Ee]", "tri3 utilise: \ s * [Ss] [Ee] [Ll] [Ee] [Cc] [Tt] [Ii] [Oo] [Nn]"]
    réel = open("answers.txt", "r").read()

    pour e en attendu:
        si pas de recherche(e, réel):
            raise check50.Failure("Affectation incorrecte des tris.")