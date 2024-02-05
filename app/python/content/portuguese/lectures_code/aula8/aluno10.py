# Adiciona __init__


class Aluno:
    def __init__(self, nome, casa):
        self.nome = nome
        self.casa = casa


def principal():
    aluno = criar_aluno()
    print(f"{aluno.nome} é da casa {aluno.casa}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    aluno = Aluno(nome, casa)
    return aluno


if __name__ == "__main__":
    principal()