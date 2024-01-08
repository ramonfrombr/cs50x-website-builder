import os
import re
import check50
import check50.py

BRACKET2 = [
    {"équipe": "Uruguay", "notation": 976},
    {"équipe": "Portugal", "notation": 1306},
]
BRACKET4 = [
    {"équipe": "Uruguay", "notation": 976},
    {"équipe": "Portugal", "notation": 1306},
    {"équipe": "France", "notation": 1166},
    {"équipe": "Argentine", "notation": 1254},
]
BRACKET8 = [
    {"équipe": "Uruguay", "notation": 976},
    {"équipe": "Portugal", "notation": 1306},
    {"équipe": "France", "notation": 1166},
    {"équipe": "Argentine", "notation": 1254},
    {"équipe": "Brésil", "notation": 1384},
    {"équipe": "Mexique", "notation": 1008},
    {"équipe": "Belgique", "notation": 1346},
    {"équipe": "Japon", "notation": 528},
]
BRACKET16 = [
    {"équipe": "Uruguay", "notation": 976},
    {"équipe": "Portugal", "notation": 1306},
    {"équipe": "France", "notation": 1166},
    {"équipe": "Argentine", "notation": 1254},
    {"équipe": "Brésil", "notation": 1384},
    {"équipe": "Mexique", "notation": 1008},
    {"équipe": "Belgique", "notation": 1346},
    {"équipe": "Japon", "notation": 528},
    {"équipe": "Espagne", "notation": 1162},
    {"équipe": "Russie", "notation": 493},
    {"équipe": "Croatie", "notation": 975},
    {"équipe": "Danemark", "notation": 1054},
    {"équipe": "Suède", "notation": 889},
    {"équipe": "Suisse", "notation": 1179},
    {"équipe": "Colombie", "notation": 989},
    {"équipe": "Angleterre", "notation": 1040},
]
QUESTIONS = [
    "Quelles prédictions, le cas échéant, se sont révélées incorrectes lorsque vous avez augmenté le nombre de simulations?",
    "Supposez que vous soyez facturé pour chaque seconde de temps de calcul utilisée par votre programme.\nAprès combien de simulations considéreriez-vous les prédictions comme 'assez bonnes'?"
]
SIMULATION_RUNS = [
    "10",
    "100",
    "1000",
    "10000",
    "100000",
    "1000000",
]


@check50.check()
def existe():
    """tournoi.py existe"""
    check50.exists("tournoi.py", "reponses.txt")
    check50.include("2018m.csv", "2019w.csv")


@check50.check(existe)
def importations():
    """tournoi.py importe"""
    check50.py.import_("tournoi.py")


@check50.check(importations)
def sim_tournoi_2():
    """simule_tournoi gère un tableau de taille 2"""
    verifier_tournoi(BRACKET2)


@check50.check(importations)
def sim_tournoi_4():
    """simule_tournoi gère un tableau de taille 4"""
    verifier_tournoi(BRACKET4)


@check50.check(importations)
def sim_tournoi_8():
    """simule_tournoi gère un tableau de taille 8"""
    verifier_tournoi(BRACKET8)


@check50.check(importations)
def sim_tournoi_16():
    """simule_tournoi gère un tableau de taille 16"""
    verifier_tournoi(BRACKET16)


@check50.check(importations)
def comptes():
    """tient correctement compte des victoires"""
    actual = check50.run("python3 tournoi.py 2018m.csv").stdout()
    pourcentages = re.findall("[0-9]*\.[0-9]", actual)
    pourcentages = [float(x) for x in pourcentages]
    if sum(pourcentages) < 99 or sum(pourcentages) > 101:
        raise check50.Failure("ne tient pas correctement compte des victoires")


@check50.check(importations)
def equipes_correctes1():
    """rapporte correctement les informations sur les équipes pour la Coupe du Monde Masculine"""
    actual = check50.run("python3 tournoi.py 2018m.csv").stdout()
    expected = ["Belgique", "Brésil", "Portugal", "Espagne"]
    not_expected = ["Allemagne"]
    for equipe in expected:
        if equipe not in actual:
            raise check50.Failure(f"n'a pas trouvé l'équipe {equipe}")
    for equipe in not_expected:
        if equipe in actual:
            raise check50.Failure(f"a trouvé à tort l'équipe {equipe}")


@check50.check(importations)
def equipes_correctes2():
    """rapporte correctement les informations sur les équipes pour la Coupe du Monde Féminine"""
    actual = check50.run("python3 tournoi.py 2019w.csv").stdout()
    expected = ["Allemagne", "États-Unis", "Angleterre"]
    not_expected = ["Belgique"]
    for equipe in expected:
        if equipe not in actual:
            raise check50.Failure(f"n'a pas trouvé l'équipe {equipe}")
    for equipe in not_expected:
        if equipe in actual:
            raise check50.Failure(f"a trouvé à tort l'équipe {equipe}")

    pourcentages = re.findall("[0-9]*\.[0-9]", actual)
    pourcentages = [float(x) for x in pourcentages]
    if sum(pourcentages) < 99 or sum(pourcentages) > 101:
        raise check50.Failure("ne tient pas correctement compte des victoires")


@check50.check(importations)
def verifier_reponses():
    """reponses.txt est complet"""
    with open("reponses.txt") as f:
        contents = f.read()

        # Vérifier les durées
        for runs in SIMULATION_RUNS:
            match = re.search(
                rf"(?i){re.escape(runs)} simulations:\s*(\d+m\d+\.\d\d\ds)(?<!0m0\.000s)",
                contents,
            )
            if not match:
                raise check50.Failure(
                    "reponses.txt n'inclut pas les durées pour chaque nombre de simulations",
                    help="Avez-vous mis toutes vos réponses au format 0m0.000s ?",
                )

        # Vérifier les réponses libres
        num_questions = len(QUESTIONS)
        for i, question in enumerate(QUESTIONS):

            # Recherche de la question, avec au moins 3 mots après
            if i + 1 < num_questions:

                # L'expression régulière comprend la question posée, la réponse et la question suivante
                regex = (
                    rf"(?i){re.escape(question)}"
                    + r":\s*(\S+\s+){3,}"
                    + rf"{re.escape(QUESTIONS[i + 1])}"
                )
            else:

                # La dernière expression régulière comprend la question posée et la réponse
                regex = rf"(?i){re.escape(question)}" + r":\s*(\S+\s+){3,}"

            match = re.search(regex, contents)
            if not match:
                raise check50.Failure(
                    "reponses.txt n'inclut pas les réponses aux questions libres",
                    help="Avez-vous écrit une réponse suffisante à chaque question ?",
                )


# Aide


def verifier_tour(*args):
    tournoi = check50.py.import_("tournoi.py")
    actual = tournoi.simuler_tour(args[0])

    for i in range(len(actual)):
        expected = [args[0][2 * i], args[0][2 * i + 1]]
        if not (actual[i] in expected):
            raise check50.Failure(
                "simuler_tour ne parvient pas à déterminer les gagnants d'un tour"
            )


def verifier_tournoi(*args):
    tournoi = check50.py.import_("tournoi.py")
    actual = tournoi.simuler_tournoi(args[0])
    equipes = [x["équipe"] for x in args[0]]

    if not actual in equipes:
        raise check50.Failure(
            "simuler_tournoi ne renvoie pas le nom d'une équipe gagnante"
        )