import check50
import check50.c


@check50.check()
def existe():
    """no-vowels.c existe"""
    check50.exists("no-vowels.c")


@check50.check(existe)
def compile():
    """no-vowels.c compile"""
    check50.c.compile("no-vowels.c", lcs50=True)


@check50.check(compile)
def simple():
    """Entrée de \"hello\" produit la sortie \"h3ll0\""""
    verifier_sans_voyelles(input="hello", output="h3ll0")


@check50.check(compile)
def mot_long():
    """Entrée de \"pseudocode\" produit la sortie \"ps3ud0c0d3\""""
    verifier_sans_voyelles(input="pseudocode", output="ps3ud0c0d3")


@check50.check(compile)
def majuscules():
    """Entrée de \"Hello World\" produit la sortie \"H3ll0 W0rld\""""
    verifier_sans_voyelles(input="\"Hello World\"", output="H3ll0 W0rld")


@check50.check(compiles)
def nombres():
    """Entrée de \"This is CS50\" produit la sortie \"Th1s 1s CS50\""""
    verifier_sans_voyelles(input="\"This is CS50\"", output="Th1s 1s CS50")


# Fonctions auxiliaires
def verifier_sans_voyelles(input: str, output: str):
    check50.run(f"./sans-voyelles {input}").stdout(output)