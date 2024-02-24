# Função a ser testada


def principal():
    nome = input("Qual é o seu nome? ")
    saudacao(nome)


def saudacao(para="mundo"):
    print("olá,", para)


if __name__ == "__main__":
    principal()