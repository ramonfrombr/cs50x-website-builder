# Agrega bóvedas, almacenando el total en una nueva bóveda


class Boveda:
    def __init__(self, galeones=0, sickles=0, knuts=0):
        self.galeones = galeones
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galeones} Galeones, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Boveda(100, 50, 25)
print(potter)

weasley = Boveda(25, 50, 100)
print(weasley)

galeones = potter.galeones + weasley.galeones
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Boveda(galeones, sickles, knuts)
print(total)