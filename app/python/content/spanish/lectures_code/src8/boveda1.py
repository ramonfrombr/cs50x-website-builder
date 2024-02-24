# Agrega bóvedas mediante sobrecarga de operadores

class Boveda:
    def __init__(self, galeones=0, sickles=0, knuts=0):
        self.galeones = galeones
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galeones} Galeones, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galeones = self.galeones + other.galeones
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Boveda(galeones, sickles, knuts)

potter = Boveda(100, 50, 25)
print(potter)

weasley = Boveda(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)