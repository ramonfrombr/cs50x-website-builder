# Imprime quadrado de tijolos usando uma função com loops aninhados

def principal():
    imprimir_quadrado(3)

def imprimir_quadrado(tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            print("#", end="")
        print()

principal()