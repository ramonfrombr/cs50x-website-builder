from hello1 import hola


def probar_predeterminada():
    assert hola() == "¡Hola, mundo!"


def probar_argumento():
    assert hola("David") == "¡Hola, David"