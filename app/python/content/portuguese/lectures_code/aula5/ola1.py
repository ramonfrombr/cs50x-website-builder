# Tem função retornar uma str em vez disso


def principal():
    nome = input("Qual é o seu nome? ")
    print(ola(nome))


def ola(para="mundo"):
    return f"olá, {para}"


if __name__ == "__main__":
    principal()