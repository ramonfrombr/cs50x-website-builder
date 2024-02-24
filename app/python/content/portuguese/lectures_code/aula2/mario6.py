# Imprime quadrado de tijolos usando uma função com loop e multiplicação de str

def principal():
    imprimir_quadrado(3)

def imprimir_quadrado(tamanho):
    for _ in range(tamanho):
        print("#" * tamanho)

principal()