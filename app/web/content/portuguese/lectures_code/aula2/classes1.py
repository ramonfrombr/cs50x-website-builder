class Voo:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []

    def adicionar_passageiro(self, nome):
        if not self.assentos_disponiveis():
            return False
        self.passageiros.append(nome)
        return True

    def assentos_disponiveis(self):
        return self.capacidade - len(self.passageiros)


voo = Voo(capacidade=3)

pessoas = ["Harry", "Ron", "Hermione", "Ginny"]
for pessoa in pessoas:
    if voo.adicionar_passageiro(pessoa):
        print(f"{pessoa} adicionado ao voo.")
    else:
        print(f"Não há assentos disponíveis para {pessoa}.")
