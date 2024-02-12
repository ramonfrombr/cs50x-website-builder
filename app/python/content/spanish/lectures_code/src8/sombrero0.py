# Implementa sort() con un método de instancia

import random


class Sombrero:
    def __init__(self):
        self.casas = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def ordenar(self, nombre):
        print(nombre, "está en", random.choice(self.casas))


sombrero = Sombrero()
sombrero.ordenar("Harry")