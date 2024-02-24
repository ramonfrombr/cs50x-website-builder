# Solicita o patronus também, mas ainda não exibe


class Aluno:
    def __init__(self, nome, casa, patronus):
        if not nome:
            raise ValueError("Nome faltando")
        if casa not in ["Grifinória", "Lufa-Lufa", "Corvinal", "Sonserina"]:
            raise ValueError("Casa inválida")
        self.nome = nome
        self.casa = casa
        self.patronus = patronus

    def __str__(self):
        return f"{self.nome} é da casa {self.casa}"


def principal():
    aluno = criar_aluno()
    print(aluno)


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    patronus = input("Patronus: ")
    return Aluno(nome, casa, patronus)


if __name__ == "__main__":
    principal()