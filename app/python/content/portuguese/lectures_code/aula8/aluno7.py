# Elimina variável desnecessária


def principal():
    aluno = criar_aluno()
    print(f"{aluno['nome']} é da casa {aluno['casa']}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return {"nome": nome, "casa": casa}


if __name__ == "__main__":
    principal()