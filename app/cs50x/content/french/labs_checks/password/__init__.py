import check50
import check50.c


@check50.check()
def existe():
    """password.c existe"""
    check50.exists("password.c")


@check50.check(existe)
def compile():
    """password.c compile"""
    check50.c.compile("password.c", lcs50=True)


@check50.check(compile)
def valide():
    """Le mot de passe 3PQvbQ6_GvneW!3R est accepté."""
    verifier_mot_de_passe(password="3PQvbQ6_GvneW!3R", valide=True)


@check50.check(compile)
def sans_majuscule():
    """Le mot de passe hqsk3wb. est rejeté pour manque de caractères en majuscule."""
    verifier_mot_de_passe(password="hqsk3wb.", valide=False)


@check50.check(compile)
def sans_minuscule():
    """Le mot de passe F-WH8PQP est rejeté pour manque de caractères en minuscule."""
    verifier_mot_de_passe(password="F-WH8PQP", valide=False)


@check50.check(compile)
def sans_symbole():
    """Le mot de passe VnrHMtV4 est rejeté pour manque de symboles."""
    verifier_mot_de_passe(password="VnrHMtV4", valide=False)


@check50.check(compile)
def sans_chiffre():
    """Le mot de passe iWnktW*q est rejeté pour manque de chiffres."""
    verifier_mot_de_passe(password="iWnktW*q", valide=False)


# Fonctions d'aide
def verifier_mot_de_passe(password: str, valide: bool):
    programme = check50.run("./password").stdin(password)
    if valide:
        programme.stdout("Votre mot de passe est valide !")
    else:
        programme.stdout("Votre mot de passe a besoin d'au moins une lettre en majuscule, une lettre en minuscule, un chiffre et un symbole")