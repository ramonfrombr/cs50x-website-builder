# Retorna n ovelhas da função auxiliar


def principal():
    n = int(input("Qual é o valor de n? "))
    for i in range(n):
        print(ovelha(i))


def ovelha(n):
    return "🐑" * n


if __name__ == "__main__":
    principal()