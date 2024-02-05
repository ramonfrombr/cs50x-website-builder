# Retorna o aluno como uma tupla, sem desempacotá-lo


def principal():
    aluno = criar_aluno()
    print(f"{aluno[0]} é da casa {aluno[1]}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return (nome, casa)


if __name__ == "__main__":
    principal()