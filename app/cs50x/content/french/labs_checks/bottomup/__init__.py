import check50
import check50.c


@check50.check()
def existe():
    """bottomup.c existe"""
    check50.exists("bottomup.c")
    check50.include("bmp.h", "harvard_bottomup.bmp")


@check50.check(existe)
def compile():
    """bottomup compile"""
    check50.c.compile("bottomup.c", lcs50=True)


@check50.check(compile)
def test_image_flip():
    """bottomup flippe une image"""
    check50.run("./bottomup harvard_bottomup.bmp harvard_topdown.bmp").exit(0)
    if check50.hash("harvard_topdown.bmp") != "461a174d96cb75a2dc2eed99a30836cd5b516a4253c1df6af203c5dc0db8a568":
        raise check50.Failure("bottomup n'a pas inversé l'image")