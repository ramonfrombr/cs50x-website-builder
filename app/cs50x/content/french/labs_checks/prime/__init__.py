import check50
import check50.c


@check50.check()
def existe():
    """prime.c existe"""
    check50.exists("prime.c")


@check50.check(existe)
def compile():
    """prime.c compile"""
    check50.c.compile("prime.c", lcs50=True)


@check50.check(compile)
def jusqu_a_10():
    """Une entrée de 1 et 10 donne tous les nombres premiers entre 1 et 10, inclus"""
    check50.run("./prime").stdin("1").stdin("10").stdout("2\n3\n5\n7")


@check50.check(compile)
def entre_10_et_50():
    """Une entrée de 10 et 25 donne tous les nombres premiers entre 10 et 25, inclus"""
    check50.run("./prime").stdin("10").stdin("25").stdout("11\n13\n17\n19\n23")


@check50.check(compile)
def entre_50_et_60():
    """Une entrée de 50 et 60 donne tous les nombres premiers entre 50 et 60, inclus"""
    check50.run("./prime").stdin("50").stdin("60").stdout("53\n59")