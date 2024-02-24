# Move get_student para a classe Aluno

class Aluno:
    def __init__(self, nome, casa):
        self.nome = nome
        self.casa = casa

    def __str__(self):
        return f"{self.nome} é da casa {self.casa}"

    @classmethod
    def criar(cls):
        nome = input("Nome: ")
        casa = input("Casa: ")
        return cls(nome, casa)


def principal():
    aluno = Aluno.criar()
    print(aluno)


if __name__ == "__main__":
    principal()