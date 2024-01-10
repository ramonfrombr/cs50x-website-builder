Le code Python de sciences informatiques suivant traduit de l'anglais au français:

de cs50 importer SQL

import check50
import sqlparse


@check50.check()
def sql_existe():
    """Fichiers SQL existants"""
    pour i dans la plage(1, 8):
        check50.exists(f"{i}.sql")
    check50.include("songs.db")


@check50.check()
def reponses_existent():
    """answers.txt existe"""
    check50.exists("answers.txt")


@check50.check(sql_existe)
def test1():
    """1.sql donne le bon résultat"""
    solution = {
        "Dieu le Plan",
        "TRISTE!",
        "rockstar (feat. 21 Savage)",
        "Psycho (feat. Ty Dolla $ ign)",
        "Dans mes sentiments",
        "Mieux maintenant",
        "J'aime ça",
        "Un baiser (avec Dua Lipa)",
        "IDGAF",
        "AMIS",
        "Havane",
        "Rêves lucides",
        "Mieux vaut maintenant",
        "Les filles t'aiment (feat. Cardi B)",
        "Le milieu",
        "Toutes les étoiles (avec SZA)",
        "pas de larmes de gauche à pleurer",
        "X",
        "Lumière de lune",
        "Regardez vivant (feat. Drake)",
        "Ces jours-ci (feat. Jess Glynne, Macklemore & Dan Caplen)",
        "Te Bote - Remix",
        "Mienne",
        "Youngblood",
        "Nouvelles règles",
        "Forme de toi",
        "Love Lies (avec Normani)",
        "Destiné à être (feat. Florida Georgia Line)",
        "Jocelyn Flores",
        "Parfait",
        "Goût (feat. Offset)",
        "Solo (feat. Demi Lovato)",
        "Je tombe en morceaux",
        "Peu importe",
        "Echame La Culpa",
        "Eastside (avec Halsey & Khalid)",
        "Ne sois jamais le même",
        "Louve",
        "changements",
        "Dans mes pensées",
        "Rivière (feat. Ed Sheeran)",
        "Dura",
        "SICKO MODE",
        "Tonnerre",
        "Me Niego",
        "Jackie Chan",
        "Raffinement (Remix) [feat. Cardi B]",
        "Retour à toi - De 13 raisons pourquoi",
        "Je te laisserai tomber",
        "Appelle mon nom",
        "Ric Flair Drip (& Metro Boomin)",
        "Plus heureux",
        "Trop bon aux adieux",
        "Freaky Friday (feat. Chris Brown)",
        "Croyant",
        "FEFE (feat. Nicki Minaj & Murda Beatz)",
        "Ascension",
        "Corps (feat. brando)",
        "XO TOUR Llif3",
        "Sin Pijama",
        "2002",
        "Non-stop",
        "Fuck Love (feat. Trippie Redd)",
        "Dans mon sang",
        "Silence",
        "Dieu est une femme",
        "Dejala que vuelva (feat. Manuel Turizo)",
        "Flammes",
        "Ce que les amoureux font",
        "Taki Taki (avec Selena Gomez, Ozuna & Cardi B)",
        "Let Me Go (avec Alesso, Florida Georgia Line & watt)",
        "Sentez-le toujours",
        "Priez pour moi (avec Kendrick Lamar)",
        "Marche et parle",
        "Lui & moi (avec Halsey)",
        "Candy Paint",
        "Félicitations",
        "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
        "Criminel",
        "Promenade de la prise",
        "adorable (avec Khalid)",
        "Frire remuer",
        "HUMBLE.",
        "Vaina Loca",
        "Perfect Duet (Ed Sheeran & Beyonc ?)",
        "Corazon (feat. Nego do Borel)",
        "Jeune, stupide et cassé",
        "Siguelo Bailando",
        "Centre-ville",
        "Bella",
        "Promesses (avec Sam Smith)",
        "Oui en effet",
        "Je m'a