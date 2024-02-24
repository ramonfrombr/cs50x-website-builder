# Armazena o aluno como um dicionário


def principal():
    aluno = criar_aluno()
    print(f"{aluno['nome']} é da casa {aluno['casa']}")


def criar_aluno():
    aluno = {}
    aluno["nome"] = input("Nome: ")
    aluno["casa"] = input("Casa: ")
    return aluno


if __name__ == "__main__":
    principal()