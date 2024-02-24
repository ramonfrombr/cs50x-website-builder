# Armazena aluno como lista (mutável)


def principal():
    aluno = criar_aluno()
    if aluno[0] == "Padma":
        aluno[1] = "Corvinal"
    print(f"{aluno[0]} é da casa {aluno[1]}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return [nome, casa]


if __name__ == "__main__":
    principal()