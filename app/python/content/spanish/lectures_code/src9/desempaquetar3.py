# Desempaqueta una lista


def total(galeones, sickles, knuts):
    return (galeones * 17 + sickles) * 29 + knuts


monedas = [100, 50, 25]

print(total(*monedas), "Knuts")