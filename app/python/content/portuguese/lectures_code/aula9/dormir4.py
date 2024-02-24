# Usa yield


def principal():
    n = int(input("Qual é o valor de n? "))
    for s in ovelha(n):
        print(s)


def ovelha(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    principal()