# Desempaqueta un diccionario


def total(galeones, sickles, knuts):
    return (galeones * 17 + sickles) * 29 + knuts


monedas = {"galeones": 100, "sickles": 50, "knuts": 25}

print(total(**monedas), "Knuts")