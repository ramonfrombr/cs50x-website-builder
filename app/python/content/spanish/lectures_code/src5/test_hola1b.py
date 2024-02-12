from hello1 import hello


def probar_predeterminada():
    assert hello() == "¡Hola, mundo"


def probar_argumento():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"¡Hola, {name}"