# Demonstração de definição de uma função principal

def principal():
    nome = input("Qual é o seu nome? ")
    ola(nome)


def ola(para="mundo"):
    print("olá,", para)


principal()