# Não verifica __name__


def principal():
    ola("mundo")
    adeus("mundo")


def ola(nome):
    print(f"olá, {nome}")


def adeus(nome):
    print(f"adeus, {nome}")


principal()