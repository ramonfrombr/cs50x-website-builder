# Desempacota uma lista

def total(galeoes, sicles, knuts):
    return (galeoes * 17 + sicles) * 29 + knuts

moedas = [100, 50, 25]

print(total(*moedas), "Knuts")