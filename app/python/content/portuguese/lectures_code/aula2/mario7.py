# Imprime quadrados de tijolos usando uma função com um loop e multiplicação de str

def principal():
    imprimir_quadrado(3)


def imprimir_quadrado(tamanho):
    for _ in range(tamanho):
        imprimir_linha(tamanho)


def imprimir_linha(largura):
    print("#" * largura)


principal()