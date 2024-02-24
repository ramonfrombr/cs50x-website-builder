# Implementa o método sort() com um método de instância

import random


class Chapeu:
    def __init__(self):
        self.casas = ["Grifinória", "Lufa-lufa", "Corvinal", "Sonserina"]

    def sortear(self, nome):
        print(nome, " é da casa ", random.choice(self.casas))


chapeu = Chapeu()
chapeu.sortear("Harry")