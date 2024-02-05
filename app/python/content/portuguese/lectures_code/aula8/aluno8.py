# Demonstração da mutabilidade de dicionários


def principal():
    aluno = criar_aluno()
    if aluno["nome"] == "Padma":
        aluno["casa"] = "Corvinal"
    print(f"{aluno['nome']} é da casa {aluno['casa']}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return {"nome": nome, "casa": casa}


if __name__ == "__main__":
    principal()