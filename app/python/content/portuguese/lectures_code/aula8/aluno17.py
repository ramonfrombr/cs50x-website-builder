# Remove patronus para simplicidade, contorna verificação de erros definindo atributo

class Aluno:
    def __init__(self, nome, casa):
        if not nome:
            raise ValueError("Nome inválido")
        if casa not in ["Grifinória", "Lufa-lufa", "Corvinal", "Sonserina"]:
            raise ValueError("Casa inválida")
        self.nome = nome
        self.casa = casa

    def __str__(self):
        return f"{self.nome} da casa {self.casa}"

def principal():
    aluno = criar_aluno()
    aluno.casa = "Rua Privet Drive, número Quatro"
    print(aluno)

def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return Aluno(nome, casa)

if __name__ == "__main__":
    principal()