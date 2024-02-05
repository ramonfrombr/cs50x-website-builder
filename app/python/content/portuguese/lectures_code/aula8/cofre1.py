# Adiciona cofres através de sobrecarga de operadores

class Cofre:
    def __init__(self, galeoes=0, sicles=0, nuques=0):
        self.galeoes = galeoes
        self.sicles = sicles
        self.nuques = nuques

    def __str__(self):
        return f"{self.galeoes} Galeões, {self.sicles} Sicles, {self.nuques} Nuques"

    def __add__(self, outro):
        galeoes = self.galeoes + outro.galeoes
        sicles = self.sicles + outro.sicles
        nuques = self.nuques + outro.nuques
        return Cofre(galeoes, sicles, nuques)


potter = Cofre(100, 50, 25)
print(potter)

weasley = Cofre(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)