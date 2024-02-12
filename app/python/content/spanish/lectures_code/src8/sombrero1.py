# Implementa el método sort() con una clase

import random


class Sombrero:

    casas = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def ordenar(cls, nombre):
        print(nombre, "está en", random.choice(cls.casas))


Sombrero.ordenar("Harry")