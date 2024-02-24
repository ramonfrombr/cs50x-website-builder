# Retorna uma lista de ovelhas

def principal():
    n = int(input("Qual é o valor de n? "))
    for s in ovelhas(n):
        print(s)


def ovelhas(n):
    rebanho = []
    for i in range(n):
        rebanho.append("🐑" * i)
    return rebanho


if __name__ == "__main__":
    principal()