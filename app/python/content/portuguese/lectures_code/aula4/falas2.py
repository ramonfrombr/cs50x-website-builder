# Verificar __name__


def principal():
    ola("mundo")
    adeus("mundo")


def ola(nome):
    print(f"olá, {nome}")


def adeus(nome):
    print(f"adeus, {nome}")


if __name__ == "__main__":
    principal()