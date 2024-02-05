# Demonstração de definição de uma função com um parâmetro com um valor padrão

def saudacao(para="mundo"):
    print("ola,", para)

saudacao()
nome = input("Qual é o seu nome? ")
saudacao(nome)