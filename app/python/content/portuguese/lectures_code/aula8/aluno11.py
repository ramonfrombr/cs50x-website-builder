# Elimina a variável desnecessária


class Aluno:
    def __init__(self, nome, casa):
        self.nome = nome
        self.casa = casa


def principal():
    aluno = criar_aluno()
    print(f"{aluno.nome} da casa {aluno.casa}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return Aluno(nome, casa)


if __name__ == "__main__":
    principal()