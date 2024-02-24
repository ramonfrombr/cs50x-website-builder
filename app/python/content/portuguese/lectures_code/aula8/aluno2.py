# Retorna o aluno como uma tupla, desempacotando-a


def principal():
    nome, casa = criar_aluno()
    print(f"{nome} é da casa {casa}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return nome, casa


if __name__ == "__main__":
    principal()