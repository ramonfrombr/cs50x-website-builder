# Adiciona principal


def principal():
    n = int(input("Qual é o valor de n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    principal()