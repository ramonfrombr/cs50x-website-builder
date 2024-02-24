# Demonstração da imutabilidade de tuplas, remove parênteses
# https://scifi.stackexchange.com/q/105992

def principal():
    aluno = criar_aluno()
    if aluno[0] == "Padma":
        aluno[1] = "Corvinal"
    print(f"{aluno[0]} é da casa {aluno[1]}")

def criar_aluno():
    nome = input("Nome: ")
    casa = input("Casa: ")
    return nome, casa

if __name__ == "__main__":
    principal()