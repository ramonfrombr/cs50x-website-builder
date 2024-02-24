# Adiciona cofres, armazenando o total em um novo cofre


class Cofre:
    def __init__(self, galeoes=0, sicles=0, nuques=0):
        self.galeoes = galeoes
        self.sicles = sicles
        self.nuques = nuques

    def __str__(self):
        return f"{self.galeoes} Galeões, {self.sicles} Sicles, {self.nuques} Nuques"


potter = Cofre(100, 50, 25)
print(potter)

weasley = Cofre(25, 50, 100)
print(weasley)

galeoes = potter.galeoes + weasley.galeoes
sicles = potter.sicles + weasley.sicles
nuques = potter.nuques + weasley.nuques

total = Cofre(galeoes, sicles, nuques)
print(total)