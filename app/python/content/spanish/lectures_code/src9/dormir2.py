# Devuelve n ovejas desde la función auxiliar

def principal():
    n = int(input("¿Qué es n? "))
    for i in range(n):
        print(oveja(i))


def oveja(n):
    return "🐑" * n


if __name__ == "__main__":
    principal()