# Mostra como definir uma função com um valor de retorno

def principal():
    x = int(input("Qual é o valor de x? "))
    print("O quadrado de x é", quadrado(x))

def quadrado(n):
    return n * n

if __name__ == "__main__":
    principal()