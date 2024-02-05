# Demonstrates herança [talvez não adicione `if` para verificação de erros]


class Bruxo:
    def __init__(self, nome):
        if not nome:
            raise ValueError("Nome faltando")
        self.nome = nome

    ...


class Aluno(Bruxo):
    def __init__(self, nome, casa):
        super().__init__(nome)
        self.casa = casa

    ...


class Professor(Bruxo):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    ...


bruxo = Bruxo("Albus")
aluno = Aluno("Harry", "Grifinória")
professor = Professor("Severus", "Defesa Contra as Artes das Trevas")
...