import check50
import check50.c

@check50.check()
def existe():
    """scrabble.c existe"""
    check50.exists("scrabble.c")

@check50.check(existe)
def compile():
    """scrabble.c compile"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compile)
def gestion_cases():
    """gère correctement les cases des lettres"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compile)
def gestion_ponctuation():
    """gère correctement la ponctuation"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compile)
def test1():
    """identifie correctement 'Question?' et 'Question!' comme une égalité"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compile)
def test2():
    """identifie correctement 'drawing' et 'illustration' comme une égalité"""
    check50.run("./scrabble").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compile)
def test3():
    """identifie correctement 'hai!' comme gagnant sur 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

@check50.check(compile)
def test4():
    """identifie correctement 'COMPUTER' comme gagnant sur 'science'"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compile)
def test5():
    """identifie correctement 'Scrabble' comme gagnant sur 'wiNNeR'"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compile)
def test6():
    """identifie correctement 'pig' comme gagnant sur 'dog'"""
    check50.run("./scrabble").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compile)
def cas_complexe():
    """identifie correctement 'Skating!' comme gagnant sur 'figure?'"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)