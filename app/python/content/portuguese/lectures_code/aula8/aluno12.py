# Adiciona validação em __init__ usando raise


class Aluno:
    def __init__(self, nome, casa):
        if not nome:
            raise ValueError("Nome faltando")
        if casa not in ["Grifinória", "Lufa-lufa", "Corvinal", "Sonserina"]:
            raise ValueError("Casa inválida")
        self.nome = nome
        self.casa = casa


def principal():
    aluno = criar_aluno()
    print(f"{aluno.nome} é da casa {aluno.casa}")


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return Aluno(nome, casa)


if __name__ == "__main__":
    principal()