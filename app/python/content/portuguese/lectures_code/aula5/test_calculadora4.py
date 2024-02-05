from calculadora import quadrado


def principal():
    test_quadrado()


def test_quadrado():
    try:
        assert quadrado(2) == 4
    except AssertionError:
        print("2 ao quadrado resultou em 4")
    try:
        assert quadrado(3) == 9
    except AssertionError:
        print("3 ao quadrado resultou em 9")
    try:
        assert quadrado(-2) == 4
    except AssertionError:
        print("-2 ao quadrado resultou em 4")
    try:
        assert quadrado(-3) == 9
    except AssertionError:
        print("-3 ao quadrado resultou em 9")
    try:
        assert quadrado(0) == 0
    except AssertionError:
        print("0 ao quadrado resultou em 0")


if __name__ == "__main__":
    principal()