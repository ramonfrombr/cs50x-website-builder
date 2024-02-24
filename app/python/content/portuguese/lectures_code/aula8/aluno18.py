# Adiciona @property para casa


class Aluno:
    def __init__(self, nome, casa):
        if not nome:
            raise ValueError("Nome inválido")
        self.nome = nome
        self.casa = casa

    def __str__(self):
        return f"{self.nome} da casa {self.casa}"

    @property
    def casa(self):
        return self._casa

    @casa.setter
    def casa(self, casa):
        if casa not in ["Grifinória", "Lufa-Lufa", "Corvinal", "Sonserina"]:
            raise ValueError("Casa inválida")
        self._casa = casa


def main():
    aluno = criar_aluno()
    print(aluno)


def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return Aluno(nome, casa)


if __name__ == "__main__":
    main()