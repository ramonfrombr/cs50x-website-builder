import check50
import check50.c


@check50.check()
def existe():
    """helpers.c existe"""
    check50.exists("helpers.c")
    check50.include("Makefile", "bmp.h", "helpers.h", "colorize.c", "smiley.bmp")


@check50.check(existe)
def compile():
    """colorize compile"""
    check50.c.compile("colorize.c", "helpers.c", lcs50=True)


@check50.check(compiler)
def test_creation_image():
    """colorize crée une image"""
    check50.run("./colorize smiley.bmp smiley_out.bmp").exit(0)
    check50.exists("smiley_out.bmp")


@check50.check(test_creation_image)
def couleur_différente():
    """colorize change les couleurs de l'image"""
    check50.run("./colorize smiley.bmp smiley_out.bmp")
    if check50.hash("smiley_out.bmp") == "1c137ffd2d7adeae0f22e00136d187f6237a4128e2dd8a413c8f9372db673a05":
        raise check50.Failure("colorize n'a pas changé l'image")