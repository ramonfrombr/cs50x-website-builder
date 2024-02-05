# Define a classe para um aluno


class Aluno:
    ...


def principal():
    aluno = criar_aluno()
    print(f"{aluno.nome} de {aluno.casa}")


def criar_aluno():
    aluno = Aluno()
    aluno.nome = input("Nome: ")
    aluno.casa = input("Casa: ")
    return aluno


if __name__ == "__main__":
    principal()