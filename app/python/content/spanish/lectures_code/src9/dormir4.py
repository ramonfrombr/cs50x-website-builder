# Usa yield


def main():
    n = int(input("¿Cuál es n? "))
    for s in oveja(n):
        print(s)


def oveja(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()