# Decompacota um dicionário

def total(galeoes, sicles, knuts):
    return (galeoes * 17 + sicles) * 29 + knuts

moedas = {"galeoes": 100, "sicles": 50, "knuts": 25}

print(total(**moedas), "Knuts")