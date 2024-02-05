# Implementa sort() com um método de classe

import random


class Chapeu:

    casas = ["Grifinória", "Lufa-Lufa", "Corvinal", "Sonserina"]

    @classmethod
    def sortear(cls, nome):
        print(nome, " é da casa ", random.choice(cls.casas))


Chapeu.sortear("Harry")