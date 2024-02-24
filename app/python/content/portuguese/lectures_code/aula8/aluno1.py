# Modulariza a obtenção do nome do aluno e da casa


def principal():
    nome = receber_nome()
    casa = receber_casa()
    print(f"{nome} é da casa {casa}")


def receber_nome():
    return input("Nome: ")


def receber_casa():
    return input("Casa: ")


if __name__ == "__main__":
    principal()