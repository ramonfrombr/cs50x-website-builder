# Devuelve una lista de ovejas


def principal():
    n = int(input("¿Cuál es n? "))
    for s in ovejas(n):
        print(s)


def ovejas(n):
    rebano = []
    for i in range(n):
        rebano.append("🐑" * i)
    return rebano


if __name__ == "__main__":
    principal()