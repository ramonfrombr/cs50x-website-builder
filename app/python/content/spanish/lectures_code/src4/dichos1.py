# No verifica __name__


def principal():
    hola("mundo")
    adios("mundo")


def hola(nombre):
    print(f"hola, {nombre}")


def adios(nombre):
    print(f"adios, {nombre}")


principal()