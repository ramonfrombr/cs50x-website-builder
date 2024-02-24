# Imprime uma coluna de tijolos usando uma função com um loop


def principal():
    imprimir_coluna(3)


def imprimir_coluna(altura):
    for _ in range(altura):
        print("#")


principal()