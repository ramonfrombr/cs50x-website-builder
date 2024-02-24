# Agrega el principal


def principal():
    n = int(input("¿Cuál es n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    principal()