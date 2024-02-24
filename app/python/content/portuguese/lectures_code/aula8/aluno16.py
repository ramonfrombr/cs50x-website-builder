# Adiciona o método charm para lançar um encanto


class Aluno:
    def __init__(self, nome, casa, patronus=None):
        if not nome:
            raise ValueError("Nome faltando")
        if casa not in ["Grifinória", "Lufa-lufa", "Corvinal", "Sonserina"]:
            raise ValueError("Casa inválida")
        if patronus and patronus not in ["Cervo", "Lontra", "Jack Russell Terrier"]:
            raise ValueError("Patronus inválido")
        self.nome = nome
        self.casa = casa
        self.patronus = patronus

    def __str__(self):
        return f"{self.nome} é da casa {self.casa}"

    def encanto(self):
        match self.patronus:
            case "Cervo":
                return "🐴"
            case "Lontra":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"


def principal():
    aluno = criar_aluno()
    print("Expecto Patronum!")
    print(aluno.encanto())


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    patronus = input("Patronus: ") or None
    return Aluno(nome, casa, patronus)


if __name__ == "__main__":
    principal()